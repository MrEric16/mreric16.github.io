from lib import *
from svgs import *
A = """Butterflies are among the most familiar insects, and there are about eighteen thousand species, found on every continent except Antarctica. They range in size from the tiny western pygmy blue, which measures about one centimetre across its wings, to the Queen Alexandra's birdwing of Papua New Guinea, whose wings can span about a quarter of a metre. Though fragile in appearance, butterflies are remarkable survivors, and their life cycle, which has four separate stages, is one of the most striking transformations in nature."""
B = """The cycle begins with an egg. A female butterfly lays her eggs, often hundreds in a lifetime, on a particular kind of plant, which she recognises by taste, using sensors on her feet. The choice is important, because the young that hatch will feed on this plant, and the wrong one would starve them. The eggs are tiny, usually smaller than a pinhead, and may be round, oval or shaped like a barrel. They hatch in three to ten days, depending on the temperature."""
C = """From the egg comes the larva, which is called a caterpillar. Its only job is to eat, and it does so almost without stopping, increasing its weight by about a thousand times in only two weeks. Because its skin cannot stretch, the caterpillar must shed it several times as it grows, a process known as moulting. Many caterpillars have bright colours or spines to warn birds that they taste bad, while others look like twigs or bird droppings, so that predators ignore them."""
D = """When it has grown as large as it can, the caterpillar attaches itself to a twig or a leaf and changes into a pupa, called a chrysalis. From outside, it seems that nothing is happening. Inside, however, the body of the caterpillar breaks down almost completely, and a new body, with wings, legs and eyes, is built from the remains. Some pupae are camouflaged to look like dead leaves, and others are decorated with spots of shining gold. This stage lasts about two weeks, but in cold climates it may last all winter."""
E = """The adult butterfly breaks out of the chrysalis, and at first its wings are wet and folded. It hangs still for several hours, pumping fluid into the wings to open them and waiting for them to dry. Then it flies away to find food and a mate. Adults drink nectar through a long tube called a proboscis, which is rolled up when not in use, and they help plants by carrying pollen from flower to flower. Most live for only a few weeks, though some species survive for ten months. Males and females often look quite different from each other, and in some species the males gather in groups beside puddles to drink the minerals dissolved in the water."""
F = """A few butterflies make extraordinary journeys. The monarch butterfly of North America flies up to four thousand kilometres to spend the winter in the mountain forests of central Mexico. No single butterfly makes the return trip: it takes several generations to travel back north in spring. How the young find the way to a place that they have never seen remains a mystery, although scientists believe that they use the position of the Sun and the Earth's magnetic field."""
G = """Butterflies are now in danger in many countries. The destruction of meadows and forests, the use of chemicals on farms, and the warming of the climate have all reduced their numbers. In some regions, the numbers have fallen by half in only a few decades. Dr Tomas Brandt, a butterfly specialist, says that butterflies are an early warning of damage to the environment, since they respond quickly to change. He recommends that gardeners plant native flowers and leave some areas of grass uncut."""
S, PT, W, H = cycle(4)
P = passage('p39', 'A Life in Four Stages', 'Biology', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Butterflies live on every continent.', 'F', 'A', 'except Antarctica'),
  ('The life cycle of a butterfly has four stages.', 'T', 'A', 'four separate stages'),
  ('A female butterfly recognises the right plant by its taste.', 'T', 'B', 'which she recognises by taste'),
  ('Eggs usually hatch within a day.', 'F', 'B', 'three to ten days'),
  ('A caterpillar sheds its skin because the skin cannot stretch.', 'T', 'C', 'its skin cannot stretch'),
  ('All caterpillars are brightly coloured.', 'F', 'C', 'others look like twigs or bird droppings'),
  ('A chrysalis is a resting stage in which nothing happens inside.', 'F', 'D', 'the body of the caterpillar breaks down almost completely'),
  ('Adult butterflies drink nectar.', 'T', 'E', 'drink nectar through a long tube'),
  ('Monarch butterflies fly to Mexico each winter for food.', 'NG', 'F', 'to spend the winter in the mountain forests of central Mexico', 'The reason for the journey is not stated.'),
 ]),
 mcq([
  ('Why is the choice of plant for the eggs important?', ['The eggs need sunlight.', 'The young will feed on it.', 'The plant protects the adult.', 'The plant is warm.'], 1, 'B', 'the young that hatch will feed on this plant'),
  ('What happens in the chrysalis?', ['The caterpillar sleeps.', 'A new body is built.', 'The eggs hatch.', 'The wings are painted.'], 1, 'D', 'a new body, with wings, legs and eyes, is built from the remains'),
  ('What is a butterfly an early warning of, according to Dr Brandt?', ['Cold winters.', 'Damage to the environment.', 'Floods.', 'Farm prices.'], 1, 'G', 'an early warning of damage to the environment'),
 ]),
 multi('Which TWO ways do caterpillars avoid predators, according to paragraph C?', ['Bright warning colours.', 'Looking like twigs.', 'Hiding underground.', 'Flying away.', 'Making loud noises.'], [0, 1], [('C', 'bright colours or spines to warn birds'), ('C', 'look like twigs or bird droppings')]),
 head(['Introducing a remarkable insect', 'The first stage: a tiny beginning', 'A stage of constant eating', 'A stage of transformation', 'Emerging and flying', 'An epic journey', 'Falling numbers and what to do', 'How bees make honey', 'The history of silk'],
  [('A', 0, 'one of the most striking transformations in nature'), ('B', 1, 'The cycle begins with an egg'), ('C', 2, 'Its only job is to eat'), ('D', 3, 'changes into a pupa, called a chrysalis'), ('E', 4, 'The adult butterfly breaks out of the chrysalis'), ('F', 5, 'A few butterflies make extraordinary journeys'), ('G', 6, 'Butterflies are now in danger in many countries')]),
 info([
  ('a comparison of the size of eggs with an object', 'B', 'smaller than a pinhead'),
  ('a reference to the increase in a caterpillar\'s weight', 'C', 'about a thousand times in only two weeks'),
  ('a mention of a pupa that looks like dead leaves', 'D', 'camouflaged to look like dead leaves'),
  ('a name for the tube used for drinking', 'E', 'a long tube called a proboscis'),
  ('a suggestion for gardeners', 'G', 'plant native flowers'),
 ]),
 ends(['hatch in three to ten days.', 'must shed its skin several times.', 'lasts about two weeks.', 'carries pollen from flower to flower.', 'is found only in Mexico.', 'lives for a hundred years.', 'is the largest insect in the world.'], [
  ('The eggs', 0, 'B', 'They hatch in three to ten days'),
  ('A caterpillar', 1, 'C', 'the caterpillar must shed it several times'),
  ('The pupa stage', 2, 'D', 'This stage lasts about two weeks'),
  ('An adult butterfly', 3, 'E', 'they help plants by carrying pollen from flower to flower'),
 ]),
 diag('Label the four stages of the life cycle, going clockwise from the top. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['egg'], 'B', 'The cycle begins with an egg'), (['larva', 'caterpillar'], 'C', 'the larva, which is called a caterpillar'), (['chrysalis', 'pupa'], 'D', 'a pupa, called a chrysalis'), (['butterfly', 'adult'], 'E', 'The adult butterfly')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['The female lays eggs on a particular kind of [[1]].', 'The caterpillar eats constantly and must [[2]] its skin several times.', 'The caterpillar changes into a [[3]] attached to a twig.', 'The adult pumps fluid into its wings and waits for them to [[4]].'],
  [(['plant'], 'B', 'a particular kind of plant'), (['shed'], 'C', 'must shed it'), (['chrysalis', 'pupa'], 'D', 'a pupa, called a chrysalis'), (['dry'], 'E', 'waiting for them to dry')], 1),
 sent(2, [
  ('The Queen Alexandra\'s birdwing comes from Papua ___ Guinea.', ['new'], 'A', 'Papua New Guinea'),
  ('Butterflies use sensors on their ___ to taste plants.', ['feet'], 'B', 'sensors on her feet'),
  ('Adults carry ___ from flower to flower.', ['pollen'], 'E', 'carrying pollen'),
  ('Monarchs spend the winter in the forests of central ___.', ['mexico'], 'F', 'central Mexico'),
 ]),
 short(3, [
  ('How long does the pupa stage last?', ['two weeks', 'about two weeks'], 'D', 'about two weeks'),
  ('How many species of butterfly are there?', ['eighteen thousand', '18,000'], 'A', 'about eighteen thousand species'),
  ('What does a butterfly use to drink?', ['a proboscis', 'proboscis'], 'E', 'a long tube called a proboscis'),
 ]),
])
