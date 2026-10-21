from lib import *
from svgs import *
A = """The Silk Road was not a single road but a vast network of trading routes which linked China with the Mediterranean for about fifteen hundred years. The name was invented in 1877 by a German geographer, Ferdinand von Richthofen, who chose it because silk was the most famous product carried along the way, though traders also carried spices, glass, horses, paper and precious stones. The routes crossed deserts, mountains and some of the harshest country in the world, and few merchants travelled the whole distance. Instead, goods were passed from trader to trader, becoming more expensive at every stage, so that a piece of silk bought in China cost a fortune by the time it reached Rome."""
B = """The network began to take shape in the second century before our era, when the Chinese emperor sent an envoy, Zhang Qian, to look for allies against the nomads of the north. His journey took him through Central Asia, and when he returned after more than a decade he brought news of rich cities and fine horses. The emperor was impressed and sent more expeditions. Soon, caravans of camels were carrying silk westwards, and in return came horses, glass and gold. For the Chinese, the trade was valuable not only for the goods but also for the strength it gave the empire along its western border."""
C = """Between East and West, a chain of great cities grew rich on the trade. Samarkand and Bukhara, in what is now Uzbekistan, were among the most famous. Their markets sold goods from every corner of the known world, and their craftsmen produced fine cloth, ceramics and paper. Merchants rested in caravanserais, large inns with walled courtyards, where animals could be fed and goods stored safely behind locked gates. A traveller in Samarkand might hear a dozen languages in a single day, and the city was famous as a meeting place of religions and cultures, including Buddhists, Christians, Muslims and Zoroastrians."""
D = """The routes carried far more than goods. Ideas, religions and inventions travelled with the caravans. Buddhism spread from India into China along the Silk Road, and Islam later moved eastward into Central Asia. The Chinese invention of papermaking reached the Islamic world in the eighth century, and from there passed on to Europe, where it later made the printing of books affordable. Knowledge of astronomy, mathematics and medicine also passed in both directions, so that scholars in Baghdad, Samarkand and Beijing built on one another's discoveries. Historians often say that the Silk Road was the first great network for the exchange of knowledge."""
E = """The routes became safer in the thirteenth century, when the Mongol Empire controlled most of Asia and guarded the roads. In this period the Venetian merchant Marco Polo travelled to China and spent many years at the court of the emperor. When he returned to Europe, he wrote a famous account of what he had seen, which astonished readers with its descriptions of wealthy cities, paper money and a postal system. Some scholars doubt that he saw everything he described, but his book encouraged many Europeans to dream of the East, and it was read by explorers for centuries."""
F = """The Silk Road also carried dangers. In the fourteenth century, a terrible disease, the Black Death, is thought to have travelled westward along the trade routes and killed millions of people in Asia and Europe. At the same time, the Mongol Empire weakened, and the roads became less safe again. Meanwhile, European sailors found new sea routes to Asia, which were cheaper and could carry far more cargo than a caravan of camels. By the sixteenth century, most of the long-distance trade had moved to the sea, and many of the cities along the old routes lost their wealth."""
G = """Today, the Silk Road is remembered with pride. Dr Aziza Karimova, a historian of Central Asia, says that the great cities along the route developed a culture of tolerance and curiosity, because their prosperity depended on welcoming strangers. Many of the old monuments of Samarkand and Bukhara are now protected, and thousands of tourists visit them every year. Several governments have also announced plans to build new roads, railways and ports along the ancient routes, in what they call a revival of the Silk Road. Historians are cautious, however: they point out that the old network worked because it served the interests of many different peoples."""
P = passage('p78', 'The Silk Road', 'History', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Silk Road was a single road.', 'F', 'A', 'not a single road'),
  ('The name Silk Road was invented in 1877.', 'T', 'A', 'in 1877'),
  ('Few merchants travelled the whole distance.', 'T', 'A', 'few merchants travelled the whole distance'),
  ('Zhang Qian was sent by the Chinese emperor.', 'T', 'B', 'the Chinese emperor sent an envoy'),
  ('Samarkand and Bukhara are in what is now Uzbekistan.', 'T', 'C', 'in what is now Uzbekistan'),
  ('Caravanserais were large inns.', 'T', 'C', 'large inns with walled courtyards'),
  ('Buddhism spread from China to India along the road.', 'F', 'D', 'Buddhism spread from India into China'),
  ('Papermaking reached the Islamic world in the eighth century.', 'T', 'D', 'eighth century'),
  ('Marco Polo wrote his book in prison.', 'NG', 'E', 'he wrote a famous account', 'Where he wrote it is not mentioned.'),
 ]),
 mcq([
  ('Why did goods become very expensive?', ['They were passed from trader to trader.', 'They were stolen.', 'They were rare.', 'They were heavy.'], 0, 'A', 'becoming more expensive at every stage'),
  ('Why did the routes become safer in the thirteenth century?', ['The Mongol Empire guarded the roads.', 'Camels were faster.', 'The deserts shrank.', 'Rome fell.'], 0, 'E', 'guarded the roads'),
  ('Why did trade move to the sea?', ['Sea routes were cheaper and carried more cargo.', 'Camels died.', 'Silk was banned.', 'Cities closed.'], 0, 'F', 'cheaper and could carry far more cargo'),
 ]),
 feat('Match each statement with the correct person, A to D.', ['Zhang Qian', 'Marco Polo', 'Ferdinand von Richthofen', 'Dr Karimova'], [
  ('He gave the Silk Road its name.', 2, 'A', 'invented in 1877 by a German geographer'),
  ('He spent many years at the court of an emperor.', 1, 'E', 'spent many years at the court of the emperor'),
  ('He returned with news of rich cities.', 0, 'B', 'news of rich cities and fine horses'),
  ('She is a historian of Central Asia.', 3, 'G', 'historian of Central Asia'),
 ]),
 multi('Which TWO products carried along the Silk Road are mentioned in paragraph A?', ['Spices.', 'Glass.', 'Cars.', 'Coal.', 'Oil.'], [0, 1], [('A', 'spices'), ('A', 'glass')]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Item', 'Detail'],
  [['Zhang Qian', 'Sent to look for [[1]]'], ['Caravanserai', 'Animals could be [[2]]'], ['Papermaking', 'Reached Europe, making books [[3]]'], ['Black Death', 'Killed [[4]] of people']],
  [(['allies'], 'B', 'look for allies'), (['fed'], 'C', 'animals could be fed'), (['affordable'], 'D', 'books affordable'), (['millions'], 'F', 'killed millions of people')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Goods are passed from [[1]] to trader.', 'The price rises at every [[2]].', 'Camel [[3]] carry silk westwards.', 'Merchants rest in a [[4]].'],
  [(['trader'], 'A', 'from trader to trader'), (['stage'], 'A', 'at every stage'), (['caravans'], 'B', 'caravans of camels'), (['caravanserai'], 'C', 'caravanserais')], 1),
 head(['A network, not a road', 'The first expeditions', 'Cities of the desert', 'More than goods', 'A traveller\'s tale', 'Disease and decline', 'A proud memory', 'The history of tea', 'The invention of the compass'],
  [('A', 0, 'not a single road but a vast network'), ('B', 1, 'sent an envoy'), ('C', 2, 'a chain of great cities grew rich on the trade'), ('D', 3, 'The routes carried far more than goods'), ('E', 4, 'wrote a famous account of what he had seen'), ('F', 5, 'The Silk Road also carried dangers'), ('G', 6, 'remembered with pride')]),
 info([
  ('a reference to the cost of silk in Rome', 'A', 'cost a fortune'),
  ('a reference to a long journey of more than ten years', 'B', 'more than a decade'),
  ('a reference to many languages in one day', 'C', 'a dozen languages in a single day'),
  ('a reference to scholars in several cities', 'D', 'scholars in Baghdad, Samarkand and Beijing'),
  ('a reference to paper money', 'E', 'paper money and a postal system'),
 ]),
 ends(['was invented by a German geographer.', 'was a meeting place of religions.', 'were cheaper than caravans.', 'are now protected.', 'were built by Marco Polo.', 'are found only in China.', 'were sold as silk.'], [
  ('The name Silk Road', 0, 'A', 'a German geographer'),
  ('Samarkand', 1, 'C', 'meeting place of religions and cultures'),
  ('Sea routes', 2, 'F', 'cheaper and could carry far more cargo'),
  ('Many old monuments', 3, 'G', 'now protected'),
 ]),
 sent(2, [
  ('Ferdinand von Richthofen was a German ___.', ['geographer'], 'A', 'German geographer'),
  ('Merchants rested in ___.', ['caravanserais'], 'C', 'caravanserais'),
  ('The Venetian merchant ___ travelled to China.', ['marco polo', 'polo'], 'E', 'Marco Polo'),
  ('Dr Karimova is a historian of ___ Asia.', ['central'], 'G', 'Central Asia'),
 ]),
 short(3, [
  ('Which animals carried the silk?', ['camels'], 'B', 'caravans of camels'),
  ('Which disease may have travelled along the routes?', ['the black death', 'black death'], 'F', 'the Black Death'),
  ('When did the Mongol Empire make the routes safer?', ['thirteenth century', 'the thirteenth century'], 'E', 'thirteenth century'),
 ]),
])
