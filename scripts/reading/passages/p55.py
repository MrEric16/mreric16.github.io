from lib import *
from svgs import *
A = """Chocolate is made from the seeds of the cacao tree, which grows only in the hot, wet regions near the equator, in a belt about twenty degrees north and south of it. The Maya and Aztecs of Central America drank a bitter chocolate drink, often flavoured with chilli, more than three thousand years ago, and they valued the seeds so highly that they were used as money. Spanish explorers brought cacao to Europe in the sixteenth century, and when sugar was added, the drink became a fashion of the wealthy."""
B = """The journey from tree to bar begins with harvesting. The cacao tree produces large pods, about the size of a rugby ball, directly on its trunk and thick branches. Each pod contains thirty to fifty seeds, which are called beans, surrounded by a white, sweet pulp. Farmers cut the ripe pods from the tree with a sharp knife on a long pole, taking care not to damage the tree, and split them open with a machete. The work is done by hand, because the trees are fragile and the pods ripen at different times."""
C = """The wet beans and pulp are piled into heaps or boxes and covered with banana leaves, and then left for between five and seven days to ferment. During this time, the pulp turns to liquid and drains away, the temperature rises to about fifty degrees Celsius, and the beans change chemically. Fermentation is essential: without it, the beans taste bitter and have none of the flavours that we recognise as chocolate. Producers often turn the heap every day so that all the beans ferment evenly."""
D = """Next comes drying. The beans are dried, usually by spreading them out in the sun for about a week. They are raked regularly so that they dry evenly, and covered at night or when it rains. The beans lose about half of their weight as the water evaporates. Drying must be done carefully, because beans that are too wet grow mould, while those that are dried too fast stay sour. After drying, the beans are packed into large sacks and shipped to factories, often thousands of kilometres from the farm."""
E = """Roasting follows. At the factory, the beans are cleaned and roasted at temperatures between 100 and 150 degrees Celsius for about half an hour, which develops the flavour. The thin shells are then cracked and removed, leaving small pieces of the bean called nibs. The nibs are ground into a thick, smooth liquid, known as chocolate liquor, although it contains no alcohol. Its fat, called cocoa butter, makes up about half of its weight, and it is the cocoa butter that gives chocolate its characteristic quality of melting in the mouth."""
F = """To make milk chocolate, the liquor is mixed with sugar, milk powder and extra cocoa butter. The mixture is then kneaded for many hours in a machine called a conche, which makes the texture smooth and removes the last traces of bitterness. Finally, the chocolate is heated and cooled in a careful sequence, called tempering, so that it sets with a glossy surface and breaks with a sharp snap. Dark chocolate contains no milk, and the quantity of cocoa in it, shown as a percentage on the packet, tells the buyer how intense the flavour will be."""
G = """The industry faces serious problems. Most of the world's cacao is grown by small farmers in West Africa, many of whom earn very little. Reports have found that in some regions children work on farms in dangerous conditions. Dr Amara Diallo, an agricultural economist, says that farmers receive only a small share of the price of a bar and that the only lasting solution is to pay more for the beans. Some companies now buy only certified cacao, which guarantees fair treatment, though critics say that it is still too rare."""
S, PT, W, H = chain(4)
P = passage('p55', 'The Story of Chocolate', 'Food and culture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The cacao tree grows only near the equator.', 'T', 'A', 'only in the hot, wet regions near the equator'),
  ('The Aztecs used cacao seeds as money.', 'T', 'A', 'they were used as money'),
  ('Spanish explorers brought cacao to Europe.', 'T', 'A', 'Spanish explorers brought cacao to Europe'),
  ('Cacao pods grow at the ends of thin branches.', 'F', 'B', 'directly on its trunk and thick branches'),
  ('Each pod contains thirty to fifty beans.', 'T', 'B', 'thirty to fifty seeds'),
  ('Beans are fermented for about a month.', 'F', 'C', 'between five and seven days'),
  ('Beans lose about half their weight during drying.', 'T', 'D', 'lose about half of their weight'),
  ('Chocolate liquor contains alcohol.', 'F', 'E', 'it contains no alcohol'),
  ('Dark chocolate is the healthiest kind.', 'NG', 'F', 'Dark chocolate contains no milk', 'Health effects are not discussed.'),
 ]),
 mcq([
  ('Why is harvesting done by hand?', ['Machines are banned.', 'The trees are fragile and pods ripen at different times.', 'Pods are small.', 'Workers are cheap.'], 1, 'B', 'the trees are fragile and the pods ripen at different times'),
  ('What happens if beans are not fermented?', ['They taste bitter.', 'They grow mould.', 'They turn green.', 'They become sweet.'], 0, 'C', 'the beans taste bitter'),
  ('What does Dr Diallo say is the lasting solution?', ['New trees.', 'Paying more for the beans.', 'Fewer farms.', 'Cheaper sugar.'], 1, 'G', 'pay more for the beans'),
 ]),
 multi('Which TWO things are added to chocolate liquor to make milk chocolate?', ['Sugar.', 'Milk powder.', 'Salt.', 'Water.', 'Honey.'], [0, 1], [('F', 'sugar, milk powder and extra cocoa butter'), ('F', 'sugar, milk powder and extra cocoa butter')]),
 head(['Ancient origins', 'Gathering the pods', 'A chemical change in heaps', 'Removing the water', 'Making the liquid', 'Smoothing and shaping', 'Trouble for farmers', 'The history of sugar', 'How to taste chocolate'],
  [('A', 0, 'more than three thousand years ago'), ('B', 1, 'The journey from tree to bar begins with harvesting'), ('C', 2, 'left for between five and seven days to ferment'), ('D', 3, 'Next comes drying'), ('E', 4, 'The nibs are ground into a thick, smooth liquid'), ('F', 5, 'To make milk chocolate'), ('G', 6, 'The industry faces serious problems')]),
 info([
  ('a comparison of the size of a pod with a ball', 'B', 'about the size of a rugby ball'),
  ('a reference to the temperature of fermentation', 'C', 'about fifty degrees Celsius'),
  ('a reference to the risk of mould', 'D', 'beans that are too wet grow mould'),
  ('a description of a substance that makes chocolate melt in the mouth', 'E', 'cocoa butter'),
  ('a reference to children working', 'G', 'children work on farms'),
 ]),
 ends(['are cut with a knife on a pole.', 'are covered with banana leaves.', 'are raked regularly.', 'are cracked to remove the shells.', 'are grown only in Europe.', 'were invented by the Spanish.', 'are never roasted.'], [
  ('Ripe pods', 0, 'B', 'cut the ripe pods from the tree with a sharp knife on a long pole'),
  ('Fermenting beans', 1, 'C', 'covered with banana leaves'),
  ('Drying beans', 2, 'D', 'They are raked regularly'),
  ('Roasted beans', 3, 'E', 'The thin shells are then cracked and removed'),
 ]),
 diag('Label the stages in the journey of chocolate. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['harvesting'], 'B', 'begins with harvesting'), (['fermentation'], 'C', 'Fermentation is essential'), (['drying'], 'D', 'Next comes drying'), (['roasting'], 'E', 'Roasting follows')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Stage', 'Detail'],
  [['Harvesting', 'Pods are split open with a [[1]]'], ['Fermenting', 'Beans are covered with [[2]] leaves'], ['Drying', 'Beans are spread out in the [[3]]'], ['Conching', 'The machine is called a [[4]]']],
  [(['machete'], 'B', 'with a machete'), (['banana'], 'C', 'banana leaves'), (['sun'], 'D', 'in the sun'), (['conche'], 'F', 'a machine called a conche')], 1),
 sent(2, [
  ('The Maya and Aztecs flavoured their drink with ___.', ['chilli'], 'A', 'flavoured with chilli'),
  ('The beans are surrounded by a white, sweet ___.', ['pulp'], 'B', 'a white, sweet pulp'),
  ('Small pieces of bean are called ___.', ['nibs'], 'E', 'called nibs'),
  ('Heating and cooling chocolate carefully is called ___.', ['tempering'], 'F', 'called tempering'),
 ]),
 short(3, [
  ('How long are beans dried?', ['about a week', 'a week'], 'D', 'for about a week'),
  ('What makes up about half of the liquor?', ['cocoa butter'], 'E', 'Its fat, called cocoa butter'),
  ('Where is most cacao grown?', ['west africa'], 'G', 'in West Africa'),
 ]),
])
