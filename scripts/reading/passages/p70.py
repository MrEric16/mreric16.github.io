from lib import *
from svgs import *
A = """The imaginary country of Calderia depends on visitors for a large part of its income, and the national tourist board has counted the number of guests at four well-known resorts in each season of last year. The figures show that the seasons matter a great deal: a resort that is crowded in July may be almost empty in January, and the reverse can also be true. Managers must therefore plan carefully, hiring staff only when they are needed and finding other work for the quiet months. This passage describes the pattern at each resort, using the board's charts, and considers what the managers do to survive."""
B = """The first resort is on the Golden Coast, a long stretch of sand and warm sea. It is busy in summer and autumn, when the water is warm enough for swimming, and the hotels are full from June to November. In winter and spring, however, the weather is cool and the sea is cold, and the number of guests falls to a small fraction of the peak. Most of the cafés and shops close for four months, and many workers return to their families inland or look for work in the fruit harvest. The hotel owners have long wished that they could attract visitors in the quiet months."""
C = """The second resort, in the Zandra mountains, has exactly the opposite problem. It is crowded in winter, when snow covers the slopes, and almost empty for the other three seasons. The skiers come from the cities, and they fill the hotels from December to March, paying high prices. In spring, summer and autumn, the lifts stand still and the shops are shut. The manager, Mr Dario Costa, has tried to change this by building a network of walking paths and a mountain bike park, but so far they have attracted only a small number of visitors in summer, and he says that it will take years before they make a real difference."""
D = """The third resort is the old city of Marin, famous for its palaces, museums and gardens. Its visitors come mainly in spring and summer, when the days are long and the streets are pleasant for walking, and numbers drop sharply in autumn and winter, when the weather is wet. The city has tried to spread the visitors over the year by holding festivals in the quiet months, and these have had some success. A winter music festival, now in its fifth year, fills many of the hotels in December, although the total is still lower than in the summer months."""
E = """The fourth resort is a spa town called Hallen, whose hot springs are said to cure many illnesses. Its pattern is unusual: it is busiest in spring and in winter, and it is quiet in summer and autumn. Doctors recommend that patients visit the spa in cool weather, when hot baths are most enjoyable, and in summer the heat makes the treatments uncomfortable. Many of the visitors are elderly and stay for two or three weeks. The owners say that this long stay is valuable to them, because a guest who stays for three weeks spends far more than a tourist who comes for a weekend."""
F = """Dr Beatriz Almeida, a tourism economist, studied all four resorts. She found that the resorts with only one busy season are the most at risk. When a wet summer ruins a beach season or a mild winter leaves the ski slopes bare, a year's income can be lost in a few weeks. She advises resorts to develop attractions that do not depend on the weather, such as conference centres, museums and covered swimming pools, so that visitors have a reason to come in every season. She also suggests that the board offer cheap tickets in the quiet months to encourage people to travel then."""
G = """The tourist board has accepted her advice and will begin a campaign next year. It will publish a calendar showing the events at each resort, and offer discounts for those who visit outside the peak. The board has also promised money to help resorts build new facilities, which will be repaid from the extra income. Critics say that the plan does not take account of the climate: a beach cannot be warm in January, whatever the board does. Supporters agree, but they reply that the aim is not to make every month equally busy, only to make the quiet months a little less quiet."""
P = passage('p70', 'Four Resorts, Four Seasons', 'Tourism', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which bar chart, A to D, shows the visitors in each season (spring, summer, autumn, winter) at each resort?', [(bars([1, 5, 5, 1]), 160, 120), (bars([1, 1, 1, 5]), 160, 120), (bars([5, 5, 1, 1]), 160, 120), (bars([5, 1, 1, 5]), 160, 120)], [
  ('the Golden Coast', 0, 'B', 'It is busy in summer and autumn'),
  ('the ski resort', 1, 'C', 'crowded in winter'),
  ('Marin', 2, 'D', 'mainly in spring and summer'),
  ('Hallen', 3, 'E', 'busiest in spring and in winter'),
 ]),
 tfng([
  ('Calderia is an imaginary country.', 'T', 'A', 'imaginary country of Calderia'),
  ('The Golden Coast hotels are full from June to November.', 'T', 'B', 'from June to November'),
  ('Most cafés on the coast close for four months.', 'T', 'B', 'close for four months'),
  ('The ski resort is busy all year.', 'F', 'C', 'almost empty for the other three seasons'),
  ('Mr Costa has built a mountain bike park.', 'T', 'C', 'a mountain bike park'),
  ('Marin is famous for its beaches.', 'F', 'D', 'palaces, museums and gardens'),
  ('The winter music festival is in its fifth year.', 'T', 'D', 'now in its fifth year'),
  ('Many visitors to Hallen are elderly.', 'T', 'E', 'Many of the visitors are elderly'),
  ('The Hallen springs are the hottest in the world.', 'NG', 'E', 'hot springs', 'No comparison is made.'),
 ]),
 mcq([
  ('Why do doctors recommend cool weather for the spa?', ['Hot baths are most enjoyable then.', 'Prices are low.', 'The roads are open.', 'Doctors are free.'], 0, 'E', 'when hot baths are most enjoyable'),
  ('What does Dr Almeida say about one-season resorts?', ['They are the most at risk.', 'They are the richest.', 'They are the biggest.', 'They are new.'], 0, 'F', 'the most at risk'),
  ('What do critics say about the board\'s plan?', ['It costs too much.', 'It ignores the climate.', 'It is too slow.', 'It helps nobody.'], 1, 'G', 'does not take account of the climate'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Resort', 'Detail'],
  [['Beach', 'The water is warm enough for [[1]]'], ['Ski', 'Hotels are full from December to [[2]]'], ['City', 'The [[3]] are pleasant for walking'], ['Spa', 'Many visitors are [[4]]']],
  [(['swimming'], 'B', 'warm enough for swimming'), (['march'], 'C', 'December to March'), (['streets'], 'D', 'the streets are pleasant for walking'), (['elderly'], 'E', 'are elderly')], 1),
 multi('Which TWO attractions that do not depend on the weather does Dr Almeida suggest in paragraph F?', ['Conference centres.', 'Covered swimming pools.', 'Open-air cinemas.', 'Beach volleyball.', 'Sailing schools.'], [0, 1], [('F', 'conference centres'), ('F', 'covered swimming pools')]),
 head(['Why seasons matter', 'Sun, sand and a long winter', 'Snow and little else', 'A city that tries festivals', 'A town for the cool months', 'Advice on avoiding risk', 'A new campaign', 'The history of the hotel', 'Cooking by the sea'],
  [('A', 0, 'The figures show that the seasons matter a great deal'), ('B', 1, 'Most of the cafés and shops close for four months'), ('C', 2, 'the lifts stand still and the shops are shut'), ('D', 3, 'holding festivals in the quiet months'), ('E', 4, 'Doctors recommend that patients visit the spa in cool weather'), ('F', 5, 'the resorts with only one busy season are the most at risk'), ('G', 6, 'will begin a campaign next year')]),
 info([
  ('a reference to workers returning inland', 'B', 'return to their families inland'),
  ('a reference to a network of paths', 'C', 'a network of walking paths'),
  ('a reference to festivals in the quiet months', 'D', 'holding festivals in the quiet months'),
  ('a reference to long stays by patients', 'E', 'stay for two or three weeks'),
  ('a reference to discounts', 'G', 'offer discounts'),
 ]),
 ends(['are full from June to November.', 'come from the cities.', 'holds festivals in the quiet months.', 'will start a campaign next year.', 'closes in summer.', 'sells ski equipment.', 'is run by doctors.'], [
  ('The Golden Coast hotels', 0, 'B', 'the hotels are full from June to November'),
  ('The skiers', 1, 'C', 'The skiers come from the cities'),
  ('Marin', 2, 'D', 'holding festivals in the quiet months'),
  ('The tourist board', 3, 'G', 'begin a campaign next year'),
 ]),
 sent(2, [
  ('The Golden Coast is a long stretch of ___.', ['sand'], 'B', 'stretch of sand'),
  ('The manager of the ski resort is Mr Dario ___.', ['costa'], 'C', 'Dario Costa'),
  ('Hallen is a ___ town.', ['spa'], 'E', 'a spa town'),
  ('Dr Almeida is a tourism ___.', ['economist'], 'F', 'tourism economist'),
 ]),
 short(3, [
  ('Where is the ski resort?', ['the zandra mountains', 'zandra mountains'], 'C', 'Zandra mountains'),
  ('How long do many Hallen visitors stay?', ['three weeks'], 'E', 'two or three weeks'),
  ('What would the board offer in quiet months?', ['cheap tickets'], 'F', 'cheap tickets in the quiet months'),
 ]),
])
