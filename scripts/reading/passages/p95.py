from lib import *
from svgs import *
A = """Rice is the main food of more than half of the world's people. In many Asian languages, the word for rice is the same as the word for meal, and to ask someone whether they have eaten is to ask whether they have eaten rice. About ninety per cent of the world's rice is grown and eaten in Asia, though it is also an important crop in Africa and Latin America, and in Uzbekistan the rice dish plov is a national symbol. Rice has been cultivated for around nine thousand years, and it supplies about a fifth of all the calories eaten by humans. This passage explains how rice is grown, why it is special and what threatens it."""
B = """Rice is a grass, and its seeds, called grains, are the part we eat. Most of it is grown in flooded fields called paddies. The farmer begins by preparing the soil and flooding the field with water. Young plants are raised in a nursery and then transplanted by hand, or by machine, into the mud. The plants grow for three to six months, standing in water that is about ten centimetres deep. Flooding helps rice for two reasons: it suppresses weeds, which cannot grow in deep water, and it provides the plants with a steady supply of moisture."""
C = """The process of harvesting begins when the field is drained and the grains turn golden. In many parts of the world, the crop is still cut with a sickle, but large farms use combine harvesters. The grain is separated from the stalks by threshing and then dried, which prevents it from rotting in storage. At this stage the grain is still covered by a hard husk. Removing the husk gives brown rice, which keeps its outer layer of bran, and polishing it off gives white rice. Brown rice has more fibre and vitamins, but white rice stores better, which is why it is more widely eaten."""
D = """Many varieties of rice exist: scientists estimate that there are over forty thousand. Long-grain rice, such as basmati, stays separate and fluffy when cooked, while short-grain rice becomes sticky, and is used for dishes like sushi and rice pudding. Uzbekistan is famous for its own varieties, including a firm, long grain grown in the Khorezm and Syr Darya regions, which is considered ideal for plov because it absorbs flavour without turning to paste. Different cultures use rice in many ways, from porridge for breakfast to noodles, flour, drinks and even paper."""
E = """Rice farming has a surprising effect on the environment. Flooded paddies contain very little oxygen, so bacteria in the mud produce methane, a gas which traps heat in the atmosphere far more effectively than carbon dioxide. Rice fields are estimated to produce around ten per cent of the methane released by human activity. Growing rice also requires a great deal of water: producing one kilogram of rice may require between two and five thousand litres, depending on the method used. In regions where water is scarce, such as parts of Central Asia, this is a serious problem."""
F = """In the 1960s, scientists in the Philippines developed new varieties of rice which were short and sturdy, so that they did not fall over when loaded with grain, and which gave much higher yields. This was part of the Green Revolution, which is credited with feeding hundreds of millions of people who might otherwise have starved. Dr Ravi Menon, a plant breeder, notes that yields in many countries have since doubled or tripled. However, the new varieties often need large amounts of fertiliser and water, and critics say that the traditional varieties, which are adapted to local conditions, were lost in the process."""
G = """Today the challenge is to grow more rice with less water and less pollution. One technique, called alternate wetting and drying, lets the field dry out for a few days between irrigations, and it can save a quarter of the water and cut methane by almost half, without lowering yields. Scientists are also developing varieties which tolerate drought, salt or floods, and one has been bred to carry extra vitamin A. Dr Menon believes that with careful management, rice farmers will be able to feed a growing population, but warns that climate change, which may bring droughts to some regions and floods to others, will test them severely."""
P = passage('p95', 'The Story of Rice', 'Agriculture', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Rice is the main food of more than half the world\'s people.', 'T', 'A', 'more than half of the world\'s people'),
  ('About ninety per cent of rice is grown in Asia.', 'T', 'A', 'About ninety per cent'),
  ('Rice has been cultivated for about nine thousand years.', 'T', 'A', 'nine thousand years'),
  ('Rice is a type of tree.', 'F', 'B', 'Rice is a grass'),
  ('Flooding helps suppress weeds.', 'T', 'B', 'suppresses weeds'),
  ('White rice contains more fibre than brown rice.', 'F', 'C', 'Brown rice has more fibre'),
  ('There are over forty thousand varieties of rice.', 'T', 'D', 'over forty thousand'),
  ('Rice fields produce around ten per cent of human methane emissions.', 'T', 'E', 'around ten per cent'),
  ('Basmati rice is grown in Uzbekistan.', 'NG', 'D', 'Long-grain rice, such as basmati', 'Where basmati grows is not stated.'),
 ]),
 mcq([
  ('Why is white rice more widely eaten than brown?', ['It stores better.', 'It is cheaper to grow.', 'It has more vitamins.', 'It has more fibre.'], 0, 'C', 'white rice stores better'),
  ('Why is Uzbek rice ideal for plov?', ['It absorbs flavour without turning to paste.', 'It is sticky.', 'It is white.', 'It is sweet.'], 0, 'D', 'absorbs flavour without turning to paste'),
  ('What is a criticism of the Green Revolution?', ['Traditional varieties were lost.', 'Yields fell.', 'Rice became smaller.', 'Farmers used less water.'], 0, 'F', 'traditional varieties'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The soil is prepared and the field is [[1]].', 'Young plants are transplanted into the [[2]].', 'The field is [[3]] and the grains turn golden.', 'The grain is separated by [[4]].'],
  [(['flooded'], 'B', 'flooded fields'), (['mud'], 'B', 'into the mud'), (['drained'], 'C', 'drained'), (['threshing'], 'C', 'threshing')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Type', 'Feature'],
  [['Brown rice', 'Keeps its outer layer of [[1]]'], ['White rice', 'Stores [[2]]'], ['Long-grain rice', 'Stays [[3]] and fluffy'], ['Short-grain rice', 'Becomes [[4]]']],
  [(['bran'], 'C', 'bran'), (['better'], 'C', 'stores better'), (['separate'], 'D', 'separate and fluffy'), (['sticky'], 'D', 'becomes sticky')], 1),
 feat('Match each statement with the correct item, A to D.', ['Paddy', 'Methane', 'Green Revolution', 'Alternate wetting and drying'], [
  ('A flooded field for rice.', 0, 'B', 'flooded fields called paddies'),
  ('A gas that traps heat.', 1, 'E', 'traps heat'),
  ('It developed higher-yielding varieties in the 1960s.', 2, 'F', 'much higher yields'),
  ('It can save a quarter of the water.', 3, 'G', 'a quarter of the water'),
 ]),
 multi('Which TWO uses of rice are mentioned in paragraph D?', ['Porridge.', 'Noodles.', 'Fuel.', 'Medicine.', 'Soap.'], [0, 1], [('D', 'porridge'), ('D', 'noodles')]),
 head(['The food of billions', 'Growing in water', 'From field to bowl', 'Thousands of varieties', 'A hidden cost', 'A revolution in the fields', 'Growing more with less', 'The history of sushi', 'Cooking tips'],
  [('A', 0, 'main food of more than half'), ('B', 1, 'flooded fields called paddies'), ('C', 2, 'Removing the husk'), ('D', 3, 'over forty thousand'), ('E', 4, 'surprising effect on the environment'), ('F', 5, 'Green Revolution'), ('G', 6, 'grow more rice with less water')]),
 info([
  ('a reference to the word for meal', 'A', 'the word for meal'),
  ('a reference to seedlings in a nursery', 'B', 'nursery'),
  ('a reference to a sickle', 'C', 'sickle'),
  ('a reference to the Khorezm region', 'D', 'Khorezm'),
  ('a reference to vitamin A', 'G', 'vitamin A'),
 ]),
 ends(['is a symbol of Uzbekistan.', 'suppresses weeds.', 'produce methane.', 'tolerate drought.', 'is grown on trees.', 'needs no water.', 'is eaten only in Asia.'], [
  ('Plov', 0, 'A', 'national symbol'),
  ('Flooding', 1, 'B', 'suppresses weeds'),
  ('Rice fields', 2, 'E', 'around ten per cent of the methane'),
  ('New varieties', 3, 'G', 'tolerate drought'),
 ]),
 sent(2, [
  ('Rice is a type of ___.', ['grass'], 'B', 'a grass'),
  ('The hard covering of the grain is called the ___.', ['husk'], 'C', 'hard husk'),
  ('Producing one kilogram of rice needs two to five thousand ___ of water.', ['litres'], 'E', 'thousand litres'),
  ('Dr Menon is a plant ___.', ['breeder'], 'F', 'plant breeder'),
 ]),
 short(3, [
  ('How deep is the water in a paddy?', ['ten centimetres', 'about ten centimetres'], 'B', 'about ten centimetres'),
  ('Where were the new varieties developed?', ['the philippines', 'philippines'], 'F', 'in the Philippines'),
  ('How much methane can drying cut?', ['almost half'], 'G', 'almost half'),
 ]),
])
