from lib import *
from svgs import *
A = """Every year in March, people across Uzbekistan celebrate Navruz, the festival of the new year. The word comes from Persian and means new day. The festival is held on or around the twenty-first of March, the day of the spring equinox, when day and night are almost equal in length and the sun begins to spend longer in the sky. For thousands of years, people in Central Asia, Iran, Afghanistan, the Caucasus and many other regions have used this moment to mark the end of winter and the beginning of the farming year. In 2009, UNESCO added Navruz to its list of the intangible cultural heritage of humanity."""
B = """The origins of Navruz go back more than three thousand years, to the ancient religion of Zoroastrianism, which honoured light, fire and the renewal of nature. The date of the festival has always been linked to the sun, and not to a calendar based on the moon, so it does not move from year to year. Over the centuries, Navruz survived the arrival of other religions, and it has been celebrated by Muslims, Christians and people of other faiths. For this reason, it is seen less as a religious festival than as a celebration of nature and community that belongs to everyone."""
C = """Preparations begin weeks beforehand. Families clean their houses thoroughly, repair what is broken and pay old debts, so as to start the year afresh. People wear new clothes, and in some places they jump over small bonfires to leave the troubles of the old year behind. Women sprout wheat grains in dishes, and the green shoots are a symbol of the renewal of life. Neighbours who have quarrelled are expected to forgive one another, and visits to relatives and friends, especially older ones, are an important part of the holiday."""
D = """Food is at the centre of the celebration. The best-known dish is sumalak, a thick sweet paste made from sprouted wheat, flour and water. It is cooked in huge cauldrons for up to twenty-four hours, and people stay up through the night, taking turns to stir it and singing songs. According to tradition, a few smooth stones are put in the bottom of the pot to prevent it from burning. The pot is often shared between whole neighbourhoods. Other dishes include halim, a dish of wheat and meat, and pilaf, as well as sweets, nuts and dried fruits that are put on a generous table."""
E = """The streets are also full of public celebration. In towns and villages, there are fairs where craftsmen sell their work, and concerts with traditional music and dancing. Competitions are held in which strong men wrestle, riders play a horseback game called kupkari, and tightrope walkers perform. Children fly kites and play games. In Tashkent and other cities, parks are decorated with flowers, and stages are put up for the performers. Many people dress in national costume, and the festival is a good opportunity to see regional dishes, music and crafts from all over the country."""
F = """Navruz has not always been celebrated freely. During parts of the twentieth century, in the Soviet period, the festival was officially discouraged in some regions, though people continued to keep its customs at home. After independence in 1991, Uzbekistan restored Navruz as an official holiday, and today it is a day off work, often extended to several days. Dr Gulnora Rashidova, an ethnographer who studies traditional festivals, says that the revival was welcomed with great emotion. Older people, she reports, remembered the celebrations of their childhood, and younger people were glad to learn the customs of their grandparents."""
G = """The meaning of Navruz is the same everywhere. Whether people celebrate it in Tashkent, Tehran, Kabul or Baku, it is a time for hope, generosity and the renewal of friendships. In 2010, the United Nations General Assembly recognised the International Day of Navruz, to be marked each year on the twenty-first of March. Dr Rashidova believes that the festival has lasted so long because it speaks to a basic human need, the wish to believe that after a hard winter comes a time of warmth and growth. As the old saying goes, what you do on the first day of the year will be repeated through the whole year."""
P = passage('p91', 'Navruz: The Festival of Spring', 'Culture', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Navruz means new day.', 'T', 'A', 'means new day'),
  ('Navruz is held around the twenty-first of March.', 'T', 'A', 'twenty-first of March'),
  ('UNESCO added Navruz to its list in 2009.', 'T', 'A', 'In 2009'),
  ('The date of Navruz is linked to the moon.', 'F', 'B', 'linked to the sun'),
  ('Navruz is celebrated only by Muslims.', 'F', 'B', 'Muslims, Christians and people of other faiths'),
  ('Families pay old debts before the festival.', 'T', 'C', 'pay old debts'),
  ('Sumalak is cooked for up to twenty-four hours.', 'T', 'D', 'up to twenty-four hours'),
  ('Smooth stones are placed in the pot to stop it burning.', 'T', 'D', 'prevent it from burning'),
  ('Navruz is celebrated in Turkey.', 'NG', 'G', 'Tashkent, Tehran, Kabul or Baku', 'Turkey is not mentioned.'),
 ]),
 mcq([
  ('Why do people sprout wheat grains?', ['The green shoots symbolise renewal.', 'To feed animals.', 'To sell at fairs.', 'To make bread.'], 0, 'C', 'renewal of life'),
  ('What happened after independence in 1991?', ['Navruz was restored as an official holiday.', 'Navruz was banned.', 'The date was moved.', 'Fairs were closed.'], 0, 'F', 'restored Navruz as an official holiday'),
  ('Why has Navruz lasted so long, according to Dr Rashidova?', ['It speaks to the wish for warmth and growth.', 'It is cheap.', 'It is short.', 'It is ordered by law.'], 0, 'G', 'speaks to a basic human need'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Date', 'The spring [[1]]'], ['Origin', 'Zoroastrianism, which honoured light and [[2]]'], ['Sumalak', 'Made from sprouted [[3]]'], ['Kupkari', 'A game played on [[4]]']],
  [(['equinox'], 'A', 'spring equinox'), (['fire'], 'B', 'light, fire'), (['wheat'], 'D', 'sprouted wheat'), (['horseback'], 'E', 'horseback game')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Families clean their [[1]].', 'Women sprout [[2]] in dishes.', 'Neighbours who have quarrelled [[3]] one another.', 'People visit [[4]] and friends.'],
  [(['houses'], 'C', 'clean their houses'), (['wheat'], 'C', 'sprout wheat'), (['forgive'], 'C', 'forgive one another'), (['relatives'], 'C', 'relatives and friends')], 1),
 feat('Match each statement with the correct item, A to D.', ['Sumalak', 'Halim', 'Kupkari', 'Dr Rashidova'], [
  ('It is made from sprouted wheat, flour and water.', 0, 'D', 'sprouted wheat, flour and water'),
  ('It is a dish of wheat and meat.', 1, 'D', 'wheat and meat'),
  ('It is a horseback game.', 2, 'E', 'horseback game'),
  ('She is an ethnographer.', 3, 'F', 'ethnographer'),
 ]),
 multi('Which TWO activities for children are mentioned in paragraph E?', ['Flying kites.', 'Playing games.', 'Wrestling.', 'Driving carts.', 'Cooking.'], [0, 1], [('E', 'fly kites'), ('E', 'play games')]),
 head(['A new day, a new year', 'Ancient roots', 'Getting ready', 'The cooking pot', 'Fairs and games', 'A festival revived', 'A message for everyone', 'The history of calendars', 'The history of kites'],
  [('A', 0, 'the festival of the new year'), ('B', 1, 'more than three thousand years'), ('C', 2, 'Preparations begin weeks beforehand'), ('D', 3, 'Food is at the centre'), ('E', 4, 'fairs where craftsmen sell their work'), ('F', 5, 'restored Navruz as an official holiday'), ('G', 6, 'hope, generosity and the renewal of friendships')]),
 info([
  ('a reference to jumping over bonfires', 'C', 'jump over small bonfires'),
  ('a reference to a night of singing', 'D', 'singing songs'),
  ('a reference to tightrope walkers', 'E', 'tightrope walkers'),
  ('a reference to the Soviet period', 'F', 'Soviet period'),
  ('a reference to the United Nations', 'G', 'United Nations General Assembly'),
 ]),
 ends(['began in Zoroastrian times.', 'are put in the cooking pot.', 'sell their work at fairs.', 'was restored after 1991.', 'is always in June.', 'is only for children.', 'is held in autumn.'], [
  ('Navruz', 0, 'B', 'Zoroastrianism'),
  ('Smooth stones', 1, 'D', 'smooth stones'),
  ('Craftsmen', 2, 'E', 'craftsmen sell their work'),
  ('The official holiday', 3, 'F', 'After independence in 1991'),
 ]),
 sent(2, [
  ('Navruz means new ___.', ['day'], 'A', 'new day'),
  ('People wear new ___ for the festival.', ['clothes'], 'C', 'new clothes'),
  ('Sumalak is cooked in huge ___.', ['cauldrons'], 'D', 'huge cauldrons'),
  ('The UN recognised the International Day of Navruz in ___.', ['2010'], 'G', 'In 2010'),
 ]),
 short(3, [
  ('When is the spring equinox?', ['twenty-first of march', 'march'], 'A', 'twenty-first of March'),
  ('What did the Soviet period do to Navruz in some regions?', ['discouraged it', 'discouraged'], 'F', 'officially discouraged'),
  ('What do day and night do at the equinox?', ['almost equal'], 'A', 'almost equal in length'),
 ]),
])
