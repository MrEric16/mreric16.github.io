from lib import *
from svgs import *
A = """Coral reefs cover less than one per cent of the ocean floor, yet they are home to about a quarter of all marine species, which makes them among the richest habitats on Earth. They are often called the rainforests of the sea. A reef looks like a rocky landscape of colourful stones, but it is in fact a living structure, built over thousands of years by tiny animals called polyps. The largest reef system, the Great Barrier Reef off the coast of Australia, stretches for about two thousand three hundred kilometres and can be seen from space. This passage explains how reefs are built, why they are so rich in life and why they are in danger."""
B = """A coral polyp is a small, soft animal, usually only a few millimetres across, with a ring of tentacles around a mouth. It protects itself by building a hard skeleton of limestone around its body, which it makes from calcium taken from seawater. When the polyp dies, the skeleton remains, and new polyps grow on top of it. Over thousands of years, millions of skeletons accumulate to form a reef. Corals grow slowly, usually by only a few centimetres a year, so a large reef is very old: some of the structures in the Great Barrier Reef are several thousand years old."""
C = """Most reef-building corals live in partnership with microscopic algae, which live inside the polyps' tissues. The algae use sunlight to make sugars by photosynthesis, and they share most of this food with the coral. In return, the coral gives the algae shelter and the chemicals that they need. This partnership explains why reefs grow only in clear, shallow water, where enough sunlight can reach the algae, and in warm seas, with temperatures of between twenty and thirty degrees Celsius. It also gives corals their colours, since the algae provide most of the reds, browns and greens that we see."""
D = """Because of this food supply, a reef supports a great variety of life. Thousands of species of fish, including tiny, brightly coloured ones, shelter among the branches of coral. Sea turtles feed on the sponges and jellyfish, sharks patrol the edges, and crabs, shrimps and starfish hide in cracks. Many fish that people eat spend their early lives in the shelter of the reef before moving to open water. Reefs also protect the coast: they act as natural breakwaters that absorb the force of waves and storms, and so they prevent damage to villages and farms on the shore. Millions of people also depend on them for food and for jobs in tourism."""
E = """The greatest threat to reefs is the warming of the seas. When the water becomes too warm, the corals are stressed and expel the algae living in their tissues. Without the algae, the coral loses its colour and turns white, a condition called bleaching, and since the algae provided most of its food, it begins to starve. A coral can recover if the water cools quickly, but if the heat lasts for weeks, the coral dies. Severe bleaching events have affected the Great Barrier Reef several times in recent years, and scientists fear that in a hotter world they will become more frequent."""
F = """Warming is not the only problem. Chemicals from farms and sewage that flow into the sea feed the growth of seaweed, which smothers the coral. The oceans are also becoming more acidic as they absorb carbon dioxide from the air, which makes it harder for polyps to build their skeletons. In some places fishermen use explosives or poison, which kill all the life around them, and overfishing removes the fish that clean the coral of algae. In addition, a starfish that eats coral, the crown-of-thorns, has sometimes appeared in huge numbers, and has stripped large areas of the reef bare."""
G = """Despite the dangers, there is hope. Dr Sofia Marchetti, a marine biologist, leads a project in which broken pieces of coral are grown in underwater nurseries and then fixed to damaged parts of a reef. She has found that some corals are more resistant to heat than others, and she is breeding these in order to produce reefs that can survive in warmer water. But she stresses that such work can only buy time. The real answer, she says, is to reduce the gases that warm the planet, to control pollution, and to create protected areas, where fishing is forbidden and the reef can recover."""
P = passage('p74', 'Coral Reefs Under Threat', 'Ecology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Coral reefs cover less than one per cent of the ocean floor.', 'T', 'A', 'less than one per cent of the ocean floor'),
  ('Reefs are home to about a quarter of marine species.', 'T', 'A', 'about a quarter of all marine species'),
  ('The Great Barrier Reef is the oldest reef in the world.', 'NG', 'A', 'The largest reef system', 'Its age relative to others is not given.'),
  ('A polyp builds a skeleton of limestone.', 'T', 'B', 'hard skeleton of limestone'),
  ('Corals grow by several metres a year.', 'F', 'B', 'a few centimetres a year'),
  ('Algae live inside the polyps.', 'T', 'C', 'which live inside the polyps'),
  ('Reefs grow in cold, deep water.', 'F', 'C', 'clear, shallow water'),
  ('Reefs protect the coast from waves.', 'T', 'D', 'natural breakwaters'),
  ('Bleached coral is always dead.', 'F', 'E', 'A coral can recover if the water cools quickly'),
 ]),
 mcq([
  ('Why do reefs grow only in clear, shallow water?', ['Sunlight must reach the algae.', 'Fish need space.', 'Sharks avoid deep water.', 'Waves are small.'], 0, 'C', 'where enough sunlight can reach the algae'),
  ('What happens when corals lose their algae?', ['They turn white and begin to starve.', 'They grow faster.', 'They change into sponges.', 'They sink.'], 0, 'E', 'turns white'),
  ('What does Dr Marchetti say about her work?', ['It can only buy time.', 'It will save every reef.', 'It is too costly.', 'It has failed.'], 0, 'G', 'can only buy time'),
 ]),
 feat('Match each statement with the correct threat, A to D.', ['Warming seas', 'Pollution from farms', 'Acidic oceans', 'Crown-of-thorns starfish'], [
  ('It causes bleaching.', 0, 'E', 'a condition called bleaching'),
  ('It feeds seaweed that smothers coral.', 1, 'F', 'feed the growth of seaweed'),
  ('It makes it harder to build skeletons.', 2, 'F', 'harder for polyps to build their skeletons'),
  ('It has stripped large areas of reef bare.', 3, 'F', 'stripped large areas of the reef bare'),
 ]),
 multi('Which TWO benefits of reefs are mentioned in paragraph D?', ['They protect the coast from waves.', 'They provide jobs in tourism.', 'They produce oil.', 'They warm the sea.', 'They supply fresh water.'], [0, 1], [('D', 'absorb the force of waves and storms'), ('D', 'jobs in tourism')]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The sea becomes too [[1]].', 'The coral expels its [[2]].', 'The coral turns white and begins to [[3]].', 'If the heat lasts for weeks, the coral [[4]].'],
  [(['warm'], 'E', 'water becomes too warm'), (['algae'], 'E', 'expel the algae'), (['starve'], 'E', 'begins to starve'), (['dies'], 'E', 'the coral dies')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Polyp', 'Builds a skeleton of [[1]]'], ['Algae', 'Make sugars by [[2]]'], ['Bleaching', 'Corals turn [[3]]'], ['Nurseries', 'Broken pieces of coral are [[4]]']],
  [(['limestone'], 'B', 'skeleton of limestone'), (['photosynthesis'], 'C', 'photosynthesis'), (['white'], 'E', 'turns white'), (['grown'], 'G', 'grown in underwater nurseries')], 1),
 head(['A rich habitat', 'Tiny builders', 'A partnership', 'A crowded community', 'Danger from heat', 'More threats', 'Rescue efforts', 'The history of diving', 'Cooking fish'],
  [('A', 0, 'among the richest habitats on Earth'), ('B', 1, 'building a hard skeleton of limestone'), ('C', 2, 'live in partnership with microscopic algae'), ('D', 3, 'a reef supports a great variety of life'), ('E', 4, 'The greatest threat to reefs is the warming of the seas'), ('F', 5, 'Warming is not the only problem'), ('G', 6, 'there is hope')]),
 info([
  ('a reference to visibility from space', 'A', 'seen from space'),
  ('a reference to how fast corals grow', 'B', 'a few centimetres a year'),
  ('a mention of a temperature range', 'C', 'between twenty and thirty degrees Celsius'),
  ('a reference to turtles feeding', 'D', 'Sea turtles feed on the sponges and jellyfish'),
  ('a mention of explosives', 'F', 'explosives or poison'),
 ]),
 ends(['build skeletons of limestone.', 'act as natural breakwaters.', 'happens when corals expel algae.', 'grows coral in underwater nurseries.', 'lives in the desert.', 'sells fish.', 'flies from space.'], [
  ('Polyps', 0, 'B', 'hard skeleton of limestone'),
  ('Reefs', 1, 'D', 'natural breakwaters'),
  ('Bleaching', 2, 'E', 'expel the algae'),
  ('Dr Marchetti', 3, 'G', 'underwater nurseries'),
 ]),
 sent(2, [
  ('Reefs are often called the rainforests of the ___.', ['sea'], 'A', 'rainforests of the sea'),
  ('Most reef corals live with microscopic ___.', ['algae'], 'C', 'microscopic algae'),
  ('The oceans are becoming more ___ as they absorb carbon dioxide.', ['acidic'], 'F', 'more acidic'),
  ('Dr Marchetti is a marine ___.', ['biologist'], 'G', 'marine biologist'),
 ]),
 short(3, [
  ('What do polyps take from seawater?', ['calcium'], 'B', 'calcium taken from seawater'),
  ('What is the loss of colour called?', ['bleaching'], 'E', 'called bleaching'),
  ('Where is the Great Barrier Reef?', ['australia', 'off australia'], 'A', 'off the coast of Australia'),
 ]),
])
