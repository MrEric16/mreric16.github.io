from lib import *
from svgs import *
A = """Zendia is an imaginary island nation of about four million people, and its government has published figures for the last twenty years showing how its main industries have changed. The figures are useful because they show four very different patterns, and each tells a story about the economy. This passage looks at tourism, fishing, farming and mining, and then at what economists say about the lessons for the future. Like many islands, Zendia has few natural resources, and the country depends on trade, so changes in any one industry are felt by almost every family in the country and by every town on the coast."""
B = """Tourism is the story of success. Twenty years ago, the island received fewer than two hundred thousand visitors a year, most of whom stayed only a few days. Since then the number has risen steadily, with only a short pause during a worldwide economic crisis, and it now exceeds two million. The government built a new airport, advertised the island's beaches and rain forests abroad, and encouraged families to open small guest houses. As a result, tourism has become the largest employer in the country, providing jobs for about one worker in four, though some residents complain that crowds spoil the beaches during the summer season."""
C = """Fishing has followed the opposite course. Zendia's waters were once rich in tuna and sardines, and in the early years of the survey the fleet landed a record catch. The numbers have fallen every year since, because too many boats took too many fish and the populations could not recover. Many fishing families have moved to the towns, and the number of working boats has halved. The government has now introduced strict limits on the catch and closed some areas completely for part of the year, but scientists say that it will take decades for the stocks to return to their former level, even if the rules are strictly obeyed by everyone."""
D = """Farming shows a rise followed by a fall. In the early years, new irrigation schemes and cheaper fertiliser allowed farmers to produce more rice and sugar, and output reached its highest point about twelve years ago. After that, harvests declined, partly because the soil became exhausted and partly because many young people left the villages to work in the hotels. Some land has been abandoned altogether. Farmers who remain say that prices are too low and that the cost of seed and fuel is too high, and they are asking for help to buy modern machinery that would let a smaller number of people produce a larger harvest."""
E = """Mining has behaved in a different way again. The island has one large copper mine, and the amount of metal that it produced stayed almost exactly the same for the whole period, because the mine works at full capacity and cannot easily produce more. The price of copper has gone up and down, however, and so the income from the mine has been unpredictable. Economists describe this as a hidden danger: an industry that looks stable may still bring unstable profits, and the government cannot plan its spending properly when it does not know how much the mine will earn in the following year."""
F = """Dr Samira Haddad, an economist who advises the government, argues that the four patterns point to a single lesson: no industry can be relied upon for ever. A country that depends on one source of income, she says, is like a farmer who plants only one crop. The decline of fishing was predictable, since the fish were being caught faster than they could breed, yet no one acted until the catch had already collapsed. She believes that a government should watch warning signs carefully, spend some of the profits from good years on new businesses, and train workers in skills which can be used in several different industries."""
G = """The government has accepted much of this advice. Its new plan, published last year, aims to develop technology services and renewable energy, so that the economy does not rely so heavily on tourists and metal. A training college will open next year to teach computer skills to young people from fishing and farming families. Critics say that the plan is too ambitious, since the island has few engineers and poor internet connections in the countryside. Supporters reply that the cost of doing nothing would be greater, and they point out that the earlier success of tourism began with an equally bold decision to build the airport."""
P = passage('p60', 'An Island and Its Industries', 'Economics', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the trend in each industry described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('level'), 160, 120)], [
  ('tourism', 0, 'B', 'the number has risen steadily'),
  ('fishing', 1, 'C', 'The numbers have fallen every year since'),
  ('farming', 2, 'D', 'output reached its highest point'),
  ('mining', 3, 'E', 'stayed almost exactly the same'),
 ]),
 tfng([
  ('Zendia is a real country.', 'F', 'A', 'imaginary island nation'),
  ('Zendia has about four million people.', 'T', 'A', 'about four million people'),
  ('Tourism now employs about one worker in four.', 'T', 'B', 'about one worker in four'),
  ('The island received over a million visitors twenty years ago.', 'F', 'B', 'fewer than two hundred thousand visitors a year'),
  ('The number of working fishing boats has halved.', 'T', 'C', 'the number of working boats has halved'),
  ('Scientists say that fish stocks will recover within five years.', 'F', 'C', 'it will take decades'),
  ('Farm output was highest about twelve years ago.', 'T', 'D', 'about twelve years ago'),
  ('The copper mine is owned by a foreign company.', 'NG', 'E', 'one large copper mine', 'Ownership is not mentioned.'),
  ('Dr Haddad compares an economy with one income to a farmer with one crop.', 'T', 'F', 'like a farmer who plants only one crop'),
 ]),
 mcq([
  ('Why did farm harvests decline?', ['The soil became exhausted and young people left.', 'Rain stopped.', 'Prices were too high.', 'The airport closed.'], 0, 'D', 'partly because the soil became exhausted'),
  ('Why is income from the mine unpredictable?', ['The price of copper goes up and down.', 'Output changes every year.', 'Workers go on strike.', 'The mine is closed.'], 0, 'E', 'The price of copper has gone up and down'),
  ('What is Dr Haddad\'s main lesson?', ['Fishing should stop.', 'No industry can be relied upon for ever.', 'Tourism is dangerous.', 'Mining is best.'], 1, 'F', 'no industry can be relied upon for ever'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Industry', 'Detail'],
  [['Tourism', 'The government built a new [[1]]'], ['Fishing', 'Strict [[2]] on the catch'], ['Farming', 'Output fell as the [[3]] became exhausted'], ['Mining', 'There is only one large [[4]] mine']],
  [(['airport'], 'B', 'a new airport'), (['limits'], 'C', 'strict limits on the catch'), (['soil'], 'D', 'the soil became exhausted'), (['copper'], 'E', 'one large copper mine')], 1),
 head(['An island and its figures', 'A tale of growth', 'Fewer fish each year', 'A rise and then a decline', 'Steady output, unsteady income', 'Why no industry is safe', 'Plans for new skills', 'The history of copper', 'A holiday guide'],
  [('A', 0, 'its main industries have changed'), ('B', 1, 'Tourism is the story of success'), ('C', 2, 'Fishing has followed the opposite course'), ('D', 3, 'Farming shows a rise followed by a fall'), ('E', 4, 'Mining has behaved in a different way again'), ('F', 5, 'no industry can be relied upon for ever'), ('G', 6, 'The government has accepted much of this advice')]),
 info([
  ('a reference to a worldwide economic crisis', 'B', 'worldwide economic crisis'),
  ('a mention of areas closed for part of the year', 'C', 'closed some areas completely for part of the year'),
  ('a reference to abandoned land', 'D', 'Some land has been abandoned altogether'),
  ('a mention of a danger that is not obvious', 'E', 'hidden danger'),
  ('a reference to poor connections in the countryside', 'G', 'poor internet connections in the countryside'),
 ]),
 ends(['has become the largest employer.', 'caught too many fish.', 'left the villages to work in hotels.', 'will teach computer skills.', 'closed the airport.', 'sold the beaches.', 'refused all help.'], [
  ('Tourism', 0, 'B', 'tourism has become the largest employer in the country'),
  ('The fishing fleet', 1, 'C', 'too many boats took too many fish'),
  ('Many young people', 2, 'D', 'left the villages to work in the hotels'),
  ('A new college', 3, 'G', 'teach computer skills'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Tourism has [[1]] steadily, while fishing has [[2]] because boats took too many fish. Farm output [[3]] its highest point twelve years ago, and mining output has stayed the [[4]].',
  [(['risen'], 'B', 'has risen steadily'), (['fallen'], 'C', 'have fallen every year'), (['reached'], 'D', 'reached its highest point'), (['same'], 'E', 'exactly the same')], 1,
  bank=['risen', 'fallen', 'reached', 'same', 'closed', 'doubled', 'copper', 'rice']),
 sent(2, [
  ('The government has published figures for the last ___ years.', ['twenty', '20'], 'A', 'last twenty years'),
  ('The largest employer in the country is ___.', ['tourism'], 'B', 'tourism has become'),
  ('Dr Haddad is an ___.', ['economist'], 'F', 'an economist'),
  ('The new plan aims to develop technology services and ___ energy.', ['renewable'], 'G', 'renewable energy'),
 ]),
 short(3, [
  ('Which fish were once plentiful?', ['tuna and sardines'], 'C', 'tuna and sardines'),
  ('What did irrigation help farmers produce?', ['rice and sugar'], 'D', 'rice and sugar'),
  ('When will the training college open?', ['next year'], 'G', 'next year'),
 ]),
])
