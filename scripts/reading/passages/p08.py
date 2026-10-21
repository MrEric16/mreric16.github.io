from lib import *
A = """Global plastic production has grown rapidly since the 1950s, and a great deal of what is made is thrown away within a few years. Only a small proportion is recycled, so most ends up in landfill sites or in the environment. Plastic is durable, which is why it is so useful, and also why it is such a problem. Left in the environment, it does not rot; it breaks into smaller and smaller pieces. Those under five millimetres in length are known as microplastics, and they have now been found almost everywhere that scientists have looked, from the summit of high mountains to the deepest part of the ocean."""
B = """Microplastics fall into two groups. Primary microplastics are made small on purpose. They include the tiny beads once added to face scrubs and toothpaste, and the pellets, each about the size of a lentil, that factories melt to make plastic goods. Secondary microplastics are created when larger items, such as bottles, bags and fishing nets, are broken up by sunlight, waves and friction. Most of the microplastic in the sea is believed to be secondary."""
C = """Some of the largest sources are surprising. Clothes made from synthetic fabrics such as polyester shed tiny fibres every time they are washed, and a single load of washing may release hundreds of thousands of them. Car tyres are another important source, since the rubber contains plastic polymers and wears away a little on every journey. Together, these two sources are thought to account for a greater share of microplastic pollution than the beads in cosmetics ever did."""
D = """The route that fibres take is easy to follow. They leave the washing machine in the waste water and flow through the drains to a treatment plant. The plant removes the majority of them, which settle out as a thick substance called sludge. Unfortunately, the sludge is often spread on farmland as fertiliser, and rain can then wash the fibres into streams and rivers. From there they travel to the sea, where they are eaten by plankton, the tiny creatures at the base of the marine food chain."""
E = """Whether microplastics harm living things is still being studied. Dr Hannah Cole's team fed plankton with polystyrene beads and found that the animals ate less of their normal food and produced fewer eggs. Because small fish eat plankton, and larger animals eat the fish, plastic may be passed up the food chain in this way. Particles have also been detected in drinking water, in the air, and in samples of human blood. However, no study has yet shown that the particles inside our bodies cause disease, and scientists disagree about how worried we should be."""
F = """Professor Rafael Duarte believes that public alarm has run ahead of the evidence. Most laboratory experiments, he points out, expose animals to concentrations of plastic far higher than any found in nature, so their results may exaggerate the danger. He does not deny that plastic pollution is a problem, but he thinks that the attention given to microplastics distracts from larger plastic objects, which kill many more seabirds and turtles. Other scientists reply that waiting for certainty would be reckless, since the particles will remain in the environment for centuries."""
G = """Governments and industry have begun to act. Britain banned microbeads in rinse-off cosmetics in 2018, and France has passed a law requiring filters on new washing machines. Individuals can help by washing synthetic clothes less often, at lower temperatures and with a full load, all of which reduce the number of fibres released. Most researchers agree, however, that these measures only treat the symptoms, and that the real solution is to make and throw away less plastic in the first place."""
P = passage('p08', 'The Plastic We Cannot See', 'Environment', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Plastic left in the environment breaks into smaller and smaller pieces.', 'T', 'A', 'it breaks into smaller and smaller pieces'),
  ('Microplastics have been found only in the oceans.', 'F', 'A', 'from the summit of high mountains to the deepest part of the ocean'),
  ('Primary microplastics are manufactured to be small.', 'T', 'B', 'Primary microplastics are made small on purpose'),
  ('Most plastic pellets are made in Asia.', 'NG', 'B', 'the pellets, each about the size of a lentil', 'The passage says nothing about where pellets are made.'),
  ('Most of the microplastic in the sea is thought to come from larger items that have broken up.', 'T', 'B', 'Most of the microplastic in the sea is believed to be secondary'),
  ('Beads in cosmetics are the largest source of microplastic pollution.', 'F', 'C', 'a greater share of microplastic pollution than the beads in cosmetics ever did'),
  ('Treatment plants fail to remove most of the fibres.', 'F', 'D', 'The plant removes the majority of them'),
  ('Sludge from treatment plants is often used as fertiliser.', 'T', 'D', 'the sludge is often spread on farmland as fertiliser'),
  ('Dr Cole\'s plankton produced fewer eggs after eating plastic.', 'T', 'E', 'produced fewer eggs'),
  ('It has been proved that microplastics inside the human body cause disease.', 'F', 'E', 'no study has yet shown that the particles inside our bodies cause disease'),
  ('Professor Duarte has carried out experiments on seabirds.', 'NG', 'F', 'which kill many more seabirds and turtles', 'Seabirds are mentioned only as victims of larger plastic objects.'),
 ]),
 mcq([
  ('Why are car tyres a source of microplastics?', ['They are made of a type of plastic that melts.', 'They contain polymers and wear away as they are used.', 'They are broken up by sunlight.', 'They are washed into the drains.'], 1, 'C', 'the rubber contains plastic polymers and wears away a little on every journey'),
  ('What is Professor Duarte\'s main criticism of laboratory experiments?', ['They use too few animals.', 'They ignore larger plastic objects.', 'They use unrealistically high concentrations.', 'They last for too short a time.'], 2, 'F', 'concentrations of plastic far higher than any found in nature'),
  ('What do most researchers think about the measures in paragraph G?', ['They are enough to solve the problem.', 'They deal with effects and not causes.', 'They are too expensive for governments.', 'They will not be adopted by industry.'], 1, 'G', 'these measures only treat the symptoms'),
 ]),
 multi('Which TWO actions to reduce the number of fibres from clothes are suggested in paragraph G?', ['washing synthetic clothes less often', 'washing clothes at lower temperatures', 'using more detergent', 'drying clothes outdoors', 'washing clothes by hand'], [0, 1], [('G', 'washing synthetic clothes less often'), ('G', 'at lower temperatures')]),
 head(['Two kinds of tiny plastic', 'Unexpected sources', 'From the washing machine to the sea', 'Effects on animals and people', 'A sceptic\'s view', 'Steps that are being taken', 'The history of plastic production', 'How to recycle plastic bottles'],
  [('B', 0, 'Microplastics fall into two groups'), ('C', 1, 'Some of the largest sources are surprising'), ('D', 2, 'The route that fibres take is easy to follow'), ('E', 3, 'Whether microplastics harm living things is still being studied'), ('F', 4, 'public alarm has run ahead of the evidence'), ('G', 5, 'Governments and industry have begun to act')]),
 info([
  ('a statement of the size of the particles called microplastics', 'A', 'Those under five millimetres in length'),
  ('a comparison between two sources of pollution', 'C', 'a greater share of microplastic pollution than the beads in cosmetics ever did'),
  ('a description of a substance produced at a treatment plant', 'D', 'a thick substance called sludge'),
  ('an effect on the reproduction of small animals', 'E', 'produced fewer eggs'),
  ('a reason why waiting for certainty could be dangerous', 'F', 'the particles will remain in the environment for centuries'),
  ('a law that applies to household machines', 'G', 'a law requiring filters on new washing machines'),
 ]),
 sent(2, [
  ('Microplastics are pieces of plastic shorter than ___ millimetres.', ['five', '5'], 'A', 'under five millimetres'),
  ('Factory pellets are about the size of a ___.', ['lentil'], 'B', 'about the size of a lentil'),
  ('Polyester is an example of a ___ fabric.', ['synthetic'], 'C', 'synthetic fabrics such as polyester'),
  ('The thick substance that settles out at a treatment plant is called ___.', ['sludge'], 'D', 'a thick substance called sludge'),
  ('Plankton are at the base of the marine ___ chain.', ['food'], 'D', 'the marine food chain'),
  ('Britain banned microbeads in ___ cosmetics in 2018.', ['rinse-off', 'rinse off'], 'G', 'microbeads in rinse-off cosmetics'),
 ]),
 short(3, [
  ('What wears away a little on every journey?', ['car tyres', 'tyres', 'tyre', 'car tyre'], 'C', 'Car tyres are another important source'),
  ('What did Dr Cole feed to plankton?', ['polystyrene beads', 'polystyrene'], 'E', 'fed plankton with polystyrene beads'),
  ('Which animals does Duarte say are killed in greater numbers by larger plastic objects?', ['seabirds and turtles'], 'F', 'seabirds and turtles'),
  ('For how long will the particles remain in the environment?', ['centuries', 'for centuries'], 'F', 'for centuries'),
 ]),
 summ('Complete the summary. Write ONE WORD ONLY from the passage for each answer.',
  'Dr Cole fed plankton with polystyrene beads and found that they ate less and produced fewer [[1]]. Microplastics have also been detected in drinking water, in the air and in human [[2]]. However, no study has yet shown that the particles in our bodies cause [[3]].',
  [(['eggs'], 'E', 'produced fewer eggs'), (['blood'], 'E', 'samples of human blood'), (['disease'], 'E', 'cause disease')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Fibres leave the washing machine in the [[1]].', 'They flow through the [[2]] to a treatment plant.', 'Most of the fibres settle out as [[3]].', 'The sludge is spread on [[4]] as fertiliser.', 'Rain washes the fibres into rivers and then into the [[5]].'],
  [(['waste water'], 'D', 'in the waste water'), (['drains'], 'D', 'through the drains'), (['sludge'], 'D', 'called sludge'), (['farmland'], 'D', 'spread on farmland'), (['sea'], 'D', 'travel to the sea')], 2),
])
