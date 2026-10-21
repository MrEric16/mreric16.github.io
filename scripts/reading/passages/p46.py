from lib import *
from svgs import *
A = """Houses are shaped by the places in which they are built. Walk through any town in the world, and you will notice how the roofs differ: some are flat, others steeply sloped, and some rise into domes or tall points. Architects and builders did not choose these shapes only for their appearance. Most roof types were developed over centuries to deal with local weather, to use the materials that were available, and to meet the needs of those who lived beneath them. In this passage, five basic types are described, from the simple flat roof to the tall spire, and the effects of modern materials and of the changing climate are considered at the end."""
B = """In hot, dry regions, such as the deserts of the Middle East and North Africa, houses usually have flat roofs. There is little rain, so the water does not need to run off, and a flat roof is simple to build from mud brick and wooden beams. It also serves as an extra room. In summer, families sleep on it to escape the heat of the night, and in the daytime it is used for drying fruit, washing and storing grain."""
C = """In places where there is heavy rain or snow, the roof is usually pitched, which means that it slopes steeply from a central ridge down to the walls on each side. Rain runs off quickly, and snow slides to the ground instead of piling up and breaking the roof. In the mountains of Switzerland and Norway, roofs may be inclined at an angle of forty-five degrees or more, and many have a wide overhang to protect the walls from melting snow."""
D = """A dome is a different solution, and it is found mainly on large public buildings. The Romans perfected the technique, and their Pantheon, built about 1,900 years ago, has a dome that remains the largest unreinforced concrete dome in the world. Domes were later used for mosques, such as those in Samarkand and Istanbul, and for churches and observatories. Because a dome has no corners, it distributes its weight evenly, and it can cover a large space without internal columns."""
E = """The spire is tall and thin, narrowing to a point. It is common on churches in Europe, where it rises above the town as a landmark and, in the Middle Ages, as a sign of the builders' devotion. The tallest spires, such as that of Ulm Minster in Germany at 161 metres, took generations to complete. Because they are exposed to wind and lightning, they are fitted with iron frames and conductors, and every few decades they require expensive repairs. Many have needed major repairs, and some have been rebuilt completely after fires or wars."""
F = """Modern materials have changed the pattern. With steel and reinforced concrete, builders can cover wide areas with flat roofs even in rainy countries, using waterproof membranes to keep the water out. Roofs may also be planted with grass and flowers, which cool the building in summer and reduce flooding in cities by absorbing rainwater. Dr Elif Demir, an architect, believes that the roof, long neglected as a mere cover, may become one of the most useful parts of the city building."""
G = """Climate change is likely to alter roof design once again. In countries where the summers are becoming hotter, designers are rediscovering white and reflective surfaces, which bounce back the sunlight, and shaded terraces. In regions that are expected to receive more heavy rain, drainage is being redesigned. Roofs are also being fitted with solar panels in large numbers, and some countries now require them on new houses. The oldest part of the building is thus becoming the newest."""
P = passage('p46', 'Roofs Around the World', 'Architecture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which roof, A to D, is described in each paragraph of the passage?', [(roof('flat'), 160, 120), (roof('pitched'), 160, 120), (roof('dome'), 160, 120), (roof('spire'), 160, 120)], [
  ('a roof used for sleeping in summer', 0, 'B', 'families sleep on it'),
  ('a roof that lets snow slide off', 1, 'C', 'snow slides to the ground'),
  ('a roof with no corners that needs no columns', 2, 'D', 'Because a dome has no corners'),
  ('a roof that is tall and narrows to a point', 3, 'E', 'narrowing to a point'),
 ]),
 tfng([
  ('Roof shapes were chosen only for their appearance.', 'F', 'A', 'did not choose these shapes only for their appearance'),
  ('Flat roofs are common in hot, dry regions.', 'T', 'B', 'houses usually have flat roofs'),
  ('Flat roofs in deserts are made from steel.', 'F', 'B', 'mud brick and wooden beams'),
  ('Pitched roofs slope from a central ridge.', 'T', 'C', 'from a central ridge down to the walls'),
  ('Swiss roofs may slope at forty-five degrees or more.', 'T', 'C', 'forty-five degrees or more'),
  ('The Pantheon\'s dome is made of reinforced concrete.', 'F', 'D', 'unreinforced concrete'),
  ('The Pantheon is in Rome.', 'NG', 'D', 'The Romans perfected the technique, and their Pantheon', 'The city is not named in the passage.'),
  ('Spires need regular repairs.', 'T', 'E', 'require expensive repairs'),
  ('Green roofs help reduce flooding.', 'T', 'F', 'reduce flooding in cities by absorbing rainwater'),
 ]),
 mcq([
  ('Why are flat roofs suitable for deserts?', ['They look beautiful.', 'There is little rain.', 'They are cold.', 'They are made of glass.'], 1, 'B', 'There is little rain'),
  ('Why do domes need no internal columns?', ['They are small.', 'They spread their weight evenly.', 'They are made of wood.', 'They have windows.'], 1, 'D', 'distributes its weight evenly'),
  ('What is the benefit of a reflective roof?', ['It collects water.', 'It bounces back sunlight.', 'It stores snow.', 'It makes noise.'], 1, 'G', 'bounce back the sunlight'),
 ]),
 multi('Which TWO uses of a flat roof are mentioned in paragraph B?', ['Sleeping.', 'Drying fruit.', 'Keeping animals.', 'Growing trees.', 'Playing football.'], [0, 1], [('B', 'families sleep on it'), ('B', 'drying fruit')]),
 head(['Why roofs differ', 'Roofs for heat and dust', 'Roofs for rain and snow', 'Roofs for great spaces', 'Roofs that point to the sky', 'Roofs and modern materials', 'Roofs and a warmer planet', 'The history of glass', 'How to build a house'],
  [('A', 0, 'Most roof types were developed over centuries'), ('B', 1, 'In hot, dry regions'), ('C', 2, 'where there is heavy rain or snow'), ('D', 3, 'A dome is a different solution'), ('E', 4, 'The spire is tall and thin'), ('F', 5, 'Modern materials have changed the pattern'), ('G', 6, 'Climate change is likely to alter roof design once again')]),
 info([
  ('a reference to local materials', 'A', 'to use the materials that were available'),
  ('a mention of a country with steep roofs', 'C', 'Switzerland and Norway'),
  ('an example of a city with domed mosques', 'D', 'Samarkand and Istanbul'),
  ('a reference to a tall spire in Germany', 'E', 'Ulm Minster in Germany at 161 metres'),
  ('a mention of an architect', 'F', 'Dr Elif Demir'),
 ]),
 sent(2, [
  ('A flat roof is simple to build from mud ___ and wooden beams.', ['brick'], 'B', 'mud brick'),
  ('In the mountains of Switzerland and Norway many roofs have a wide ___.', ['overhang'], 'C', 'a wide overhang'),
  ('The ___ built the Pantheon.', ['romans'], 'D', 'The Romans'),
  ('Roofs may be planted with grass and ___.', ['flowers'], 'F', 'grass and flowers'),
 ]),
 short(3, [
  ('What protects spires from lightning?', ['conductors'], 'E', 'iron frames and conductors'),
  ('What do some countries require on new houses?', ['solar panels'], 'G', 'solar panels'),
  ('How old is the Pantheon?', ['1,900 years'], 'D', 'about 1,900 years ago'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Flat roofs suit dry regions, while [[1]] roofs suit rain and snow. Domes spread weight [[2]] and cover large spaces. Modern roofs may be planted with [[3]] or fitted with solar [[4]].',
  [(['pitched'], 'C', 'the roof is usually pitched'), (['evenly'], 'D', 'distributes its weight evenly'), (['grass'], 'F', 'grass and flowers'), (['panels'], 'G', 'solar panels')], 1,
  bank=['pitched', 'evenly', 'grass', 'panels', 'flat', 'rarely', 'stone', 'glass']),
])
