from lib import *
from svgs import *
A = """The Olympic Games are the largest sporting event in the world, watched by billions of people and attended by more than ten thousand athletes from over two hundred countries. Yet the modern Games are the revival of a very old tradition, and many of their customs, from the torch to the motto, show the influence of the past. The story of the Games is also a story about how attitudes have changed: who is allowed to compete, what counts as a sport and what the Games are for. This passage looks at three periods: the ancient Games, the revival in the nineteenth century and the Games of today."""
B = """The first Games, according to tradition, were held in 776 BC at Olympia, in southern Greece, and they were repeated every four years for nearly twelve centuries. They were held in honour of Zeus, the king of the gods, and they were as much a religious festival as a sporting contest. At first the only event was a short foot race; later the programme grew to include wrestling, boxing, chariot racing and the pentathlon. The competitors were free men, who trained for months and took an oath to compete fairly, and the winners received not gold but a wreath of olive leaves. Even so, their cities honoured them as heroes."""
C = """A remarkable feature of the ancient Games was the sacred truce. Before each festival, messengers travelled across the Greek world to announce that all wars must stop, so that athletes and spectators could travel safely to Olympia and home again. The truce was not always obeyed, but it was respected for centuries, and the idea that sport can create a pause in conflict is still part of the Olympic ideal. Women were not allowed to compete, and married women were forbidden to watch, though a separate festival for women, in honour of the goddess Hera, was held there."""
D = """The ancient Games ended around the year 393 AD, when a Christian emperor banned pagan festivals. They were forgotten for fifteen hundred years, until a French nobleman, Pierre de Coubertin, became convinced that sport could improve education and promote peace. He organised a congress, and in 1896 the first modern Olympic Games were held in Athens, with about two hundred and fifty athletes from fourteen nations, all of them men. The marathon was added, inspired by the legend of a messenger who ran from the battlefield of Marathon to Athens, and its victory by a Greek runner made the crowd wild with joy."""
E = """The Games grew steadily. Women first competed in 1900, in tennis and golf, and their number has increased until, at recent Games, they have made up nearly half of all athletes. The first Winter Games were held in Chamonix, France, in 1924, for sports on snow and ice. In 1960, in Rome, the first Paralympic Games were held for athletes with disabilities, and since then they have grown into a major event of their own, held in the same city shortly after the Olympics. Each Games has added new events, from beach volleyball to skateboarding, to attract young audiences."""
F = """The Games are rich in symbols. The five interlocking rings, designed by Coubertin, stand for the five inhabited continents as they were then understood, and the colours, together with the white background, include at least one colour from the flag of every nation. The motto, in Latin, is Citius, Altius, Fortius, which means Faster, Higher, Stronger. The torch is lit in Olympia by the rays of the sun and carried by relay to the host city, a custom introduced in 1936. At the opening ceremony the athletes march behind their national flags, and at the end of each event the national anthem of the winner is played."""
G = """Not everyone is pleased with the modern Games. Dr Helen Brandt, a sports historian, notes that the cost of hosting the Games has risen enormously, and that several cities have been left with empty stadiums that are expensive to maintain. There have also been scandals about doping and corruption. Yet she believes that the Games remain valuable. They give athletes a goal that inspires them to train for years, and they give ordinary people a rare moment in which countries compete without violence. She suggests that future Games should use existing buildings and be shared between several cities, to reduce costs and waste."""
S, PT, W, H = chain(4)
P = passage('p81', 'The Olympic Games Through Time', 'History', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('More than ten thousand athletes attend the Games.', 'T', 'A', 'more than ten thousand athletes'),
  ('The first ancient Games were held in 776 BC, according to tradition.', 'T', 'B', 'in 776 BC'),
  ('Winners in the ancient Games received gold.', 'F', 'B', 'not gold but a wreath of olive leaves'),
  ('The ancient Games were held every four years.', 'T', 'B', 'every four years'),
  ('Wars were supposed to stop during the sacred truce.', 'T', 'C', 'all wars must stop'),
  ('Women competed at Olympia.', 'F', 'C', 'Women were not allowed to compete'),
  ('Coubertin was a French nobleman.', 'T', 'D', 'a French nobleman'),
  ('About 250 athletes took part in 1896.', 'T', 'D', 'about two hundred and fifty athletes'),
  ('The first modern Games were broadcast on radio.', 'NG', 'D', 'the first modern Olympic Games', 'Broadcasting is not mentioned.'),
 ]),
 mcq([
  ('Why were the ancient Games held?', ['To honour Zeus.', 'To end a war.', 'To sell goods.', 'To train soldiers.'], 0, 'B', 'in honour of Zeus'),
  ('Why did Coubertin revive the Games?', ['Sport could improve education and promote peace.', 'He wanted money.', 'He liked Greek food.', 'He was a soldier.'], 0, 'D', 'sport could improve education and promote peace'),
  ('What does Dr Brandt suggest?', ['Using existing buildings and sharing the Games between cities.', 'Ending the Games.', 'Building bigger stadiums.', 'Banning doping tests.'], 0, 'G', 'use existing buildings and be shared between several cities'),
 ]),
 diag('Label the places in the history of the Games, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['olympia'], 'B', 'at Olympia'), (['athens'], 'D', 'were held in Athens'), (['chamonix'], 'E', 'in Chamonix'), (['rome'], 'E', 'in Rome')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Messengers announce the sacred [[1]].', 'Athletes travel safely to [[2]].', 'Winners receive a wreath of olive [[3]].', 'Their cities honour them as [[4]].'],
  [(['truce'], 'C', 'sacred truce'), (['olympia'], 'C', 'safely to Olympia'), (['leaves'], 'B', 'olive leaves'), (['heroes'], 'B', 'as heroes')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Year', 'Event'],
  [['1896', 'The first modern Games, held in [[1]]'], ['1900', 'Women first [[2]]'], ['1924', 'The first [[3]] Games'], ['1936', 'The torch [[4]] was introduced']],
  [(['athens'], 'D', 'held in Athens'), (['competed'], 'E', 'Women first competed'), (['winter'], 'E', 'first Winter Games'), (['relay'], 'F', 'carried by relay')], 1),
 feat('Match each statement with the correct event, A to D.', ['The ancient Games', 'The 1896 Games', 'The Winter Games', 'The Paralympic Games'], [
  ('Competitors took an oath to compete fairly.', 0, 'B', 'took an oath to compete fairly'),
  ('The marathon was added.', 1, 'D', 'The marathon was added'),
  ('They began in Chamonix.', 2, 'E', 'Chamonix, France'),
  ('They are held shortly after the Olympics.', 3, 'E', 'shortly after the Olympics'),
 ]),
 multi('Which TWO events of the ancient Games are mentioned in paragraph B?', ['Wrestling.', 'Boxing.', 'Swimming.', 'Football.', 'Tennis.'], [0, 1], [('B', 'wrestling'), ('B', 'boxing')]),
 head(['A global festival with ancient roots', 'Honouring the gods', 'A pause in war', 'A dream revived', 'A growing programme', 'Signs and symbols', 'Costs and hopes', 'The history of football', 'Training for a marathon'],
  [('A', 0, 'the revival of a very old tradition'), ('B', 1, 'in honour of Zeus'), ('C', 2, 'all wars must stop'), ('D', 3, 'the first modern Olympic Games were held in Athens'), ('E', 4, 'Each Games has added new events'), ('F', 5, 'The Games are rich in symbols'), ('G', 6, 'Not everyone is pleased with the modern Games')]),
 info([
  ('a reference to an oath', 'B', 'took an oath'),
  ('a reference to a festival for women', 'C', 'festival for women'),
  ('a reference to a legend of a messenger', 'D', 'legend of a messenger'),
  ('a reference to new events aimed at young audiences', 'E', 'beach volleyball to skateboarding'),
  ('a reference to unused stadiums', 'G', 'empty stadiums'),
 ]),
 ends(['were held in honour of Zeus.', 'organised a congress.', 'is lit by the rays of the sun.', 'suggests sharing the Games between cities.', 'banned the Games.', 'invented the marathon.', 'won in 1896.'], [
  ('The ancient Games', 0, 'B', 'in honour of Zeus'),
  ('Pierre de Coubertin', 1, 'D', 'organised a congress'),
  ('The torch', 2, 'F', 'lit in Olympia by the rays of the sun'),
  ('Dr Brandt', 3, 'G', 'shared between several cities'),
 ]),
 sent(2, [
  ('The ancient Games were held at ___.', ['olympia'], 'B', 'at Olympia'),
  ('The Latin motto is Citius, Altius, ___.', ['fortius'], 'F', 'Fortius'),
  ('The five rings stand for the five inhabited ___.', ['continents'], 'F', 'inhabited continents'),
  ('Dr Brandt is a sports ___.', ['historian'], 'G', 'sports historian'),
 ]),
 short(3, [
  ('Who founded the modern Games?', ['pierre de coubertin', 'coubertin'], 'D', 'Pierre de Coubertin'),
  ('In which year did women first compete?', ['1900'], 'E', 'in 1900'),
  ('What does the Latin motto mean?', ['faster, higher, stronger', 'faster higher stronger'], 'F', 'Faster, Higher, Stronger'),
 ]),
])
