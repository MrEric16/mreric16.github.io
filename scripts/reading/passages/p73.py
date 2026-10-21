from lib import *
from svgs import *
A = """The bicycle is one of the simplest and most successful machines ever invented. It converts human energy into movement more efficiently than any other vehicle, it needs no fuel but food, and it is cheap enough for millions of people who could never afford a car. Today more than a billion bicycles are in use around the world. Yet the machine that we know was not invented in a single moment. It developed over about seventy years, as many inventors tried different ideas, and several of their designs were so uncomfortable or dangerous that they seem almost comic today."""
B = """The story begins in 1817, when a German baron, Karl von Drais, built a wooden machine with two wheels in a line, a seat and a steering handle. There were no pedals: the rider sat astride and pushed against the ground with his feet, like a child on a scooter. The machine was called the draisine, after its inventor, or the hobby horse. It was fast on smooth roads, and for a few years it was a fashion among wealthy young men. But the roads of the time were rough and muddy, and the machine was heavy, so the craze soon faded, and the draisine was forgotten for decades."""
C = """In the 1860s, French makers added pedals directly to the front wheel, and the machine became the velocipede. It was an important step, because the rider could now keep his feet off the ground, but the machine was heavy and its iron-rimmed wheels made the ride so rough that it earned the nickname boneshaker. A single turn of the pedals moved the machine forward by only one turn of the wheel, so that speed depended on the size of the wheel. This simple fact led makers to a new idea: if a larger wheel meant greater speed, the front wheel should be made as large as possible."""
D = """The result, in the 1870s, was the penny-farthing, named after two British coins, one large and one small. The front wheel might be more than a metre and a half across, and the rider sat high above it, with the tiny rear wheel following behind. These machines were fast, and racing became popular, but they were also very dangerous. A sudden stop or a stone on the road could throw the rider over the handlebars and on to his head. Riding one required skill and courage, and only young, athletic men attempted it, so the bicycle remained a toy for the few and not a vehicle for everyone."""
E = """The breakthrough came in the 1880s with the safety bicycle, designed by John Kemp Starley in England. It had two wheels of equal size, a low seat, and a chain which carried power from the pedals to the rear wheel. Because the gearing allowed the wheels to turn faster than the pedals, a small wheel could still give good speed. The rider sat close to the ground, could put his feet down in an emergency, and was no longer in danger of a fall from a great height. The shape of the design, with a diamond-shaped frame, has changed remarkably little in more than a century."""
F = """A further improvement came in 1888, when a Scottish veterinary surgeon, John Boyd Dunlop, invented the air-filled, or pneumatic, tyre for his son's tricycle. Soft tyres absorbed the shocks from the road and also reduced friction, so that cycling became both more comfortable and faster. Within a few years almost every maker had adopted the idea. With the safety bicycle and the pneumatic tyre together, cycling suddenly became practical and enjoyable for ordinary people, including women, for whom the new machine offered an unprecedented freedom to travel without a man or a horse."""
G = """In the twentieth century the bicycle continued to develop. Gears, lighter metals, better brakes and, more recently, electric motors that help the rider on hills, have all been added. Dr Maria Kovac, a historian of technology, says that the bicycle is a model of good design: every part has a purpose, and nothing can be removed without loss. She believes that it will remain important in the future, because cities are becoming crowded, and a machine that carries a person at the speed of a car in traffic, while taking up far less space, is an obvious answer to the problem."""
S, PT, W, H = chain(5)
P = passage('p73', 'How the Bicycle Evolved', 'Technology', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('More than a billion bicycles are in use today.', 'T', 'A', 'more than a billion bicycles'),
  ('The bicycle developed over about seventy years.', 'T', 'A', 'about seventy years'),
  ('The draisine had pedals.', 'F', 'B', 'There were no pedals'),
  ('The draisine was built in 1817.', 'T', 'B', 'in 1817'),
  ('The velocipede was nicknamed the boneshaker.', 'T', 'C', 'the nickname boneshaker'),
  ('The penny-farthing was named after two coins.', 'T', 'D', 'two British coins'),
  ('The penny-farthing was safe for everyone to ride.', 'F', 'D', 'very dangerous'),
  ('The safety bicycle was designed in England.', 'T', 'E', 'John Kemp Starley in England'),
  ('Dunlop became rich from his invention.', 'NG', 'F', 'John Boyd Dunlop', 'His wealth is not discussed.'),
 ]),
 mcq([
  ('Why did the draisine craze fade?', ['Roads were rough and the machine was heavy.', 'It had no seat.', 'It was too slow.', 'Wheels were square.'], 0, 'B', 'the roads of the time were rough and muddy'),
  ('Why did makers enlarge the front wheel?', ['A larger wheel meant greater speed.', 'It looked better.', 'It was cheaper.', 'It was lighter.'], 0, 'C', 'a larger wheel meant greater speed'),
  ('What makes the bicycle a model of good design, according to Dr Kovac?', ['Every part has a purpose.', 'It is cheap.', 'It is fast.', 'It is old.'], 0, 'G', 'every part has a purpose'),
 ]),
 diag('Label the stages in the development of the bicycle, in order. Write ONE OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['draisine'], 'B', 'called the draisine'), (['velocipede'], 'C', 'became the velocipede'), (['penny-farthing', 'penny farthing'], 'D', 'was the penny-farthing'), (['safety bicycle', 'safety'], 'E', 'the safety bicycle'), (['pneumatic'], 'F', 'or pneumatic, tyre')], 2),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Machine', 'Detail'],
  [['Draisine', 'Invented by a German [[1]]'], ['Velocipede', 'Nicknamed the [[2]]'], ['Penny-farthing', 'A rider could be thrown over the [[3]]'], ['Safety bicycle', 'Power was carried by a [[4]]']],
  [(['baron'], 'B', 'German baron'), (['boneshaker'], 'C', 'nickname boneshaker'), (['handlebars'], 'D', 'over the handlebars'), (['chain'], 'E', 'a chain which carried power')], 1),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'The first machine was built in 1817 by a German [[1]], and it had no [[2]]. The safety bicycle used a [[3]] to carry power to the rear wheel, and the [[4]] tyre made riding more comfortable.',
  [(['baron'], 'B', 'German baron'), (['pedals'], 'B', 'no pedals'), (['chain'], 'E', 'a chain'), (['pneumatic'], 'F', 'pneumatic')], 1,
  bank=['baron', 'pedals', 'chain', 'pneumatic', 'wooden', 'iron', 'electric', 'steam']),
 multi('Which TWO improvements from the pneumatic tyre are mentioned in paragraph F?', ['It absorbed shocks from the road.', 'It reduced friction.', 'It was cheaper than iron.', 'It lasted for a century.', 'It was made of wood.'], [0, 1], [('F', 'absorbed the shocks from the road'), ('F', 'reduced friction')]),
 head(['A simple machine with a long history', 'A machine without pedals', 'A rough ride', 'Speed and danger', 'A safer design', 'Comfort on air', 'Looking ahead', 'The history of the car', 'Cycling holidays'],
  [('A', 0, 'one of the simplest and most successful machines ever invented'), ('B', 1, 'There were no pedals'), ('C', 2, 'earned the nickname boneshaker'), ('D', 3, 'they were also very dangerous'), ('E', 4, 'The breakthrough came in the 1880s'), ('F', 5, 'the air-filled, or pneumatic, tyre'), ('G', 6, 'the bicycle continued to develop')]),
 info([
  ('a reference to a fashion among wealthy young men', 'B', 'a fashion among wealthy young men'),
  ('a reference to a nickname', 'C', 'the nickname boneshaker'),
  ('a reference to racing', 'D', 'racing became popular'),
  ('a reference to new freedom for women', 'F', 'including women'),
  ('a reference to electric motors', 'G', 'electric motors'),
 ]),
 ends(['was pushed along by the rider\'s feet.', 'had a very large front wheel.', 'had a chain.', 'invented the pneumatic tyre.', 'built the first car.', 'raced in 1817.', 'lived in France.'], [
  ('The draisine', 0, 'B', 'pushed against the ground with his feet'),
  ('The penny-farthing', 1, 'D', 'front wheel might be more than a metre and a half across'),
  ('The safety bicycle', 2, 'E', 'a chain which carried power'),
  ('John Boyd Dunlop', 3, 'F', 'invented the air-filled, or pneumatic, tyre'),
 ]),
 sent(2, [
  ('Karl von Drais was a German ___.', ['baron'], 'B', 'German baron'),
  ('The velocipede appeared in the ___.', ['1860s'], 'C', 'In the 1860s'),
  ('The safety bicycle had a diamond-shaped ___.', ['frame'], 'E', 'diamond-shaped frame'),
  ('Dr Kovac is a historian of ___.', ['technology'], 'G', 'historian of technology'),
 ]),
 short(3, [
  ('What else was the draisine called?', ['the hobby horse', 'hobby horse'], 'B', 'the hobby horse'),
  ('What was Dunlop\'s profession?', ['veterinary surgeon'], 'F', 'veterinary surgeon'),
  ('What helps riders on hills today?', ['electric motors'], 'G', 'electric motors'),
 ]),
])
