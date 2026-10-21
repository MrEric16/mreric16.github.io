from lib import *
from svgs import *
A = """Every year the teachers of Riverbank College, an imaginary school, compare the average marks that pupils receive in four subjects: mathematics, history, science and art. The marks over the last four years show a number of interesting patterns. This passage describes them and offers some possible explanations. It also asks whether the changes are a reason for celebration or for concern, and what the school should do next to improve the results in every subject. The figures are averages for about four hundred pupils in each year, so a small change in the marks of a few pupils is unlikely to have much effect on the pattern."""
B = """In mathematics, the average mark has risen each year. Four years ago, it was well below the other subjects, but a new programme of weekly small-group lessons has helped weaker pupils, and the results have climbed steadily since. The head of mathematics says that the greatest improvement is among pupils who once lost confidence in the subject, and that the extra lessons have taught them to ask questions instead of hiding their difficulties."""
C = """History has moved in the opposite direction. The average mark was the highest of the four subjects at the beginning of the period, but it has fallen every year since. Teachers suggest several reasons: the course has become longer, the number of lessons has been reduced to make room for other subjects, and many pupils now prefer to read short summaries online instead of whole books. The school is considering restoring the lost lessons."""
D = """Science shows no clear change at all. The average mark has stayed at almost the same level for four years, and the differences between one year and the next are too small to be significant. Some teachers regard this stability as a sign of a mature and well-organised course. Others fear that it indicates a lack of fresh ideas, and they have asked for new equipment so that pupils can carry out more experiments for themselves."""
E = """Art follows a more unusual pattern. Marks rose sharply during the first two years, after the school opened a new studio and employed a second teacher. Since then, however, they have fallen back to roughly their previous level. The head of art believes that the first rise was due to the novelty of the new facilities, and that the second change took place because the extra teacher left and was not replaced for a full year."""
F = """What lessons can be drawn from these four cases? Dr Samira Haddad, an education researcher who has studied the school, says that marks are influenced by many factors and that it is dangerous to explain a change by a single cause. She notes that investment in a subject often leads to quick results, but that the results fade unless the investment is kept up. She recommends that the school watches the trends for several more years before it makes any large decisions."""
G = """The school has decided to follow her advice. It will keep the small-group lessons in mathematics, restore some of the lessons in history, and ask the science staff for a plan for improvement. In art, it will recruit a replacement teacher as soon as possible. The headteacher said that the aim is not to have every subject rise at the same speed, but to ensure that no pupil is left behind and that each subject has the support that it needs to flourish. Parents will be sent a short report each term, and a meeting is planned for the spring so that families can ask questions about the results and about the plans for the coming year."""
P = passage('p54', 'Marks at Riverbank College', 'Education', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which bar chart, A to D, shows the average marks over four years in each subject?', [(bars([2, 3, 4, 5]), 160, 120), (bars([5, 4, 3, 2]), 160, 120), (bars([4, 4, 4, 4]), 160, 120), (bars([2, 5, 5, 2]), 160, 120)], [
  ('mathematics', 0, 'B', 'the average mark has risen each year'),
  ('history', 1, 'C', 'it has fallen every year since'),
  ('science', 2, 'D', 'stayed at almost the same level'),
  ('art', 3, 'E', 'Marks rose sharply during the first two years'),
 ]),
 tfng([
  ('Riverbank College is a real school.', 'F', 'A', 'an imaginary school'),
  ('Mathematics marks were the lowest at the start.', 'T', 'B', 'well below the other subjects'),
  ('Small-group lessons have helped weaker pupils.', 'T', 'B', 'has helped weaker pupils'),
  ('History marks were the highest at the beginning.', 'T', 'C', 'the highest of the four subjects at the beginning'),
  ('The number of history lessons has been increased.', 'F', 'C', 'the number of lessons has been reduced'),
  ('Science marks have changed a great deal.', 'F', 'D', 'shows no clear change at all'),
  ('All the science teachers want new equipment.', 'NG', 'D', 'they have asked for new equipment', 'Only some teachers are said to have asked.'),
  ('Art marks rose after a new studio opened.', 'T', 'E', 'after the school opened a new studio'),
  ('Dr Haddad says that a single cause usually explains a change.', 'F', 'F', 'it is dangerous to explain a change by a single cause'),
 ]),
 mcq([
  ('Why has maths improved?', ['Longer exams.', 'Weekly small-group lessons.', 'A new textbook.', 'Fewer pupils.'], 1, 'B', 'weekly small-group lessons'),
  ('What may have caused the fall in art marks?', ['A teacher left and was not replaced for a year.', 'The studio closed.', 'Exams became harder.', 'Pupils lost interest.'], 0, 'E', 'the extra teacher left and was not replaced'),
  ('What does Dr Haddad recommend?', ['Large changes at once.', 'Watching trends for several more years.', 'Closing subjects.', 'Raising fees.'], 1, 'F', 'watches the trends for several more years'),
 ]),
 multi('Which TWO reasons for the fall in history marks are given in paragraph C?', ['The course has become longer.', 'The number of lessons has been reduced.', 'Teachers left.', 'Pupils missed exams.', 'The books were lost.'], [0, 1], [('C', 'the course has become longer'), ('C', 'the number of lessons has been reduced')]),
 head(['Introducing the study', 'A subject on the rise', 'A subject in decline', 'A subject that stays the same', 'A rise and a fall', 'Advice from a researcher', 'The school\'s decisions', 'The history of exams', 'How to revise'],
  [('A', 0, 'This passage describes them'), ('B', 1, 'the average mark has risen each year'), ('C', 2, 'History has moved in the opposite direction'), ('D', 3, 'Science shows no clear change at all'), ('E', 4, 'Art follows a more unusual pattern'), ('F', 5, 'What lessons can be drawn from these four cases'), ('G', 6, 'The school has decided to follow her advice')]),
 info([
  ('a reference to pupils who lost confidence', 'B', 'pupils who once lost confidence in the subject'),
  ('a reference to short summaries online', 'C', 'short summaries online'),
  ('a mention of experiments done by pupils', 'D', 'carry out more experiments for themselves'),
  ('a reference to the novelty of facilities', 'E', 'the novelty of the new facilities'),
  ('a plan to recruit a teacher', 'G', 'recruit a replacement teacher'),
 ]),
 sent(2, [
  ('Marks are compared in mathematics, history, science and ___.', ['art'], 'A', 'science and art'),
  ('The lessons in mathematics are held ___.', ['weekly'], 'B', 'weekly small-group lessons'),
  ('The school opened a new ___ in art.', ['studio'], 'E', 'a new studio'),
  ('Dr Haddad is an education ___.', ['researcher'], 'F', 'an education researcher'),
 ]),
 short(3, [
  ('What might the school restore in history?', ['the lost lessons', 'lessons'], 'C', 'restoring the lost lessons'),
  ('How long was the art post empty?', ['a full year', 'a year'], 'E', 'for a full year'),
  ('Who said the aim is that no pupil is left behind?', ['the headteacher', 'headteacher'], 'G', 'The headteacher said'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Maths marks have [[1]] each year, while history marks have fallen. Science marks have stayed at almost the [[2]] level, and art marks rose and then fell. The school will keep the small-group lessons and [[3]] some history lessons, and it will recruit a [[4]] art teacher.',
  [(['risen'], 'B', 'has risen each year'), (['same'], 'D', 'almost the same level'), (['restore'], 'G', 'restore some of the lessons'), (['replacement'], 'G', 'a replacement teacher')], 1,
  bank=['risen', 'same', 'restore', 'replacement', 'fallen', 'remove', 'new', 'cheaper']),
])
