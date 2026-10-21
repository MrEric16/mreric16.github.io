from lib import *
from svgs import *
A = """When we pick a mushroom from the forest floor, we are picking only a small part of a much larger organism. Mushrooms are the fruit of fungi, in the same way that apples are the fruit of trees. The main body of the fungus is hidden underground or inside rotting wood, in a network of fine threads. Fungi are neither plants nor animals; scientists place them in a kingdom of their own. There are an estimated two or three million species, of which only about a tenth have been named. This passage looks at how fungi live, why they matter and what they may do for us in the future."""
B = """The threads of a fungus are called hyphae, and a mass of them is known as a mycelium. A single hypha is thinner than a human hair, but a mycelium can spread through soil for great distances. Unlike plants, fungi cannot make their own food from sunlight. Instead, they release chemicals into their surroundings which break down dead matter, and then absorb the nutrients. In this way fungi are the main recyclers of the forest, turning fallen leaves, branches and animal remains into food for other organisms. Without them, dead material would pile up and the nutrients it contains would be unavailable to living plants."""
C = """Many fungi form partnerships with the roots of trees. The fungus wraps around the root and gathers water and minerals, particularly phosphorus, from the soil, which it passes to the tree. In exchange, the tree supplies the fungus with sugars made by photosynthesis. This relationship is called mycorrhiza, and it is thought to be present in more than ninety per cent of land plants. Some scientists believe that the fungal network also carries chemical signals between trees, which allows a forest to behave in some ways as a connected community, although the extent of this effect is still being debated."""
D = """The largest known living organism may be a fungus. A honey fungus in the Blue Mountains of Oregon, in the United States, covers an area of about nine square kilometres, and is thought to be between two thousand and eight thousand years old. Most of it is underground, and it is noticed only when its yellowish mushrooms appear in autumn. The fungus kills the trees whose roots it attacks. Other fungi are tiny: yeast, which is used for making bread, consists of single cells, and thousands could fit on the head of a pin."""
E = """People have used fungi for a very long time. Yeast makes dough rise and turns sugar into alcohol, and moulds are used to ripen some cheeses. Mushrooms are eaten all over the world, and in some countries they are a popular crop. Most are grown in dark rooms on a bed of compost, and the farmer harvests them within weeks. Fungi are also the source of medicines. In 1928, Alexander Fleming noticed that a mould called Penicillium killed bacteria in his laboratory dishes, and the discovery led to penicillin, which has saved millions of lives."""
F = """Not all fungi are friendly. Some cause diseases of plants, such as wheat rust, which can destroy a harvest, and others infect humans, as in athlete's foot. A few mushrooms are deadly. The death cap, which looks harmless, contains a poison that damages the liver and kills thousands of people every year if eaten by mistake. It is impossible to tell a safe mushroom from a poisonous one by a simple rule, and experts advise that nobody should eat a wild mushroom unless it has been identified by a specialist. Several species of fungus even attack insects, taking over their bodies and controlling their behaviour."""
G = """Researchers are now finding new uses for fungi. Dr Marta Silva, a mycologist, leads a team which grows packaging material from mycelium and farm waste. The mixture is placed in a mould, and within days the fungus binds it into a solid block, which replaces plastic foam. When it is no longer needed, the packaging is simply put on a compost heap. Other scientists use fungi to clean polluted soil, to produce leather-like fabrics and even to build bricks. Dr Silva believes that fungi, which have been neglected for so long, may provide cheap and sustainable alternatives to many products that harm the planet."""
P = passage('p93', 'The Hidden World of Fungi', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Mushrooms are the fruit of fungi.', 'T', 'A', 'the fruit of fungi'),
  ('Fungi are classified as plants.', 'F', 'A', 'a kingdom of their own'),
  ('About a tenth of fungal species have been named.', 'T', 'A', 'about a tenth'),
  ('Fungi make their own food from sunlight.', 'F', 'B', 'cannot make their own food from sunlight'),
  ('Fungi break down dead matter.', 'T', 'B', 'break down dead matter'),
  ('Mycorrhiza is present in more than ninety per cent of land plants.', 'T', 'C', 'more than ninety per cent'),
  ('The Oregon honey fungus covers about nine square kilometres.', 'T', 'D', 'nine square kilometres'),
  ('Penicillium killed bacteria in Fleming\'s dishes.', 'T', 'E', 'killed bacteria'),
  ('Fleming won a Nobel Prize for his discovery.', 'NG', 'E', 'In 1928, Alexander Fleming', 'No prize is mentioned.'),
 ]),
 mcq([
  ('What does the tree give the fungus?', ['Sugars.', 'Water.', 'Phosphorus.', 'Light.'], 0, 'C', 'supplies the fungus with sugars'),
  ('Why is the death cap dangerous?', ['It looks harmless.', 'It is large.', 'It grows underground.', 'It is rare.'], 0, 'F', 'looks harmless'),
  ('What is Dr Silva\'s packaging used to replace?', ['Plastic foam.', 'Glass.', 'Paper.', 'Metal.'], 0, 'G', 'replaces plastic foam'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The fungus wraps around a tree [[1]].', 'It gathers water and [[2]] from the soil.', 'The tree supplies [[3]].', 'The relationship is called [[4]].'],
  [(['root'], 'C', 'wraps around the root'), (['minerals'], 'C', 'water and minerals'), (['sugars'], 'C', 'sugars'), (['mycorrhiza'], 'C', 'called mycorrhiza')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Fungus', 'Use or effect'],
  [['Yeast', 'Makes dough [[1]]'], ['Penicillium', 'Source of [[2]]'], ['Death cap', 'Damages the [[3]]'], ['Mycelium packaging', 'Put on a compost [[4]]']],
  [(['rise'], 'E', 'dough rise'), (['penicillin'], 'E', 'led to penicillin'), (['liver'], 'F', 'damages the liver'), (['heap'], 'G', 'compost heap')], 1),
 feat('Match each statement with the correct item, A to D.', ['Hyphae', 'Honey fungus', 'Yeast', 'Wheat rust'], [
  ('They are thinner than a human hair.', 0, 'B', 'thinner than a human hair'),
  ('It may be thousands of years old.', 1, 'D', 'two thousand and eight thousand years old'),
  ('It consists of single cells.', 2, 'D', 'single cells'),
  ('It can destroy a harvest.', 3, 'F', 'destroy a harvest'),
 ]),
 multi('Which TWO uses of fungi in food are mentioned in paragraph E?', ['Making dough rise.', 'Ripening cheeses.', 'Making sugar.', 'Smoking fish.', 'Preserving meat.'], [0, 1], [('E', 'dough rise'), ('E', 'ripen some cheeses')]),
 head(['More than a mushroom', 'The great recyclers', 'Partners of the trees', 'Giants and dwarfs', 'Fungi in daily life', 'Dangers', 'Materials of the future', 'The history of cooking', 'Gardening tips'],
  [('A', 0, 'only a small part of a much larger organism'), ('B', 1, 'main recyclers of the forest'), ('C', 2, 'form partnerships with the roots of trees'), ('D', 3, 'largest known living organism'), ('E', 4, 'People have used fungi for a very long time'), ('F', 5, 'Not all fungi are friendly'), ('G', 6, 'new uses for fungi')]),
 info([
  ('a reference to a kingdom of their own', 'A', 'kingdom of their own'),
  ('a reference to nutrients unavailable to plants', 'B', 'unavailable to living plants'),
  ('a reference to a debate among scientists', 'C', 'still being debated'),
  ('a reference to growing in dark rooms', 'E', 'dark rooms'),
  ('a reference to insects being controlled', 'F', 'controlling their behaviour'),
 ]),
 ends(['are fungal threads.', 'recycle dead matter.', 'live in Oregon.', 'lead to penicillin.', 'are plants.', 'make their own food.', 'are always safe.'], [
  ('Hyphae', 0, 'B', 'threads of a fungus'),
  ('Fungi', 1, 'B', 'main recyclers'),
  ('The honey fungus', 2, 'D', 'Blue Mountains of Oregon'),
  ('Fleming\'s discovery', 3, 'E', 'led to penicillin'),
 ]),
 sent(2, [
  ('A mass of hyphae is called a ___.', ['mycelium'], 'B', 'mycelium'),
  ('Honey fungus mushrooms appear in ___.', ['autumn'], 'D', 'in autumn'),
  ('Fleming noticed the mould in his ___ dishes.', ['laboratory'], 'E', 'laboratory dishes'),
  ('Dr Silva is a ___.', ['mycologist'], 'G', 'a mycologist'),
 ]),
 short(3, [
  ('What do fungi release into their surroundings?', ['chemicals'], 'B', 'release chemicals'),
  ('When did Fleming make his observation?', ['1928', 'in 1928'], 'E', 'In 1928'),
  ('What can fungi clean?', ['polluted soil'], 'G', 'polluted soil'),
 ]),
])
