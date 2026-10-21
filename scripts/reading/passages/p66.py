from lib import *
from svgs import *
A = """Lakes are among the most sensitive indicators of change in the natural world. Their level goes up when the rains are heavy and falls in times of drought, and it can also be altered by human actions such as building dams or taking water for farms. In the imaginary island nation of Zendia, scientists have measured the water level in four important lakes every month for twenty years, and their records show four very different patterns. This passage describes each lake in turn and then discusses what the pattern teaches us about managing water, a question of growing importance for many countries."""
B = """Lake Aru lies in the north of the island and is fed by melting snow from the mountains. Its level has risen slowly but steadily throughout the twenty years, by roughly a metre in all. Scientists believe that the cause is warmer weather, which has caused the glaciers to melt faster and sent more water into the streams that feed the lake. This may sound like good news, but it is not entirely so: villages on the shore have been flooded several times, and farmers have lost fields that had been used for generations. The glaciers will not last for ever, and the lake is expected to shrink when the ice is gone."""
C = """Lake Bellu followed a different course. For the first seven years, its level fell, as a long drought dried up the rivers that feed it and farmers took water from its shores for irrigation. At its lowest point, the lake was less than half its former size, and the fishing boats lay on dry mud. Then the rains returned, the government limited the amount of water that farms could take, and the level rose again, until by the end of the twenty years it was nearly as high as it had been at the start. The recovery surprised the scientists, who had feared that the damage would be permanent."""
D = """The level of Lake Cora has gone up and down without any lasting trend. In the wet season it rises by several metres, and in the dry season it falls again, and the pattern has repeated itself year after year. The lake has no dam and no towns on its shore, and people leave it alone, so it behaves as nature intended. Biologists value it for exactly this reason, because the rising water floods the surrounding forest each year and carries nutrients to the fish that breed there. They call it a healthy lake, and they use it as a standard against which to judge the others."""
E = """Lake Dalu provides the sharpest contrast. Its level stayed almost constant for twelve years, and then suddenly dropped by more than three metres in a single season, after engineers opened a new canal to carry water from the lake to a city in the south. The level has remained at the lower height ever since. The canal supplies drinking water to nearly a million people, which is a great benefit, but the lower lake has damaged the wetlands at its edge, and several species of bird that nested there have disappeared. The government says that the city's need for water had to come first."""
F = """Dr Tomas Lindqvist, a hydrologist who has studied all four lakes, believes that they show how a lake's level can be changed in different ways: slowly, by the climate; temporarily, by drought; regularly, by the seasons; and suddenly, by human decisions. He argues that the last kind is the most dangerous, because it gives nature no time to adjust. A slow change can be followed and prepared for, but a sudden one may destroy habitats before anyone has noticed what is happening. He therefore urges the government to study the effects of every large project before it is approved."""
G = """The government has responded by promising a new law, under which any scheme to take large amounts of water from a lake must be studied for two years before work may begin. Environmental groups welcome the plan but say that it should have been introduced earlier. The government also intends to continue the monthly measurements, which have already proved their value. A new instrument, placed in each lake next year, will send readings directly to a central computer, so that scientists can see the level at any moment without travelling to the shore."""
P = passage('p66', 'Four Lakes of Zendia', 'Environment', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the water level of each lake over twenty years?', [(graph('rise'), 160, 120), (graph('dip'), 160, 120), (graph('fluct'), 160, 120), (graph('drop'), 160, 120)], [
  ('Lake Aru', 0, 'B', 'risen slowly but steadily'),
  ('Lake Bellu', 1, 'C', 'the level rose again'),
  ('Lake Cora', 2, 'D', 'gone up and down without any lasting trend'),
  ('Lake Dalu', 3, 'E', 'suddenly dropped by more than three metres'),
 ]),
 tfng([
  ('Zendia is an imaginary island nation.', 'T', 'A', 'imaginary island nation'),
  ('The levels were measured every month for twenty years.', 'T', 'A', 'every month for twenty years'),
  ('Lake Aru is fed by melting snow.', 'T', 'B', 'fed by melting snow from the mountains'),
  ('Lake Aru has risen by roughly a metre.', 'T', 'B', 'roughly a metre in all'),
  ('Lake Aru is expected to keep growing for ever.', 'F', 'B', 'expected to shrink when the ice is gone'),
  ('Lake Bellu at its lowest was less than half its former size.', 'T', 'C', 'less than half its former size'),
  ('Lake Cora has a dam.', 'F', 'D', 'The lake has no dam'),
  ('Lake Dalu\'s canal supplies water to nearly a million people.', 'T', 'E', 'nearly a million people'),
  ('The new canal cost a great deal of money.', 'NG', 'E', 'a new canal', 'Its cost is not mentioned.'),
 ]),
 mcq([
  ('What caused the fall of Lake Bellu?', ['A long drought and irrigation.', 'A new canal.', 'Melting snow.', 'A dam.'], 0, 'C', 'a long drought dried up the rivers'),
  ('Why do biologists value Lake Cora?', ['It is the deepest.', 'Rising water floods the forest and feeds fish.', 'It has many towns.', 'It supplies a city.'], 1, 'D', 'the rising water floods the surrounding forest each year'),
  ('Why does Dr Lindqvist think sudden changes are most dangerous?', ['They give nature no time to adjust.', 'They cost money.', 'They are slow.', 'They are natural.'], 0, 'F', 'it gives nature no time to adjust'),
 ]),
 feat('Match each statement with the correct lake, A to D.', ['Lake Aru', 'Lake Bellu', 'Lake Cora', 'Lake Dalu'], [
  ('Villages on its shore have been flooded.', 0, 'B', 'villages on the shore have been flooded'),
  ('Its recovery surprised scientists.', 1, 'C', 'The recovery surprised the scientists'),
  ('It is a standard for judging other lakes.', 2, 'D', 'a standard against which to judge the others'),
  ('Birds that nested at its edge have disappeared.', 3, 'E', 'several species of bird that nested there have disappeared'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Lake', 'Detail'],
  [['Aru', 'Fed by melting [[1]]'], ['Bellu', 'Farmers took water for [[2]]'], ['Cora', 'Rising water carries [[3]] to fish'], ['Dalu', 'Engineers opened a new [[4]]']],
  [(['snow'], 'B', 'melting snow'), (['irrigation'], 'C', 'for irrigation'), (['nutrients'], 'D', 'carries nutrients to the fish'), (['canal'], 'E', 'opened a new canal')], 1),
 multi('Which TWO causes of the changes in Lake Bellu are given in paragraph C?', ['A long drought dried up rivers.', 'Farmers took water for irrigation.', 'A dam was built.', 'Glaciers melted.', 'Engineers opened a canal.'], [0, 1], [('C', 'a long drought dried up the rivers'), ('C', 'farmers took water from its shores for irrigation')]),
 head(['Measuring the lakes', 'A lake that keeps rising', 'Falling and recovering', 'A natural rhythm', 'A sudden change', 'Four kinds of change', 'New rules and new instruments', 'The life of fish', 'How to build a boat'],
  [('A', 0, 'measured the water level in four important lakes'), ('B', 1, 'risen slowly but steadily'), ('C', 2, 'the level rose again'), ('D', 3, 'rises by several metres'), ('E', 4, 'suddenly dropped by more than three metres'), ('F', 5, 'changed in different ways'), ('G', 6, 'promising a new law')]),
 info([
  ('a reference to glaciers melting faster', 'B', 'the glaciers to melt faster'),
  ('a reference to boats on dry mud', 'C', 'fishing boats lay on dry mud'),
  ('a mention of the absence of towns on the shore', 'D', 'no towns on its shore'),
  ('a reference to a water supply for a city', 'E', 'drinking water to nearly a million people'),
  ('a reference to readings sent to a computer', 'G', 'send readings directly to a central computer'),
 ]),
 ends(['is fed by snow from the mountains.', 'recovered after the rains returned.', 'has no dam.', 'supplies a city in the south.', 'is the largest lake in the world.', 'froze in winter.', 'has been drained.'], [
  ('Lake Aru', 0, 'B', 'fed by melting snow from the mountains'),
  ('Lake Bellu', 1, 'C', 'the rains returned'),
  ('Lake Cora', 2, 'D', 'The lake has no dam'),
  ('Lake Dalu', 3, 'E', 'a city in the south'),
 ]),
 sent(2, [
  ('Lake Aru lies in the ___ of the island.', ['north'], 'B', 'in the north'),
  ('Biologists call Lake Cora a ___ lake.', ['healthy'], 'D', 'a healthy lake'),
  ('Dr Lindqvist is a ___.', ['hydrologist'], 'F', 'a hydrologist'),
  ('Schemes must be studied for ___ years before work begins.', ['two', '2'], 'G', 'two years'),
 ]),
 short(3, [
  ('For how long was the level of Lake Dalu almost constant?', ['twelve years'], 'E', 'twelve years'),
  ('Where does the canal carry water to?', ['a city'], 'E', 'a city in the south'),
  ('What does Dr Lindqvist urge the government to study?', ['every large project'], 'F', 'every large project'),
 ]),
])
