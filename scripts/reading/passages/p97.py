from lib import *
from svgs import *
A = """Salt is so ordinary that we forget how important it is. Every cell in the human body needs it, and without it, we cannot digest food, send messages along our nerves or move our muscles. An adult body contains about two hundred and fifty grams of salt, and we lose some every day in sweat and urine, so we must replace it. For most of history, salt was also valuable for another reason: it kept food from rotting. Whole economies and empires were built on the salt trade, and the word salary comes from the Latin word for salt. This passage describes where salt comes from, how it has shaped history and why too much of it is harmful."""
B = """Salt, or sodium chloride, is found in two main places. The oceans contain huge amounts, about thirty-five grams in every litre of sea water, and the salt can be obtained by evaporation. In hot, dry countries, seawater is led into shallow pools where the sun slowly evaporates the water and leaves crystals behind. The second source is underground. Millions of years ago, ancient seas dried up and left thick layers of salt, which were later buried by rock. These deposits, called rock salt, can be mined like coal, or dissolved in water pumped down a well and then evaporated."""
C = """Early people discovered salt in many ways, and it soon became an important trade item. In ancient times, caravans carried salt across the Sahara, and in some places it was worth its weight in gold. The Roman army paid its soldiers partly in salt, or with money to buy it, and ancient roads such as the Via Salaria were built to carry it. In medieval Europe, towns that controlled salt supplies, such as Venice, grew rich. Governments realised that everyone needs salt and therefore taxed it. In several countries, the salt tax was hated, and it caused rebellions, including one in France before the revolution."""
D = """The greatest use of salt in the past was to preserve food. Before refrigerators were invented, meat and fish went bad in a few days. Salt draws water out of food and out of bacteria, and so prevents them from growing. Packed in salt, or soaked in brine, meat, fish and vegetables could be kept for months. Many traditional foods owe their flavour to this method: salted fish, ham, pickles, olives and cheese. Explorers and sailors depended on salted food for long voyages, and armies carried salted meat on campaigns."""
E = """Today, most salt is not used for food. Of the 280 million tonnes produced each year, only a small fraction is eaten. Chemical industries use salt as a raw material for chlorine and sodium hydroxide, which are used to make plastics, paper, soap and many other products. In cold countries, salt is spread on roads in winter, because it lowers the freezing point of water and melts ice. Salt is also used in water softening and in making glass. Some of the biggest producers are China, the United States and India, and Uzbekistan also has large natural deposits, including at Tuzkan Lake."""
F = """Although we need salt, we eat far too much of it. Health authorities recommend that adults eat no more than five grams a day, about a teaspoon, but in many countries the average is nearly double that. Too much salt raises blood pressure, which increases the risk of heart disease and stroke. Dr Irina Volkova, a nutritionist, notes that most of the salt in our diet does not come from the saltshaker. It is hidden in bread, cheese, processed meat, soups and ready meals. Reading labels, she advises, is the first step towards cutting down."""
G = """Fortunately, the taste for salt can be changed. Taste buds adapt in a few weeks: people who gradually reduce their salt find that their food tastes salty enough, and that they begin to notice other flavours. Some governments have asked food manufacturers to cut salt in their products, and the results have been encouraging. Dr Volkova also points out that some salt is needed in the diet, particularly for people who sweat heavily, and that in some regions, a lack of iodine is prevented by adding it to table salt. Salt, in short, is both a necessity and a danger, and the aim is to find the right amount."""
P = passage('p97', 'The Story of Salt', 'Science and history', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The human body needs salt to send messages along the nerves.', 'T', 'A', 'send messages along our nerves'),
  ('An adult body contains about two hundred and fifty grams of salt.', 'T', 'A', 'two hundred and fifty grams'),
  ('The word salary comes from the Latin word for salt.', 'T', 'A', 'Latin word for salt'),
  ('Sea water contains about thirty-five grams of salt per litre.', 'T', 'B', 'thirty-five grams in every litre'),
  ('Rock salt can be mined.', 'T', 'B', 'mined like coal'),
  ('Salt was never worth more than gold.', 'F', 'C', 'worth its weight in gold'),
  ('Governments taxed salt.', 'T', 'C', 'taxed it'),
  ('Salt prevents bacteria from growing.', 'T', 'D', 'prevents them from growing'),
  ('Salt was first discovered in China.', 'NG', 'C', 'Early people discovered salt in many ways', 'The place is not given.'),
 ]),
 mcq([
  ('How does salt preserve food?', ['It draws water out of bacteria.', 'It adds sugar.', 'It cools the food.', 'It kills fish.'], 0, 'D', 'draws water out'),
  ('Why is salt spread on roads in winter?', ['It lowers the freezing point of water.', 'It makes roads dry.', 'It is cheap.', 'It adds grip.'], 0, 'E', 'lowers the freezing point'),
  ('Where does most salt in our diet come from?', ['Processed foods.', 'The saltshaker.', 'Fruit.', 'Water.'], 0, 'F', 'hidden in bread'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Sea water is led into shallow [[1]].', 'The sun evaporates the [[2]].', 'Salt [[3]] are left behind.', 'Rock salt can be [[4]] like coal.'],
  [(['pools'], 'B', 'shallow pools'), (['water'], 'B', 'evaporates the water'), (['crystals'], 'B', 'crystals'), (['mined'], 'B', 'mined like coal')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Use', 'Detail'],
  [['Preserving food', 'Meat soaked in [[1]]'], ['Industry', 'Raw material for [[2]]'], ['Winter roads', 'Melts [[3]]'], ['Health', 'Too much raises blood [[4]]']],
  [(['brine'], 'D', 'brine'), (['chlorine'], 'E', 'chlorine'), (['ice'], 'E', 'melts ice'), (['pressure'], 'F', 'blood pressure')], 1),
 feat('Match each statement with the correct item, A to D.', ['Venice', 'Brine', 'Tuzkan Lake', 'Iodine'], [
  ('It grew rich by controlling salt supplies.', 0, 'C', 'grew rich'),
  ('Meat and fish could be kept in it for months.', 1, 'D', 'soaked in brine'),
  ('It is a natural salt deposit in Uzbekistan.', 2, 'E', 'Tuzkan Lake'),
  ('It is added to table salt in some regions.', 3, 'G', 'adding it to table salt'),
 ]),
 multi('Which TWO traditional foods preserved with salt are mentioned in paragraph D?', ['Ham.', 'Olives.', 'Rice.', 'Apples.', 'Bread.'], [0, 1], [('D', 'ham'), ('D', 'olives')]),
 head(['A common but vital substance', 'Where salt comes from', 'Salt and power', 'Keeping food fresh', 'Industrial uses', 'The hidden danger', 'Changing our taste', 'The history of bread', 'The oceans'],
  [('A', 0, 'Every cell in the human body needs it'), ('B', 1, 'found in two main places'), ('C', 2, 'important trade item'), ('D', 3, 'to preserve food'), ('E', 4, 'Today, most salt is not used for food'), ('F', 5, 'we eat far too much of it'), ('G', 6, 'the taste for salt can be changed')]),
 info([
  ('a reference to the Sahara', 'C', 'across the Sahara'),
  ('a reference to a Roman road', 'C', 'Via Salaria'),
  ('a reference to long voyages', 'D', 'long voyages'),
  ('a reference to a teaspoon', 'F', 'about a teaspoon'),
  ('a reference to taste buds', 'G', 'Taste buds adapt'),
 ]),
 ends(['evaporate sea water.', 'were fought over salt taxes.', 'prevents bacteria growing.', 'raises blood pressure.', 'is a gas.', 'cures all disease.', 'is made in Venice.'], [
  ('Sun-heated pools', 0, 'B', 'evaporates the water'),
  ('Rebellions', 1, 'C', 'caused rebellions'),
  ('Salt', 2, 'D', 'prevents them from growing'),
  ('Too much salt', 3, 'F', 'raises blood pressure'),
 ]),
 sent(2, [
  ('Salt is also called sodium ___.', ['chloride'], 'B', 'sodium chloride'),
  ('The salt tax caused ___ in several countries.', ['rebellions'], 'C', 'rebellions'),
  ('Adults should eat no more than ___ grams a day.', ['five', '5'], 'F', 'five grams'),
  ('Dr Volkova is a ___.', ['nutritionist'], 'F', 'a nutritionist'),
 ]),
 short(3, [
  ('How much salt is produced each year?', ['280 million tonnes'], 'E', '280 million tonnes'),
  ('What do taste buds do in a few weeks?', ['adapt'], 'G', 'adapt in a few weeks'),
  ('Which army paid soldiers partly in salt?', ['roman', 'the roman army'], 'C', 'The Roman army'),
 ]),
])
