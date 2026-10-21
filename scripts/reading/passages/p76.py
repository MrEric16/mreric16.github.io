from lib import *
from svgs import *
A = """Rivers are the arteries of a landscape, and the way in which their flow changes through the year affects farmers, fishermen, engineers and wildlife. In the imaginary island nation of Zendia, hydrologists measured the flow of four rivers in each of the four seasons of last year, and published the results as bar charts. The four rivers differ greatly in their sources and in their surroundings, and so their patterns differ too. This passage describes each of them, in turn, explaining what determines the amount of water that it carries and why the pattern matters to the people who live along it."""
B = """The river Aru is the most reliable. It rises from a large underground spring, and its flow is almost the same in all four seasons, whatever the weather. The spring is fed by rain which fell on distant hills many years ago and has been slowly filtering through the rock ever since, so that a dry summer makes little difference. For this reason the Aru supplies drinking water to the capital city, and the local council has banned building and farming within a kilometre of its banks, to keep the water clean. Fishermen also value the river, because its steady temperature is ideal for trout."""
C = """The river Beru is a snow river, which means that its water comes from the melting snow in the mountains. It is at its highest in spring, when the snow melts, and its flow then falls with each season, until in winter it is only a trickle. The spring flood is often violent, and villages along its banks have been flooded several times. The authorities have built a dam to store some of the water, which is released slowly in summer for farmers' fields. Without the dam, the Beru would be too wild in spring and almost dry in the autumn and winter, when the fields need it."""
D = """The river Ceru behaves in the opposite way. Its flow is smallest in spring and grows with each season, reaching its maximum in winter. The reason is that the Ceru drains a region in the south-west where the heaviest rain falls in autumn and winter, and where the soil is thin, so that the water runs quickly into the river. In summer the Ceru is so low that the farmers cannot take water from it, and in winter it often floods the lower fields. The people living on its banks say that they must always be ready to leave their houses in a hurry."""
E = """The river Deru is the most unusual. It is highest in summer, falls in autumn, and reaches its lowest in winter, while in spring it carries a moderate amount. Its water comes from glaciers high in the mountains, which melt fastest in the heat of July and August, so that the river swells just when the weather is driest and the farmers need water most. As the climate warms, however, the glaciers are shrinking, and hydrologists predict that the summer flow will fall in the coming decades, perhaps within the lifetime of the children now at school."""
F = """Dr Pavel Horak, a river scientist who led the survey, says that the four patterns demonstrate why a country needs different strategies for different rivers. The steady Aru needs protection from pollution; the Beru needs storage to hold back its spring flood; the Ceru needs flood defences in winter; and the Deru needs careful planning, because its future is uncertain. He adds that a single national rule, such as one limit on the quantity of water that farmers may take, would be harmful, because it would be too strict in one place and too generous in another."""
G = """The government has asked Dr Horak to prepare a plan for each river, and the first, for the Deru, will be published next year. It will include a study of the glaciers, a map of the farms that depend on their meltwater, and a proposal for a new reservoir to store water for the dry months. Environmental groups have welcomed the plan but warn that reservoirs damage the habitat of fish. Dr Horak accepts the argument and has promised that any new reservoir will include a channel through which fish can pass. Local farmers, meanwhile, have formed a committee which will meet the planners every month, so that their experience of the river can be heard before decisions are made."""
P = passage('p76', 'Four Rivers, Four Seasons', 'Geography', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which bar chart, A to D, shows the flow of each river in spring, summer, autumn and winter?', [(bars([3, 3, 3, 3]), 160, 120), (bars([5, 3, 2, 1]), 160, 120), (bars([1, 2, 3, 5]), 160, 120), (bars([2, 5, 3, 1]), 160, 120)], [
  ('the Aru', 0, 'B', 'almost the same in all four seasons'),
  ('the Beru', 1, 'C', 'at its highest in spring'),
  ('the Ceru', 2, 'D', 'smallest in spring and grows with each season'),
  ('the Deru', 3, 'E', 'highest in summer'),
 ]),
 tfng([
  ('Zendia is an imaginary island nation.', 'T', 'A', 'imaginary island nation'),
  ('The Aru rises from an underground spring.', 'T', 'B', 'a large underground spring'),
  ('Building is banned within a kilometre of the Aru.', 'T', 'B', 'within a kilometre of its banks'),
  ('The flow of the Aru changes greatly between seasons.', 'F', 'B', 'almost the same in all four seasons'),
  ('The Beru is fed by melting snow.', 'T', 'C', 'melting snow in the mountains'),
  ('A dam stores water from the Beru.', 'T', 'C', 'built a dam'),
  ('The Ceru is lowest in winter.', 'F', 'D', 'reaching its maximum in winter'),
  ('The water of the Deru comes from glaciers.', 'T', 'E', 'glaciers high in the mountains'),
  ('The council plans to ban fishing on the Aru.', 'NG', 'B', 'Fishermen also value the river', 'No ban on fishing is mentioned.'),
 ]),
 mcq([
  ('Why does a dry summer make little difference to the Aru?', ['It is fed by rain that fell long ago.', 'It is very wide.', 'It is frozen.', 'It has a dam.'], 0, 'B', 'rain which fell on distant hills many years ago'),
  ('Why are the villages by the Beru at risk?', ['The spring flood is often violent.', 'The river is dry.', 'The dam is broken.', 'Glaciers are melting.'], 0, 'C', 'The spring flood is often violent'),
  ('Why does Dr Horak oppose a single national rule?', ['It would be too strict in one place and too generous in another.', 'It is too complicated.', 'It costs money.', 'It is illegal.'], 0, 'F', 'too strict in one place and too generous in another'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['River', 'Detail'],
  [['Aru', 'Supplies drinking water to the [[1]]'], ['Beru', 'Water is released slowly for [[2]] fields'], ['Ceru', 'Often floods the lower [[3]] in winter'], ['Deru', 'Glaciers melt fastest in [[4]]']],
  [(['capital'], 'B', 'the capital city'), (['farmers'], 'C', 'for farmers\' fields'), (['fields'], 'D', 'often floods the lower fields'), (['july'], 'E', 'July and August')], 1),
 feat('Match each statement with the correct river, A to D.', ['The Aru', 'The Beru', 'The Ceru', 'The Deru'], [
  ('It provides drinking water for the capital.', 0, 'B', 'drinking water to the capital city'),
  ('A dam controls it.', 1, 'C', 'built a dam'),
  ('It drains a region with thin soil.', 2, 'D', 'the soil is thin'),
  ('It may shrink as the climate warms.', 3, 'E', 'the glaciers are shrinking'),
 ]),
 multi('Which TWO measures are included in the plan for the Deru, according to paragraph G?', ['A study of the glaciers.', 'A proposal for a new reservoir.', 'A ban on farming.', 'A new canal to the sea.', 'A tax on fishermen.'], [0, 1], [('G', 'a study of the glaciers'), ('G', 'a proposal for a new reservoir')]),
 head(['Why river flow matters', 'A steady supply', 'A spring flood', 'A winter flood', 'A summer peak', 'Different rivers, different plans', 'The next step', 'The history of bridges', 'Swimming safely'],
  [('A', 0, 'affects farmers, fishermen, engineers and wildlife'), ('B', 1, 'The river Aru is the most reliable'), ('C', 2, 'The spring flood is often violent'), ('D', 3, 'in winter it often floods the lower fields'), ('E', 4, 'It is highest in summer'), ('F', 5, 'different strategies for different rivers'), ('G', 6, 'will be published next year')]),
 info([
  ('a reference to the filtering of rainwater through rock', 'B', 'filtering through the rock'),
  ('a reference to repeated floods', 'C', 'flooded several times'),
  ('a reference to thin soil', 'D', 'the soil is thin'),
  ('a prediction about summer flow', 'E', 'summer flow will fall'),
  ('a promise concerning fish', 'G', 'fish can pass'),
 ]),
 ends(['is protected from building.', 'is controlled by a dam.', 'often floods the lower fields.', 'led the survey.', 'is a glacier.', 'has no water.', 'dries up in winter.'], [
  ('The Aru', 0, 'B', 'banned building and farming'),
  ('The Beru', 1, 'C', 'built a dam'),
  ('The Ceru', 2, 'D', 'often floods the lower fields'),
  ('Dr Horak', 3, 'F', 'who led the survey'),
 ]),
 sent(2, [
  ('The Beru is a ___ river.', ['snow'], 'C', 'a snow river'),
  ('The Ceru drains a region in the ___.', ['south-west', 'southwest'], 'D', 'south-west'),
  ('Dr Horak is a river ___.', ['scientist'], 'F', 'river scientist'),
  ('Local farmers have formed a ___.', ['committee'], 'G', 'formed a committee'),
 ]),
 short(3, [
  ('What is the Beru in winter?', ['a trickle'], 'C', 'only a trickle'),
  ('When is the Deru at its highest?', ['summer', 'in summer'], 'E', 'highest in summer'),
  ('How often will farmers meet the planners?', ['every month'], 'G', 'every month'),
 ]),
])
