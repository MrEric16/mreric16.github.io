from lib import *
from svgs import *
A = """A home is a shelter first of all, and the shape of a traditional house usually tells us about the climate, the materials and the way of life of the people who built it. Across the world, people have invented hundreds of designs, from houses on stilts to homes dug into hillsides, and many are still used today. This passage looks at four traditional homes, each of which has a distinctive roof: a flat-roofed house of mud, a pitched-roof house of wood, a domed shelter of snow and a cone-shaped tent. Each is a clever solution to a problem that people faced in their own environment, and each has lessons for modern architects."""
B = """In dry regions, such as the edge of the Sahara, the Middle East and parts of Central Asia, people built houses with thick walls of mud bricks and a flat roof. Mud is cheap and plentiful, and a wall half a metre thick keeps the heat out during the day and holds it in at night, so that the rooms stay comfortable even when the temperature outside changes by twenty degrees. Because rain is rare, there is no need for a sloping roof. The flat roof is a useful extra room, where families dry fruit and sleep on hot summer nights. The weak point is rain: a heavy storm can wash away the mud, and the roof must be repaired every year."""
C = """In forested, rainy lands, such as Scandinavia and Japan, people built houses of timber with steep, pitched roofs. A steep roof sheds rain and snow quickly, which prevents the weight of snow from crushing the house. Wood is a good insulator, and a thick roof of thatch, turf or wooden tiles keeps out the cold. Some of these houses are raised on stone or wooden supports, to protect the wood from damp. In Japan, the roofs of old farmhouses are so steep that people call the style praying hands, and the space beneath them was used for raising silkworms."""
D = """In the Arctic, the Inuit built temporary winter shelters of snow, called igloos. The builder cut blocks of hard snow with a long knife and laid them in a rising spiral, each block leaning slightly inwards, until the walls met at the top in a dome. A dome is the strongest shape for a roof of blocks, because the weight presses the pieces together. Snow is a better insulator than most people expect, since it is full of trapped air; inside an igloo heated only by a small lamp, the temperature may be close to zero while outside it falls to minus forty. A skilled builder could make an igloo in about an hour."""
E = """The nomads of the North American plains lived in tipis, tents shaped like cones. A tipi has a frame of long wooden poles tied together at the top, covered with animal skins, and it has an opening at the top through which the smoke from a fire escapes. The cone is a good shape for wind, because a strong gust slides around it, and when the weather becomes hot, the bottom edge can be lifted for air to pass through. The most important advantage, however, is that a family could take it down in less than half an hour and carry it on horses to follow the herds of buffalo."""
F = """In Central Asia, nomads in Kazakhstan, Kyrgyzstan and Mongolia developed another kind of portable home, the yurt. It has a circular wall of folding wooden lattice, a roof of curved poles meeting in a wheel at the top, and a covering of thick felt made from sheep's wool. The roof is rounded like a low dome. A yurt is warm in the winter, cool in the summer, and so strong that it can withstand fierce steppe winds. It can be taken apart and loaded on to camels or horses in a few hours. Today, many families still keep a yurt for the summer pastures, and tourists stay in them."""
G = """Dr Leila Haddad, an architect who studies traditional buildings, says that modern designers have much to learn. Each of these homes uses local materials, requires little energy, and is suited exactly to its climate. Modern glass buildings, by contrast, often need air-conditioning all year round. She does not suggest that people should return to mud and felt, but argues that new houses should borrow the ideas: thick walls in hot countries, steep roofs where snow falls, and materials that can be found nearby. Some builders have already begun to follow her advice, and several new schools in dry regions are built of rammed earth."""
P = passage('p61', 'Homes Around the World', 'Architecture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which roof shape, A to D, belongs to each home?', [(roof('flat'), 160, 120), (roof('pitched'), 160, 120), (roof('dome'), 160, 120), (roof('spire'), 160, 120)], [
  ('the mud house', 0, 'B', 'a flat roof'),
  ('the timber house', 1, 'C', 'steep, pitched roofs'),
  ('the igloo', 2, 'D', 'the walls met at the top in a dome'),
  ('the tipi', 3, 'E', 'tents shaped like cones'),
 ]),
 tfng([
  ('Traditional houses reflect the climate where they are built.', 'T', 'A', 'the climate'),
  ('Mud walls keep heat out during the day.', 'T', 'B', 'keeps the heat out during the day'),
  ('Flat roofs of mud are good in heavy rain.', 'F', 'B', 'a heavy storm can wash away the mud'),
  ('Steep roofs shed snow quickly.', 'T', 'C', 'sheds rain and snow quickly'),
  ('In Japan, the space under steep roofs was used for raising silkworms.', 'T', 'C', 'raising silkworms'),
  ('Igloo blocks are laid in a rising spiral.', 'T', 'D', 'a rising spiral'),
  ('A tipi takes several days to take down.', 'F', 'E', 'less than half an hour'),
  ('A yurt is covered with felt.', 'T', 'F', 'thick felt'),
  ('Yurts are cheaper than tipis.', 'NG', 'F', 'another kind of portable home', 'Cost is not compared.'),
 ]),
 mcq([
  ('Why is a dome a strong shape?', ['The weight presses the blocks together.', 'It is made of stone.', 'It is small.', 'It is flat.'], 0, 'D', 'the weight presses the pieces together'),
  ('Why is the cone a good shape for wind?', ['A strong gust slides around it.', 'It has no door.', 'It is heavy.', 'It is underground.'], 0, 'E', 'a strong gust slides around it'),
  ('What does Dr Haddad suggest?', ['Return to mud and felt.', 'Borrow ideas from traditional homes.', 'Ban glass.', 'Build more igloos.'], 1, 'G', 'new houses should borrow the ideas'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Home', 'Detail'],
  [['Mud house', 'Walls half a metre [[1]]'], ['Timber house', 'Raised on [[2]] to protect from damp'], ['Igloo', 'Made of blocks of [[3]]'], ['Yurt', 'Covered with [[4]]']],
  [(['thick'], 'B', 'half a metre thick'), (['supports'], 'C', 'wooden supports'), (['snow'], 'D', 'blocks of hard snow'), (['felt'], 'F', 'thick felt')], 1),
 feat('Match each statement with the correct home, A to D.', ['Mud house', 'Timber house', 'Igloo', 'Yurt'], [
  ('Families sleep on the roof on hot nights.', 0, 'B', 'sleep on hot summer nights'),
  ('The style is called praying hands in Japan.', 1, 'C', 'praying hands'),
  ('A skilled builder could make it in about an hour.', 2, 'D', 'about an hour'),
  ('It has a roof of curved poles meeting in a wheel.', 3, 'F', 'meeting in a wheel at the top'),
 ]),
 multi('Which TWO advantages of the tipi are given in paragraph E?', ['Strong gusts slide around it.', 'It can be taken down in less than half an hour.', 'It is made of stone.', 'It is cooler than a yurt.', 'It has glass windows.'], [0, 1], [('E', 'a strong gust slides around it'), ('E', 'less than half an hour')]),
 head(['Houses and their environments', 'Mud for the desert', 'Timber for the forest', 'Snow as a building material', 'A cone for the plains', 'A home of felt on the steppe', 'What modern builders can learn', 'The history of glass', 'Furniture design'],
  [('A', 0, 'tells us about the climate'), ('B', 1, 'thick walls of mud bricks and a flat roof'), ('C', 2, 'houses of timber with steep, pitched roofs'), ('D', 3, 'blocks of hard snow'), ('E', 4, 'tents shaped like cones'), ('F', 5, 'a covering of thick felt'), ('G', 6, 'modern designers have much to learn')]),
 info([
  ('a reference to yearly repairs', 'B', 'repaired every year'),
  ('a list of roof materials', 'C', 'thatch, turf or wooden tiles'),
  ('a reference to a source of heat in an igloo', 'D', 'a small lamp'),
  ('a reference to following herds', 'E', 'follow the herds of buffalo'),
  ('a reference to schools built of earth', 'G', 'rammed earth'),
 ]),
 ends(['keep rooms comfortable.', 'may stand on supports.', 'lean slightly inwards.', 'can withstand steppe winds.', 'are made of glass.', 'float on water.', 'were built by Dr Haddad.'], [
  ('Mud walls', 0, 'B', 'keeps the heat out during the day'),
  ('Timber houses', 1, 'C', 'raised on stone or wooden supports'),
  ('Igloo blocks', 2, 'D', 'leaning slightly inwards'),
  ('Yurts', 3, 'F', 'withstand fierce steppe winds'),
 ]),
 sent(2, [
  ('The Inuit shelter of snow is called an ___.', ['igloo'], 'D', 'called igloos'),
  ('A tipi has an opening at the top for ___.', ['smoke'], 'E', 'smoke from a fire'),
  ('A yurt is covered with ___ made from sheep\'s wool.', ['felt'], 'F', 'thick felt'),
  ('Dr Haddad is an ___.', ['architect'], 'G', 'an architect'),
 ]),
 short(3, [
  ('What do families dry on the flat roof?', ['fruit'], 'B', 'dry fruit'),
  ('What does snow contain that insulates?', ['trapped air', 'air'], 'D', 'trapped air'),
  ('Who stays in yurts today?', ['tourists'], 'F', 'tourists stay in them'),
 ]),
])
