from lib import *
from svgs import *
A = """An ant colony is one of the most successful societies on Earth. Ants have lived on the planet for over a hundred million years, and today there are more than twelve thousand species, found in every land environment except the coldest polar regions. By some estimates, the total weight of all ants in the world is similar to that of all humans. Individually, an ant is tiny and has a brain smaller than a grain of sand. Yet colonies build elaborate nests, farm crops, wage war and find the shortest route to food. This passage examines how such small animals achieve so much by working together."""
B = """A typical colony has three kinds of ant. The queen is the mother of the colony, and her only task is to lay eggs, which she may do for ten years or more. The males exist only to mate with queens and die soon after. The vast majority of ants are workers, which are all females. They look for food, build and repair the nest, look after the eggs and defend against enemies. In some species, workers are divided into groups of different sizes: large soldier ants, with powerful jaws, guard the entrance, while smaller workers do the delicate work inside the nest."""
C = """The life of an ant starts as an egg, which hatches into a worm-like larva. The larva is fed by workers and grows quickly, then becomes a pupa, which is sometimes protected by a cocoon. Inside the pupa, the body is completely rebuilt, and after a few weeks an adult ant emerges. This transformation is called complete metamorphosis, and it is the same process as that of a butterfly. A new worker's first jobs are usually inside the nest, caring for the young; later in life, as she grows older, she goes outside to look for food, which is more dangerous."""
D = """Ants communicate mainly by chemicals called pheromones. When a worker finds food, she returns to the nest, leaving a trail of scent on the ground. Other ants smell the trail and follow it, and as they return with food, they add to the scent. The more ants that use the path, the stronger the trail becomes. If a shorter route exists, ants using it return sooner, so the scent builds up faster and eventually most ants prefer it. In this way, the colony finds the best path although no single ant has planned it. Computer scientists have copied this method to solve problems such as planning delivery routes."""
E = """Some ants have developed remarkable ways of life. Leafcutter ants of South America cut pieces of leaf and carry them back to the nest, but they do not eat them. Instead, they use the leaves to grow a fungus, which is their food, in underground gardens. The ants take care of the garden, removing harmful moulds. Army ants have no permanent nest. They march in huge columns, eating insects and other small animals in their path, and the queen is carried in the middle of the group. Weaver ants build nests in trees by joining leaves with silk produced by their larvae."""
F = """Colonies cooperate in other ways, too. When a river floods, fire ants link their bodies to form a floating raft, with the queen and the young at the centre, which can survive for weeks. Some species keep aphids, small insects that feed on plant juice, as cattle, protecting them from enemies and taking the sweet liquid which they produce. Other ants fight organised wars against neighbouring colonies for territory. Dr Thomas Reiner, an entomologist, points out that these behaviours are all the result of simple rules followed by thousands of individuals, with no leader who gives orders."""
G = """The queen, in fact, does not rule at all. She is a source of eggs, not of commands. Dr Reiner calls the colony a superorganism, which means that it behaves like a single living creature, with the ants playing the role of cells. No ant knows what the colony as a whole is doing, but all the decisions emerge from their interactions. Scientists believe that studying ants may help engineers to design swarms of robots that can explore disaster zones, working together without central control. Meanwhile, ants remain essential to the planet, since they aerate the soil, spread seeds and are food for many other animals."""
P = passage('p89', 'Inside an Ant Colony', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Ants have lived on Earth for over a hundred million years.', 'T', 'A', 'over a hundred million years'),
  ('There are more than twelve thousand species of ant.', 'T', 'A', 'more than twelve thousand species'),
  ('An ant\'s brain is larger than a grain of sand.', 'F', 'A', 'smaller than a grain of sand'),
  ('The queen lays eggs.', 'T', 'B', 'lay eggs'),
  ('Worker ants are all male.', 'F', 'B', 'all females'),
  ('An ant larva grows into a pupa.', 'T', 'C', 'becomes a pupa'),
  ('Ants communicate mainly by chemicals.', 'T', 'D', 'chemicals called pheromones'),
  ('Leafcutter ants eat the leaves they cut.', 'F', 'E', 'they do not eat them'),
  ('Weaver ants live in South America.', 'NG', 'E', 'Weaver ants build nests in trees', 'Their location is not given.'),
 ]),
 mcq([
  ('What is the queen\'s only task?', ['Laying eggs.', 'Finding food.', 'Guarding the nest.', 'Building tunnels.'], 0, 'B', 'only task is to lay eggs'),
  ('Why does the colony eventually prefer the shorter route?', ['Scent builds up faster there.', 'The queen orders it.', 'It is safer.', 'It is flatter.'], 0, 'D', 'scent builds up faster'),
  ('What does Dr Reiner call the colony?', ['A superorganism.', 'A machine.', 'A family.', 'An army.'], 0, 'G', 'superorganism'),
 ]),
 diag('Label the stages in the life of an ant, in order. Write ONE WORD from the passage for each answer.', *chain(4)[2:], chain(4)[0], chain(4)[1],
  [(['egg'], 'C', 'starts as an egg'), (['larva'], 'C', 'worm-like larva'), (['pupa'], 'C', 'becomes a pupa'), (['adult'], 'C', 'adult ant')], 1) if False else
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Egg', 'Hatches into a [[1]]'], ['Larva', 'Is fed by [[2]]'], ['Pupa', 'Body is completely [[3]]'], ['Adult', 'Emerges after a few [[4]]']],
  [(['larva'], 'C', 'worm-like larva'), (['workers'], 'C', 'fed by workers'), (['rebuilt'], 'C', 'completely rebuilt'), (['weeks'], 'C', 'a few weeks')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['A worker finds [[1]].', 'She leaves a trail of [[2]] on the way home.', 'Other ants follow the [[3]].', 'The shortest route becomes the [[4]] one.'],
  [(['food'], 'D', 'finds food'), (['scent'], 'D', 'trail of scent'), (['trail'], 'D', 'follow it'), (['strongest'], 'D', 'stronger')], 1) if False else
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['A worker finds [[1]].', 'She leaves a trail of [[2]] on the way home.', 'The more ants that use the path, the [[3]] the trail becomes.', 'Most ants eventually prefer the [[4]] route.'],
  [(['food'], 'D', 'finds food'), (['scent'], 'D', 'trail of scent'), (['stronger'], 'D', 'stronger'), (['shorter'], 'D', 'shorter route')], 1),
 feat('Match each statement with the correct ant, A to D.', ['The queen', 'Leafcutter ants', 'Army ants', 'Fire ants'], [
  ('She may lay eggs for ten years or more.', 0, 'B', 'ten years or more'),
  ('They grow a fungus in underground gardens.', 1, 'E', 'underground gardens'),
  ('They march in huge columns.', 2, 'E', 'huge columns'),
  ('They link their bodies to form a raft.', 3, 'F', 'floating raft'),
 ]),
 multi('Which TWO jobs of workers are mentioned in paragraph B?', ['Building and repairing the nest.', 'Looking after the eggs.', 'Teaching the males.', 'Flying to new colonies.', 'Hunting birds.'], [0, 1], [('B', 'build and repair the nest'), ('B', 'look after the eggs')]),
 head(['A tiny giant', 'Who does what', 'A body rebuilt', 'Messages in scent', 'Gardeners and marchers', 'Rafts, cattle and wars', 'No ruler at all', 'The history of insects', 'Ants as pets'],
  [('A', 0, 'one of the most successful societies on Earth'), ('B', 1, 'three kinds of ant'), ('C', 2, 'completely rebuilt'), ('D', 3, 'communicate mainly by chemicals'), ('E', 4, 'remarkable ways of life'), ('F', 5, 'form a floating raft'), ('G', 6, 'does not rule at all')]),
 info([
  ('a comparison between the weight of ants and humans', 'A', 'weight of all humans' if False else 'similar to that of all humans'),
  ('a reference to powerful jaws', 'B', 'powerful jaws'),
  ('a reference to delivery routes', 'D', 'delivery routes'),
  ('a reference to silk', 'E', 'silk produced by their larvae'),
  ('a reference to robots', 'G', 'swarms of robots'),
 ]),
 ends(['lays eggs.', 'grow a fungus.', 'leave a scent trail.', 'form a raft.', 'build roads.', 'make honey.', 'rule the colony.'], [
  ('The queen', 0, 'B', 'lay eggs'),
  ('Leafcutter ants', 1, 'E', 'grow a fungus'),
  ('Foraging workers', 2, 'D', 'leaving a trail of scent'),
  ('Fire ants', 3, 'F', 'floating raft'),
 ]),
 sent(2, [
  ('Ants communicate by chemicals called ___.', ['pheromones'], 'D', 'pheromones'),
  ('Army ants have no permanent ___.', ['nest'], 'E', 'no permanent nest'),
  ('Aphids feed on plant ___.', ['juice'], 'F', 'plant juice'),
  ('Dr Reiner is an ___.', ['entomologist'], 'F', 'an entomologist'),
 ]),
 short(3, [
  ('How long may a queen lay eggs?', ['ten years'], 'B', 'ten years'),
  ('What did computer scientists copy?', ['this method'], 'D', 'copied this method'),
  ('Where do leafcutter ants live?', ['south america'], 'E', 'South America'),
 ]),
])
