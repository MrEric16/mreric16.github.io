from lib import *
from svgs import *
A = """Ibn Sina, known in Europe as Avicenna, is one of the most important scientists of the Middle Ages. He was born in the year 980 in a village near Bukhara, which at the time was one of the greatest centres of learning in the world. His father was an official, and the family was wealthy enough to give the boy the best teachers. Ibn Sina was a prodigy: according to his own account, he had memorised the Quran by the age of ten, and he had become so skilled in medicine by the age of sixteen that established doctors came to him for advice. Today he is remembered above all as a physician and a philosopher."""
B = """When Ibn Sina was about seventeen, the ruler of Bukhara fell seriously ill, and the court physicians could not cure him. The young man was called, and he succeeded. As a reward, he was allowed to use the royal library, a collection so large that, in his words, he had never seen the like of it. He read hungrily, often through the night, and he later said that he had studied the books until he knew them thoroughly. This opportunity shaped his future, and it demonstrates the importance of libraries and of rulers who support learning."""
C = """Ibn Sina's life was not peaceful. When the Samanid dynasty fell and Bukhara was conquered, he left the city and spent the rest of his life moving from court to court in Persia, working as a physician and as an adviser to rulers. He wrote at astonishing speed, sometimes at night after a day of work, and in some periods he produced several pages every day. Illness and political trouble interrupted his career, and at one point he was imprisoned for several months. He died in 1037 in the city of Hamadan, at the age of about fifty-seven."""
D = """His most important work is the Canon of Medicine, completed around 1025. It is an enormous encyclopedia in five books, which gathered the medical knowledge of the Greeks, Persians, Indians and Arabs and added his own observations. The first book describes the principles of medicine and the causes of disease; the second lists hundreds of medicines made from plants, minerals and animal products; the third and fourth cover diseases of the body from head to foot; and the fifth contains recipes for compound drugs. The book was clear and well organised, and doctors found that they could use it as a reference for a particular problem."""
E = """Ibn Sina understood many things that were not widely accepted for centuries. He noticed that certain illnesses, such as tuberculosis, pass from one person to another, and he suggested that a sick person should be kept apart from the healthy. He described the importance of diet, exercise and sleep for health. He insisted that a new medicine should be tested before it was used, and he laid down rules for the testing: the drug must be free of other influences, it must be tried on a disease that is not complicated, and it must produce the same result every time. These rules anticipate the clinical trials of modern medicine."""
F = """The Canon of Medicine was translated into Latin in the twelfth century, and for about six hundred years it was the standard textbook in the medical schools of Europe, as well as in the Islamic world. Students in Italy, France and England studied his words, and his name remained on university reading lists long after his death. The book was printed in dozens of editions after the invention of printing. Ibn Sina also wrote The Book of Healing, a vast work of philosophy and science, which discussed logic, physics, mathematics and music as well as the soul."""
G = """Dr Zarina Mirzaeva, a historian of medicine in Tashkent, says that Ibn Sina's greatest lesson is that a scientist must observe carefully and think freely. In Bukhara, a statue and a museum honour his memory. The ordinary habits he recommended, such as moderate eating and regular exercise, are what doctors recommend today. Yet Dr Mirzaeva reminds students that Ibn Sina was also a hard worker, who sat for long hours with his books, and she says that genius without effort would never have produced the Canon. She hopes that young people will read his works, in translation if necessary, and learn from his curiosity."""
P = passage('p78', 'Ibn Sina and the Canon of Medicine', 'History of science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Ibn Sina was born near Bukhara.', 'T', 'A', 'near Bukhara'),
  ('He was born in the year 980.', 'T', 'A', 'in the year 980'),
  ('He was a skilled doctor by the age of sixteen.', 'T', 'A', 'by the age of sixteen'),
  ('The court physicians cured the ruler of Bukhara.', 'F', 'B', 'court physicians could not cure him'),
  ('Ibn Sina died in Bukhara.', 'F', 'C', 'died in 1037 in the city of Hamadan'),
  ('The Canon of Medicine has five books.', 'T', 'D', 'five books'),
  ('Ibn Sina suggested that sick people should be kept apart.', 'T', 'E', 'kept apart from the healthy'),
  ('The Canon was a standard textbook in Europe for about six hundred years.', 'T', 'F', 'for about six hundred years'),
  ('Ibn Sina wrote poetry in Latin.', 'NG', 'F', 'Ibn Sina also wrote The Book of Healing', 'Poetry is not mentioned.'),
 ]),
 mcq([
  ('What reward did Ibn Sina receive?', ['Gold.', 'Use of the royal library.', 'A palace.', 'A title.'], 1, 'B', 'allowed to use the royal library'),
  ('Why could doctors use the Canon easily?', ['It was short.', 'It was clear and well organised.', 'It was in pictures.', 'It was free.'], 1, 'D', 'clear and well organised'),
  ('What does Dr Mirzaeva say about genius?', ['It needs effort.', 'It is rare.', 'It is lucky.', 'It is quick.'], 0, 'G', 'genius without effort would never have produced the Canon'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Ibn Sina cured the ruler of [[1]].', 'He was allowed to use the royal [[2]].', 'He left the city when the Samanid [[3]] fell.', 'He died in the city of [[4]].'],
  [(['bukhara'], 'B', 'ruler of Bukhara'), (['library'], 'B', 'royal library'), (['dynasty'], 'C', 'Samanid dynasty fell'), (['hamadan'], 'C', 'city of Hamadan')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Book', 'Contents'],
  [['Book one', 'Principles of medicine and causes of [[1]]'], ['Book two', 'Hundreds of [[2]]'], ['Book five', 'Recipes for compound [[3]]'], ['Book of Healing', 'Philosophy and [[4]]']],
  [(['disease'], 'D', 'causes of disease'), (['medicines'], 'D', 'hundreds of medicines'), (['drugs'], 'D', 'compound drugs'), (['science'], 'F', 'philosophy and science')], 1),
 feat('Match each statement with the correct period, A to D.', ['Early life', 'Wandering years', 'The Canon of Medicine', 'Later fame'], [
  ('He memorised the Quran by the age of ten.', 0, 'A', 'memorised the Quran by the age of ten'),
  ('He was imprisoned for several months.', 1, 'C', 'imprisoned for several months'),
  ('It was completed around 1025.', 2, 'D', 'completed around 1025'),
  ('It was printed in dozens of editions.', 3, 'F', 'dozens of editions'),
 ]),
 multi('Which TWO rules for testing a medicine are mentioned in paragraph E?', ['The drug must be free of other influences.', 'It must produce the same result every time.', 'It must be sweet.', 'It must be given to children.', 'It must be tried on animals only.'], [0, 1], [('E', 'free of other influences'), ('E', 'the same result every time')]),
 head(['A gifted boy', 'A cure and a library', 'Years of movement', 'An encyclopedia in five books', 'Ideas ahead of their time', 'Six centuries of influence', 'Lessons for today', 'The history of surgery', 'Travel in Persia'],
  [('A', 0, 'Ibn Sina was a prodigy'), ('B', 1, 'allowed to use the royal library'), ('C', 2, 'moving from court to court'), ('D', 3, 'an enormous encyclopedia in five books'), ('E', 4, 'not widely accepted for centuries'), ('F', 5, 'the standard textbook in the medical schools of Europe'), ('G', 6, 'a scientist must observe carefully and think freely')]),
 info([
  ('a reference to reading through the night', 'B', 'often through the night'),
  ('a reference to writing at speed', 'C', 'astonishing speed'),
  ('a list of sources of medicines', 'D', 'plants, minerals and animal products'),
  ('a reference to tuberculosis', 'E', 'tuberculosis'),
  ('a reference to physics and music', 'F', 'physics, mathematics and music'),
 ]),
 ends(['rewarded Ibn Sina with the library.', 'wrote at astonishing speed.', 'was translated into Latin.', 'honour him in Bukhara.', 'was written in Greek.', 'cured every disease.', 'was lost.'], [
  ('The ruler of Bukhara', 0, 'B', 'allowed to use the royal library'),
  ('Ibn Sina', 1, 'C', 'astonishing speed'),
  ('The Canon', 2, 'F', 'translated into Latin'),
  ('A statue and a museum', 3, 'G', 'honour his memory'),
 ]),
 sent(2, [
  ('Ibn Sina is known in Europe as ___.', ['avicenna'], 'A', 'Avicenna'),
  ('The Canon of Medicine was completed around ___.', ['1025'], 'D', 'around 1025'),
  ('Ibn Sina suggested that sick people should be kept ___ from the healthy.', ['apart'], 'E', 'kept apart'),
  ('Dr Mirzaeva is a historian of ___.', ['medicine'], 'G', 'historian of medicine'),
 ]),
 short(3, [
  ('How old was Ibn Sina when he died?', ['about fifty-seven', 'fifty-seven'], 'C', 'about fifty-seven'),
  ('What did the first book of the Canon describe?', ['principles of medicine'], 'D', 'principles of medicine'),
  ('Where did Ibn Sina die?', ['hamadan'], 'C', 'Hamadan'),
 ]),
])
