from lib import *
from svgs import *
A = """Tourism has changed the economy of many countries, and Calderia is no exception: the imaginary country of Calderia, used as an example here, has seen its tourism industry transformed in only a few decades. When the country gained independence in 1991, only a small number of foreign visitors came each year. Since then, the numbers have changed in several different ways, and the pattern is not a simple one. The industry now employs many thousands of people, from hotel staff and taxi drivers to guides and craft sellers, and its success matters to families in every region. This passage looks at four trends in the Calderian tourism industry and at the reasons behind them."""
B = """Visits from neighbouring countries have grown steadily for three decades. Families from Northmark, Estavia and Torvia travel to Verano and Hallen for shopping, medical care and weddings, and because the journey is short and cheap, the number of such visits has risen almost every year. They now make up the large majority of all arrivals."""
C = """Visitors from Europe have followed a different path. Numbers climbed fast in the 1990s, when the mountain towns were new to Western travellers, and they reached a peak around 2005. After that, they fell sharply, partly because flights were expensive and partly because the country was little advertised abroad. In recent years, the fall has stopped, and the numbers have begun to recover, helped by cheaper flights and by a successful advertising campaign in several European capitals."""
D = """The number of tourists who arrive by train has changed in yet another way. For many years it was small and almost constant, because the routes were slow. The opening of a fast train between Verano, Hallen and Brisca in 2011 changed that, and since then the number has risen quickly and then levelled off, as the carriages are now usually full and the company cannot add more trains until it has bought new engines. Local guides report that many passengers are families who prefer the train because it is comfortable and avoids the crowded roads."""
E = """Visits in winter show the most unusual pattern. In the early years, almost nobody came in the cold months. Numbers then rose and fell from year to year, depending on the weather and on special events such as festivals and ski competitions. Hotel owners say that this makes planning difficult, since they never know how many guests to expect, and so most small hotels close for part of the winter. Owners of larger hotels say that they would stay open if the government offered a small subsidy for heating."""
F = """The government has tried to influence these trends. A visa-free regime, introduced for citizens of many countries, was followed by a clear rise in arrivals from Asia and Europe. The government has also paid for restoration of old buildings and for a new airport terminal. Dr Elena Marsh, a tourism economist, argues that these investments are useful, but that better promotion abroad would bring more visitors at a lower cost."""
G = """What can be said about the future? Most analysts believe that the total number of visitors will continue to rise, although at a slower speed than in recent years. The industry will have to learn to attract guests in the winter, to improve its services, and to protect the old cities from the damage that too many tourists can cause. The government has promised to publish a plan next year, and the industry will be watching closely to see whether it includes money for training guides, for repairing roads in the mountains and for protecting the fragile old streets of the towns that visitors love best. If it succeeds, tourism could become one of the most important parts of the Calderian economy."""
P = passage('p24', 'Counting the Visitors', 'Economics', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Calderia became independent in 1991.', 'T', 'A', 'gained independence in 1991'),
  ('Visitors from neighbouring countries come mainly for holidays at the seaside.', 'F', 'B', 'shopping, medical care and weddings'),
  ('Most arrivals are from neighbouring countries.', 'T', 'B', 'the large majority of all arrivals'),
  ('European visitors reached their peak in 2005.', 'T', 'C', 'a peak around 2005'),
  ('European visitors have continued to fall in recent years.', 'F', 'C', 'the fall has stopped'),
  ('The fast train opened in 2011.', 'T', 'D', 'in 2011'),
  ('The fast train is usually half empty.', 'F', 'D', 'the carriages are now usually full'),
  ('Most small hotels stay open all year.', 'F', 'E', 'most small hotels close for part of the winter'),
  ('The new airport terminal cost more than the restored buildings.', 'NG', 'F', 'a new airport terminal', 'No costs are compared.'),
 ]),
 pic('Which graph, A to D, shows each trend described in the passage?', [(graph('rise'), 160, 120), (graph('peak'), 160, 120), (graph('plateau'), 160, 120), (graph('fluct'), 160, 120)], [
  ('visits from neighbouring countries', 0, 'B', 'has risen almost every year'),
  ('visitors from Europe over the whole period', 1, 'C', 'reached a peak around 2005'),
  ('tourists arriving by train after 2011', 2, 'D', 'risen quickly and then levelled off'),
  ('visits in winter', 3, 'E', 'rose and fell from year to year'),
 ]),
 mcq([
  ('Why did European arrivals fall after 2005?', ['Wars in the region.', 'Expensive flights and little advertising.', 'Closed borders.', 'Lack of hotels.'], 1, 'C', 'flights were expensive and partly because the country was little advertised'),
  ('What problem do hotel owners mention?', ['High taxes.', 'Not knowing how many guests will come.', 'Rude visitors.', 'Poor roads.'], 1, 'E', 'they never know how many guests to expect'),
  ('What does Dr Marsh prefer?', ['Higher visa fees.', 'Better promotion abroad.', 'More hotels.', 'Fewer tourists.'], 1, 'F', 'better promotion abroad would bring more visitors at a lower cost'),
 ]),
 multi('Which TWO reasons for the rise in arrivals by train are suggested in paragraph D?', ['A new fast train opened.', 'The carriages became full.', 'Tickets became free.', 'The routes were made slower.', 'Visitors preferred night travel.'], [0, 1], [('D', 'fast train between Verano, Hallen and Brisca'), ('D', 'usually full')]),
 head(['Introducing the topic', 'A steady rise', 'A rise, a peak and a fall', 'Growth that levelled off', 'An unpredictable season', 'The role of government', 'Looking ahead', 'The history of the railway', 'A comparison of hotel prices'],
  [('A', 0, 'This passage looks at four trends'), ('B', 1, 'Visits from neighbouring countries have grown steadily'), ('C', 2, 'Numbers climbed fast in the 1990s'), ('D', 3, 'levelled off'), ('E', 4, 'Visits in winter show the most unusual pattern'), ('F', 5, 'The government has tried to influence these trends'), ('G', 6, 'What can be said about the future')]),
 info([
  ('a list of countries that send visitors', 'B', 'Northmark, Estavia and Torvia'),
  ('a reason for slow train travel', 'D', 'the routes were slow'),
  ('an example of special winter events', 'E', 'festivals and ski competitions'),
  ('a policy that was followed by more arrivals', 'F', 'A visa-free regime'),
  ('a danger caused by too many tourists', 'G', 'the damage that too many tourists can cause'),
 ]),
 sent(2, [
  ('Families travel to Verano and Hallen for shopping, medical care and ___.', ['weddings'], 'B', 'shopping, medical care and weddings'),
  ('Western travellers found the mountain towns ___ in the 1990s.', ['new'], 'C', 'were new to Western travellers'),
  ('Dr Marsh is a tourism ___.', ['economist'], 'F', 'a tourism economist'),
  ('Tourism may become one of the most important parts of the Calderian ___.', ['economy'], 'G', 'the Calderian economy'),
 ]),
 short(3, [
  ('Which cities does the fast train connect with Tashkent?', ['hallen and brisca', 'hallen', 'brisca'], 'D', 'Verano, Hallen and Brisca'),
  ('What was introduced for citizens of many countries?', ['a visa-free regime', 'visa-free regime'], 'F', 'A visa-free regime'),
  ('How do most analysts expect visitor numbers to change?', ['continue to rise', 'rise'], 'G', 'will continue to rise'),
 ]),
])
