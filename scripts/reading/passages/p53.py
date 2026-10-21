from lib import *
A = """The giant panda is one of the most easily recognised animals in the world, with its round face, black patches around the eyes and thick black-and-white coat. It lives in a few mountain forests in central China, in the provinces of Sichuan, Shaanxi and Gansu, at heights of between 1,200 and 3,400 metres. Pandas have become the symbol of the World Wide Fund for Nature, and the sight of one chewing bamboo can attract crowds of visitors to zoos in many countries of the world. Its slow, gentle manner and its habit of sitting upright to eat make it especially appealing to children, and baby pandas are among the most popular animals ever filmed."""
B = """Although pandas belong to the group of animals known as carnivores, which includes bears, cats and dogs, their diet consists almost entirely of bamboo. A panda eats between twelve and thirty-eight kilograms of it each day, and spends about twelve hours a day feeding. Because bamboo gives little nourishment, and the panda's digestive system is better suited to meat, it must eat huge amounts. Pandas have a special adaptation: a bone in the wrist, called the false thumb, which they use to hold the stalks."""
C = """Pandas are solitary animals. Each adult has its own territory, which it marks with scent from glands under its tail, and it avoids contact with others except during the breeding season in spring. Female pandas can have babies only once every two years, and they usually give birth to one or two cubs. A newborn cub is tiny, weighing about one hundred grams, which is roughly a thousandth of its mother's weight, and it is blind, pink and almost hairless."""
D = """If two cubs are born, the mother usually raises only one, because she cannot find enough food for both. The cub opens its eyes at about six to eight weeks, and begins to crawl after three months. It stays with its mother for about eighteen months to two years, learning which bamboo to eat and how to climb trees. Cubs are very playful and spend much of their time wrestling with each other and rolling down slopes, which scientists believe helps to develop strong muscles."""
E = """During the twentieth century, the panda's population fell dangerously. The forests where it lives were cut down for farmland and for timber, and the bamboo itself periodically flowers and dies, which leaves pandas without food unless they can move to another area. In the 1980s, the number of wild pandas fell to about 1,100. China responded by creating a network of nature reserves, planting bamboo corridors between forests, and banning hunting and logging."""
F = """The effort has been successful. A survey in 2014 counted 1,864 pandas in the wild, and in 2016 the International Union for Conservation of Nature, which keeps the record of threatened species, changed the panda's status from 'endangered' to 'vulnerable'. Zoos have contributed by learning how to breed pandas in captivity, a task that was long thought to be impossible. Some captive-bred animals have been released into the forests, but a good deal of care is needed to prepare them. Scientists teach the young animals to find food and to avoid people before they leave the breeding centre, and they track them afterwards with collars that send signals to satellites."""
G = """Nevertheless, the future of the panda is not secure. Climate change may reduce the area of bamboo by a third in the next eighty years, and roads and dams divide the forests into smaller pieces, so that pandas cannot find mates. Dr Wei Zhang, a conservation biologist, says that protecting the panda also protects thousands of other species that share its forest, which is why the animal is sometimes called an umbrella species. The panda thus matters far more than its charm alone would suggest."""
P = passage('p53', 'The Giant Panda', 'Wildlife', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Giant pandas live in the mountains of central China.', 'T', 'A', 'mountain forests in central China'),
  ('Pandas are the symbol of the World Wide Fund for Nature.', 'T', 'A', 'the symbol of the World Wide Fund for Nature'),
  ('Pandas eat mainly meat.', 'F', 'B', 'consists almost entirely of bamboo'),
  ('Pandas spend about twelve hours a day feeding.', 'T', 'B', 'about twelve hours a day feeding'),
  ('Pandas live in large groups.', 'F', 'C', 'Pandas are solitary animals'),
  ('A newborn cub is blind.', 'T', 'C', 'it is blind, pink and almost hairless'),
  ('The mother raises both cubs when two are born.', 'F', 'D', 'usually raises only one'),
  ('Pandas in zoos are all descended from wild pandas caught in 1980.', 'NG', 'F', 'learning how to breed pandas in captivity', 'The origin of captive pandas is not given.'),
  ('The panda\'s status was changed in 2016.', 'T', 'F', 'in 2016'),
 ]),
 mcq([
  ('Why must pandas eat so much bamboo?', ['It is delicious.', 'It gives little nourishment.', 'It is easy to find.', 'They share it with cubs.'], 1, 'B', 'bamboo gives little nourishment'),
  ('What happens when bamboo flowers and dies?', ['Pandas move away or lack food.', 'Pandas breed more.', 'The forest grows.', 'Pandas hibernate.'], 0, 'E', 'leaves pandas without food unless they can move'),
  ('Why is the panda called an umbrella species?', ['It is large.', 'Protecting it protects other species.', 'It lives in the rain.', 'It is white.'], 1, 'G', 'protects thousands of other species'),
 ]),
 multi('Which TWO measures taken by China are mentioned in paragraph E?', ['Creating nature reserves.', 'Planting bamboo corridors.', 'Building zoos in cities.', 'Importing bamboo.', 'Moving pandas to Europe.'], [0, 1], [('E', 'creating a network of nature reserves'), ('E', 'planting bamboo corridors between forests')]),
 head(['An animal known around the world', 'A strange diet', 'A solitary way of life', 'Raising a cub', 'A population in danger', 'Signs of success', 'Continuing threats', 'The history of zoos', 'How to grow bamboo'],
  [('A', 0, 'one of the most easily recognised animals in the world'), ('B', 1, 'their diet consists almost entirely of bamboo'), ('C', 2, 'Pandas are solitary animals'), ('D', 3, 'If two cubs are born'), ('E', 4, 'the panda\'s population fell dangerously'), ('F', 5, 'The effort has been successful'), ('G', 6, 'the future of the panda is not secure')]),
 info([
  ('a list of provinces where pandas live', 'A', 'Sichuan, Shaanxi and Gansu'),
  ('a reference to a special bone', 'B', 'a bone in the wrist, called the false thumb'),
  ('a comparison of a cub\'s weight with its mother\'s', 'C', 'roughly a thousandth of its mother\'s weight'),
  ('a mention of a figure for the wild population in the 1980s', 'E', 'about 1,100'),
  ('a mention of a threat caused by roads and dams', 'G', 'roads and dams divide the forests into smaller pieces'),
 ]),
 ends(['holds stalks with a false thumb.', 'marks its territory with scent.', 'stays with its mother for about two years.', 'was changed to vulnerable in 2016.', 'is a kind of tree.', 'lives in the desert.', 'is a meat-eater only.'], [
  ('A panda', 0, 'B', 'a bone in the wrist, called the false thumb, which they use to hold the stalks'),
  ('An adult panda', 1, 'C', 'marks with scent from glands under its tail'),
  ('A cub', 2, 'D', 'stays with its mother for about eighteen months to two years'),
  ('The status of the panda', 3, 'F', 'changed the panda\'s status from \'endangered\' to \'vulnerable\''),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Topic', 'Detail'],
  [['Diet', 'Almost entirely [[1]]'], ['Breeding', 'Females have cubs once every [[2]] years'], ['1980s', 'About [[3]] wild pandas remained'], ['2014', 'A survey counted [[4]] pandas']],
  [(['bamboo'], 'B', 'almost entirely of bamboo'), (['two'], 'C', 'once every two years'), (['1,100'], 'E', 'about 1,100'), (['1,864'], 'F', '1,864 pandas in the wild')], 2),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Two cubs are born, but the mother raises only [[1]].', 'The cub opens its [[2]] at six to eight weeks.', 'It begins to [[3]] after three months.', 'It stays with its mother for up to two [[4]].'],
  [(['one'], 'D', 'raises only one'), (['eyes'], 'D', 'opens its eyes'), (['crawl'], 'D', 'begins to crawl'), (['years'], 'D', 'two years')], 1),
 sent(2, [
  ('Pandas live at heights of between 1,200 and 3,400 ___.', ['metres'], 'A', 'between 1,200 and 3,400 metres'),
  ('A newborn cub weighs about one hundred ___.', ['grams'], 'C', 'about one hundred grams'),
  ('Forests were cut down for farmland and ___.', ['timber'], 'E', 'farmland and for timber'),
  ('Dr Zhang is a conservation ___.', ['biologist'], 'G', 'a conservation biologist'),
 ]),
 short(3, [
  ('How much bamboo does a panda eat in a day, at most?', ['thirty-eight kilograms', '38 kilograms'], 'B', 'thirty-eight kilograms'),
  ('What do pandas use the false thumb for?', ['to hold stalks', 'hold the stalks', 'holding stalks'], 'B', 'which they use to hold the stalks'),
  ('Who keeps the record of threatened species?', ['international union', 'iucn'], 'F', 'the International Union for Conservation of Nature'),
 ]),
])
