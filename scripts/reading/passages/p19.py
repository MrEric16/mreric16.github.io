from lib import *
A = """In the first half of the fifteenth century, Samarkand was one of the great centres of learning in the world. Its ruler, Ulugh Beg, was the grandson of the conqueror Timur, but he cared far more for science than for war. He had studied mathematics and astronomy from a young age, and as ruler he invited scholars from many countries to his court, and the libraries and workshops of the city became famous across Asia. He also founded a madrasa in Samarkand, completed in 1420, where students studied mathematics and astronomy alongside religion."""
B = """Around 1420, Ulugh Beg began to build an observatory on a hill outside the city. It was one of the largest in the world at that time. Its main instrument was a giant sextant with a radius of about forty metres, built partly below ground in a trench cut into the rock and fitted with a scale of marble. The size mattered, because a larger instrument allows the observer to read smaller divisions of the scale, and so to measure angles with greater accuracy. Observers followed the Sun, the Moon and the stars as they crossed the sky, and recorded their positions night after night for many years."""
C = """With his team, which included the astronomers Qadi Zada al-Rumi and Ali Qushji, Ulugh Beg spent almost twenty years on observation. The results were gathered in a star catalogue, completed in 1437, which listed the positions of 1,018 stars. It was the first major catalogue since that of Ptolemy, written about thirteen centuries earlier, and unlike most earlier work it was based largely on new observations rather than on old ones. The catalogue became known as the Zij-i-Sultani, or the Royal Tables."""
D = """The accuracy of the work was remarkable. The team measured the length of the sidereal year at 365 days, 6 hours, 10 minutes and 8 seconds, which is wrong by less than a minute. These figures were obtained without a telescope, which was not invented for more than a century and a half. The astronomers achieved their results by careful design, by repeating each measurement many times, and by using mathematics to reduce the effect of small errors."""
E = """Scientific success did not protect Ulugh Beg. Many religious leaders disapproved of his interest in the stars, and his own son, Abd al-Latif, rose against him. In 1449 Ulugh Beg was killed on his son's orders, and the observatory soon fell into ruin. The ruler who had gathered the finest astronomers of his age died at the age of about fifty-five, and the community of scholars that he had created gradually broke up, although several of his pupils continued the work in other cities."""
F = """The catalogue, however, survived. Copies travelled to Persia, Turkey and India, and in the seventeenth century it was translated and printed in England, where European astronomers used it for many years. The observatory itself was forgotten until 1908, when a Russian archaeologist, Vasily Vyatkin, discovered the remains of the great sextant after studying an old written description of its position. Part of the underground arc can be visited today, and it is one of the most popular sites for visitors to Samarkand."""
G = """Modern historians see Ulugh Beg as evidence of a wider truth: that the centuries between the ancient Greeks and the European Renaissance were not a period of darkness for science. In the cities of Central Asia, scholars preserved the works of the Greeks, checked them against new evidence and corrected them. Dr Laylo Karimova, a historian of science, says that his work 'shows that knowledge is built by many hands in many places'. In Uzbekistan, his name is carried by schools, a university and a crater on the Moon."""
P = passage('p19', 'Ulugh Beg and the Stars of Samarkand', 'History of science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Ulugh Beg was more interested in science than in war.', 'T', 'A', 'he cared far more for science than for war'),
  ('Ulugh Beg\'s madrasa taught only religion.', 'F', 'A', 'mathematics and astronomy alongside religion'),
  ('The observatory stood inside the city walls.', 'F', 'B', 'on a hill outside the city'),
  ('A larger instrument allows smaller divisions of the scale to be read.', 'T', 'B', 'a larger instrument allows the observer to read smaller divisions of the scale'),
  ('Ptolemy\'s catalogue was written about thirteen centuries before Ulugh Beg\'s.', 'T', 'C', 'written about thirteen centuries earlier'),
  ('Ali Qushji wrote most of the catalogue.', 'NG', 'C', 'which included the astronomers Qadi Zada al-Rumi and Ali Qushji', 'The passage names him as a team member but says nothing about who wrote what.'),
  ('The team\'s measurement of the year was wrong by more than a minute.', 'F', 'D', 'wrong by less than a minute'),
  ('Ulugh Beg was killed in 1449.', 'T', 'E', 'In 1449 Ulugh Beg was killed'),
  ('The observatory was rediscovered by a Uzbek archaeologist.', 'F', 'F', 'a Russian archaeologist'),
 ]),
 mcq([
  ('Why was the sextant built so large?', ['To impress visitors.', 'To measure angles more accurately.', 'To protect it from the weather.', 'To follow the Moon only.'], 1, 'B', 'to measure angles with greater accuracy'),
  ('What made the catalogue unusual?', ['It was written in Latin.', 'It listed planets only.', 'It was based largely on new observations.', 'It was printed in Samarkand.'], 2, 'C', 'based largely on new observations'),
  ('What does Dr Karimova\'s quotation suggest?', ['Science belongs to one country.', 'Knowledge is a shared achievement.', 'Greek science was wrong.', 'Ulugh Beg worked alone.'], 1, 'G', 'knowledge is built by many hands in many places'),
 ]),
 head(['A ruler who loved science', 'An enormous instrument', 'A new map of the sky', 'Results without a telescope', 'A violent end', 'Rediscovery and legacy', 'Lessons for the history of science', 'The conquests of Timur', 'How a telescope works'],
  [('A', 0, 'he cared far more for science than for war'), ('B', 1, 'giant sextant'), ('C', 2, 'a star catalogue'), ('D', 3, 'The accuracy of the work was remarkable'), ('E', 4, 'Ulugh Beg was killed on his son\'s orders'), ('F', 5, 'The catalogue, however, survived'), ('G', 6, 'not a period of darkness for science')]),
 info([
  ('the year in which a school was completed', 'A', 'completed in 1420'),
  ('a description of the position of the instrument', 'B', 'built partly below ground in a trench'),
  ('another name for a catalogue', 'C', 'the Royal Tables'),
  ('a method used to reduce errors', 'D', 'repeating each measurement many times'),
  ('a person who found the observatory remains', 'F', 'Vasily Vyatkin'),
 ]),
 sent(2, [
  ('Ulugh Beg was the grandson of ___.', ['timur'], 'A', 'the grandson of the conqueror Timur'),
  ('The catalogue listed the positions of ___ stars.', ['1,018', '1018'], 'C', 'positions of 1,018 stars'),
  ('The team made its measurements without a ___.', ['telescope'], 'D', 'without a telescope'),
  ('The catalogue was printed in ___ in the seventeenth century.', ['england'], 'F', 'printed in England'),
 ]),
 short(3, [
  ('Who rose against Ulugh Beg?', ['his son', 'abd al-latif'], 'E', 'his own son, Abd al-Latif, rose against him'),
  ('When was the observatory remains discovered?', ['1908'], 'F', 'The observatory itself was forgotten until 1908'),
  ('What on the Moon carries his name?', ['a crater', 'crater'], 'G', 'a crater on the Moon'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Ulugh Beg builds an [[1]] on a hill outside Samarkand.', 'The team spends almost twenty years on [[2]].', 'The results are gathered in a star [[3]], completed in 1437.', 'Copies travel abroad, but the observatory falls into [[4]].'],
  [(['observatory'], 'B', 'an observatory on a hill'), (['observation'], 'C', 'almost twenty years on observation'), (['catalogue'], 'C', 'a star catalogue'), (['ruin'], 'E', 'fell into ruin')], 1),
 feat('Match each statement with the correct person, A to C.', ['Ulugh Beg', 'Abd al-Latif', 'Vasily Vyatkin'], [
  ('founded a madrasa in Samarkand', 0, 'A', 'He also founded a madrasa in Samarkand'),
  ('ordered the death of a ruler', 1, 'E', 'killed on his son\'s orders'),
  ('found the remains of the sextant', 2, 'F', 'discovered the remains of the great sextant'),
  ('invited scholars from many countries', 0, 'A', 'invited scholars from many countries'),
 ], cls=True),
])
