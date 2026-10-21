from lib import *
A = """Until the 1960s, the Aral Sea in Central Asia was the fourth largest lake in the world, with an area of about sixty-eight thousand square kilometres, roughly the size of Ireland. It lay between what are now Kazakhstan and Uzbekistan and was fed by two great rivers, the Amu Darya and the Syr Darya, which carry melted snow from the mountains far to the south and east. Fishing boats worked its waters, and the port towns on its shores were prosperous."""
B = """The change began when Soviet planners decided to turn the dry land around the sea into cotton fields. They dug thousands of kilometres of canals to carry water from the two rivers to the crops. Many of the canals were unlined, so a large share of the water soaked into the ground or evaporated before it reached the fields. Cotton also needs a great deal of water. By the 1980s, in most years, almost nothing was left of the rivers by the time they reached the sea."""
C = """The sea responded by shrinking. By 1987 it had divided into two separate parts, a small northern lake and a larger southern one, and by 2007 it had lost about ninety per cent of its original area. As the water fell, the remaining water became saltier, and the native fish could not survive. The fishing industry, which had once employed tens of thousands of people, collapsed. The old port of Moynaq is now many kilometres from the water, and the rusting hulks of ships lie half buried in the sand."""
D = """The consequences reached far beyond the fishing villages. The exposed seabed is covered with salt, as well as with chemical residues from the fertilisers and pesticides that drained from the cotton fields over the years. Strong winds lift this material into the air and carry it for hundreds of kilometres. Doctors in the region report high rates of throat and lung disease. The climate has also changed: without the sea to moderate the temperature, the summers are hotter and the winters colder than they once were."""
E = """In the north, a more hopeful story has unfolded. In 2005 Kazakhstan completed the Kok-Aral dam, a barrier across the channel that separates the northern lake from the southern one. Water from the Syr Darya, which once drained away south, now stays in the north. Within a few years the level had risen, the salt content had fallen, and the fish had returned. The catch has grown steadily, and the shoreline has moved back towards the town of Aralsk."""
F = """The southern part of the sea has not been so fortunate. Most scientists agree that it cannot be restored, because the water that would be needed is now used for farming, and there is no political will to give it up. Efforts have therefore concentrated on limiting the damage. In Uzbekistan, workers have planted saxaul, a hardy desert shrub, over large areas of the dry seabed, now called the Aralkum desert, in order to hold the soil in place and reduce the dust. Some communities have also turned to new work, such as raising livestock or taking part in the search for oil and gas."""
G = """The Aral Sea has become a warning to the world. It shows how quickly a large body of water can disappear when too much is taken from the rivers that feed it, and how hard it is to reverse the damage afterwards. Farmers in the region are now being encouraged to line canals, to use drip irrigation, which delivers water directly to the roots of plants, and to grow crops that need less water than cotton. Such measures are expensive, but supporters argue that they cost far less than the damage that the disappearance of the sea has caused."""
P = passage('p12', 'The Vanishing Aral Sea', 'Geography', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Aral Sea was once the fourth largest lake in the world.', 'T', 'A', 'the fourth largest lake in the world'),
  ('The Aral Sea was fed by three major rivers.', 'F', 'A', 'two great rivers, the Amu Darya and the Syr Darya'),
  ('Soviet planners wanted to grow cotton on dry land near the sea.', 'T', 'B', 'turn the dry land around the sea into cotton fields'),
  ('Most of the canals were lined to prevent water loss.', 'F', 'B', 'Many of the canals were unlined'),
  ('By 1987 the sea had split into two parts.', 'T', 'C', 'By 1987 it had divided into two separate parts'),
  ('Native fish were killed by chemicals dumped by factories.', 'F', 'C', 'the remaining water became saltier, and the native fish could not survive'),
  ('The port of Moynaq is now far from the water.', 'T', 'C', 'now many kilometres from the water'),
  ('Dust from the seabed has been blown as far as the Arctic.', 'NG', 'D', 'carry it for hundreds of kilometres', 'The passage says dust travels hundreds of kilometres but names no destination.'),
  ('Summers in the region are now cooler than they were.', 'F', 'D', 'the summers are hotter and the winters colder'),
  ('The Kok-Aral dam was completed in 2005.', 'T', 'E', 'In 2005 Kazakhstan completed the Kok-Aral dam'),
  ('Experts believe the southern sea can be restored within ten years.', 'F', 'F', 'it cannot be restored'),
 ]),
 tfng([
  ('Closing the Kok-Aral dam has benefited the northern lake.', 'Y', 'E', 'the level had risen, the salt content had fallen, and the fish had returned'),
  ('The southern sea could easily be refilled if politicians wished.', 'N', 'F', 'there is no political will to give it up'),
  ('Cotton is a crop that uses little water.', 'N', 'B', 'Cotton also needs a great deal of water'),
  ('Measures to save water in farming are cheaper than the damage done by the loss of the sea.', 'NG', 'G', 'supporters argue that they cost far less than the damage', 'The writer reports what supporters argue and does not give a personal view.'),
  ('The disappearance of the sea is a lesson for other parts of the world.', 'Y', 'G', 'The Aral Sea has become a warning to the world'),
  ('Planting saxaul has completely solved the dust problem.', 'N', 'F', 'in order to hold the soil in place and reduce the dust'),
 ], yn=True),
 mcq([
  ('Why was so much canal water lost before it reached the cotton fields?', ['The canals were too narrow.', 'Many canals had no lining.', 'The rivers were frozen in winter.', 'Farmers took too much from each canal.'], 1, 'B', 'Many of the canals were unlined'),
  ('What happened to the fishing industry as the sea shrank?', ['It moved to the north.', 'It was replaced by fish farming.', 'It collapsed.', 'It became more profitable.'], 2, 'C', 'The fishing industry, which had once employed tens of thousands of people, collapsed'),
  ('Why does the writer describe the north as a more hopeful story?', ['The northern lake has recovered in several ways.', 'The Syr Darya has been refilled completely.', 'The town of Aralsk has been rebuilt.', 'The dam has been copied in the south.'], 0, 'E', 'the level had risen, the salt content had fallen, and the fish had returned'),
 ]),
 multi('Which TWO health or climate effects are mentioned in paragraph D?', ['Throat and lung disease is common.', 'Summers have become hotter.', 'Rainfall has doubled.', 'Skin disease has spread.', 'Winters have become warmer.'], [0, 1], [('D', 'high rates of throat and lung disease'), ('D', 'the summers are hotter')]),
 head(['A great lake and its rivers', 'How the water was taken away', 'A sea cut in two', 'Dust, disease and a harsher climate', 'A partial recovery in the north', 'Limiting the damage in the south', 'A warning and some remedies', 'The history of cotton farming', 'New fish species for the lake'],
  [('A', 0, 'Until the 1960s, the Aral Sea'), ('B', 1, 'The change began when Soviet planners decided'), ('C', 2, 'The sea responded by shrinking'), ('D', 3, 'The consequences reached far beyond the fishing villages'), ('E', 4, 'In the north, a more hopeful story has unfolded'), ('F', 5, 'Efforts have therefore concentrated on limiting the damage'), ('G', 6, 'The Aral Sea has become a warning to the world')]),
 info([
  ('a comparison between the size of the lake and a country', 'A', 'roughly the size of Ireland'),
  ('a reason why so little river water was left by the 1980s', 'B', 'almost nothing was left of the rivers'),
  ('a description of ships left behind by the water', 'C', 'rusting hulks of ships'),
  ('a mention of chemicals from farming in the dust', 'D', 'chemical residues from the fertilisers and pesticides'),
  ('a reference to a plant used to hold the soil in place', 'F', 'saxaul, a hardy desert shrub'),
  ('a method of watering that reaches the roots directly', 'G', 'drip irrigation, which delivers water directly to the roots'),
 ]),
 sent(3, [
  ('The Aral Sea is fed by the Amu Darya and the ___ Darya.', ['syr'], 'A', 'the Amu Darya and the Syr Darya'),
  ('By 2007 the sea had lost about ___ per cent of its original area.', ['ninety', '90'], 'C', 'about ninety per cent of its original area'),
  ('The old port of ___ is now many kilometres from the water.', ['moynaq'], 'C', 'The old port of Moynaq'),
  ('Winds carry dust from the exposed seabed for hundreds of ___.', ['kilometres', 'kilometers'], 'D', 'for hundreds of kilometres'),
  ('The ___ dam has helped the northern lake to recover.', ['kok-aral', 'kok aral'], 'E', 'the Kok-Aral dam'),
  ('The dry seabed is now called the ___ desert.', ['aralkum'], 'F', 'now called the Aralkum desert'),
 ]),
 short(3, [
  ('What did Soviet planners want to grow around the sea?', ['cotton'], 'B', 'cotton fields'),
  ('In which year was the Kok-Aral dam completed?', ['2005'], 'E', 'In 2005 Kazakhstan completed'),
  ('Which town has seen its shoreline move closer again?', ['aralsk'], 'E', 'the town of Aralsk'),
  ('What kind of animals do some communities now raise?', ['livestock'], 'F', 'raising livestock'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Canals carry water from the two [[1]] to the cotton fields.', 'Much of the water [[2]] before it reaches the crops.', 'Almost nothing is left of the rivers by the time they reach the sea.', 'The sea shrinks and the remaining water becomes [[3]].', 'The native [[4]] cannot survive and the fishing industry collapses.'],
  [(['rivers'], 'B', 'from the two rivers'), (['evaporated'], 'B', 'soaked into the ground or evaporated'), (['saltier'], 'C', 'became saltier'), (['fish'], 'C', 'the native fish could not survive')], 2),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'In the north, the Kok-Aral [[1]] keeps water from the Syr Darya in the northern lake. The water level has [[2]], the salt content has fallen and the [[3]] have returned. In the south, workers have planted [[4]] to hold the soil in place and reduce dust.',
  [(['dam'], 'E', 'the Kok-Aral dam'), (['risen'], 'E', 'the level had risen'), (['fish'], 'E', 'the fish had returned'), (['saxaul'], 'F', 'planted saxaul')], 1,
  bank=['dam', 'risen', 'fish', 'saxaul', 'fallen', 'birds', 'cotton', 'canal']),
])
