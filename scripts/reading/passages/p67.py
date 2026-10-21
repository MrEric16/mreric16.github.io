from lib import *
from svgs import *
A = """Tropical rainforests cover only about six per cent of the Earth's land, but they hold perhaps half of all the plant and animal species on the planet. They grow in a belt around the equator, in places such as the Amazon basin, the Congo basin and South-East Asia, where it is hot and wet throughout the year. A rainforest is not a uniform mass of trees but a tall structure with distinct layers, and each layer has its own climate, its own plants and its own animals. Scientists often compare it to a building with several floors, in which the residents of one floor may never visit another. This passage describes the four layers from top to bottom."""
B = """The highest layer is the emergent layer, formed by a few giant trees that rise above the rest of the forest, sometimes to sixty metres or more, higher than a twenty-storey building. These trees stand in full sunlight, and they are exposed to strong winds, heat and dryness, so that their leaves are small and thick. Eagles and other large birds nest in their crowns, and certain monkeys and bats travel among them. Few animals live permanently in this layer, since there is little shelter, and the creatures that do must be able to cope with the extremes of weather."""
C = """Below it lies the canopy, a thick roof of leaves and branches about thirty to forty-five metres above the ground. This is the busiest layer of the forest. It captures most of the sunlight, and so most of the flowers and fruit grow here, attracting an enormous variety of animals: monkeys, parrots, tree frogs, sloths and countless insects. Some animals spend their entire lives in the canopy without ever touching the ground. The branches are linked by climbing plants, called lianas, which act as ropes and bridges, and the leaves collect rainwater in small pools that become homes for insects and frogs."""
D = """Beneath the canopy is the understory, a dim and humid layer, where only a small fraction of the sunlight arrives. The plants that grow here, such as young trees, ferns and shrubs, have large leaves to catch what little light is available. The air is still and moist, and it is home to snakes, jaguars and many insects, which hunt among the trunks. Many of the animals of the understory are coloured to blend with the leaves and the shadows, and they move slowly and quietly. Seedlings of canopy trees wait here for years, growing slowly, until a falling tree opens a gap in the roof and lets the light in."""
E = """The forest floor is the darkest place of all; as little as two per cent of the sunlight reaches it, and few plants can grow there. The ground is covered with fallen leaves, fruit and dead wood, which rot very quickly in the warm, damp air, within weeks and not years. Fungi, termites and bacteria break down this material, and the nutrients are absorbed at once by the shallow roots of the trees, so that the soil itself is surprisingly thin and poor. Large animals, such as tapirs and wild pigs, walk here, together with enormous numbers of ants and beetles."""
F = """Dr Carlos Ferreira, an ecologist who has spent twenty years studying rainforests, says that the layers depend on each other. The canopy shades the floor and keeps it humid, the floor feeds the canopy by recycling nutrients, and animals carry seeds from one layer to another. When people cut down the large trees, the effect spreads to the whole structure: the floor dries out, the soil washes away in heavy rain, and the animals that need the canopy disappear. He adds that a forest which has been cleared may need several centuries to recover, if it recovers at all."""
G = """Despite these dangers, there are encouraging signs. Several countries have created national parks and banned logging in the most valuable areas, and some companies now buy only timber that has been cut with care. Local communities, who know the forest better than anyone, are increasingly given the right to manage it. Dr Ferreira believes that the key is to show that a living forest is worth more than a cleared one: it produces fruit, medicines and fresh water, it attracts tourists and it stores carbon dioxide. If people see the value, he says, they will protect it."""
S, PT, W, H = layers(4)
P = passage('p67', 'Layers of the Rainforest', 'Ecology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Rainforests cover about six per cent of the Earth\'s land.', 'T', 'A', 'about six per cent'),
  ('Rainforests grow in a belt around the equator.', 'T', 'A', 'a belt around the equator'),
  ('Emergent trees can reach sixty metres.', 'T', 'B', 'sixty metres or more'),
  ('Many animals live permanently in the emergent layer.', 'F', 'B', 'Few animals live permanently'),
  ('Most flowers and fruit grow in the canopy.', 'T', 'C', 'most of the flowers and fruit grow here'),
  ('Lianas are climbing plants.', 'T', 'C', 'climbing plants, called lianas'),
  ('The understory receives plenty of sunlight.', 'F', 'D', 'only a small fraction of the sunlight'),
  ('Fallen leaves rot within weeks.', 'T', 'E', 'within weeks and not years'),
  ('Dr Ferreira was born in Brazil.', 'NG', 'F', 'Dr Carlos Ferreira', 'His birthplace is not given.'),
 ]),
 mcq([
  ('Why do emergent trees have small, thick leaves?', ['They are exposed to wind, heat and dryness.', 'They need little light.', 'They are young.', 'They grow slowly.'], 0, 'B', 'exposed to strong winds, heat and dryness'),
  ('What waits in the understory for years?', ['Seedlings of canopy trees.', 'Eagles.', 'Lianas.', 'Tapirs.'], 0, 'D', 'Seedlings of canopy trees wait here for years'),
  ('Why is the forest soil thin and poor?', ['Roots absorb nutrients at once.', 'Rain washes it away daily.', 'It is frozen.', 'Animals eat it.'], 0, 'E', 'absorbed at once by the shallow roots'),
 ]),
 diag('Label the layers of the rainforest, from the highest to the lowest. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['emergent'], 'B', 'is the emergent layer'), (['canopy'], 'C', 'lies the canopy'), (['understory'], 'D', 'is the understory'), (['floor'], 'E', 'The forest floor')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Layer', 'Detail'],
  [['Emergent', 'Eagles nest in the [[1]]'], ['Canopy', 'Leaves collect rainwater in small [[2]]'], ['Understory', 'Plants have large [[3]] to catch light'], ['Floor', 'Fungi, termites and [[4]] break down dead material']],
  [(['crowns'], 'B', 'nest in their crowns'), (['pools'], 'C', 'small pools'), (['leaves'], 'D', 'large leaves'), (['bacteria'], 'E', 'termites and bacteria')], 1),
 multi('Which TWO animals of the canopy are mentioned in paragraph C?', ['Monkeys.', 'Parrots.', 'Jaguars.', 'Tapirs.', 'Eagles.'], [0, 1], [('C', 'monkeys'), ('C', 'parrots')]),
 head(['A building with floors', 'Above the forest', 'The busy roof', 'A dim middle', 'The dark ground', 'A web of dependence', 'Reasons for hope', 'The history of timber', 'Crossing a river'],
  [('A', 0, 'a building with several floors'), ('B', 1, 'giant trees that rise above the rest of the forest'), ('C', 2, 'the busiest layer of the forest'), ('D', 3, 'a dim and humid layer'), ('E', 4, 'The forest floor is the darkest place of all'), ('F', 5, 'the layers depend on each other'), ('G', 6, 'there are encouraging signs')]),
 info([
  ('a comparison with a tall building', 'B', 'twenty-storey building'),
  ('a reference to ropes and bridges', 'C', 'ropes and bridges'),
  ('a reference to camouflage', 'D', 'blend with the leaves'),
  ('a figure for the sunlight reaching the ground', 'E', 'two per cent'),
  ('a reference to centuries of recovery', 'F', 'several centuries'),
 ]),
 ends(['stand in full sunlight.', 'captures most of the sunlight.', 'wait for a gap in the roof.', 'are given the right to manage the forest.', 'live on the forest floor only.', 'are made of lianas.', 'cut down all trees.'], [
  ('Emergent trees', 0, 'B', 'stand in full sunlight'),
  ('The canopy', 1, 'C', 'captures most of the sunlight'),
  ('Seedlings', 2, 'D', 'opens a gap in the roof'),
  ('Local communities', 3, 'G', 'right to manage it'),
 ]),
 sent(2, [
  ('The rainforest is compared to a ___ with several floors.', ['building'], 'A', 'a building with several floors'),
  ('Climbing plants in the canopy are called ___.', ['lianas'], 'C', 'lianas'),
  ('Fungi, termites and ___ break down dead material.', ['bacteria'], 'E', 'termites and bacteria'),
  ('Dr Ferreira is an ___.', ['ecologist'], 'F', 'an ecologist'),
 ]),
 short(3, [
  ('How tall can emergent trees grow?', ['sixty metres'], 'B', 'sixty metres or more'),
  ('Which animals walk on the forest floor?', ['tapirs'], 'E', 'tapirs and wild pigs'),
  ('What does a living forest store?', ['carbon dioxide'], 'G', 'carbon dioxide'),
 ]),
])
