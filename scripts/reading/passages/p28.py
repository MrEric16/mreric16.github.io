from lib import *
from svgs import *
A = """The water on our planet is very old. The same water that dinosaurs drank is still here today, because water is not made or destroyed but moves constantly between the sea, the air and the land. This endless movement is called the water cycle. It is driven by the heat of the Sun and by the force of gravity, and it has no beginning or end, although it is usually described as a series of four stages. Understanding the cycle helps scientists to predict floods and droughts and to plan the use of rivers and lakes."""
B = """The first stage is evaporation. When the Sun heats the surface of the oceans, lakes and rivers, some of the liquid water turns into an invisible gas called water vapour and rises into the air. About ninety per cent of the water vapour in the atmosphere comes from the oceans. Plants add to it by releasing water through tiny holes in their leaves, a process known as transpiration, and a single large tree can release hundreds of litres of water on a hot day."""
C = """As the warm, moist air rises, it cools. Cold air cannot hold as much water vapour as warm air, so the vapour changes back into tiny drops of liquid water. This is condensation. The drops gather around specks of dust and form clouds, and in very cold air they freeze into crystals of ice. You can see condensation at home when the mirror in a bathroom becomes misty after a hot shower, or when drops appear on the outside of a cold glass of water."""
D = """When the drops in a cloud grow too heavy to stay in the air, they fall as precipitation. Rain is the most common form, but precipitation may also be snow, sleet or hail, depending on the temperature. The amount varies enormously from place to place. Some towns in the mountains of India receive more than eleven metres of rain a year, while parts of the Atacama Desert in Chile may wait for several years between showers, and some weather stations there have never recorded any rain at all."""
E = """After it reaches the ground, the water follows many different paths. Some runs over the surface into streams and rivers, which carry it back to the sea. Some soaks into the soil and becomes groundwater, which may stay underground for thousands of years before it emerges at a spring. Water that falls as snow on high mountains can be locked up in glaciers for centuries. This stage is known as collection, since the water gathers again in rivers, lakes, oceans and underground stores."""
F = """Humans interfere with the cycle in many ways. Cutting down forests reduces transpiration, so that less moisture returns to the air, and the climate of the region may become drier. Dams hold back water that would otherwise flow to the sea, and cities with paved streets prevent rain from soaking into the soil, so it rushes into drains and may cause floods. Farmers who pump groundwater faster than it is replaced can lower the water table, and wells that once supplied villages may run dry."""
G = """Climate change is now altering the cycle itself. A warmer atmosphere holds more water vapour, so storms are becoming heavier in many regions, while other places face longer droughts. Glaciers are melting, which provides extra water for rivers at first but threatens the supply of millions of people in the long term. Professor David Okoye, a hydrologist, says that the central lesson of the water cycle is that every drop is connected to every other, and that what is done to the water in one place will sooner or later affect another."""
S, PT, W, H = cycle(4)
P = passage('p28', 'The Water Cycle', 'Earth science', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Water on the Earth is constantly being destroyed.', 'F', 'A', 'water is not made or destroyed'),
  ('The water cycle is usually described in four stages.', 'T', 'A', 'a series of four stages'),
  ('Most water vapour in the atmosphere comes from the oceans.', 'T', 'B', 'About ninety per cent of the water vapour in the atmosphere comes from the oceans'),
  ('Plants release water through their roots.', 'F', 'B', 'tiny holes in their leaves'),
  ('Warm air can hold more water vapour than cold air.', 'T', 'C', 'Cold air cannot hold as much water vapour as warm air'),
  ('Clouds form around specks of dust.', 'T', 'C', 'gather around specks of dust'),
  ('Some weather stations in the Atacama Desert have never recorded rain.', 'T', 'D', 'have never recorded any rain at all'),
  ('Groundwater always reaches the surface within a few years.', 'F', 'E', 'stay underground for thousands of years'),
  ('Dams make floods less likely in cities.', 'NG', 'F', 'Dams hold back water that would otherwise flow to the sea', 'The effect of dams on city floods is not discussed.'),
 ]),
 mcq([
  ('What drives the water cycle?', ['Wind and tides.', 'The Sun and gravity.', 'Rivers and lakes.', 'Plants and animals.'], 1, 'A', 'driven by the heat of the Sun and by the force of gravity'),
  ('What happens when a cloud\'s drops become too heavy?', ['They evaporate.', 'They freeze.', 'They fall as precipitation.', 'They form vapour.'], 2, 'D', 'grow too heavy to stay in the air, they fall as precipitation'),
  ('What is the effect of cutting down forests?', ['More rain falls.', 'Less moisture returns to the air.', 'Rivers become wider.', 'The Sun becomes hotter.'], 1, 'F', 'less moisture returns to the air'),
 ]),
 multi('Which TWO everyday examples of condensation are given in paragraph C?', ['A misty bathroom mirror.', 'Drops on a cold glass.', 'A boiling kettle.', 'A frozen lake.', 'Wet clothes drying.'], [0, 1], [('C', 'the mirror in a bathroom becomes misty'), ('C', 'drops appear on the outside of a cold glass of water')]),
 head(['A cycle without an end', 'Water rising into the air', 'Vapour turning back into drops', 'Water falling from the sky', 'The many routes back to the sea', 'The effect of human actions', 'A changing climate', 'The life of a river fish', 'How to make rain'],
  [('A', 0, 'This endless movement is called the water cycle'), ('B', 1, 'The first stage is evaporation'), ('C', 2, 'This is condensation'), ('D', 3, 'they fall as precipitation'), ('E', 4, 'the water follows many different paths'), ('F', 5, 'Humans interfere with the cycle in many ways'), ('G', 6, 'Climate change is now altering the cycle itself')]),
 info([
  ('a reference to creatures that lived long ago', 'A', 'The same water that dinosaurs drank'),
  ('a name for the release of water by leaves', 'B', 'transpiration'),
  ('a list of forms of precipitation', 'D', 'snow, sleet or hail'),
  ('a mention of a place where rain may not fall for years', 'D', 'the Atacama Desert in Chile'),
  ('a description of water locked in ice', 'E', 'locked up in glaciers for centuries'),
 ]),
 ends(['is called evaporation.', 'is called condensation.', 'is called precipitation.', 'is called collection.', 'is called transpiration.', 'is called groundwater.', 'is called a glacier.'], [
  ('The change of liquid water into vapour', 0, 'B', 'The first stage is evaporation'),
  ('The change of vapour into drops', 1, 'C', 'This is condensation'),
  ('Rain, snow, sleet or hail falling', 2, 'D', 'they fall as precipitation'),
  ('Water gathering in rivers, lakes and seas', 3, 'E', 'This stage is known as collection'),
 ]),
 diag('Label the stages of the water cycle, going clockwise from the top. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['evaporation'], 'B', 'The first stage is evaporation'), (['condensation'], 'C', 'This is condensation'), (['precipitation'], 'D', 'they fall as precipitation'), (['collection'], 'E', 'known as collection')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['The Sun heats the oceans, and liquid water becomes water [[1]].', 'The vapour rises and cools, forming tiny [[2]] and then clouds.', 'The drops grow heavy and fall as [[3]].', 'The water gathers in rivers, lakes, oceans and [[4]] stores.'],
  [(['vapour'], 'B', 'called water vapour'), (['drops'], 'C', 'tiny drops of liquid water'), (['precipitation', 'rain'], 'D', 'they fall as precipitation'), (['underground'], 'E', 'underground stores')], 1),
 sent(2, [
  ('A large tree can release hundreds of ___ of water on a hot day.', ['litres'], 'B', 'hundreds of litres'),
  ('In very cold air the drops freeze into crystals of ___.', ['ice'], 'C', 'crystals of ice'),
  ('Water that soaks into the soil becomes ___.', ['groundwater'], 'E', 'becomes groundwater'),
  ('A warmer atmosphere holds more water ___.', ['vapour'], 'G', 'more water vapour'),
 ]),
 short(3, [
  ('How much rain do some Indian mountain towns receive a year?', ['eleven metres', '11 metres'], 'D', 'more than eleven metres of rain a year'),
  ('What can lower the water table?', ['pump groundwater', 'pumping groundwater'], 'F', 'pump groundwater faster'),
  ('What is Professor Okoye\'s subject?', ['hydrology', 'hydrologist'], 'G', 'a hydrologist'),
 ]),
])
