from lib import *
A = """Tea is the most widely drunk beverage in the world after water. According to legend, it was discovered in China around 2737 BC, when leaves from a wild tree blew into a pot of water that the emperor Shennong was boiling. Whatever the truth of the story, Chinese people were certainly drinking tea more than two thousand years ago, at first as a medicine and later for pleasure. By the Tang dynasty, in the eighth century, tea had become so popular that a scholar named Lu Yu wrote the first known book about it, describing how to grow, prepare and serve the drink."""
B = """Tea comes from a single plant, Camellia sinensis, an evergreen bush that grows best in warm, wet climates on hillsides. The young leaves and buds are picked by hand, and the best tea comes from the top two leaves and the bud. A skilled worker can pick about twenty kilograms of leaves in a day, but it takes around four kilograms of fresh leaf to make one kilogram of dry tea. Because the work is so careful, tea-picking has traditionally been done mainly by women, who learn the skill from their mothers and grandmothers."""
C = """The difference between types of tea lies in how the leaves are treated after picking. For green tea, the leaves are heated quickly to stop them from changing colour, and then dried. For black tea, the leaves are rolled and left to oxidise, which turns them dark and gives a stronger flavour. Oolong tea is partly oxidised, so its taste lies between the two. White tea is the least treated: the young buds are simply dried in the air. Each type must be brewed differently: green and white teas need cooler water, while black tea is best made with water that has just boiled."""
D = """Tea reached Europe in the early seventeenth century, carried by Dutch and Portuguese traders. At first it was so expensive that only the rich could afford it. By the eighteenth century, however, Britain was importing huge quantities, and a heavy tax led to widespread smuggling. Later, the British began to grow tea in India and Sri Lanka, because they wanted a supply that did not depend on China. Today, afternoon tea with sandwiches and cakes is still seen as a typical British custom, although most people now drink their tea from a simple bag."""
E = """In Central Asia, tea has always played a social role. In Uzbekistan, a host who pours tea for a guest shows respect by filling the cup only part of the way. The guest's cup is refilled often, so that the tea stays hot, and a full cup is sometimes taken as a sign that the host would like the guest to leave. Visitors to a home are often offered tea before anything else, and refusing it may seem impolite. Tea is usually served in a teahouse, or choyxona, together with bread, sweets and dried fruit."""
F = """Tea has long been linked with good health. Researchers have found that tea contains antioxidants, substances that may protect cells from damage, and that moderate drinking is unlikely to cause harm. However, the claims made for tea are sometimes exaggerated. Dr Yuki Tanaka, a nutrition scientist, notes that the strongest evidence comes from studies of people who drink tea, which cannot prove that tea alone is the cause of their good health."""
G = """Today, tea is a major industry. India and China together produce more than half of the world's tea, and Kenya is the largest exporter of black tea. Climate change is a growing worry for growers, because rising temperatures and changing rainfall affect both the quantity and the flavour of the leaves. Some farms have started to plant at higher altitudes, where the air is cooler, while others are testing new varieties that tolerate heat."""
P = passage('p23', 'Tea: From Leaf to Cup', 'Food and culture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Tea is the most widely drunk beverage in the world.', 'F', 'A', 'after water'),
  ('The legend says tea was discovered in China.', 'T', 'A', 'discovered in China around 2737 BC'),
  ('Tea was first used as a medicine.', 'T', 'A', 'at first as a medicine'),
  ('The best tea is picked by machine.', 'F', 'B', 'picked by hand'),
  ('It takes about four kilograms of fresh leaf to make a kilogram of dry tea.', 'T', 'B', 'around four kilograms of fresh leaf to make one kilogram of dry tea'),
  ('Green tea is left to oxidise.', 'F', 'C', 'heated quickly to stop them from changing colour'),
  ('Tea was cheap when it first reached Europe.', 'F', 'D', 'so expensive that only the rich could afford it'),
  ('Dutch traders brought the first tea to Britain.', 'NG', 'D', 'carried by Dutch and Portuguese traders', 'Europe is mentioned, but not Britain in particular.'),
  ('Tea is served with bread and sweets in a choyxona.', 'T', 'E', 'together with bread, sweets and dried fruit'),
 ]),
 mcq([
  ('Why did the British grow tea in India?', ['They liked Indian tea better.', 'They wanted a supply independent of China.', 'Tea was cheaper in China.', 'They wished to avoid tax.'], 1, 'D', 'did not depend on China'),
  ('What does a full cup of tea sometimes suggest in Uzbekistan?', ['The tea is very good.', 'The host is generous.', 'The host would like the guest to leave.', 'The guest is a child.'], 2, 'E', 'the host would like the guest to leave'),
  ('What does Dr Tanaka say about the evidence for tea\'s health benefits?', ['It proves that tea is a medicine.', 'It cannot show that tea is the only cause.', 'It is mostly from laboratory tests.', 'It is stronger than for other drinks.'], 1, 'F', 'cannot prove that tea alone is the cause'),
 ]),
 head(['A drink with a legendary beginning', 'A plant and its harvest', 'Why teas differ', 'The journey west', 'Hospitality and tradition', 'Is tea good for us?', 'A global business and its future', 'The invention of the teapot', 'Tea and coffee compared'],
  [('A', 0, 'According to legend, it was discovered in China'), ('B', 1, 'Tea comes from a single plant'), ('C', 2, 'The difference between types of tea'), ('D', 3, 'Tea reached Europe in the early seventeenth century'), ('E', 4, 'In Central Asia, tea has always played a social role'), ('F', 5, 'Tea has long been linked with good health'), ('G', 6, 'Today, tea is a major industry')]),
 info([
  ('the name of a plant', 'B', 'Camellia sinensis'),
  ('a reference to the least processed type of tea', 'C', 'White tea is the least treated'),
  ('a reason why smuggling grew', 'D', 'a heavy tax led to widespread smuggling'),
  ('a word for a place where tea is served', 'E', 'a teahouse, or choyxona'),
  ('a reference to farms moving to higher places', 'G', 'plant at higher altitudes'),
 ]),
 ends(['are picked by hand.', 'are rolled and left to oxidise.', 'are dried in the air.', 'led to widespread smuggling.', 'is the largest exporter of black tea.', 'were first grown in Europe.', 'was invented in Kenya.'], [
  ('The young leaves and buds', 0, 'B', 'picked by hand'),
  ('The leaves of black tea', 1, 'C', 'the leaves are rolled and left to oxidise'),
  ('The buds of white tea', 2, 'C', 'simply dried in the air'),
  ('A heavy tax on tea', 3, 'D', 'a heavy tax led to widespread smuggling'),
 ]),
 multi('Which TWO places are named as large tea producers in paragraph G?', ['India.', 'China.', 'Japan.', 'Turkey.', 'Argentina.'], [0, 1], [('G', 'India and China together'), ('G', 'India and China together')]),
 sent(2, [
  ('Tea comes from an ___ bush.', ['evergreen'], 'B', 'an evergreen bush'),
  ('Oolong tea is only ___ oxidised.', ['partly'], 'C', 'partly oxidised'),
  ('Tea reached Europe in the early ___ century.', ['seventeenth', '17th'], 'D', 'early seventeenth century'),
  ('Tea contains antioxidants, which may protect ___.', ['cells'], 'F', 'protect cells from damage'),
 ]),
 short(3, [
  ('What was the emperor called who was boiling water in the legend?', ['shennong'], 'A', 'the emperor Shennong'),
  ('How much leaf can a skilled worker pick in a day?', ['twenty kilograms', '20 kilograms', '20 kg'], 'B', 'about twenty kilograms of leaves in a day'),
  ('What is worrying tea growers about the climate?', ['rising temperatures', 'changing rainfall'], 'G', 'rising temperatures and changing rainfall'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Type of tea', 'How it is treated'],
  [['Green tea', 'Heated quickly, then [[1]]'], ['Black tea', 'Rolled and left to [[2]]'], ['Oolong tea', 'Partly [[3]]'], ['White tea', 'Young [[4]] dried in the air']],
  [(['dried'], 'C', 'and then dried'), (['oxidise'], 'C', 'left to oxidise'), (['oxidised'], 'C', 'partly oxidised'), (['buds'], 'C', 'the young buds are simply dried')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['The young leaves and buds are [[1]] by hand.', 'The leaves are [[2]] and left to oxidise.', 'They turn dark and gain a stronger [[3]].', 'The tea is dried and sold as [[4]] tea.'],
  [(['picked'], 'B', 'are picked by hand'), (['rolled'], 'C', 'the leaves are rolled'), (['flavour'], 'C', 'a stronger flavour'), (['black'], 'C', 'For black tea')], 1),
])
