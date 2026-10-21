from lib import *
A = """Mount Everest, on the border between Nepal and Tibet, is the highest mountain on Earth. Its summit stands 8,849 metres above sea level, which is more than ten times the height of the tallest building in the world. The mountain is known as Sagarmatha in Nepali and Chomolungma in Tibetan, and it was named in English after Sir George Everest, a British surveyor, although he never saw it. For climbers, the mountain has been a challenge for more than a century, and for the people who live beneath it, it is a sacred place."""
B = """The first serious attempts to climb Everest were made by British expeditions in the 1920s. In 1924, George Mallory and Andrew Irvine disappeared near the summit, and nobody knows whether they reached it; Mallory's body was found in 1999, but the question remains open. The mountain was finally climbed on 29 May 1953 by Edmund Hillary, a beekeeper from New Zealand, and Tenzing Norgay, a Sherpa from Nepal. They spent only about fifteen minutes on the top, and Hillary later described the view as the most beautiful that he had ever seen."""
C = """Climbing Everest is not a single effort but a long process. Expeditions usually spend six to eight weeks on the mountain, and most of this time is used for acclimatisation, the gradual process by which the body adapts to the thin air. Climbers go up to a higher camp, sleep there, and return to a lower one, repeating the process several times. There are four camps above Base Camp, which stands at 5,364 metres, and the climbers reach the summit from the highest one, Camp Four, in a final push of fifteen hours or more."""
D = """The most important danger is the lack of oxygen. At the summit, the air pressure is about one third of that at sea level, so each breath contains only a third of the oxygen. Most climbers use bottled oxygen above 8,000 metres, a region known as the death zone, where the body cannot recover and grows weaker every hour. The cold is also severe, with temperatures as low as minus forty degrees Celsius, and the wind can exceed two hundred kilometres an hour, which makes any mistake extremely dangerous."""
E = """Sherpas, an ethnic group from the high valleys of Nepal, play a crucial part in every expedition. They carry equipment, fix ropes and set up camps, work that is both difficult and dangerous. The mountain has claimed more than three hundred lives since the first attempt, and about a third of the dead have been Sherpas. In recent years, Sherpas have campaigned for better pay and insurance, and some have become famous climbers in their own right, with record numbers of ascents to their names."""
F = """The popularity of Everest has created new problems. In some years, over eight hundred people have reached the summit, and queues have formed on the narrow ridge near the top, where climbers wait for hours in the cold. The mountain is also littered with discarded tents, bottles and oxygen cylinders, and human waste from the camps pollutes the glaciers. The Nepalese government now requires climbers to bring their waste back down, and teams of Sherpas have removed tonnes of rubbish."""
G = """Climate change is changing the mountain itself. The glaciers on which the route depends are melting faster, which makes the icefall at the start of the climb less stable. Dr Pema Lama, a glaciologist, says that some of the ice may disappear within a generation. She also notes that melting reveals bodies and equipment left decades ago. Even so, the number of people who wish to climb does not decline, and each year the debate about whether the mountain should be limited to fewer visitors becomes louder."""
P = passage('p47', 'Climbing Mount Everest', 'Geography', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Everest is on the border between Nepal and Tibet.', 'T', 'A', 'on the border between Nepal and Tibet'),
  ('Sir George Everest climbed the mountain named after him.', 'F', 'A', 'he never saw it'),
  ('Mallory and Irvine definitely reached the summit.', 'F', 'B', 'nobody knows whether they reached it'),
  ('Hillary was a beekeeper.', 'T', 'B', 'a beekeeper from New Zealand'),
  ('Tenzing Norgay was born in Britain.', 'F', 'B', 'a Sherpa from Nepal'),
  ('Most of an expedition is spent on acclimatisation.', 'T', 'C', 'most of this time is used for acclimatisation'),
  ('Climbers use bottled oxygen above 8,000 metres.', 'T', 'D', 'bottled oxygen above 8,000 metres'),
  ('Sherpas are paid well for the risks they take.', 'NG', 'E', 'Sherpas have campaigned for better pay and insurance', 'The passage says they have campaigned for better pay; it does not state their current level.'),
  ('The Nepalese government forbids climbers to leave waste on the mountain.', 'T', 'F', 'requires climbers to bring their waste back down'),
 ]),
 mcq([
  ('Why do climbers go up and down between camps?', ['To avoid the wind.', 'To let the body adapt to thin air.', 'To collect rubbish.', 'To rest their guides.'], 1, 'C', 'the gradual process by which the body adapts to the thin air'),
  ('What is the death zone?', ['A glacier.', 'The region above 8,000 metres.', 'The icefall.', 'Base Camp.'], 1, 'D', 'above 8,000 metres, a region known as the death zone'),
  ('What does Dr Lama say about the ice?', ['It is getting thicker.', 'Some may disappear within a generation.', 'It is safe.', 'It cannot be measured.'], 1, 'G', 'some of the ice may disappear within a generation'),
 ]),
 multi('Which TWO problems caused by the popularity of Everest are mentioned in paragraph F?', ['Queues near the top.', 'Rubbish on the mountain.', 'Falling prices.', 'Lack of guides.', 'Avalanches in the village.'], [0, 1], [('F', 'queues have formed on the narrow ridge'), ('F', 'littered with discarded tents, bottles and oxygen cylinders')]),
 head(['The highest place on Earth', 'The first success', 'A long climb in stages', 'The thin air and the cold', 'The people who carry the loads', 'The cost of popularity', 'A melting mountain', 'The history of Nepal', 'How to choose boots'],
  [('A', 0, 'is the highest mountain on Earth'), ('B', 1, 'The mountain was finally climbed on 29 May 1953'), ('C', 2, 'Climbing Everest is not a single effort but a long process'), ('D', 3, 'The most important danger is the lack of oxygen'), ('E', 4, 'play a crucial part in every expedition'), ('F', 5, 'The popularity of Everest has created new problems'), ('G', 6, 'Climate change is changing the mountain itself')]),
 info([
  ('a comparison between the height of the mountain and a building', 'A', 'more than ten times the height of the tallest building'),
  ('a year in which a body was found', 'B', 'found in 1999'),
  ('a figure for the height of Base Camp', 'C', 'Base Camp, which stands at 5,364 metres'),
  ('a figure for the lowest temperature', 'D', 'minus forty degrees Celsius'),
  ('a mention of a danger at the start of the climb', 'G', 'the icefall at the start of the climb'),
 ]),
 ends(['spent only fifteen minutes on top.', 'spend six to eight weeks on the mountain.', 'contains a third of the oxygen at sea level.', 'make up about a third of the dead.', 'is the highest camp.', 'was named after Sherpas.', 'is found only in Tibet.'], [
  ('The first climbers', 0, 'B', 'They spent only about fifteen minutes on the top'),
  ('Expeditions', 1, 'C', 'usually spend six to eight weeks on the mountain'),
  ('Each breath at the summit', 2, 'D', 'each breath contains only a third of the oxygen'),
  ('Sherpas', 3, 'E', 'about a third of the dead have been Sherpas'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Topic', 'Detail'],
  [['1924', 'Mallory and Irvine [[1]] near the summit'], ['1953', 'Hillary and Tenzing reach the [[2]]'], ['Above 8,000 metres', 'Most climbers use bottled [[3]]'], ['Waste', 'Climbers must bring it back [[4]]']],
  [(['disappeared'], 'B', 'disappeared near the summit'), (['summit', 'top'], 'B', 'climbed on 29 May 1953'.replace('climbed on 29 May 1953','top')), (['oxygen'], 'D', 'bottled oxygen'), (['down'], 'F', 'bring their waste back down')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Climbers go up to a higher [[1]].', 'They sleep there, then return to a [[2]] one.', 'They repeat the process several times to adapt to the thin [[3]].', 'They reach the summit from Camp [[4]] in a final push.'],
  [(['camp'], 'C', 'go up to a higher camp'), (['lower'], 'C', 'return to a lower one'), (['air'], 'C', 'thin air'), (['four'], 'C', 'Camp Four')], 1),
 sent(2, [
  ('Everest is called Chomolungma in ___.', ['tibetan'], 'A', 'Chomolungma in Tibetan'),
  ('Hillary was from New ___.', ['zealand'], 'B', 'New Zealand'),
  ('Sherpas fix ___ on the mountain.', ['ropes'], 'E', 'fix ropes'),
  ('Dr Lama is a ___.', ['glaciologist'], 'G', 'a glaciologist'),
 ]),
 short(3, [
  ('How high is the summit?', ['8,849 metres', '8849 metres'], 'A', '8,849 metres'),
  ('When was Mallory\'s body found?', ['1999'], 'B', 'found in 1999'),
  ('What pollutes the glaciers?', ['human waste'], 'F', 'human waste from the camps'),
 ]),
])
