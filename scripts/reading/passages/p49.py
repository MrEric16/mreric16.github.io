from lib import *
from svgs import *
A = """Shopping has changed more in the last twenty years than in the previous two hundred. In the imaginary country of Zendia, the national statistics office has measured the way in which people buy goods since 1995, and its figures show clear and very different trends in four kinds of shopping. This passage describes them and considers the reasons, for businesses and for customers. It also asks what the figures may suggest about the next twenty years. Its authors point out that the figures include only goods bought in Zendia, and that purchases made on foreign websites, which are growing quickly, are not yet counted in the same way."""
B = """Online clothes shopping is the clearest case of growth. In 1995, it was almost unknown, because few households owned a computer. The share of clothes bought on the internet has risen every year since, and it now accounts for more than a third of all clothing sales. Free delivery and easy returns have been important, since customers can try the goods at home and send back anything that does not fit, which has removed an important reason for caution."""
C = """High-street shops, which sell goods in towns, have followed the opposite path. Their share of all sales was above ninety per cent in 1995, and it has fallen without a pause ever since. Many well-known stores have closed, and rows of empty premises are now a common sight in the centres of smaller towns. Local councils have tried to help by lowering parking charges and by arranging markets and events, but with little effect so far."""
D = """Paper catalogues, which once arrived in every home and offered goods by post, show a pattern with a peak. Orders grew until about 2002, helped by the arrival of telephone ordering and credit cards. After that, they began to fall, as customers moved to websites, which offer a wider choice and more up-to-date prices. The largest catalogue company stopped printing its paper edition in 2016, and it now exists only online."""
E = """The last case is grocery delivery, which changed little for many years. Supermarkets began to offer it in the early 2000s, but few customers used it, and the share of orders remained close to zero for more than a decade. Then, in 2020, when many people were advised to stay at home, the share jumped abruptly. It has remained higher than before, though it has not yet fallen back, which suggests that many people have found a habit they wish to keep."""
F = """Why do these four cases differ so much? Dr Anna Ivanova, a retail economist, believes that the answer lies in how easily the experience of buying can be copied on a screen. Clothes can be returned and compared, and catalogues are already pictures, so both moved online easily. Fresh food is harder, because customers like to choose it themselves. Dr Ivanova adds that events such as the stay-at-home period can change habits permanently, and that firms should expect more surprises."""
G = """For town centres, the lesson is that they must offer something that a screen cannot, such as meeting friends, enjoying a meal or attending an event. A number of towns have already turned former shops into homes, libraries and small workshops. Retailers, too, are experimenting, combining a website with shops that let customers collect their orders on the same day. Estate agents report that former shops in good locations are now rented for cafes, gyms and health centres, which attract many more visitors than a clothes shop did. It is too early to say which model will succeed, but nobody expects a return to the situation of 1995."""
P = passage('p49', 'How Zendia Shops', 'Society', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the trend for each kind of shopping described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('sharp'), 160, 120)], [
  ('online clothes shopping', 0, 'B', 'has risen every year since'),
  ('high-street shopping', 1, 'C', 'it has fallen without a pause ever since'),
  ('paper catalogue orders', 2, 'D', 'Orders grew until about 2002'),
  ('grocery delivery', 3, 'E', 'the share jumped abruptly'),
 ]),
 tfng([
  ('Zendia is an imaginary country.', 'T', 'A', 'the imaginary country of Zendia'),
  ('The figures cover the period since 1995.', 'T', 'A', 'since 1995'),
  ('Few households owned a computer in 1995.', 'T', 'B', 'few households owned a computer'),
  ('Online clothes shopping now accounts for more than half of sales.', 'F', 'B', 'more than a third of all clothing sales'),
  ('High-street shops had over ninety per cent of sales in 1995.', 'T', 'C', 'above ninety per cent'),
  ('Council efforts have greatly improved high-street sales.', 'F', 'C', 'with little effect so far'),
  ('The largest catalogue company stopped printing in 2016.', 'T', 'D', 'stopped printing its paper edition in 2016'),
  ('Grocery delivery grew rapidly in the early 2000s.', 'F', 'E', 'the share of orders remained close to zero for more than a decade'),
  ('Supermarkets in Zendia plan to close all their shops.', 'NG', 'G', 'a website with shops that let customers collect their orders', 'No plan to close all shops is mentioned.'),
 ]),
 mcq([
  ('Why has free delivery helped online clothes sales?', ['Customers can return what does not fit.', 'Clothes are cheaper.', 'Computers are faster.', 'Shops are closed.'], 0, 'B', 'send back anything that does not fit'),
  ('Why did catalogue orders fall?', ['Prices rose.', 'Customers moved to websites.', 'Post became slower.', 'Credit cards were banned.'], 1, 'D', 'customers moved to websites'),
  ('What does Dr Ivanova say about the stay-at-home period?', ['It changed nothing.', 'Events can change habits permanently.', 'It ruined retail.', 'It ended in 2020.'], 1, 'F', 'can change habits permanently'),
 ]),
 multi('Which TWO ways councils have tried to help high streets are mentioned in paragraph C?', ['Lowering parking charges.', 'Arranging markets and events.', 'Banning online shops.', 'Building new roads.', 'Giving out free vouchers.'], [0, 1], [('C', 'lowering parking charges'), ('C', 'arranging markets and events')]),
 head(['A changed way of buying', 'A steady climb', 'A steady decline', 'A rise followed by a fall', 'A sudden jump', 'Explaining the differences', 'What town centres can do', 'The history of money', 'Advice on saving'],
  [('A', 0, 'This passage describes them'), ('B', 1, 'Online clothes shopping is the clearest case of growth'), ('C', 2, 'High-street shops'), ('D', 3, 'show a pattern with a peak'), ('E', 4, 'The last case is grocery delivery'), ('F', 5, 'Why do these four cases differ so much'), ('G', 6, 'For town centres, the lesson is')]),
 info([
  ('a reference to an advantage of free returns', 'B', 'Free delivery and easy returns'),
  ('a mention of empty premises', 'C', 'rows of empty premises'),
  ('a reference to technology that helped catalogue orders', 'D', 'telephone ordering and credit cards'),
  ('an explanation of why fresh food is difficult to sell online', 'F', 'customers like to choose it themselves'),
  ('a mention of shops turned into libraries', 'G', 'homes, libraries and small workshops'),
 ]),
 sent(2, [
  ('Few households owned a ___ in 1995.', ['computer'], 'B', 'owned a computer'),
  ('Many well-known ___ have closed.', ['stores'], 'C', 'well-known stores'),
  ('Supermarkets began to offer delivery in the early ___.', ['2000s'], 'E', 'in the early 2000s'),
  ('Dr Ivanova is a retail ___.', ['economist'], 'F', 'a retail economist'),
 ]),
 short(3, [
  ('In which year did the grocery share jump?', ['2020'], 'E', 'in 2020'),
  ('What do catalogues now exist as?', ['online', 'online only'], 'D', 'it now exists only online'),
  ('What can customers collect on the same day?', ['their orders', 'orders'], 'G', 'collect their orders on the same day'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Online clothes sales have [[1]] every year, while the share of high-street shops has [[2]] without a pause. Catalogue orders reached a [[3]] in 2002, and grocery delivery jumped in [[4]].',
  [(['risen'], 'B', 'has risen every year'), (['fallen'], 'C', 'it has fallen without a pause'), (['peak'], 'D', 'a pattern with a peak'), (['2020'], 'E', 'in 2020')], 1,
  bank=['risen', 'fallen', 'peak', '2020', 'gained', '2002', 'low', 'closed']),
])
