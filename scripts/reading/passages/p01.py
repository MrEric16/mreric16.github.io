from lib import *
A = """In the early 2000s, a beekeeper in a large northern city placed two hives on the roof of an office block and waited to see what would happen. By the end of the summer, each hive had produced more honey than the average hive on a farm thirty kilometres away. The result surprised him, and it was soon repeated by others. Today hives can be found on the roofs of hotels, hospitals and department stores, and in some countries the number of urban beekeepers has doubled in a decade."""
B = """The explanation lies in what a city offers a bee. Modern farmland is often a desert for pollinators: huge fields of a single crop flower for only a few weeks, and the margins between fields have been cleared to make room for machinery. A city, by contrast, is a patchwork of parks, gardens, window boxes, cemeteries and railway embankments, and something is in flower for most of the year. Lime trees, which line many European streets, are especially valuable, since a single tree can supply nectar for several hives during its short flowering season."""
C = """Pesticides are the second advantage. Farmers who spray their crops may unintentionally poison the bees that feed on them, whereas most city authorities have restricted or banned the use of the strongest chemicals in public parks. Warmth also helps. Because buildings and roads store heat, a city can be several degrees warmer than the surrounding countryside, which allows colonies to begin foraging earlier in spring and to continue later into autumn."""
D = """The honey itself has attracted attention. Because bees from a single hive visit many different plants, urban honey tends to have a complex flavour that changes from street to street and from month to month. In one project, a group of chefs and a university laboratory compared samples from fourteen districts of a single city and found that no two jars tasted the same. Some producers now label their honey with the name of the neighbourhood, in the same way that winemakers label bottles with the name of a vineyard. Researchers have also tested city honey for heavy metals such as lead; the levels were generally lower than the limits set for food safety, because bees filter much of what they carry and because leaded petrol has long been banned."""
E = """Not everyone is persuaded that the boom is good news. Dr Imogen Hale, an ecologist, argues that honeybees are only one of more than two hundred bee species found in a typical European country, and that most of the others are wild, solitary insects that nest in the ground or in dead wood. Her team counted wild bees on flowering plants in thirty city parks and discovered that, in parks containing several hives, the wild bees were fewer and visited the flowers less often. "A city can only produce so much nectar," she says. "If we keep adding hives, the honeybees take a growing share and the wild species go hungry.\""""
F = """Beekeepers accept that hive numbers need limits, but they question how far her findings can be generalised. The parks in the study were small, they point out, and the survey lasted a single summer. Some of them also argue that the bigger threat to wild bees is the loss of nesting sites, not competition for food. A few councils have started to respond by encouraging the planting of flowers that produce nectar over a long season, and by leaving small areas of grass uncut so that wild bees can nest there."""
G = """A sensible middle path is beginning to emerge. Guidelines drawn up by one city council suggest that only a fixed number of hives should be kept within a given distance of each other, and that anyone wanting to keep bees must complete a short training course first. Educators have taken up the cause too: several schools now run hives as part of their science lessons, and children who have watched a colony at work often become the most enthusiastic defenders of all insects, not only the honeybee. If that attitude spreads, the city may prove to be a refuge for far more than the honeybee alone."""
P = passage('p01', 'Bees in the City', 'Ecology', 1,
 'You should spend about 20 minutes on this passage.',
 [A, B, C, D, E, F, G], [
 tfng([
  ('The first rooftop hives described in the passage gave more honey than a typical hive on a nearby farm.', 'T', 'A', 'each hive had produced more honey than the average hive on a farm thirty kilometres away'),
  ('Most farmland gives bees flowers to feed on all year round.', 'F', 'B', 'huge fields of a single crop flower for only a few weeks'),
  ('Lime trees flower for a long period each year.', 'F', 'B', 'during its short flowering season'),
  ('City authorities have banned every pesticide in public parks.', 'F', 'C', 'restricted or banned the use of the strongest chemicals in public parks'),
  ('Tests found dangerous levels of lead in city honey.', 'F', 'D', 'the levels were generally lower than the limits set for food safety'),
  ('The honey comparison project was paid for by a food company.', 'NG', 'D', 'a group of chefs and a university laboratory compared samples from fourteen districts', 'The passage names the people who ran the project but never says who paid for it.'),
  ('Dr Hale\'s team studied wild bees in thirty city parks.', 'T', 'E', 'counted wild bees on flowering plants in thirty city parks'),
  ('Dr Hale thinks beekeepers should need a licence.', 'NG', 'E', 'If we keep adding hives, the honeybees take a growing share', 'She warns about too many hives but never mentions licences.'),
  ('The park survey continued for more than one summer.', 'F', 'F', 'the survey lasted a single summer'),
  ('Some beekeepers consider a shortage of nesting sites a greater danger to wild bees than competition for food.', 'T', 'F', 'the bigger threat to wild bees is the loss of nesting sites, not competition for food'),
 ]),
 mcq([
  ('According to paragraph B, farmland is a poor habitat for bees because', ['flowers there bloom briefly and the edges of fields have been removed', 'farm machinery frightens bees away from the crops', 'most crops are grown without any flowers', 'fields are too large for bees to cross'], 0, 'B', 'flower for only a few weeks, and the margins between fields have been cleared'),
  ('City colonies can start foraging earlier in spring because', ['plants in cities are watered more often', 'buildings and roads keep the city warmer', 'there are fewer birds that eat bees', 'hives on roofs receive more sunlight'], 1, 'C', 'Because buildings and roads store heat, a city can be several degrees warmer'),
  ('What do some beekeepers say about Dr Hale\'s research?', ['It was paid for by farmers.', 'It ignored the wild bees in small parks.', 'It may not apply to every situation.', 'It proved that hives should be banned.'], 2, 'F', 'The parks in the study were small, they point out, and the survey lasted a single summer'),
 ]),
 head(['A year-round supply of flowers', 'Fewer chemicals and warmer air', 'Honey with a sense of place', 'A scientist\'s warning about wild species', 'Doubts about the evidence', 'Towards sensible rules and education', 'The decline of the honey industry', 'Bees that travel long distances to feed'],
  [('B', 0, 'A city, by contrast, is a patchwork of parks, gardens'), ('C', 1, 'Pesticides are the second advantage'), ('D', 2, 'urban honey tends to have a complex flavour'), ('E', 3, 'honeybees are only one of more than two hundred bee species'), ('F', 4, 'they question how far her findings can be generalised'), ('G', 5, 'A sensible middle path is beginning to emerge')]),
 info([
  ('a surprising result from the first rooftop hives', 'A', 'The result surprised him'),
  ('a claim that one kind of tree is especially useful for nectar', 'B', 'Lime trees, which line many European streets, are especially valuable'),
  ('a reference to how city temperatures affect bee activity', 'C', 'allows colonies to begin foraging earlier in spring'),
  ('an example of councils encouraging action to help wild bees', 'F', 'A few councils have started to respond'),
  ('a rule that people must be trained before keeping bees', 'G', 'must complete a short training course first'),
  ('a comparison between honey labels and wine labels', 'D', 'in the same way that winemakers label bottles'),
 ]),
 sent(2, [
  ('Many councils limit the use of powerful ___ in parks.', ['chemicals'], 'C', 'the use of the strongest chemicals in public parks'),
  ('Some producers name their honey after the ___ where the bees feed.', ['neighbourhood', 'neighborhood'], 'D', 'label their honey with the name of the neighbourhood'),
  ('Dr Hale\'s researchers surveyed wild bees in thirty ___.', ['city parks', 'parks'], 'E', 'thirty city parks'),
  ('Dr Hale describes most wild bees as ___ insects.', ['solitary'], 'E', 'wild, solitary insects'),
  ('Some councils leave small areas of ___ uncut so that wild bees can nest.', ['grass'], 'F', 'leaving small areas of grass uncut'),
  ('Several schools use hives in their ___ lessons.', ['science'], 'G', 'as part of their science lessons'),
 ]),
 short(4, [
  ('Which type of tree is said to be especially valuable on European streets?', ['lime trees', 'lime tree', 'lime'], 'B', 'Lime trees, which line many European streets'),
  ('What did chefs and a university laboratory compare in one project?', ['samples', 'honey samples'], 'D', 'compared samples from fourteen districts'),
  ('How many bee species does Dr Hale say live in a typical European country?', ['more than two hundred', 'more than 200', 'over 200', '200', 'two hundred'], 'E', 'more than two hundred bee species'),
  ('What must a person complete before keeping bees under one council\'s guidelines?', ['a short training course', 'training course', 'short training course'], 'G', 'complete a short training course first'),
 ]),
 summ('Complete the summary. Write ONE WORD ONLY from the passage for each answer.',
  'Dr Hale found that wild bees were [[1]] in parks with several hives, and that they visited flowers less [[2]]. She believes a city can produce only a limited amount of [[3]], so extra hives leave wild species short of food. Beekeepers reply that the parks in her study were [[4]] and that the survey covered only one [[5]]. They add that wild bees may suffer more from the loss of [[6]] sites.',
  [(['fewer'], 'E', 'the wild bees were fewer and visited the flowers less often'), (['often'], 'E', 'the wild bees were fewer and visited the flowers less often'), (['nectar'], 'E', 'A city can only produce so much nectar'), (['small'], 'F', 'The parks in the study were small'), (['summer'], 'F', 'the survey lasted a single summer'), (['nesting'], 'F', 'the loss of nesting sites')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Advantage', 'Detail'],
  [['Year-round flowers', 'Parks, gardens and [[1]] supply food for most of the year'], ['Fewer chemicals', 'The strongest [[2]] are restricted in public parks'], ['Warmth', 'Buildings and roads store [[3]]'], ['Honey quality', 'Lead levels are below the [[4]] limits']],
  [(['window boxes'], 'B', 'parks, gardens, window boxes, cemeteries'), (['chemicals'], 'C', 'the strongest chemicals'), (['heat'], 'C', 'buildings and roads store heat'), (['food safety'], 'D', 'limits set for food safety')], 2),
])
