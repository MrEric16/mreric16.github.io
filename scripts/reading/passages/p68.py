from lib import *
from svgs import *
A = """Butterflies are among the most admired insects, and their lives show one of the most remarkable changes in nature. A butterfly does not simply grow bigger, as a puppy does. It passes through four distinct stages, egg, larva, pupa and adult, and in each of them it looks and behaves quite differently. This process is called complete metamorphosis, a word from Greek meaning change of shape. The whole cycle may take a month in a warm climate or most of a year in a cold one, and in some species the adults live for only a week or two, while in others they survive for many months."""
B = """The cycle begins with the egg. A female butterfly lays her eggs on a particular plant, chosen with great care by tasting it with sensors on her feet, because the plant will be the only food of the young. The eggs are tiny, often no bigger than a pinhead, and may be round, oval or ribbed. Some species lay them one at a time, others in clusters of hundreds. After three to ten days, depending on the temperature, a tiny creature bites its way out, and often its first meal is its own eggshell, which contains useful nutrients."""
C = """The creature that emerges is a larva, better known as a caterpillar. It has one purpose, which is to eat, and it eats almost without stopping. Some caterpillars increase their weight a thousand times in two weeks. Because its skin cannot stretch, the caterpillar must shed it several times, a process called moulting, and each stage between moults is called an instar. Many caterpillars are green or brown, to hide among the leaves, while others are brightly coloured, to warn birds that they taste unpleasant or are poisonous. Birds learn quickly to avoid them, and a few species of harmless insects have even evolved to copy these warning colours."""
D = """When the caterpillar is fully grown, it stops eating and finds a safe place, usually on the underside of a branch. It fixes itself with silk, sheds its skin for the last time and becomes a pupa, or chrysalis. From the outside, the pupa seems to be resting, but inside a dramatic transformation is taking place. Most of the caterpillar's body breaks down into a liquid, from which new organs are built, including wings, long legs and eyes. This stage lasts from about one week to several months; some species spend the whole winter as pupae and emerge only when the spring warmth returns."""
E = """At last the adult butterfly splits the chrysalis and crawls out. Its wings are damp and crumpled, and it must hang still for several hours while it pumps fluid into them and lets them dry and harden. Only then can it fly. The adult feeds on nectar, drinking through a long tube called a proboscis, which it keeps coiled like a spring when not in use. Its main tasks are to find a mate and to lay eggs, and so the cycle begins again. Some butterflies, such as the monarch, also make remarkable journeys of thousands of kilometres between their summer and winter homes."""
F = """Dr Naomi Fletcher, an entomologist, studies how butterflies sense their world. She explains that their eyes can detect ultraviolet light, which humans cannot see, and that many flowers have patterns visible only in this light, which guide the insects to the nectar like landing lights at an airport. Butterflies also taste with their feet and smell with their antennae. Dr Fletcher says that this variety of senses is the reason why butterflies are such effective pollinators, spreading pollen from flower to flower as they feed, and why the loss of butterflies would be a danger to many plants."""
G = """Unfortunately, butterflies are in decline in many parts of the world. The main reasons are the loss of wild flowers and meadows, the use of chemicals on farms, and changes in the climate. Ordinary people can help. Planting flowers that provide nectar, leaving a corner of the garden uncut, and avoiding pesticides will all give butterflies a place to feed and breed. Schools can also take part in counting projects, in which children record the species that they see in a fixed period of time and send their results to scientists, who use the data to measure the changes from year to year."""
S, PT, W, H = cycle(4)
P = passage('p68', 'The Life of a Butterfly', 'Biology', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('A butterfly passes through four stages.', 'T', 'A', 'four distinct stages'),
  ('Adult butterflies always live for months.', 'F', 'A', 'only a week or two'),
  ('The female tastes plants with her feet.', 'T', 'B', 'sensors on her feet'),
  ('Eggs are always laid one at a time.', 'F', 'B', 'others in clusters of hundreds'),
  ('A caterpillar\'s skin can stretch without limit.', 'F', 'C', 'its skin cannot stretch'),
  ('Bright colours warn birds that a caterpillar is unpleasant.', 'T', 'C', 'to warn birds that they taste unpleasant or are poisonous'),
  ('A pupa feeds actively.', 'F', 'D', 'it stops eating'),
  ('Adults drink nectar through a proboscis.', 'T', 'E', 'drinking through a long tube called a proboscis'),
  ('Dr Fletcher keeps butterflies at home.', 'NG', 'F', 'Dr Naomi Fletcher', 'Her home is not mentioned.'),
 ]),
 mcq([
  ('Why does the female taste the plant?', ['It will be the only food of the young.', 'She is hungry.', 'It protects her wings.', 'It is her nest.'], 0, 'B', 'the plant will be the only food of the young'),
  ('Why are some caterpillars brightly coloured?', ['To attract mates.', 'To warn birds.', 'To keep warm.', 'To hide in leaves.'], 1, 'C', 'to warn birds that they taste unpleasant or are poisonous'),
  ('Why must a new adult wait before flying?', ['Its wings must dry and harden.', 'It is hungry.', 'It must find a mate.', 'It is cold.'], 0, 'E', 'lets them dry and harden'),
 ]),
 feat('Match each statement with the correct stage, A to D.', ['Egg', 'Larva', 'Pupa', 'Adult'], [
  ('It may be as small as a pinhead.', 0, 'B', 'no bigger than a pinhead'),
  ('It sheds its skin several times.', 1, 'C', 'shed it several times'),
  ('Some species spend the winter in this stage.', 2, 'D', 'spend the whole winter as pupae'),
  ('It feeds on nectar.', 3, 'E', 'feeds on nectar'),
 ]),
 multi('Which TWO ways to help butterflies are mentioned in paragraph G?', ['Plant flowers that provide nectar.', 'Avoid pesticides.', 'Build wooden butterfly houses.', 'Water the lawn daily.', 'Cut all grass short.'], [0, 1], [('G', 'Planting flowers that provide nectar'), ('G', 'avoiding pesticides')]),
 head(['Four stages of change', 'The beginning of life', 'A hunger that never stops', 'Change inside a case', 'Wings and flight', 'The senses of an insect', 'A falling population', 'The history of silk', 'How to catch insects'],
  [('A', 0, 'passes through four distinct stages'), ('B', 1, 'The cycle begins with the egg'), ('C', 2, 'it eats almost without stopping'), ('D', 3, 'a dramatic transformation is taking place'), ('E', 4, 'splits the chrysalis and crawls out'), ('F', 5, 'how butterflies sense their world'), ('G', 6, 'butterflies are in decline')]),
 info([
  ('a reference to eating an eggshell', 'B', 'its own eggshell'),
  ('a figure for weight increase', 'C', 'a thousand times'),
  ('a reference to the winter spent as a pupa', 'D', 'the whole winter as pupae'),
  ('a reference to a long migration', 'E', 'journeys of thousands of kilometres'),
  ('a comparison with an airport', 'F', 'landing lights at an airport'),
 ]),
 ends(['chooses a plant by tasting it with her feet.', 'eats almost without stopping.', 'must let its wings dry.', 'can take part in counting projects.', 'lay eggs in the sea.', 'live for a century.', 'are never poisonous.'], [
  ('A female butterfly', 0, 'B', 'tasting it with sensors on her feet'),
  ('A caterpillar', 1, 'C', 'it eats almost without stopping'),
  ('A new adult', 2, 'E', 'lets them dry and harden'),
  ('Schools', 3, 'G', 'take part in counting projects'),
 ]),
 diag('Label the stages in the life cycle of a butterfly, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['egg'], 'B', 'begins with the egg'), (['larva'], 'C', 'emerges is a larva'), (['pupa'], 'D', 'becomes a pupa'), (['adult'], 'E', 'the adult butterfly splits the chrysalis')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The female lays her eggs on a particular [[1]].', 'The caterpillar sheds its [[2]] because it cannot stretch.', 'Inside the pupa, the body breaks down into a [[3]].', 'The adult dries its [[4]] before it can fly.'],
  [(['plant'], 'B', 'a particular plant'), (['skin'], 'C', 'its skin cannot stretch'), (['liquid'], 'D', 'breaks down into a liquid'), (['wings'], 'E', 'Its wings are damp and crumpled')], 1),
 sent(2, [
  ('The change from caterpillar to adult is called complete ___.', ['metamorphosis'], 'A', 'complete metamorphosis'),
  ('Shedding the skin is called ___.', ['moulting'], 'C', 'called moulting'),
  ('The long tube used to drink nectar is called a ___.', ['proboscis'], 'E', 'a proboscis'),
  ('Dr Fletcher is an ___.', ['entomologist'], 'F', 'an entomologist'),
 ]),
 short(3, [
  ('What is the one purpose of a caterpillar?', ['to eat', 'eat'], 'C', 'which is to eat'),
  ('Where does the pupa usually fix itself?', ['a branch'], 'D', 'underside of a branch'),
  ('What can butterflies see that humans cannot?', ['ultraviolet light'], 'F', 'ultraviolet light'),
 ]),
])
