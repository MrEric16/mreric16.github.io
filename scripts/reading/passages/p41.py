from lib import *
from svgs import *
A = """The ocean covers more than seventy per cent of the Earth's surface, and its average depth is about 3,700 metres. Yet we know far less about it than about the surface of the Moon. Scientists divide the water into layers, called zones, according to how much sunlight reaches them. Each zone has its own temperature, pressure and animals, and the conditions change dramatically from the top to the bottom, so that a creature adapted to one zone usually cannot survive in another. Because it is so difficult to reach, the deep ocean was long thought to be empty of life, and it was not until the nineteenth century that the first nets and lines brought up creatures from far below the surface."""
B = """The uppermost layer is the sunlight zone, which extends from the surface to about two hundred metres. Here there is enough light for plants and tiny algae to carry out photosynthesis, so this zone produces most of the food on which the rest of the ocean depends. It is also the warmest zone and home to about ninety per cent of all marine life, including most of the fish that people eat, as well as dolphins, turtles and coral reefs."""
C = """Between two hundred and one thousand metres lies the twilight zone, where the light fades into darkness. Plants cannot grow here, so the animals must feed on the creatures from above or on food that sinks from the sunlit layer. Many fish have large eyes to catch the little light that remains, and many make their own light, a feature called bioluminescence. Some animals rise to the surface at night to feed, and sink again at dawn, in the largest daily migration on Earth."""
D = """Below one thousand metres, in the midnight zone, there is no sunlight at all. The temperature is close to freezing, and the pressure can be a hundred times greater than at the surface. Animals here, such as the anglerfish, which lures prey with a glowing lamp hanging in front of its mouth, are often small, slow and black or red, and they save energy by waiting for food to come to them. The sperm whale dives to this zone to hunt giant squid."""
E = """The abyssal zone begins at about four thousand metres and covers most of the sea floor. The water is almost freezing, the pressure is crushing, and food is scarce. Yet life survives. Sea cucumbers, worms and strange fish feed on the slow rain of dead plants and animals, which scientists call marine snow. Near hot springs on the sea floor, called hydrothermal vents, there are communities of animals that depend not on sunlight but on chemicals from the Earth itself."""
F = """The deepest zone, the hadal zone, lies in trenches that drop below six thousand metres. The deepest known place is the Challenger Deep in the Mariana Trench, which is nearly eleven kilometres down. In 1960, two men, Jacques Piccard and Don Walsh, reached the bottom in a vessel called the Trieste, and in 2012 the film-maker James Cameron made the journey alone. Both found that, despite the extreme pressure, the bottom was not lifeless. Piccard reported seeing a flat fish on the sea floor, although this report has since been questioned by some scientists."""
G = """Exploring the ocean is difficult and costly, and most of the sea floor has not been mapped in detail. Dr Maria Okonkwo, an oceanographer, says that each new expedition finds species that were previously unknown, and that some may offer medicines or materials of value. She also warns that deep-sea mining and fishing may damage the sea floor before scientists have had a chance to understand it, since creatures there grow very slowly and recover from damage over centuries."""
S, PT, W, H = layers(5)
P = passage('p41', 'Zones of the Ocean', 'Marine science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('More of the Moon\'s surface is mapped than the ocean floor.', 'T', 'A', 'we know far less about it than about the surface of the Moon'),
  ('The zones are divided by how much sunlight reaches them.', 'T', 'A', 'according to how much sunlight reaches them'),
  ('Whales are the deepest-diving animals in the ocean.', 'NG', 'D', 'The sperm whale dives to this zone to hunt giant squid', 'Comparison with other divers is not made.'),
  ('Photosynthesis takes place in the sunlight zone.', 'T', 'B', 'enough light for plants and tiny algae to carry out photosynthesis'),
  ('Most marine life lives in the midnight zone.', 'F', 'B', 'about ninety per cent of all marine life'),
  ('Plants grow well in the twilight zone.', 'F', 'C', 'Plants cannot grow here'),
  ('Some animals migrate to the surface at night.', 'T', 'C', 'rise to the surface at night to feed'),
  ('The temperature in the midnight zone is warm.', 'F', 'D', 'close to freezing'),
  ('Animals in the abyssal zone depend on marine snow.', 'T', 'E', 'feed on the slow rain of dead plants and animals'),
  ('James Cameron reached the bottom with a companion.', 'F', 'F', 'made the journey alone'),
 ]),
 mcq([
  ('Why does the sunlight zone produce most of the ocean\'s food?', ['It is the largest zone.', 'Plants can use light there.', 'It is the deepest.', 'It is the coldest.'], 1, 'B', 'enough light for plants and tiny algae to carry out photosynthesis'),
  ('How does the anglerfish catch food?', ['By swimming fast.', 'By using a glowing lamp.', 'By digging.', 'By migrating.'], 1, 'D', 'lures prey with a glowing lamp'),
  ('Why might deep-sea mining be harmful?', ['It is expensive.', 'Creatures there recover very slowly.', 'It makes the water hot.', 'It stops tides.'], 1, 'G', 'recover from damage over centuries'),
 ]),
 multi('Which TWO features of animals in the twilight zone are mentioned in paragraph C?', ['Large eyes.', 'The ability to make light.', 'Thick fur.', 'Bright red skin.', 'Wings.'], [0, 1], [('C', 'large eyes to catch the little light'), ('C', 'make their own light')]),
 head(['A little-known world', 'The bright, crowded surface', 'A realm of fading light', 'Total darkness and cold', 'Life on the sea floor', 'The deepest trenches', 'Exploration and its risks', 'The history of fishing', 'The tides'],
  [('A', 0, 'Scientists divide the water into layers'), ('B', 1, 'The uppermost layer is the sunlight zone'), ('C', 2, 'where the light fades into darkness'), ('D', 3, 'there is no sunlight at all'), ('E', 4, 'The abyssal zone begins at about four thousand metres'), ('F', 5, 'The deepest zone, the hadal zone'), ('G', 6, 'Exploring the ocean is difficult and costly')]),
 info([
  ('a figure for the average depth of the ocean', 'A', 'about 3,700 metres'),
  ('a mention of the largest daily migration', 'C', 'the largest daily migration on Earth'),
  ('a comparison of pressure with the surface', 'D', 'a hundred times greater than at the surface'),
  ('a name for falling remains of dead plants and animals', 'E', 'marine snow'),
  ('a mention of a vessel that reached the bottom', 'F', 'a vessel called the Trieste'),
 ]),
 ends(['is the warmest zone.', 'make their own light.', 'is close to freezing.', 'feed on marine snow.', 'has never been explored.', 'is found only near the coast.', 'is the home of the sperm whale only.'], [
  ('The sunlight zone', 0, 'B', 'It is also the warmest zone'),
  ('Many fish in the twilight zone', 1, 'C', 'many make their own light'),
  ('The water in the midnight zone', 2, 'D', 'The temperature is close to freezing'),
  ('Sea cucumbers and worms', 3, 'E', 'feed on the slow rain of dead plants and animals'),
 ]),
 diag('Label the zones of the ocean, from the surface downwards. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['sunlight'], 'B', 'the sunlight zone'), (['twilight'], 'C', 'the twilight zone'), (['midnight'], 'D', 'the midnight zone'), (['abyssal'], 'E', 'The abyssal zone'), (['hadal'], 'F', 'the hadal zone')], 1),
 sent(2, [
  ('Between two hundred and one thousand metres is the ___ zone.', ['twilight'], 'C', 'the twilight zone'),
  ('Making your own light is called ___.', ['bioluminescence'], 'C', 'bioluminescence'),
  ('The deepest known place is the ___ Deep.', ['challenger'], 'F', 'the Challenger Deep'),
  ('Dr Okonkwo is an ___.', ['oceanographer'], 'G', 'an oceanographer'),
 ]),
 short(3, [
  ('What do hydrothermal vents provide for animals?', ['chemicals'], 'E', 'chemicals from the Earth itself'),
  ('In which trench is the Challenger Deep?', ['mariana trench', 'the mariana trench', 'mariana'], 'F', 'the Mariana Trench'),
  ('What is the sperm whale\'s prey in the midnight zone?', ['giant squid'], 'D', 'hunt giant squid'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Most marine life lives in the [[1]] zone, where light allows photosynthesis. Below it, the twilight zone has [[2]] light, and the midnight zone has none. On the sea floor, animals feed on marine [[3]], and the deepest places lie in [[4]].',
  [(['sunlight'], 'B', 'the sunlight zone'), (['little'], 'C', 'the little light that remains'), (['snow'], 'E', 'marine snow'), (['trenches'], 'F', 'lies in trenches')], 1,
  bank=['sunlight', 'little', 'snow', 'trenches', 'rivers', 'ice', 'sand', 'waves']),
])
