from lib import *
from svgs import *
A = """Land is a limited resource, and how a country uses it shapes its economy, its landscape and its wildlife. The imaginary country of Altonia has four main regions, and a recent land survey measured the share of each region covered by forest, farmland and settlements. The results, drawn as pie charts, show strikingly different patterns, which reflect the geography of each region and the way its people have chosen to live. This passage describes the four regions and explains the problems that each one faces, before looking at the national policy that the government has proposed in order to protect its most valuable land."""
B = """In the Northern Valley, seven tenths of the land is covered by forest, and the rest is divided between farms and a few small towns, with farms covering about twice as much as the towns. The valley is steep and cold, and the soil is thin, so farming has never been easy. The forests supply timber, and the clean water that flows from them is used by the cities in the south. The main problem is the pressure to cut more trees, since timber is profitable, and conservation groups have asked the government to protect the oldest woods from cutting."""
C = """The Eastern Plain is the opposite. Four fifths of the land is farmland, producing most of the country's wheat and sugar beet, and forest and settlements each cover only a tenth. The soil is deep and rich, and the land is flat, which makes machines easy to use. But farming on such a large scale has costs: the hedges and ponds where wild animals once lived have been removed, and chemicals used on the fields have polluted several streams. Farmers say that they must grow as much as possible to compete with imports, though some have started to plant strips of wild flowers along the edges of their fields."""
D = """The coastal region is more balanced: its land is divided into three almost equal parts, one third forest, one third farmland and one third towns and settlements. Many people live here, because the climate is mild and the ports bring trade, and the towns have grown rapidly. Each year they spread a little further over the farms, and the farmers complain that their best fields are being lost to houses and car parks. Planners have to decide how much further the towns may expand, knowing that every new house brings jobs and homes but also takes away land that cannot easily be replaced."""
E = """The Highland Plateau has a simple pattern: half of its land is forest and the other half is grassland, used for grazing sheep and goats, and there are hardly any buildings at all. Only a few thousand people live there, in scattered villages, and the roads are poor. Herders move their animals between summer and winter pastures, as their families have done for centuries. The plateau is the quietest region of the country, and its wildlife, which includes wolves and eagles, is the richest. The problem here is the opposite of the one on the coast: young people are leaving for the towns, and some villages have been abandoned."""
F = """Dr Rafael Mendes, a geographer, argues that every region needs a plan to protect the land that matters most. He proposes that forests of high value should be protected by law, that the best farmland should be kept for farming, and that towns should be encouraged to grow upwards instead of outwards, building taller apartments rather than spreading houses over fields. Taller buildings house more people on less land, he says, and they make public transport easier to run, because passengers live closer to the stations. Critics reply that many people prefer houses with gardens and will not accept the change."""
G = """The government has accepted part of his proposal. A new law will forbid building on the best farmland, and a fund will pay farmers who protect hedges and ponds. It has not yet agreed to protect all the old forests, because the timber industry has argued that this would cost thousands of jobs. Discussion continues, and a final decision is expected within two years. In the meantime, the survey will be repeated every five years, so that anyone can see whether the pie charts are changing and whether the promises made are being kept."""
P = passage('p71', 'How a Country Uses Its Land', 'Geography', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which pie chart, A to D, shows the land use in each region?', [(pie([70, 20, 10]), 160, 120), (pie([10, 80, 10]), 160, 120), (pie([34, 33, 33]), 160, 120), (pie([50, 50]), 160, 120)], [
  ('the Northern Valley', 0, 'B', 'seven tenths of the land is covered by forest'),
  ('the Eastern Plain', 1, 'C', 'Four fifths of the land is farmland'),
  ('the coastal region', 2, 'D', 'three almost equal parts'),
  ('the Highland Plateau', 3, 'E', 'half of its land is forest'),
 ]),
 tfng([
  ('Altonia is an imaginary country.', 'T', 'A', 'imaginary country of Altonia'),
  ('The survey measured forest, farmland and settlements.', 'T', 'A', 'forest, farmland and settlements'),
  ('The Northern Valley is steep and cold.', 'T', 'B', 'steep and cold'),
  ('Farming has always been easy in the valley.', 'F', 'B', 'farming has never been easy'),
  ('The Eastern Plain produces most of the country\'s wheat and sugar beet.', 'T', 'C', 'most of the country\'s wheat and sugar beet'),
  ('Chemicals have polluted several streams on the plain.', 'T', 'C', 'polluted several streams'),
  ('The coastal towns are shrinking.', 'F', 'D', 'spread a little further over the farms'),
  ('Wolves live on the Highland Plateau.', 'T', 'E', 'wolves and eagles'),
  ('Dr Mendes teaches at the university in the capital.', 'NG', 'F', 'Dr Rafael Mendes, a geographer', 'His workplace is not mentioned.'),
 ]),
 mcq([
  ('Why have conservation groups made a request in the valley?', ['To protect the oldest woods.', 'To plant crops.', 'To build towns.', 'To drain lakes.'], 0, 'B', 'protect the oldest woods from cutting'),
  ('What has harmed wildlife habitats on the plain?', ['Floods.', 'Removal of hedges and ponds.', 'Snow.', 'New towns.'], 1, 'C', 'the hedges and ponds where wild animals once lived have been removed'),
  ('Why does Dr Mendes favour taller buildings?', ['They house more people on less land.', 'They are cheaper.', 'They are older.', 'They are warmer.'], 0, 'F', 'house more people on less land'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Region', 'Detail'],
  [['Northern Valley', 'Cities in the south use the clean [[1]]'], ['Eastern Plain', 'Some farmers plant strips of wild [[2]]'], ['Coast', 'Farmers lose fields to houses and car [[3]]'], ['Plateau', 'Herders keep sheep and [[4]]']],
  [(['water'], 'B', 'clean water'), (['flowers'], 'C', 'wild flowers'), (['parks'], 'D', 'car parks'), (['goats'], 'E', 'sheep and goats')], 1),
 feat('Match each statement with the correct region, A to D.', ['Northern Valley', 'Eastern Plain', 'Coastal region', 'Highland Plateau'], [
  ('Timber is profitable there.', 0, 'B', 'timber is profitable'),
  ('Machines are easy to use there.', 1, 'C', 'which makes machines easy to use'),
  ('Ports bring trade.', 2, 'D', 'the ports bring trade'),
  ('Young people are leaving for the towns.', 3, 'E', 'young people are leaving for the towns'),
 ]),
 multi('Which TWO measures in the new law are mentioned in paragraph G?', ['Building on the best farmland will be forbidden.', 'A fund will pay farmers who protect hedges and ponds.', 'All old forests will be protected.', 'Taxes on timber will rise.', 'Towns will be moved.'], [0, 1], [('G', 'forbid building on the best farmland'), ('G', 'a fund will pay farmers who protect hedges and ponds')]),
 head(['Surveying the land', 'A country of trees', 'A country of fields', 'Towns on the march', 'Space and silence', 'An argument for building upwards', 'A partial agreement', 'The history of wheat', 'The wolves of Europe'],
  [('A', 0, 'a recent land survey'), ('B', 1, 'seven tenths of the land is covered by forest'), ('C', 2, 'Four fifths of the land is farmland'), ('D', 3, 'they spread a little further over the farms'), ('E', 4, 'the quietest region of the country'), ('F', 5, 'towns should be encouraged to grow upwards'), ('G', 6, 'The government has accepted part of his proposal')]),
 info([
  ('a request to protect old woods', 'B', 'protect the oldest woods'),
  ('a reference to competition from imports', 'C', 'compete with imports'),
  ('a complaint about the loss of the best fields', 'D', 'their best fields are being lost'),
  ('a reference to seasonal movement of animals', 'E', 'between summer and winter pastures'),
  ('a reference to the timber industry\'s argument', 'G', 'thousands of jobs'),
 ]),
 ends(['supply timber and clean water.', 'must compete with imports.', 'are spreading over farms.', 'say that people prefer houses with gardens.', 'ban all farming.', 'have no forests.', 'are built on the plateau.'], [
  ('The valley forests', 0, 'B', 'The forests supply timber'),
  ('Farmers on the plain', 1, 'C', 'compete with imports'),
  ('The coastal towns', 2, 'D', 'spread a little further over the farms'),
  ('Critics of Dr Mendes', 3, 'F', 'prefer houses with gardens'),
 ]),
 sent(2, [
  ('The Eastern Plain produces wheat and sugar ___.', ['beet'], 'C', 'sugar beet'),
  ('The coastal climate is ___.', ['mild'], 'D', 'climate is mild'),
  ('Dr Mendes is a ___.', ['geographer'], 'F', 'a geographer'),
  ('The survey will be repeated every ___ years.', ['five', '5'], 'G', 'every five years'),
 ]),
 short(3, [
  ('What do herders move between pastures?', ['their animals', 'animals'], 'E', 'their animals'),
  ('How many people live on the plateau?', ['a few thousand'], 'E', 'Only a few thousand people'),
  ('When is a final decision expected?', ['within two years'], 'G', 'within two years'),
 ]),
])
