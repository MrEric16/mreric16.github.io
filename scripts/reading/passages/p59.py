from lib import *
from svgs import *
A = """Frogs belong to a group of animals called amphibians, a word that comes from Greek and means two lives. The name is a good one, because most frogs spend the first part of their lives in water and the second part mainly on land, and the bodies of the young animal and the adult are so different that early naturalists thought that they were separate species. The change from one form to the other is called metamorphosis. In Europe, the common frog takes about sixteen weeks to complete the journey, while some tropical species finish in a few weeks and a few large species need two years. This passage follows a frog through the stages of its life."""
B = """The cycle begins in early spring, when adult frogs gather in ponds and ditches to breed. The female lays her eggs in a large mass of jelly, called frogspawn, which may contain from one to two thousand eggs. Each egg is a small black dot in a clear ball of jelly. The jelly protects the eggs from cold and from some enemies, and it swells as it absorbs water, so that the mass floats near the surface where the sun can warm it. Most eggs, however, will never become frogs: fish, newts, ducks and insects eat them in large numbers, and a late frost can destroy a whole mass."""
C = """After one to three weeks, depending on the temperature, the eggs hatch into tadpoles. A tadpole looks more like a small fish than a frog. It has a long tail for swimming, gills for breathing underwater, and no legs. At first it feeds on the remains of the jelly, and then it uses its tiny, rough mouth to scrape algae from stones and water plants. Tadpoles grow rapidly, and they often swim in large groups for safety. Even so, they are food for dragonfly larvae, fish and birds, and only a small number of them survive long enough to leave the water."""
D = """After about six weeks, the tadpole begins to change. First, the back legs appear as two small buds near the base of the tail, and they grow longer and develop toes. Next, the front legs push out from beneath the skin. At the same time, the lungs develop and the gills disappear, so that the animal begins to rise to the surface to gulp air. The mouth widens, the eyes grow bigger and the diet changes from plants to insects. These changes are controlled by a hormone made in a gland in the neck, and without it a tadpole would simply continue to grow without becoming a frog."""
E = """The next stage is the froglet. The animal now has four legs and looks like a tiny frog, but it still has a short tail, which it slowly absorbs: the tail is not dropped but is used as a food store, so that the froglet need not eat during the most dramatic part of its change. When the tail has gone, the froglet, about the size of a fingernail, climbs out of the water. It hides in damp grass and under stones, since its skin dries out easily, and it hunts small insects. Thousands of froglets may leave a pond on the same wet day, which is why people sometimes talk of it raining frogs."""
F = """A young frog takes about three years to become an adult, and it then returns to the pond where it was born to breed. A frog breathes not only with lungs but also through its skin, which must be kept moist, and it drinks by absorbing water through the skin of its belly. Its long, sticky tongue can catch an insect in a fraction of a second. In winter, frogs hibernate in the mud at the bottom of ponds or under piles of leaves, with their bodies slowed down so that they need almost no food. In a good place a frog may live for up to eight years."""
G = """Amphibians are now among the most threatened animals on Earth. Because their skin is so thin, frogs absorb chemicals from the water as easily as they absorb water itself, and they are therefore very sensitive to pollution. Ponds are drained for building, and a disease caused by a fungus has killed frogs in many parts of the world. Dr Rosa Contreras, a conservation biologist, says that frogs are like canaries in a coal mine: when they disappear from a place, it is a warning that something is wrong with the environment. She urges gardeners to dig small ponds, which can become a refuge for local frogs."""
S, PT, W, H = cycle(4)
P = passage('p59', 'From Tadpole to Frog', 'Biology', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The word amphibian comes from Greek.', 'T', 'A', 'comes from Greek'),
  ('Early naturalists thought young and adult frogs were separate species.', 'T', 'A', 'separate species'),
  ('Frogs lay their eggs in early spring.', 'T', 'B', 'early spring'),
  ('Most frogspawn eggs become adult frogs.', 'F', 'B', 'Most eggs, however, will never become frogs'),
  ('A tadpole has legs when it hatches.', 'F', 'C', 'no legs'),
  ('Tadpoles feed on algae.', 'T', 'C', 'scrape algae from stones and water plants'),
  ('The back legs appear before the front legs.', 'T', 'D', 'First, the back legs appear'),
  ('The tail of a froglet is used as a food store.', 'T', 'E', 'used as a food store'),
  ('Frogs live longer than tortoises.', 'NG', 'F', 'live for up to eight years', 'Tortoises are not mentioned.'),
 ]),
 mcq([
  ('Why does frogspawn float near the surface?', ['The jelly swells as it absorbs water.', 'The eggs are light.', 'The pond is shallow.', 'Fish push it up.'], 0, 'B', 'it swells as it absorbs water'),
  ('What controls the changes in a tadpole?', ['The temperature.', 'A hormone.', 'The food.', 'The light.'], 1, 'D', 'controlled by a hormone'),
  ('Why are frogs sensitive to pollution?', ['Their thin skin absorbs chemicals.', 'They eat polluted food.', 'They live in rivers.', 'They breathe smoke.'], 0, 'G', 'frogs absorb chemicals from the water'),
 ]),
 feat('Match each statement with the correct stage, A to D.', ['Egg', 'Tadpole', 'Froglet', 'Adult'], [
  ('It breathes underwater with gills.', 1, 'C', 'gills for breathing underwater'),
  ('It is about the size of a fingernail.', 2, 'E', 'about the size of a fingernail'),
  ('It returns to the pond where it was born.', 3, 'F', 'returns to the pond where it was born'),
  ('It floats in a mass of jelly.', 0, 'B', 'floats near the surface'),
 ]),
 multi('Which TWO enemies of frogspawn are mentioned in paragraph B?', ['Fish.', 'Ducks.', 'Foxes.', 'Cats.', 'Snakes.'], [0, 1], [('B', 'fish'), ('B', 'ducks')]),
 head(['Two lives', 'The start in jelly', 'A swimmer without legs', 'Legs and lungs appear', 'A small frog leaves the water', 'Life as an adult', 'A warning from nature', 'The history of ponds', 'Fishing for beginners'],
  [('A', 0, 'means two lives'), ('B', 1, 'The cycle begins in early spring'), ('C', 2, 'It has a long tail for swimming'), ('D', 3, 'the back legs appear'), ('E', 4, 'climbs out of the water'), ('F', 5, 'A young frog takes about three years to become an adult'), ('G', 6, 'canaries in a coal mine')]),
 info([
  ('a reference to a hormone', 'D', 'a hormone made in a gland'),
  ('a reference to damp hiding places', 'E', 'damp grass and under stones'),
  ('a reference to breathing through the skin', 'F', 'also through its skin'),
  ('a reference to a disease caused by a fungus', 'G', 'a disease caused by a fungus'),
  ('a reference to a rain of frogs', 'E', 'raining frogs'),
 ]),
 ends(['is protected by jelly.', 'scrape algae from stones.', 'slowly absorbs its tail.', 'urges gardeners to dig small ponds.', 'is a kind of fish.', 'lays eggs in trees.', 'eats only plants.'], [
  ('Frogspawn', 0, 'B', 'The jelly protects the eggs'),
  ('Tadpoles', 1, 'C', 'scrape algae'),
  ('A froglet', 2, 'E', 'it slowly absorbs'),
  ('Dr Contreras', 3, 'G', 'dig small ponds'),
 ]),
 diag('Label the stages in the life cycle of a frog, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['egg'], 'B', 'Each egg is a small black dot'), (['tadpole'], 'C', 'hatch into tadpoles'), (['froglet'], 'E', 'is the froglet'), (['adult'], 'F', 'become an adult')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Egg', 'Protected by a ball of [[1]]'], ['Tadpole', 'Breathes underwater with [[2]]'], ['Froglet', 'Slowly absorbs its [[3]]'], ['Adult', 'Hibernates in the [[4]]']],
  [(['jelly'], 'B', 'clear ball of jelly'), (['gills'], 'C', 'gills for breathing'), (['tail'], 'E', 'a short tail, which it slowly absorbs'), (['mud'], 'F', 'in the mud at the bottom')], 1),
 sent(2, [
  ('The word amphibian means two ___.', ['lives'], 'A', 'two lives'),
  ('A mass of frog eggs is called ___.', ['frogspawn'], 'B', 'called frogspawn'),
  ('Tadpoles breathe with ___.', ['gills'], 'C', 'gills'),
  ('Dr Contreras is a conservation ___.', ['biologist'], 'G', 'conservation biologist'),
 ]),
 short(3, [
  ('How long does the common frog take to complete metamorphosis?', ['sixteen weeks', 'about sixteen weeks'], 'A', 'about sixteen weeks'),
  ('What do froglets hunt?', ['small insects', 'insects'], 'E', 'small insects'),
  ('What does Dr Contreras compare frogs to?', ['canaries'], 'G', 'canaries in a coal mine'),
 ]),
])
