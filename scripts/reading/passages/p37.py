from lib import *
from svgs import *
A = """Sport is changing in every country, but the changes are not always simple. The imaginary country of Zendia, whose sports councils have kept careful records for forty years, shows how different activities can follow quite different paths. This passage examines four of them: running, tennis, cycling and swimming. For each one, it asks what happened, and then why. The answers help to explain what governments can and cannot do to encourage people to take exercise. The records are unusually complete, because every club and public pool in the country must report its numbers each year, and because the same definitions have been used since the 1980s."""
B = """Running is the clearest success story. In 1985, only a few thousand people in Zendia took part in organised races. Since then the number has risen without a break, and it now exceeds two million. The reasons are easy to see: running needs no club, no special place and almost no equipment, and free weekly timed races in public parks have made it easy for beginners to join. Doctors have also encouraged it, since regular running protects the heart."""
C = """The history of tennis has been less happy. Membership of tennis clubs was high in the 1980s, but it has fallen at every count since. Courts are expensive to build and to maintain, and in cities they take up land that developers want for housing. Many clubs have closed. Young people, who once learned the game at school, now have a wide choice of other sports, and the television coverage of tennis has moved from free to paid channels, which has reduced its audience."""
D = """Cycling shows the most unpredictable pattern. The number of people who cycle regularly goes up and down from one year to the next. It rises in years when the national tour passes close to large towns, and when the price of fuel is high. It falls after wet summers, and after accidents that attract much attention in the newspapers. Because the numbers move in this way, planners find it difficult to decide how many cycle paths to build, and some have given up trying."""
E = """Swimming has followed yet another course. Until 2012, the number of regular swimmers was stable, at around three million. Then two of the biggest public pools in the capital closed for repairs that were meant to last a year but in fact took four. The number of swimmers fell abruptly and has not recovered, since many of those who stopped have found other ways of exercising. The council has promised to open new pools, but the work has not started. Swimming teachers say that many children now reach the age of ten without learning to swim, which they regard as a serious risk to safety as well as to health."""
F = """What can be learned from these cases? Dr Hana Weiss, a sports economist, argues that policy should be guided by the nature of each activity. Sports that need little equipment, such as running, grow almost by themselves if the government provides safe places and information. Sports that depend on special buildings, such as swimming and tennis, need steady investment, and a short closure can do lasting damage. Sports that depend on weather, such as cycling, will always change with the season, and planners must accept this."""
G = """Looking ahead, the sports councils of Zendia are planning more flexible schemes. Instead of building one large centre, they hope to offer smaller facilities in more neighbourhoods, and to give people simple ways to try new activities. They also plan to count participants more accurately, using electronic cards, since the present figures depend on surveys that people do not always answer honestly. If the plans succeed, the next forty years may be more encouraging for the less fortunate sports."""
P = passage('p37', 'Sport in Zendia', 'Society', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the trend for each sport described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('fluct'), 160, 120), (graph('drop'), 160, 120)], [
  ('running', 0, 'B', 'the number has risen without a break'),
  ('tennis club membership', 1, 'C', 'it has fallen at every count since'),
  ('regular cycling', 2, 'D', 'goes up and down from one year to the next'),
  ('swimming', 3, 'E', 'The number of swimmers fell abruptly'),
 ]),
 tfng([
  ('Zendia is a real country.', 'F', 'A', 'The imaginary country of Zendia'),
  ('The sports councils have kept records for forty years.', 'T', 'A', 'kept careful records for forty years'),
  ('Running needs a great deal of equipment.', 'F', 'B', 'almost no equipment'),
  ('Free weekly races help beginners.', 'T', 'B', 'free weekly timed races in public parks'),
  ('Tennis membership has risen since the 1980s.', 'F', 'C', 'it has fallen at every count since'),
  ('Cycling numbers are affected by the price of fuel.', 'T', 'D', 'when the price of fuel is high'),
  ('The two pools were closed for four years.', 'T', 'E', 'in fact took four'),
  ('The council has already opened new pools.', 'F', 'E', 'the work has not started'),
  ('Running is the most popular sport in Zendia.', 'NG', 'B', 'now exceeds two million', 'The numbers for other sports are given differently, so no comparison of popularity is made.'),
 ]),
 mcq([
  ('Why has tennis declined?', ['Courts are costly and young people have more choice.', 'Players are older.', 'It is too easy.', 'Rackets are expensive.'], 0, 'C', 'Courts are expensive to build and to maintain'),
  ('Why do planners find cycling difficult to plan for?', ['It never changes.', 'The numbers keep changing.', 'It is dangerous.', 'It is unpopular.'], 1, 'D', 'planners find it difficult to decide'),
  ('What does Dr Weiss say about sports that need special buildings?', ['They grow by themselves.', 'They need steady investment.', 'They should be abandoned.', 'They are the cheapest.'], 1, 'F', 'need steady investment'),
 ]),
 multi('Which TWO reasons why running has grown are given in paragraph B?', ['It needs almost no equipment.', 'Free weekly races exist in parks.', 'Clubs are cheap to join.', 'It is shown on television.', 'It is taught at school.'], [0, 1], [('B', 'almost no equipment'), ('B', 'free weekly timed races in public parks')]),
 head(['Introducing the study', 'A sport that keeps growing', 'A sport losing members', 'A sport that follows the weather and the news', 'The effect of closing pools', 'Policy advice for different sports', 'Plans for the future', 'The history of the Olympic Games', 'How to choose a racket'],
  [('A', 0, 'This passage examines four of them'), ('B', 1, 'Running is the clearest success story'), ('C', 2, 'Membership of tennis clubs was high in the 1980s'), ('D', 3, 'Cycling shows the most unpredictable pattern'), ('E', 4, 'two of the biggest public pools in the capital closed'), ('F', 5, 'What can be learned from these cases'), ('G', 6, 'Looking ahead, the sports councils of Zendia are planning')]),
 info([
  ('a mention of a benefit to health', 'B', 'regular running protects the heart'),
  ('a reference to payment for television', 'C', 'from free to paid channels'),
  ('a reference to the national tour', 'D', 'the national tour passes close to large towns'),
  ('a figure for the number of regular swimmers', 'E', 'around three million'),
  ('a reference to electronic cards', 'G', 'using electronic cards'),
 ]),
 sent(2, [
  ('Doctors encourage running because it protects the ___.', ['heart'], 'B', 'protects the heart'),
  ('Many tennis ___ have closed.', ['clubs'], 'C', 'Many clubs have closed'),
  ('The two pools were closed for ___.', ['repairs'], 'E', 'closed for repairs'),
  ('Dr Weiss is a sports ___.', ['economist'], 'F', 'a sports economist'),
 ]),
 short(3, [
  ('How many people now take part in races in Zendia?', ['two million', 'over two million'], 'B', 'exceeds two million'),
  ('What do developers want city land for?', ['housing'], 'C', 'land that developers want for housing'),
  ('What do present figures depend on?', ['surveys'], 'G', 'depend on surveys'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Running has grown because it needs little [[1]], while tennis has declined as courts are [[2]]. Cycling rises and falls with the weather and the price of [[3]]. Swimming fell sharply when two [[4]] closed.',
  [(['equipment'], 'B', 'almost no equipment'), (['expensive'], 'C', 'Courts are expensive'), (['fuel'], 'D', 'the price of fuel'), (['pools'], 'E', 'public pools')], 1,
  bank=['equipment', 'expensive', 'fuel', 'pools', 'clubs', 'cheap', 'paths', 'races']),
])
