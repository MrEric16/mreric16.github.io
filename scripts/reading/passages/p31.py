from lib import *
from svgs import *
A = """A tree trunk looks like a solid column of wood, but a cross-section reveals several distinct layers, each with its own job. Together they support the tree, carry water and food to every part, and defend it against insects and disease. The layers also keep a record: because the trunk grows a little wider each year, a cut through it shows rings that tell scientists the age of the tree and something about the weather in each year of its life. Some living trees, including bristlecone pines in the United States, are more than four thousand years old."""
B = """On the outside is the bark, a thick, rough layer of dead cells that protects the tree like a coat. It guards against fire, cold, insects and fungi, and it limits the loss of water from the trunk. The bark of the cork oak is so thick that it can be removed every nine years without harming the tree; it is then used to make bottle stoppers, floors and notice boards. Bark varies greatly from species to species: that of the birch is thin and papery, while that of the giant redwood can be thirty centimetres thick."""
C = """Just inside the bark is the phloem, sometimes called the inner bark. It is a thin layer of living tubes that carry sugar, made by the leaves in sunlight, down to the roots and to other parts of the tree that cannot make their own food. If a ring of phloem is cut right round the trunk, the roots are starved, and the tree usually dies within a year or two. This is why deer and other animals that eat bark in winter can destroy young trees, and why foresters protect them with plastic tubes."""
D = """Next comes the cambium, a layer only a few cells thick, but the most important in the trunk. Its cells divide constantly, producing phloem on the outside and new wood on the inside. This is the source of the tree's growth in width. In spring, when water is plentiful, the cambium makes large, pale cells, and in summer it makes smaller, darker ones; the contrast between the two creates the annual ring that can be counted. A wet year produces a wide ring, and a dry year a narrow one."""
E = """The sapwood lies inside the cambium. Its tubes, called xylem, carry water and minerals from the roots to the leaves, sometimes to a height of more than a hundred metres. The water is pulled upwards, not pushed, as it evaporates from the leaves; the process works rather like drinking through a straw. Sapwood is also the part of the trunk that stores food in winter. It is usually pale and soft, and for this reason it is less valued by furniture makers than the layer beneath it."""
F = """At the centre is the heartwood. As the tree grows, the oldest sapwood stops carrying water and turns into heartwood, which is filled with natural chemicals that resist rot and insects. It is darker and harder than sapwood and gives the tree its strength, though it is no longer alive. Remarkably, a tree can survive when its heartwood has completely decayed, which is why many old trees are hollow, and some are large enough for a person to stand inside."""
G = """The rings of trees have given rise to a science called dendrochronology. By matching the pattern of wide and narrow rings in living trees with those in old beams and logs, researchers can date buildings and ships to the exact year in which the wood was cut. Dr Ravi Menon, a dendrochronologist, has used the technique to date the roof of a medieval mosque, and he believes that it can also reveal past droughts and volcanic eruptions, since these leave a clear mark in the rings of trees that lived through them."""
S, PT, W, H = layers(5)
P = passage('p31', 'Inside a Tree Trunk', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The rings of a tree show its age.', 'T', 'A', 'tell scientists the age of the tree'),
  ('Some living trees are more than four thousand years old.', 'T', 'A', 'more than four thousand years old'),
  ('Bark is made of living cells.', 'F', 'B', 'a thick, rough layer of dead cells'),
  ('Cork oak bark can be removed without harming the tree.', 'T', 'B', 'without harming the tree'),
  ('Phloem carries sugar to the roots.', 'T', 'C', 'carry sugar, made by the leaves in sunlight, down to the roots'),
  ('A tree always survives if a ring of phloem is cut.', 'F', 'C', 'the tree usually dies within a year or two'),
  ('The cambium produces large cells in summer.', 'F', 'D', 'in summer it makes smaller, darker ones'),
  ('Water is pushed up through the xylem.', 'F', 'E', 'pulled upwards, not pushed'),
  ('Heartwood is more valued by furniture makers than sapwood.', 'NG', 'E', 'less valued by furniture makers than the layer beneath it', 'The passage says sapwood is less valued; it does not state what makers think of heartwood in so many words.'),
 ]),
 mcq([
  ('Why does the cambium matter so much?', ['It protects the tree from fire.', 'It makes the tree grow wider.', 'It carries water.', 'It stores minerals.'], 1, 'D', 'the source of the tree\'s growth in width'),
  ('What does a narrow ring show?', ['A wet year.', 'A dry year.', 'A cold winter.', 'A fire.'], 1, 'D', 'a dry year a narrow one'),
  ('Why can a tree survive with hollow heartwood?', ['The heartwood is still alive.', 'The living layers are further out.', 'The bark replaces it.', 'The roots feed it.'], 1, 'F', 'a tree can survive when its heartwood has completely decayed'),
 ]),
 multi('Which TWO things does bark protect the tree against, according to paragraph B?', ['Fire.', 'Insects.', 'Floods.', 'Earthquakes.', 'Wind.'], [0, 1], [('B', 'fire, cold, insects and fungi'), ('B', 'fire, cold, insects and fungi')]),
 head(['Layers and records', 'The tree\'s protective coat', 'The food pipeline', 'The layer that makes new wood', 'Moving water upwards', 'A strong, lifeless centre', 'Dating the past with rings', 'The invention of the saw', 'Why forests are important'],
  [('A', 0, 'a cross-section reveals several distinct layers'), ('B', 1, 'the bark, a thick, rough layer of dead cells'), ('C', 2, 'Just inside the bark is the phloem'), ('D', 3, 'Next comes the cambium'), ('E', 4, 'The sapwood lies inside the cambium'), ('F', 5, 'At the centre is the heartwood'), ('G', 6, 'have given rise to a science')]),
 info([
  ('a reference to the oldest living trees', 'A', 'bristlecone pines'),
  ('an example of a use for cork', 'B', 'bottle stoppers, floors and notice boards'),
  ('a method of protecting young trees', 'C', 'plastic tubes'),
  ('a comparison with drinking', 'E', 'drinking through a straw'),
  ('a mention of what rings can reveal about the past', 'G', 'past droughts and volcanic eruptions'),
 ]),
 ends(['is a thick layer of dead cells.', 'carries sugar down to the roots.', 'produces new phloem and wood.', 'carries water to the leaves.', 'is the youngest part of the tree.', 'is made of living cells only.', 'is found only in pine trees.'], [
  ('Bark', 0, 'B', 'a thick, rough layer of dead cells'),
  ('Phloem', 1, 'C', 'carry sugar, made by the leaves in sunlight, down to the roots'),
  ('The cambium', 2, 'D', 'producing phloem on the outside and new wood on the inside'),
  ('Xylem', 3, 'E', 'carry water and minerals from the roots to the leaves'),
 ]),
 diag('Label the diagram of the trunk, from the outside to the centre. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['bark'], 'B', 'the bark'), (['phloem'], 'C', 'the phloem'), (['cambium'], 'D', 'the cambium'), (['sapwood'], 'E', 'The sapwood'), (['heartwood'], 'F', 'the heartwood')], 1),
 sent(2, [
  ('The bark of the birch is thin and ___.', ['papery'], 'B', 'thin and papery'),
  ('Sapwood stores ___ in winter.', ['food'], 'E', 'stores food in winter'),
  ('Heartwood is filled with chemicals that resist ___.', ['rot'], 'F', 'resist rot and insects'),
  ('The science of tree rings is called ___.', ['dendrochronology'], 'G', 'called dendrochronology'),
 ]),
 short(3, [
  ('How often can cork oak bark be removed?', ['every nine years', 'nine years'], 'B', 'every nine years'),
  ('What is Dr Menon\'s profession?', ['dendrochronologist', 'a dendrochronologist'], 'G', 'a dendrochronologist'),
  ('What did Dr Menon date?', ['a roof', 'the roof'], 'G', 'date the roof of a medieval mosque'),
 ]),
])
