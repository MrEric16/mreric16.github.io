from lib import *
A = """Coral reefs cover less than one per cent of the ocean floor, yet they shelter roughly a quarter of all marine species. The reef itself is built by tiny animals called polyps, which take calcium from seawater and deposit it as a hard skeleton. Over thousands of years, countless generations of polyps build on the skeletons of their predecessors, creating structures large enough to be seen from space."""
B = """Reefs take three main forms, a classification described by Charles Darwin in the 1840s. A fringing reef grows directly from the shore, with little or no water between it and the land. A barrier reef lies farther out, separated from the coast by a deep channel or lagoon; the best known runs for more than two thousand kilometres along the Australian coast. An atoll is a ring of coral surrounding a lagoon, with no land at its centre. Darwin proposed that an atoll forms when a volcanic island with a fringing reef slowly sinks while the coral continues to grow upwards, and later research largely confirmed his idea."""
C = """Corals depend on a partnership. Inside the tissues of each polyp live microscopic algae that supply most of its energy and give the reef its colour. When the water becomes too warm, the polyps expel the algae and the coral turns white, a process known as bleaching. A bleached coral is not dead, but without its partner it begins to starve, and if the heat lasts for more than a few weeks it usually dies. Severe bleaching events, once rare, have become frequent enough that some reefs have no time to recover between them."""
D = """Heat is not the only danger. Run-off from farmland carries fertiliser to the sea, where it feeds seaweed that smothers coral. Fishing with explosives destroys the structure of the reef, and the overfishing of parrotfish, which graze on algae, allows seaweed to spread. Cyclones and outbreaks of the crown-of-thorns starfish, which feeds on coral, cause further damage, although reefs have always recovered from such natural events when left alone. It is the combination of pressures that now worries scientists, since a reef weakened by pollution recovers far more slowly from a storm."""
E = """The best-known response is coral gardening. Fragments are broken from healthy colonies, grown on frames in underwater nurseries until they are large enough, and then attached to damaged reef with cement or clips. Dr Maria Okafor's team has reported that fragments survive more often when they are attached in groups than when they are planted singly, probably because neighbours shelter one another from strong currents. In several projects, restored patches have attracted fish within months, and some have begun to spawn naturally."""
F = """Professor Daniel Reyes does not want gardening abandoned, but he believes that its importance is often exaggerated. A planted coral will bleach and die just as surely as a wild one if the water stays too warm, he points out, and the cost of restoring a single hectare is very high. Because only a few fast-growing species are normally planted, a restored reef also tends to have less variety than the original. In his view, the first priority must be to cut greenhouse gas emissions and to improve the quality of coastal water."""
G = """A newer idea is to look for corals that can tolerate heat. Some colonies growing in naturally hot lagoons survive temperatures that kill their neighbours elsewhere, and researchers have begun to breed them, or to move them to cooler reefs. So far this has been tried only in small trials, and nobody yet knows whether such corals will be able to cope with other threats, such as disease. Supporters of gardening argue that it should continue regardless, because it buys time while longer-term solutions are developed."""
CORAL = '#E07A5F'; LAG = '#BFE0F0'
def sea(inner): return '<rect class="w" x="0" y="0" width="160" height="120"/>' + inner
FR = sea('<path class="g" d="M0 0H62Q78 40 54 68Q40 100 62 120H0Z"/><path d="M66 0Q82 40 58 68Q44 100 66 120" fill="none" stroke="%s" stroke-width="9"/>' % CORAL)
BA = sea('<path fill="%s" d="M60 0H104Q116 40 102 68Q92 100 108 120H60Z"/><path class="g" d="M0 0H62Q78 40 54 68Q40 100 62 120H0Z"/><path d="M106 0Q118 40 104 68Q94 100 110 120" fill="none" stroke="%s" stroke-width="9"/>' % (LAG, CORAL))
AT = sea('<ellipse cx="80" cy="60" rx="46" ry="34" fill="%s" stroke="%s" stroke-width="10"/>' % (LAG, CORAL))
PA = sea(''.join('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="#3D2A22" stroke-width="2"/>' % (x, y, r, CORAL) for x, y, r in [(40, 35, 12), (90, 28, 9), (120, 62, 14), (60, 80, 10), (100, 98, 8), (25, 95, 7)]))
P = passage('p04', 'Reefs Under Pressure', 'Marine biology', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Coral reefs cover more than one per cent of the ocean floor.', 'F', 'A', 'cover less than one per cent of the ocean floor'),
  ('Polyps take calcium from seawater to build their skeletons.', 'T', 'A', 'take calcium from seawater and deposit it as a hard skeleton'),
  ('Darwin suggested how atolls are formed.', 'T', 'B', 'Darwin proposed that an atoll forms when a volcanic island'),
  ('The best-known barrier reef is more than two thousand kilometres long.', 'T', 'B', 'runs for more than two thousand kilometres along the Australian coast'),
  ('A bleached coral is always dead.', 'F', 'C', 'A bleached coral is not dead'),
  ('Bleaching has been recorded more often since 1980.', 'NG', 'C', 'Severe bleaching events, once rare, have become frequent', 'The passage says bleaching has become frequent but gives no dates.'),
  ('Fertiliser from farmland helps seaweed to grow on reefs.', 'T', 'D', 'it feeds seaweed that smothers coral'),
  ('Reefs have never recovered from cyclones.', 'F', 'D', 'reefs have always recovered from such natural events when left alone'),
  ('Coral fragments attached in groups survive better than single ones.', 'T', 'E', 'fragments survive more often when they are attached in groups'),
  ('Professor Reyes wants coral gardening to stop.', 'F', 'F', 'does not want gardening abandoned'),
  ('Heat-tolerant corals have been used successfully on a large scale.', 'F', 'G', 'So far this has been tried only in small trials'),
 ]),
 feat('Classify each statement according to the type of reef it describes. You may use any letter more than once.', ['Fringing reef', 'Barrier reef', 'Atoll'], [
  ('Grows directly from the shore with little or no water between it and the land.', 0, 'B', 'grows directly from the shore'),
  ('Is separated from the land by a lagoon or deep channel.', 1, 'B', 'separated from the coast by a deep channel or lagoon'),
  ('May form when a volcanic island sinks.', 2, 'B', 'forms when a volcanic island with a fringing reef slowly sinks'),
  ('Has no land at its centre.', 2, 'B', 'with no land at its centre'),
  ('Includes the best-known example, off the Australian coast.', 1, 'B', 'the best known runs for more than two thousand kilometres along the Australian coast'),
 ], cls=True),
 pic('Which picture, A to D, shows each type of reef described in paragraph B? Each picture shows a view from above.', [(FR, 160, 120), (BA, 160, 120), (AT, 160, 120), (PA, 160, 120)], [
  ('a reef that grows directly from the shore', 0, 'B', 'grows directly from the shore'),
  ('a reef separated from the coast by a lagoon', 1, 'B', 'separated from the coast by a deep channel or lagoon'),
  ('a ring of coral with no land at its centre', 2, 'B', 'An atoll is a ring of coral surrounding a lagoon'),
 ]),
 mcq([
  ('What happens to a coral when its polyps expel the algae?', ['It turns white and begins to starve.', 'It dies at once.', 'It starts to grow faster.', 'It stops producing calcium.'], 0, 'C', 'the coral turns white'),
  ('What does the writer say now worries scientists most?', ['the loss of parrotfish', 'the effect of cyclones', 'the number of starfish', 'the combination of several pressures'], 3, 'D', 'It is the combination of pressures that now worries scientists'),
  ('According to Dr Okafor\'s team, why do grouped fragments survive better?', ['They grow faster in cement.', 'Neighbours shelter each other from currents.', 'Fish protect them from seaweed.', 'They reflect less heat.'], 1, 'E', 'neighbours shelter one another from strong currents'),
 ]),
 head(['Three shapes of reef and how one forms', 'A fragile partnership', 'Many threats acting together', 'Growing and replanting coral', 'Doubts about restoration', 'Hope in heat-resistant coral', 'The role of fish in controlling disease', 'Reefs that have never been damaged'],
  [('B', 0, 'Reefs take three main forms'), ('C', 1, 'Corals depend on a partnership'), ('D', 2, 'Heat is not the only danger'), ('E', 3, 'The best-known response is coral gardening'), ('F', 4, 'its importance is often exaggerated'), ('G', 5, 'A newer idea is to look for corals that can tolerate heat')]),
 info([
  ('the length of a particular reef', 'B', 'runs for more than two thousand kilometres'),
  ('a reason why some reefs cannot recover between bleaching events', 'C', 'some reefs have no time to recover between them'),
  ('a species that feeds on coral', 'D', 'crown-of-thorns starfish, which feeds on coral'),
  ('an explanation of why neighbouring planted corals do better', 'E', 'neighbours shelter one another from strong currents'),
  ('a criticism relating to the variety of species', 'F', 'a restored reef also tends to have less variety than the original'),
  ('an argument for continuing despite the limits of a method', 'G', 'it buys time while longer-term solutions are developed'),
 ]),
 sent(2, [
  ('Polyps take ___ from seawater to build their skeletons.', ['calcium'], 'A', 'take calcium from seawater'),
  ('A reef lying far from the shore, with a lagoon behind it, is a ___ reef.', ['barrier'], 'B', 'A barrier reef lies farther out'),
  ('Darwin suggested that an atoll forms when a volcanic island ___.', ['sinks'], 'B', 'slowly sinks'),
  ('Run-off from farmland carries ___ to the sea.', ['fertiliser', 'fertilizer'], 'D', 'carries fertiliser to the sea'),
  ('Reyes says that restoring one ___ of reef costs a great deal.', ['hectare'], 'F', 'restoring a single hectare is very high'.replace('restoring a single hectare is very high', 'restoring a single hectare')),
  ('Heat-tolerant corals have so far been tried only in small ___.', ['trials'], 'G', 'only in small trials'),
 ]),
 short(3, [
  ('Which fish graze on algae on reefs?', ['parrotfish'], 'D', 'parrotfish, which graze on algae'),
  ('What are coral fragments grown on in nurseries?', ['frames'], 'E', 'grown on frames in underwater nurseries'),
  ('What does Reyes say must be cut first?', ['greenhouse gas emissions', 'emissions'], 'F', 'cut greenhouse gas emissions'),
  ('Where do some heat-tolerant colonies grow naturally?', ['hot lagoons', 'naturally hot lagoons', 'lagoons'], 'G', 'naturally hot lagoons'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Corals contain microscopic [[1]] that give them energy and colour. When the sea becomes too [[2]], the polyps expel them and the coral turns [[3]]. If the heat continues for several weeks, the coral usually [[4]]. Fertiliser makes [[5]] grow, and this smothers the reef.',
  [(['algae'], 'C', 'microscopic algae'), (['warm'], 'C', 'too warm'), (['white'], 'C', 'turns white'), (['dies'], 'C', 'it usually dies'), (['seaweed'], 'D', 'feeds seaweed that smothers coral')], 1,
  bank=['algae', 'warm', 'white', 'dies', 'seaweed', 'fish', 'cold', 'green', 'grows']),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['[[1]] are broken from healthy colonies.', 'They are grown on frames in underwater [[2]].', 'When large enough, they are attached to the damaged reef with cement or [[3]].', 'Fish begin to visit the restored [[4]] within months.'],
  [(['fragments'], 'E', 'Fragments are broken from healthy colonies'), (['nurseries'], 'E', 'underwater nurseries'), (['clips'], 'E', 'cement or clips'), (['patches'], 'E', 'restored patches have attracted fish')], 2),
])
