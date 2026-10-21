from lib import *
A = """The Silk Road was not a single road. It was a network of trading routes that linked China with the Mediterranean for about fifteen hundred years. The name was invented in 1877 by a German geographer, Ferdinand von Richthofen, who wanted a simple way to describe the routes, and no traveller of the time ever used it. Very few merchants made the whole journey of more than six thousand kilometres. Instead, goods passed from trader to trader, and each one added a little to the price, so that a bolt of silk cost many times more in Rome than in China."""
B = """Silk was the most famous product, but it was far from the only one. Chinese craftsmen kept the method of making silk secret for centuries, and in Rome the cloth was worth almost its weight in gold. Caravans also carried spices, glass, horses, jade and paper. Travelling in the other direction, merchants brought gold, silver, wool and grapevines to China. The animal of choice was the camel, since a single camel could carry about two hundred kilograms and could go for days without water."""
C = """The journey was dangerous. Caravans crossed the Taklamakan Desert, whose name is often said to mean 'go in and you will not come out', and the high passes of the Pamir Mountains, where the air is thin and the cold can kill. Bandits were a constant threat. To protect themselves, merchants travelled in large groups and stayed overnight at caravanserais, walled inns built about a day's journey apart. A caravanserai offered water, food and a safe place for the animals, and its courtyard also served as a market where travellers could sell goods or exchange news."""
D = """Cities along the route grew rich. Samarkand, in what is now Uzbekistan, became one of the greatest trading centres in Central Asia, and its markets sold goods from three continents. Rulers taxed the merchants who passed through, and they spent the money on mosques, schools and observatories. The cities also became meeting places for languages and religions. Buddhism travelled from India to China along the same roads, and Islam later spread through Central Asia in the same way. A merchant in Samarkand might have spoken three or four languages."""
E = """Ideas moved as easily as goods. The art of papermaking reached the Arab world in the eighth century, after a battle near the River Talas in which Chinese prisoners taught their captors the craft. Paper later reached Europe and made printed books possible. Gunpowder, the compass and printing followed the same path westwards. Going east, mathematics from India and astronomy from the Islamic world influenced Chinese scholars, who were eager to learn from visitors."""
F = """Disease also travelled. Many historians believe that the Black Death, which killed a large share of the population of Europe in the fourteenth century, spread along trade routes from Central Asia. At about the same time, the Silk Road began to decline. The Mongol Empire, which had kept the routes safe for a century, broke up, and ships proved a cheaper way to move heavy cargo. By the sixteenth century, most merchants preferred the sea, and many of the caravanserais were abandoned."""
G = """Today the Silk Road is being rebuilt, in a way. China has paid for railways, roads and ports in many countries in a programme called the Belt and Road Initiative. Freight trains now carry goods between China and Europe in about two weeks, compared with around six weeks by sea. Supporters say that the projects bring jobs and trade to poorer countries. Critics reply that some governments are borrowing more than they can repay. Meanwhile, tourists follow the old route to see the mosques and markets of Samarkand and Bukhara."""
P = passage('p15', 'The Silk Road', 'History', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The name Silk Road was used by merchants at the time.', 'F', 'A', 'no traveller of the time ever used it'),
  ('The name was invented in the nineteenth century.', 'T', 'A', 'invented in 1877'),
  ('Most merchants travelled the whole length of the route.', 'F', 'A', 'Very few merchants made the whole journey'),
  ('Chinese craftsmen shared the method of making silk with Rome.', 'F', 'B', 'kept the method of making silk secret for centuries'),
  ('Merchants brought grapevines to China.', 'T', 'B', 'grapevines to China'),
  ('A camel could carry more than a horse.', 'NG', 'B', 'a single camel could carry about two hundred kilograms', 'Horses are not compared with camels in the passage.'),
  ('Caravanserais were built about a day\'s journey apart.', 'T', 'C', 'about a day\'s journey apart'),
  ('Bandits were rarely a problem for travellers.', 'F', 'C', 'Bandits were a constant threat'),
  ('Samarkand was the largest city in the world at that time.', 'NG', 'D', 'one of the greatest trading centres in Central Asia', 'The passage says it was one of the greatest in Central Asia, nothing more.'),
 ]),
 mcq([
  ('Why did a bolt of silk cost more in Rome than in China?', ['Roman taxes were very high.', 'Each trader added to the price.', 'Silk was cheaper to make in Rome.', 'Camels were expensive to buy.'], 1, 'A', 'each one added a little to the price'),
  ('How did papermaking reach the Arab world?', ['Merchants bought the secret.', 'Chinese prisoners taught it.', 'Scholars copied a book.', 'An Arab ruler visited China.'], 1, 'E', 'Chinese prisoners taught their captors the craft'),
  ('Why did the Silk Road decline?', ['Disease killed all the merchants.', 'The deserts grew larger.', 'Safe routes ended and sea transport was cheaper.', 'Europe stopped wanting silk.'], 2, 'F', 'ships proved a cheaper way to move heavy cargo'),
 ]),
 head(['A name for a network', 'More than just silk', 'Dangers and places to rest', 'Wealth, faith and language in the cities', 'The spread of knowledge', 'Disease and the end of the old routes', 'A modern revival', 'The invention of the camel saddle', 'The life of a Roman merchant', 'Why silk was so light'],
  [('A', 0, 'The Silk Road was not a single road'), ('B', 1, 'far from the only one'), ('C', 2, 'The journey was dangerous'), ('D', 3, 'Cities along the route grew rich'), ('E', 4, 'Ideas moved as easily as goods'), ('F', 5, 'Disease also travelled'), ('G', 6, 'Today the Silk Road is being rebuilt')]),
 info([
  ('a reference to a loaded animal\'s ability to go without water', 'B', 'go for days without water'),
  ('an explanation of the meaning of a desert\'s name', 'C', 'go in and you will not come out'),
  ('a mention of the use of tax money', 'D', 'spent the money on mosques, schools and observatories'),
  ('an example of scholars wanting to learn from foreigners', 'E', 'eager to learn from visitors'),
  ('a comparison of two travel times', 'G', 'about two weeks, compared with around six weeks by sea'),
 ]),
 sent(2, [
  ('The name Silk Road was invented by a German ___.', ['geographer'], 'A', 'a German geographer'),
  ('Caravans crossed the high passes of the ___ Mountains.', ['pamir'], 'C', 'the Pamir Mountains'),
  ('Rulers paid for schools and observatories with money from ___.', ['taxes', 'tax'], 'D', 'Rulers taxed the merchants'),
  ('Paper made printed ___ possible in Europe.', ['books'], 'E', 'made printed books possible'),
  ('The Belt and Road Initiative is paid for by ___.', ['china'], 'G', 'China has paid for railways'),
 ]),
 short(3, [
  ('What did the courtyard of a caravanserai also serve as?', ['a market', 'market'], 'C', 'its courtyard also served as a market'),
  ('Which religion travelled from India to China?', ['buddhism'], 'D', 'Buddhism travelled from India to China'),
  ('In which century did the Black Death kill many people in Europe?', ['fourteenth', 'the fourteenth', '14th'], 'F', 'in the fourteenth century'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Topic', 'Detail'],
  [['Animals', 'Merchants preferred the [[1]] for long journeys'], ['Shelter', 'Travellers slept in [[2]] on the route'], ['City', 'Samarkand is in what is now [[3]]'], ['Decline', 'The [[4]] Empire broke up']],
  [(['camel'], 'B', 'The animal of choice was the camel'), (['caravanserais'], 'C', 'stayed overnight at caravanserais'), (['uzbekistan'], 'D', 'what is now Uzbekistan'), (['mongol'], 'F', 'The Mongol Empire')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Chinese [[1]] taught the craft of making paper after a battle near the River Talas.', 'The craft reached the [[2]] world in the eighth century.', 'Paper later reached [[3]].', 'This made [[4]] books possible.'],
  [(['prisoners'], 'E', 'Chinese prisoners taught their captors'), (['arab'], 'E', 'reached the Arab world'), (['europe'], 'E', 'Paper later reached Europe'), (['printed'], 'E', 'made printed books possible')], 1),
 feat('Which place is each statement about? Choose the correct letter, A to C.', ['The Taklamakan Desert', 'Samarkand', 'The River Talas'], [
  ('Its name is said to be a warning.', 0, 'C', 'go in and you will not come out'),
  ('Its markets sold goods from three continents.', 1, 'D', 'goods from three continents'),
  ('A battle took place near it.', 2, 'E', 'a battle near the River Talas'),
  ('It is in Uzbekistan.', 1, 'D', 'in what is now Uzbekistan'),
 ], cls=True),
])
