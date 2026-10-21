from lib import *
from svgs import *
A = """Water covers about seventy per cent of the surface of the Earth, but almost all of it is in the oceans and is too salty to drink. Only about three per cent is fresh, and most of that is locked in ice at the poles and in glaciers, or lies deep underground. The small amount that remains in rivers, lakes and the air is, however, enough to support all life on land, because water is not used up. It moves continuously between the oceans, the air and the land in a process called the water cycle, which has been working for billions of years and which has no real beginning or end."""
B = """The cycle is driven by the sun. Its heat warms the surface of oceans, lakes and rivers, and some of the liquid water turns into an invisible gas called water vapour. This change is called evaporation. About eighty-six per cent of all evaporation takes place over the oceans, and it happens faster when the weather is hot, dry and windy. Plants also release vapour through tiny holes in their leaves, a process known as transpiration. A single large tree can release hundreds of litres of water into the air on a hot day, so forests have an important effect on the climate and on the amount of rain that falls nearby."""
C = """As the water vapour rises, it meets colder air and cools. Cool air cannot hold as much vapour as warm air, so the vapour turns back into tiny drops of liquid water, a change called condensation. The drops gather around specks of dust, salt or smoke in the air and form clouds. Fog is simply a cloud that touches the ground. The drops in a cloud are so small and light that they stay in the air, and a typical cloud may contain hundreds of tonnes of water. Clouds are carried over great distances by the wind, which is how water that evaporated from the sea can fall on a mountain hundreds of kilometres from the coast."""
D = """When the drops in a cloud join together and become too heavy to float, they fall as precipitation. This may be rain, snow, sleet or hail, depending on the temperature of the air through which the water falls. Snow forms when the air is below freezing, and hail forms when strong currents carry drops up and down inside a storm cloud so that layers of ice build up around them. The amount of precipitation varies enormously around the world. Some places in the desert may receive less than twenty millimetres in a year, while a few mountain villages in tropical regions receive more than ten metres, which is the reason why some regions flood and others suffer from drought."""
E = """Rain that reaches the ground follows several routes. Some runs over the surface into streams and rivers, which carry it back to the sea; this is known as runoff. Some soaks into the soil, where it feeds plants or sinks deeper to become groundwater, stored in layers of rock called aquifers. Snow and ice can hold water for thousands of years before they melt. The time that a water molecule spends in each place differs greatly: a drop may stay in the atmosphere for about nine days, but in a deep aquifer or a large ice sheet it may remain for ten thousand years or more."""
F = """People have changed the cycle in many ways. Dams store water and slow rivers, irrigation sends large amounts of water into the air from fields, and cities cover the ground with concrete, so that rain runs off quickly instead of soaking in. Dr Helena Okafor, a hydrologist, says that the greatest change is the removal of groundwater: in many regions people now pump water from aquifers far faster than rain can refill them. She warns that wells in these areas may run dry within a generation, and that careful management of water is more urgent than ever for farmers, cities and industry alike."""
G = """Climate change is also altering the cycle. A warmer atmosphere holds more water vapour, which means that storms can produce heavier rain, and floods are becoming more common in many regions. At the same time, higher temperatures cause faster evaporation from soil, making droughts longer and more severe. Mountain glaciers, which act as natural reservoirs by storing winter snow and releasing it slowly in summer, are shrinking in most parts of the world. Scientists are working to measure these changes with satellites, which can track clouds, rainfall and even the level of groundwater from space, and to use the data to plan for the future."""
S, PT, W, H = cycle(4)
P = passage('p59', 'The Journey of Water', 'Earth science', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Most of the water on Earth is too salty to drink.', 'T', 'A', 'almost all of it is in the oceans and is too salty to drink'),
  ('About three per cent of the Earth\'s water is fresh.', 'T', 'A', 'about three per cent is fresh'),
  ('Water is used up when plants and animals drink it.', 'F', 'A', 'water is not used up'),
  ('Most evaporation takes place over land.', 'F', 'B', 'eighty-six per cent of all evaporation takes place over the oceans'),
  ('Plants release vapour through their leaves.', 'T', 'B', 'Plants also release vapour through tiny holes in their leaves'),
  ('Fog is a cloud that touches the ground.', 'T', 'C', 'Fog is simply a cloud that touches the ground'),
  ('Hail forms in strong currents inside storm clouds.', 'T', 'D', 'strong currents carry drops up and down inside a storm cloud'),
  ('Water stays in the atmosphere longer than in an ice sheet.', 'F', 'E', 'in a deep aquifer or a large ice sheet it may remain for ten thousand years or more'),
  ('Water vapour is poisonous in large quantities.', 'NG', 'B', 'an invisible gas called water vapour', 'Poison is not mentioned.'),
 ]),
 mcq([
  ('Why do clouds stay in the air?', ['The drops are small and light.', 'They are warmer than the air.', 'The wind holds them.', 'They contain no water.'], 0, 'C', 'so small and light that they stay in the air'),
  ('What does Dr Okafor say is the greatest change?', ['More dams.', 'The removal of groundwater.', 'Colder weather.', 'Bigger cities.'], 1, 'F', 'the removal of groundwater'),
  ('Why are mountain glaciers called natural reservoirs?', ['They store snow and release it slowly.', 'They are made of salt.', 'They contain fish.', 'They are growing.'], 0, 'G', 'storing winter snow and releasing it slowly in summer'),
 ]),
 multi('Which TWO effects of climate change on the water cycle are mentioned in paragraph G?', ['Storms can produce heavier rain.', 'Droughts become longer and more severe.', 'Winters become colder.', 'Oceans become less salty.', 'Glaciers grow faster.'], [0, 1], [('G', 'storms can produce heavier rain'), ('G', 'making droughts longer and more severe')]),
 head(['Water that never disappears', 'Heat from the sun', 'Vapour becomes cloud', 'Water falls from the sky', 'Many routes and long waits', 'The human effect', 'A changing climate', 'The history of the oceans', 'How to make rain'],
  [('A', 0, 'water is not used up'), ('B', 1, 'The cycle is driven by the sun'), ('C', 2, 'the vapour turns back into tiny drops'), ('D', 3, 'they fall as precipitation'), ('E', 4, 'Rain that reaches the ground follows several routes'), ('F', 5, 'People have changed the cycle'), ('G', 6, 'Climate change is also altering the cycle')]),
 info([
  ('a figure for the proportion of water that is fresh', 'A', 'about three per cent is fresh'),
  ('a reference to the effect of forests on climate', 'B', 'forests have an important effect on the climate'),
  ('a description of how hail is formed', 'D', 'layers of ice build up around them'),
  ('an example of how long water may stay in the air', 'E', 'about nine days'),
  ('a reference to measuring change from space', 'G', 'track clouds, rainfall and even the level of groundwater from space'),
 ]),
 ends(['is caused by the heat of the sun.', 'form around specks of dust, salt or smoke.', 'are layers of rock that store groundwater.', 'store water and slow rivers.', 'are found only in deserts.', 'are made of ice.', 'are used up by plants.'], [
  ('Evaporation', 0, 'B', 'The cycle is driven by the sun'),
  ('Clouds', 1, 'C', 'The drops gather around specks of dust, salt or smoke in the air and form clouds'),
  ('Aquifers', 2, 'E', 'stored in layers of rock called aquifers'),
  ('Dams', 3, 'F', 'Dams store water and slow rivers'),
 ]),
 diag('Label the stages of the water cycle, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['evaporation'], 'B', 'This change is called evaporation'), (['condensation'], 'C', 'a change called condensation'), (['precipitation'], 'D', 'they fall as precipitation'), (['runoff'], 'E', 'this is known as runoff')], 1),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Process', 'Description'],
  [['Evaporation', 'Water turns into [[1]]'], ['Transpiration', 'Plants release vapour through their [[2]]'], ['Condensation', 'Vapour turns into drops around specks of [[3]]'], ['Runoff', 'Water flows into streams and [[4]]']],
  [(['vapour', 'water vapour'], 'B', 'called water vapour'), (['leaves'], 'B', 'holes in their leaves'), (['dust'], 'C', 'specks of dust'), (['rivers'], 'E', 'streams and rivers')], 2),
 sent(2, [
  ('Water covers about ___ per cent of the surface of the Earth.', ['seventy', '70'], 'A', 'about seventy per cent'),
  ('Some rain soaks into the soil and becomes ___.', ['groundwater'], 'E', 'become groundwater'),
  ('Dr Okafor is a ___.', ['hydrologist'], 'F', 'a hydrologist'),
  ('Satellites can track clouds, rainfall and the level of ___.', ['groundwater'], 'G', 'level of groundwater'),
 ]),
 short(3, [
  ('What is the release of vapour by plants called?', ['transpiration'], 'B', 'known as transpiration'),
  ('What are layers of rock that store groundwater called?', ['aquifers'], 'E', 'called aquifers'),
  ('What do mountain glaciers act as?', ['natural reservoirs'], 'G', 'natural reservoirs'),
 ]),
])
