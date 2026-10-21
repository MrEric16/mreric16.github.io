from lib import *
from svgs import *
A = """Bread is one of the oldest prepared foods in the world, and in many countries, including Uzbekistan, it is treated with respect: a piece of bread is never thrown on the ground, and guests are welcomed with it. Archaeologists have found evidence of bread-making more than fourteen thousand years ago, long before farming began. Yet every loaf is the result of a long chain of work, beginning in a field and ending in an oven, and involving farmers, millers and bakers. This passage follows the journey of a loaf of bread, step by step, and then looks at the traditional Uzbek method of baking in a clay oven."""
B = """The journey begins in the field, where farmers sow wheat seeds in autumn or in spring, depending on the variety. During the growing season the crop needs sun, rain and care: farmers must control weeds and pests and sometimes add fertiliser. When the stalks turn golden, in early summer, harvesting begins, and a combine harvester cuts the wheat and separates the grain from the straw in a single operation. A century ago the same task required dozens of people with sickles and many days of work. The grain is then dried and stored in silos, large towers in which it can be kept for a year without spoiling."""
C = """The next step is milling. The grain is cleaned, and then passed between heavy steel rollers, which crush it into flour. Each grain of wheat has three parts: the outer layer, called bran, the germ, which is the seed's embryo, and the starchy middle. In white flour, the bran and germ are sifted out, leaving a soft, pale powder that keeps for a long time; in wholemeal flour, the whole grain is used, which means the bread contains more fibre and vitamins. In the past, water mills and windmills turned heavy stones for this task, and some small mills still do."""
D = """At the bakery, the stage of mixing begins. The baker combines flour with water, salt and yeast. Yeast is a tiny living fungus, which feeds on the sugars in the flour and releases carbon dioxide. The mixture is kneaded, which means pushing and stretching it for several minutes, so that the proteins in the flour form long, elastic threads called gluten. These threads trap the gas, and they allow the dough to expand like a balloon. A good baker can tell by the feel of the dough whether it has been kneaded enough. Without yeast, the dough would not rise, and the result would be a flat bread, like the unleavened breads of ancient times."""
E = """The dough is then shaped and left to rise in a warm place, a stage called proving. During about an hour, the yeast multiplies and the dough doubles in size, filled with thousands of tiny bubbles. If the dough is left too long, the bubbles break and the loaf collapses; if it is baked too soon, the bread is dense and heavy. Bakers therefore watch the temperature carefully, for the yeast works faster in the warm air of summer than in the cold of winter. Before baking, they often cut the surface with a sharp knife, so that the loaf can expand in the oven without cracking."""
F = """Finally comes baking. In a hot oven, at around two hundred and twenty degrees, the gas in the dough expands rapidly, the yeast dies, and the starch sets into a firm structure. The outside of the loaf turns brown and crisp, as sugars and proteins react in a process which also creates the rich smell of fresh bread. A loaf of ordinary size takes about thirty to forty minutes. When it is done, it should sound hollow if tapped on the bottom. After baking, the bread should be left to cool for a short time, as the inside continues to cook slightly and the crumb needs to set."""
G = """In Uzbekistan, bread is traditionally baked in a tandoor, a round clay oven heated by burning wood at the bottom. The baker, called a nonvoy, stretches the dough on a cushion, stamps a pattern on it with a special tool, and presses it against the hot inner wall of the oven, where it bakes in a few minutes. Every region has its own style: the famous bread of Samarkand is thick and round, and is said to stay fresh for days. Dr Gulnora Rashidova, a food historian, says that the patterns on the bread are signs of local identity, much as a signature is for a person."""
S, PT, W, H = chain(5)
P = passage('p73', 'The Journey of Bread', 'Food and culture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Bread-making is more than fourteen thousand years old.', 'T', 'A', 'more than fourteen thousand years ago'),
  ('Bread is thrown away freely in Uzbekistan.', 'F', 'A', 'never thrown on the ground'),
  ('Farmers sow wheat only in autumn.', 'F', 'B', 'autumn or in spring'),
  ('A combine harvester separates grain from straw.', 'T', 'B', 'separates the grain from the straw'),
  ('White flour contains the bran.', 'F', 'C', 'the bran and germ are sifted out'),
  ('Wholemeal bread contains more fibre.', 'T', 'C', 'more fibre and vitamins'),
  ('Gluten threads trap gas in the dough.', 'T', 'D', 'trap the gas'),
  ('Dough is proved for about an hour.', 'T', 'E', 'During about an hour'),
  ('The bread of Samarkand was invented by Timur.', 'NG', 'G', 'the famous bread of Samarkand', 'Its inventor is not named.'),
 ]),
 mcq([
  ('What happens if dough is left too long to prove?', ['The loaf collapses.', 'It turns sweet.', 'It freezes.', 'It becomes flour.'], 0, 'E', 'the bubbles break and the loaf collapses'),
  ('Why do bakers cut the surface of a loaf?', ['So it can expand without cracking.', 'To add salt.', 'To cool it.', 'To measure it.'], 0, 'E', 'expand in the oven without cracking'),
  ('What do the patterns on Uzbek bread show?', ['Local identity.', 'The price.', 'The weight.', 'The age.'], 0, 'G', 'signs of local identity'),
 ]),
 diag('Label the stages in making bread, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['harvesting'], 'B', 'harvesting begins'), (['milling'], 'C', 'The next step is milling'), (['mixing'], 'D', 'the stage of mixing'), (['proving'], 'E', 'called proving'), (['baking'], 'F', 'Finally comes baking')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Harvesting', 'Grain is stored in [[1]]'], ['Milling', 'A grain has bran, starch and [[2]]'], ['Mixing', 'Without yeast, the dough would not [[3]]'], ['Baking', 'A loaf takes about thirty to forty [[4]]']],
  [(['silos'], 'B', 'stored in silos'), (['germ'], 'C', 'the germ'), (['rise'], 'D', 'the dough would not rise'), (['minutes'], 'F', 'thirty to forty minutes')], 1),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Wheat is cut by a combine [[1]] and ground into flour between steel [[2]]. Yeast makes the dough rise because the elastic threads trap the [[3]], and in Uzbekistan bread is baked in a clay oven called a [[4]].',
  [(['harvester'], 'B', 'combine harvester'), (['rollers'], 'C', 'steel rollers'), (['gas'], 'D', 'trap the gas'), (['tandoor'], 'G', 'in a tandoor')], 1,
  bank=['harvester', 'rollers', 'gas', 'tandoor', 'sickle', 'stones', 'water', 'wood']),
 multi('Which TWO parts of the wheat grain are mentioned in paragraph C?', ['The bran.', 'The germ.', 'The husk.', 'The shell.', 'The stem.'], [0, 1], [('C', 'called bran'), ('C', 'the germ')]),
 head(['An ancient food', 'From seed to silo', 'Turning grain into flour', 'Making the dough', 'Waiting for the rise', 'The heat of the oven', 'A clay oven tradition', 'The history of the plough', 'Healthy eating habits'],
  [('A', 0, 'one of the oldest prepared foods in the world'), ('B', 1, 'The journey begins in the field'), ('C', 2, 'crush it into flour'), ('D', 3, 'The baker combines flour with water, salt and yeast'), ('E', 4, 'left to rise in a warm place'), ('F', 5, 'In a hot oven'), ('G', 6, 'baked in a tandoor')]),
 info([
  ('a comparison with an earlier method of harvesting', 'B', 'dozens of people with sickles'),
  ('a reference to water mills', 'C', 'water mills and windmills'),
  ('a comparison with a balloon', 'D', 'like a balloon'),
  ('a reference to the effect of the season on yeast', 'E', 'warm air of summer'),
  ('a way of testing whether a loaf is ready', 'F', 'sound hollow'),
 ]),
 ends(['store grain for a year.', 'releases carbon dioxide.', 'makes the loaf collapse.', 'presses dough on the oven wall.', 'grinds the wheat.', 'sows the seeds.', 'sells the flour.'], [
  ('Silos', 0, 'B', 'kept for a year without spoiling'),
  ('Yeast', 1, 'D', 'releases carbon dioxide'),
  ('Overproved dough', 2, 'E', 'the loaf collapses'),
  ('A nonvoy', 3, 'G', 'presses it against the hot inner wall'),
 ]),
 sent(2, [
  ('Bread is made from flour, water, salt and ___.', ['yeast'], 'D', 'salt and yeast'),
  ('The stage when the dough rises is called ___.', ['proving'], 'E', 'called proving'),
  ('Bread is baked at around two hundred and twenty ___.', ['degrees'], 'F', 'twenty degrees'),
  ('Dr Rashidova is a food ___.', ['historian'], 'G', 'food historian'),
 ]),
 short(3, [
  ('What is the outer layer of a grain called?', ['bran'], 'C', 'called bran'),
  ('How long does a loaf take to bake?', ['forty minutes'], 'F', 'thirty to forty minutes'),
  ('What is a tandoor made of?', ['clay'], 'G', 'a round clay oven'),
 ]),
])
