from lib import *
A = """There are now more than a billion bicycles in the world, and few machines have changed so little in more than a century. Yet the bicycle took a long time to arrive. Its earliest ancestor appeared in 1817, when a German baron named Karl von Drais built a wooden machine with two wheels, a seat and a steering bar. It had no pedals. The rider simply pushed against the ground with his feet, rather like a child on a scooter, and the machine was nicknamed the hobby horse."""
B = """In the 1860s, inventors in France added pedals directly to the front wheel. This machine, called the velocipede, was much faster, but it was far from comfortable. Its wheels were made of wood and had iron rims, and on the rough roads of the time the rider was shaken so badly that people called it the boneshaker. It was popular for a few years with young, wealthy men, but most people considered it an expensive toy."""
C = """The next step was to increase the size of the front wheel. Because one turn of the pedals moved the machine a distance equal to the circumference of the front wheel, a bigger wheel meant a higher speed. By the 1870s, riders were perched on seats more than a metre above the ground on machines with front wheels over a metre and a half across. These high-wheelers, later nicknamed penny-farthings, were fast but dangerous. If the front wheel struck a stone, the rider was often thrown forward over the handlebars, and serious injuries were common."""
D = """The machine that we recognise today appeared in 1885, when an English maker named John Kemp Starley produced the Rover safety bicycle. It had two wheels of equal size, and the pedals drove the rear wheel through a chain, which meant that the rider could sit low and stay close to the ground. A few years later, in 1888, a Scottish vet named John Boyd Dunlop fitted his son's tricycle with tyres filled with air. They made the ride far smoother, and within a decade almost every bicycle used them."""
E = """The safety bicycle changed society as well as transport. It was cheap enough for workers to buy, so people could live farther from their jobs. It was especially important for women, who had little freedom to travel alone. The American campaigner Susan B. Anthony declared in the 1890s that the bicycle had done more for women's freedom than anything else in the world. Women began to wear shorter skirts and looser clothes so that they could ride, and clubs for cyclists sprang up in towns across Europe and America."""
F = """In the twentieth century the car pushed the bicycle to the edge of city life in many countries. It returned in the 1970s, when a sharp rise in oil prices made driving expensive, and its popularity has continued to grow. Cities such as Copenhagen and Amsterdam have built thousands of kilometres of separate cycle lanes, and electric bicycles, which have a small motor to help the rider on hills, have made cycling possible for people who once found it too tiring."""
G = """A modern bicycle is a simple machine. The rider sits on the saddle, steers with the handlebars and pushes the pedals. The pedals turn a chain, which drives the rear wheel. All the parts are held together by the frame, a diamond of light steel or aluminium tubes that is both strong and easy to repair. It is this simplicity, together with the fact that the rider supplies all the power, that makes the bicycle the most efficient means of transport ever invented."""
SVG = ('<circle class="l" cx="130" cy="170" r="55"/><circle class="l" cx="390" cy="170" r="55"/><circle class="l" cx="130" cy="170" r="5"/><circle class="l" cx="390" cy="170" r="5"/>'
 '<path class="l" d="M130 170L235 170L210 100L130 170M210 100L340 100L235 170M340 100L390 170M340 100L333 78L362 72"/>'
 '<path class="l" d="M190 92H232" style="stroke-width:7"/>'
 '<path class="l" d="M130 160L235 160M130 180L235 180M235 170L262 196"/><rect class="c" x="252" y="192" width="22" height="9" rx="2"/><circle class="l" cx="235" cy="170" r="14"/>'
 '<path class="l" d="M210 92V100M275 100V56M362 72V50M262 196L285 232M182 180V234"/>')
SVG = SVG.replace('M210 92V100M275 100V56M362 72V50M262 196L285 232M182 180V234','M210 90L195 55M275 100V56M362 72L385 52M274 200L295 233M182 180V232')
P = passage('p11', 'How the Bicycle Evolved', 'Technology', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The world now has more than a billion bicycles.', 'T', 'A', 'more than a billion bicycles'),
  ('Von Drais\'s machine had pedals on the front wheel.', 'F', 'A', 'It had no pedals'),
  ('The velocipede was invented in Germany.', 'F', 'B', 'inventors in France added pedals directly to the front wheel'),
  ('The velocipede was comfortable to ride on rough roads.', 'F', 'B', 'the rider was shaken so badly'),
  ('The velocipede was popular with people of every income.', 'F', 'B', 'popular for a few years with young, wealthy men'),
  ('A bigger front wheel gave a higher speed for each turn of the pedals.', 'T', 'C', 'a bigger wheel meant a higher speed'),
  ('Penny-farthings were nicknamed after two coins.', 'NG', 'C', 'later nicknamed penny-farthings', 'The passage gives the nickname but does not explain it.'),
  ('The Rover safety bicycle had wheels of the same size.', 'T', 'D', 'two wheels of equal size'),
  ('Dunlop first tested his tyres on a racing bicycle.', 'F', 'D', 'fitted his son\'s tricycle with tyres filled with air'),
  ('Cycling clubs were formed in both Europe and America.', 'T', 'E', 'clubs for cyclists sprang up in towns across Europe and America'),
  ('Electric bicycles are more expensive than ordinary bicycles.', 'NG', 'F', 'electric bicycles, which have a small motor to help the rider on hills', 'Prices are not mentioned.'),
 ]),
 feat('Which type of bicycle does each statement describe? You may use any letter more than once.', ['The hobby horse', 'The velocipede', 'The high-wheeler', 'The safety bicycle'], [
  ('The rider pushed against the ground with his feet.', 0, 'A', 'The rider simply pushed against the ground with his feet'),
  ('It had pedals attached to the front wheel.', 1, 'B', 'added pedals directly to the front wheel'),
  ('It was named for the way it shook its rider.', 1, 'B', 'people called it the boneshaker'),
  ('The rider sat more than a metre above the ground.', 2, 'C', 'more than a metre above the ground'),
  ('It used a chain to drive the rear wheel.', 3, 'D', 'the pedals drove the rear wheel through a chain'),
  ('Many riders were injured by falling over the handlebars.', 2, 'C', 'thrown forward over the handlebars'),
 ], cls=True),
 mcq([
  ('Why was a larger front wheel used on high-wheelers?', ['It made the ride more comfortable.', 'It made the machine travel faster.', 'It made the machine easier to steer.', 'It allowed the use of a chain.'], 1, 'C', 'a bigger wheel meant a higher speed'),
  ('What was the main advantage of the pneumatic tyre?', ['It was cheaper than iron.', 'It made the bicycle lighter.', 'It made riding smoother.', 'It lasted longer on rough roads.'], 2, 'D', 'They made the ride far smoother'),
  ('Why did bicycle use increase again in the 1970s?', ['Cycle lanes were built.', 'The price of oil rose sharply.', 'Electric motors were invented.', 'Bicycles became cheaper than cars.'], 1, 'F', 'a sharp rise in oil prices made driving expensive'),
 ]),
 head(['The first machine with two wheels', 'A faster but painful ride', 'Bigger wheels, bigger risks', 'The design that lasted', 'A new freedom for women and workers', 'A return after the age of the car', 'The best-known cycling races', 'Why bicycles are safer than cars'],
  [('A', 0, 'Its earliest ancestor appeared in 1817'), ('B', 1, 'it was far from comfortable'), ('C', 2, 'fast but dangerous'), ('D', 3, 'The machine that we recognise today appeared in 1885'), ('E', 4, 'The safety bicycle changed society as well as transport'), ('F', 5, 'It returned in the 1970s')]),
 info([
  ('the name of the first inventor of a two-wheeled machine', 'A', 'a German baron named Karl von Drais'),
  ('a reason why the velocipede was called the boneshaker', 'B', 'the rider was shaken so badly'),
  ('a description of the danger of high-wheelers', 'C', 'thrown forward over the handlebars'),
  ('a person who put air-filled tyres on his son\'s tricycle', 'D', 'a Scottish vet named John Boyd Dunlop'),
  ('a comment on how cheap safety bicycles were', 'E', 'cheap enough for workers to buy'),
  ('a description of the material of a modern frame', 'G', 'a diamond of light steel or aluminium tubes'),
 ]),
 sent(2, [
  ('Karl von Drais\'s machine was nicknamed the ___.', ['hobby horse'], 'A', 'nicknamed the hobby horse'),
  ('The wheels of the velocipede had ___ rims.', ['iron'], 'B', 'wood and had iron rims'),
  ('Riders of high-wheelers were often thrown over the ___.', ['handlebars'], 'C', 'over the handlebars'),
  ('Dunlop was a Scottish ___.', ['vet'], 'D', 'a Scottish vet'),
  ('Women began to wear ___ skirts so that they could ride.', ['shorter'], 'E', 'shorter skirts and looser clothes'),
  ('Amsterdam has built thousands of kilometres of separate ___ lanes.', ['cycle'], 'F', 'separate cycle lanes'),
 ]),
 short(3, [
  ('In which year did the Rover safety bicycle appear?', ['1885'], 'D', 'appeared in 1885'),
  ('What helps the rider of an electric bicycle on hills?', ['a small motor', 'small motor', 'motor'], 'F', 'a small motor to help the rider on hills'),
  ('Who said that the bicycle had done more for women\'s freedom than anything else?', ['susan b. anthony', 'susan b anthony', 'susan anthony', 'anthony'], 'E', 'Susan B. Anthony declared'),
  ('What supplies all the power for a bicycle?', ['the rider', 'rider'], 'G', 'the rider supplies all the power'),
 ]),
 table('Complete the table. Write ONE WORD ONLY from the passage for each answer.', ['Machine', 'Description'],
  [['Hobby horse', 'Had a [[1]] and a steering bar but no pedals'], ['Velocipede', 'Had pedals fixed to the [[2]] wheel'], ['High-wheeler', 'Had a [[3]] front wheel than the velocipede, for more speed'], ['Safety bicycle', 'Had a [[4]] to drive the rear wheel']],
  [(['seat'], 'A', 'two wheels, a seat and a steering bar'), (['front'], 'B', 'pedals directly to the front wheel'), (['large', 'big', 'bigger'], 'C', 'increase the size of the front wheel'.replace('increase the size of the front wheel', 'a bigger wheel')), (['chain'], 'D', 'through a chain')], 1),
 diag('Label the diagram of a bicycle. Write ONE WORD ONLY from the passage for each answer.', 520, 260, SVG, [[195, 50], [275, 48], [385, 46], [295, 245], [182, 245]],
  [(['saddle'], 'G', 'sits on the saddle'), (['frame'], 'G', 'held together by the frame'), (['handlebars'], 'G', 'steers with the handlebars'), (['pedals', 'pedal'], 'G', 'pushes the pedals'), (['chain'], 'G', 'turn a chain')], 1),
])
