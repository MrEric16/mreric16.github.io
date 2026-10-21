from lib import *
from svgs import *
A = """The African elephant is the largest animal that lives on land. A fully grown bull can stand three and a half metres at the shoulder and weigh up to six tonnes, as much as five or six family cars. Despite its size, the elephant is gentle and highly intelligent, with a brain that is the biggest of any land animal, and its social life is as complex as that of any creature except humans. For these reasons elephants have fascinated people for thousands of years, and they have appeared in the myths, art and wars of many cultures. This passage describes their remarkable bodies and minds and the dangers they now face."""
B = """The trunk is the elephant's most useful tool. It is a combination of the nose and the upper lip, and it contains about forty thousand separate muscles, but no bones. With it, an elephant can lift a log weighing several hundred kilograms or pick up a single peanut. It is used for breathing, smelling, drinking, which means sucking up as much as ten litres of water and squirting it into the mouth, and for greeting other elephants by touch. The elephant can also use the trunk as a snorkel when it crosses deep rivers. The tusks, which are very long teeth, are used for digging, for stripping bark from trees and for defence."""
C = """Elephants live in family groups, led by the oldest female, the matriarch. A herd usually consists of her sisters, daughters and their young, perhaps ten or twenty animals in all. The matriarch's most valuable asset is her memory: she remembers where to find water in a drought, which routes are safe, and which other herds are friends or enemies. Young males leave the herd at about fourteen years old and live alone or with other males. Calves are born after a pregnancy of twenty-two months, the longest of any mammal, and the whole herd helps to protect and raise them."""
D = """Elephants communicate in many ways. They trumpet when excited or alarmed, and they use a range of rumbles, snorts and cries. Some of the rumbles are so low that humans cannot hear them; these sounds, called infrasound, travel for kilometres through the ground and the air, so that herds that cannot see one another can still keep in contact. Elephants can feel these vibrations through the soles of their feet, and they sometimes stand still with one foot raised, apparently listening. They also have a range of body language, flapping their ears, raising their trunks or touching one another gently when they meet."""
E = """Elephants show signs of intelligence and emotion that few other animals match. Like dolphins and apes, they can recognise themselves in a mirror, a test which only a small number of species pass. They use tools, breaking branches to swat flies, and they have been seen to help injured companions. A herd will gather around a dead relative, touch the bones with their trunks and stay for hours, behaviour which suggests grief. Researchers have also recorded elephants showing great concern for the young, comforting a calf which is frightened with a gentle touch of the trunk."""
F = """Sadly, elephants are in danger. A century ago there were several million African elephants; today there are fewer than half a million. The main threat is the loss of habitat: as human populations grow, farms and roads divide the land, and elephants that wander on to fields may destroy a family's harvest in a single night. The second is poaching for ivory, which has killed tens of thousands of animals in some years. Because elephants live for up to seventy years and breed slowly, a population needs decades to recover from heavy losses."""
G = """Dr Wanjiru Kamau, a conservation biologist in Kenya, leads a project that helps farmers and elephants to live side by side. Farmers plant rows of chilli bushes around their fields, because elephants dislike the smell, and they hang beehives from the fence, since elephants are afraid of bees. The programme has reduced crop damage and given farmers an extra source of income from the honey. Dr Kamau believes that protecting elephants will succeed only if local people benefit, and that simple, cheap solutions are often better than expensive ones."""
P = passage('p84', 'The African Elephant', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('A bull elephant can weigh up to six tonnes.', 'T', 'A', 'up to six tonnes'),
  ('Elephants have the biggest brain of any land animal.', 'T', 'A', 'the biggest of any land animal'),
  ('The trunk contains many bones.', 'F', 'B', 'but no bones'),
  ('An elephant can suck up water with its trunk.', 'T', 'B', 'sucking up as much as ten litres of water'),
  ('The herd is led by the oldest male.', 'F', 'C', 'the oldest female'),
  ('An elephant\'s pregnancy lasts twenty-two months.', 'T', 'C', 'twenty-two months'),
  ('Infrasound can travel for kilometres.', 'T', 'D', 'travel for kilometres'),
  ('Elephants use tools.', 'T', 'E', 'They use tools'),
  ('Elephants can swim across the sea.', 'NG', 'B', 'snorkel when it crosses deep rivers', 'Crossing the sea is not mentioned.'),
 ]),
 mcq([
  ('What is the matriarch\'s most valuable asset?', ['Her tusks.', 'Her memory.', 'Her speed.', 'Her size.'], 1, 'C', 'most valuable asset is her memory'),
  ('How do elephants feel infrasound?', ['Through their ears only.', 'Through the soles of their feet.', 'Through their tusks.', 'Through their skin.'], 1, 'D', 'through the soles of their feet'),
  ('Why do farmers plant chilli bushes?', ['Elephants dislike the smell.', 'Elephants eat chilli.', 'Bees like chilli.', 'Chilli sells well.'], 0, 'G', 'elephants dislike the smell'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Trunk', 'Contains about forty thousand [[1]]'], ['Herd', 'Led by the oldest [[2]]'], ['Pregnancy', 'Lasts twenty-two [[3]]'], ['Chilli bushes', 'Elephants dislike the [[4]]']],
  [(['muscles'], 'B', 'forty thousand separate muscles'), (['female'], 'C', 'the oldest female'), (['months'], 'C', 'twenty-two months'), (['smell'], 'G', 'dislike the smell')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The matriarch remembers where to find [[1]].', 'Low rumbles called [[2]] travel for kilometres.', 'Elephants feel vibrations through their [[3]].', 'Farmers hang [[4]] from fences.'],
  [(['water'], 'C', 'where to find water'), (['infrasound'], 'D', 'called infrasound'), (['feet'], 'D', 'soles of their feet'), (['beehives'], 'G', 'hang beehives')], 1),
 feat('Match each statement with the correct item, A to D.', ['The trunk', 'The matriarch', 'Infrasound', 'Bee fences'], [
  ('It can pick up a single peanut.', 0, 'B', 'pick up a single peanut'),
  ('She remembers which routes are safe.', 1, 'C', 'which routes are safe'),
  ('It lets herds that cannot see each other keep in contact.', 2, 'D', 'cannot see one another'),
  ('They frighten elephants away from crops.', 3, 'G', 'afraid of bees'),
 ]),
 multi('Which TWO uses of the tusks are mentioned in paragraph B?', ['Digging.', 'Stripping bark from trees.', 'Fighting lions.', 'Carrying water.', 'Cutting grass.'], [0, 1], [('B', 'digging'), ('B', 'stripping bark from trees')]),
 head(['The giant of the land', 'A tool with forty thousand muscles', 'A family led by a female', 'Messages too low to hear', 'Signs of a clever mind', 'A shrinking population', 'Living side by side', 'The history of the circus', 'Elephants in Asia'],
  [('A', 0, 'the largest animal that lives on land'), ('B', 1, 'about forty thousand separate muscles'), ('C', 2, 'led by the oldest female'), ('D', 3, 'so low that humans cannot hear them'), ('E', 4, 'intelligence and emotion that few other animals match'), ('F', 5, 'fewer than half a million'), ('G', 6, 'live side by side')]),
 info([
  ('a comparison with cars', 'A', 'family cars'),
  ('a reference to a snorkel', 'B', 'snorkel'),
  ('a reference to young males leaving the herd', 'C', 'Young males leave the herd'),
  ('a reference to standing with a raised foot', 'D', 'one foot raised'),
  ('a reference to grief', 'E', 'suggests grief'),
 ]),
 ends(['is used for breathing and drinking.', 'leads the herd.', 'has killed tens of thousands.', 'works with farmers.', 'lives in Asia.', 'is a kind of tusk.', 'cannot hear.'], [
  ('The trunk', 0, 'B', 'breathing, smelling, drinking'),
  ('The matriarch', 1, 'C', 'led by the oldest female'),
  ('Poaching', 2, 'F', 'tens of thousands of animals'),
  ('Dr Kamau', 3, 'G', 'helps farmers and elephants'),
 ]),
 sent(2, [
  ('The oldest female in a herd is called the ___.', ['matriarch'], 'C', 'the matriarch'),
  ('Very low sounds are called ___.', ['infrasound'], 'D', 'called infrasound'),
  ('Elephants live for up to ___ years.', ['seventy', '70'], 'F', 'up to seventy years'),
  ('Dr Kamau is a conservation ___.', ['biologist'], 'G', 'conservation biologist'),
 ]),
 short(3, [
  ('How many muscles does the trunk contain?', ['forty thousand', 'about forty thousand'], 'B', 'about forty thousand'),
  ('At what age do young males leave the herd?', ['fourteen', 'about fourteen'], 'C', 'about fourteen years old'),
  ('What do elephants do with a dead relative?', ['touch the bones'], 'E', 'touch the bones with their trunks'),
 ]),
])
