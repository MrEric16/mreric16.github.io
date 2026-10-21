from lib import *
from svgs import *
A = """Choosing which foreign languages to teach is a difficult decision for any school, because the interests of students, the needs of employers and the supply of teachers all change over time. At Hillcrest Lyceum, in the imaginary country of Altonia, the head of languages has kept records of the number of students studying each of four languages over the last ten years. The records show four contrasting trends, and the head believes that they reveal as much about the world outside the school as about the school itself. This passage describes the trends and the explanations that teachers and students have offered for them."""
B = """English shows the clearest pattern of growth. Ten years ago, about a third of the students chose it, but the proportion has grown steadily every year, and today almost nine students in ten study it. Students give practical reasons: English is the language of the internet, of science and of international business, and certificates such as IELTS and TOEFL are required by universities abroad. The lyceum has responded by adding extra classes in the afternoon, and by employing two teachers who are native speakers. Even so, the demand has grown faster than the supply, and many classes have more than thirty students."""
C = """Russian has followed the opposite course. A decade ago it was the most popular language in the lyceum, studied by almost every student, but the numbers have declined year after year. The main reason is that fewer students now need it for their future careers: many universities have changed their entrance requirements, and some employers prefer candidates with English. Teachers of Russian are worried, and they point out that it remains the language of a great literature and of many neighbouring countries. They have started clubs where students read poetry and watch films, in the hope of reviving interest in the language."""
D = """The story of German is different again. The number of students rose for the first five years, when a German company opened a factory in the region and offered jobs and scholarships to local young people. It reached its highest point in the fifth year, but then it fell as the company reduced its work and the scholarships ended. Today about as few students study German as did ten years ago. The head of languages says that this is a lesson in how quickly the demand for a language can change when it depends on a single employer."""
E = """Korean is the newest language in the lyceum, and its history is the shortest. It was introduced six years ago, after a group of students asked for lessons because they loved Korean music and films. Numbers rose quickly for three years, and then stopped rising: for the last three years they have stayed at almost exactly the same level, because the teacher can accept only a fixed number of students. A waiting list now includes dozens of names. Some teachers worry that interest in a language based on fashion may not last, while others reply that every language began as the fashion of someone."""
F = """Dr Hana Petrova, a specialist in language education, was asked to review the records. She notes that students choose a language for three kinds of reason: usefulness, enjoyment and necessity, and that the balance among them changes. English is chosen for usefulness, Korean for enjoyment, and Russian was once chosen from necessity. She recommends that the lyceum should not simply follow the fashions of the moment, but should keep a small number of classes in each language, so that interest can recover if the situation changes. Once a language is dropped, she warns, teachers leave and the knowledge is lost, and restarting a programme is far more expensive than maintaining it."""
G = """The head of languages has accepted most of her advice. Next year, the lyceum will keep all four languages and will open a fifth, Chinese, as a one-year trial. Students will be able to change their choice after the first term, and a new library of books and films will be bought for each language. The head also plans to continue the ten-year records, so that future teachers can see how the world has changed. She says that the most important lesson of the records is that a school should educate people for a future which nobody can predict exactly."""
P = passage('p75', 'Which Language Next?', 'Education', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the number of students studying each language over ten years?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('plateau'), 160, 120)], [
  ('English', 0, 'B', 'grown steadily every year'),
  ('Russian', 1, 'C', 'declined year after year'),
  ('German', 2, 'D', 'reached its highest point in the fifth year'),
  ('Korean', 3, 'E', 'stayed at almost exactly the same level'),
 ]),
 tfng([
  ('Hillcrest Lyceum is in an imaginary country.', 'T', 'A', 'imaginary country of Altonia'),
  ('The records cover ten years.', 'T', 'A', 'last ten years'),
  ('Today almost nine students in ten study English.', 'T', 'B', 'almost nine students in ten'),
  ('English classes have fewer than twenty students.', 'F', 'B', 'more than thirty students'),
  ('Russian was the most popular language ten years ago.', 'T', 'C', 'the most popular language in the lyceum'),
  ('Teachers of Russian have started clubs.', 'T', 'C', 'started clubs'),
  ('German became popular after a company opened a factory.', 'T', 'D', 'a German company opened a factory'),
  ('Korean numbers have been constant for three years.', 'T', 'E', 'for the last three years they have stayed at almost exactly the same level'),
  ('Chinese is more difficult than Korean.', 'NG', 'G', 'Chinese, as a one-year trial', 'Difficulty is not compared.'),
 ]),
 mcq([
  ('Why did Korean numbers stop rising?', ['The teacher can accept only a fixed number.', 'Students lost interest.', 'The language was dropped.', 'The books were lost.'], 0, 'E', 'the teacher can accept only a fixed number of students'),
  ('What caused the fall in German?', ['A new teacher.', 'The company reduced its work and scholarships ended.', 'A fire.', 'A new law.'], 1, 'D', 'the company reduced its work and the scholarships ended'),
  ('What does Dr Petrova recommend?', ['Keep small classes in each language.', 'Teach only English.', 'Close Russian.', 'Follow fashions.'], 0, 'F', 'keep a small number of classes in each language'),
 ]),
 feat('Match each statement with the correct language, A to D.', ['English', 'Russian', 'German', 'Korean'], [
  ('Universities abroad require certificates in it.', 0, 'B', 'required by universities abroad'),
  ('Clubs read poetry and watch films.', 1, 'C', 'read poetry and watch films'),
  ('Scholarships ended.', 2, 'D', 'the scholarships ended'),
  ('There is a waiting list.', 3, 'E', 'waiting list'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Language', 'Detail'],
  [['English', 'Taught by two native [[1]]'], ['Russian', 'A language of a great [[2]]'], ['German', 'A company opened a [[3]]'], ['Korean', 'Introduced after students loved Korean [[4]]']],
  [(['speakers'], 'B', 'native speakers'), (['literature'], 'C', 'great literature'), (['factory'], 'D', 'opened a factory'), (['music'], 'E', 'Korean music and films')], 1),
 multi('Which TWO changes will the lyceum make next year, according to paragraph G?', ['Open a trial class in Chinese.', 'Allow students to change their choice after the first term.', 'Close the German classes.', 'Employ more native speakers.', 'Stop the records.'], [0, 1], [('G', 'open a fifth, Chinese, as a one-year trial'), ('G', 'change their choice after the first term')]),
 head(['Choosing languages', 'A rising tide', 'A language in decline', 'A boom and a bust', 'A newcomer reaches a ceiling', 'Why students choose', 'A plan for the future', 'The history of writing', 'Learning to cook'],
  [('A', 0, 'Choosing which foreign languages to teach is a difficult decision'), ('B', 1, 'the proportion has grown steadily every year'), ('C', 2, 'the numbers have declined year after year'), ('D', 3, 'It reached its highest point in the fifth year, but then it fell'), ('E', 4, 'stopped rising'), ('F', 5, 'usefulness, enjoyment and necessity'), ('G', 6, 'will keep all four languages')]),
 info([
  ('a reference to extra afternoon classes', 'B', 'extra classes in the afternoon'),
  ('a reference to changed entrance requirements', 'C', 'changed their entrance requirements'),
  ('a lesson about depending on one employer', 'D', 'depends on a single employer'),
  ('a worry that fashion may not last', 'E', 'may not last'),
  ('a reference to a trial', 'G', 'one-year trial'),
 ]),
 ends(['is needed for university certificates.', 'point out its great literature.', 'reduced its work.', 'will open a trial class in Chinese.', 'closed the lyceum.', 'teaches Korean.', 'built a library.'], [
  ('English', 0, 'B', 'certificates such as IELTS and TOEFL'),
  ('Teachers of Russian', 1, 'C', 'language of a great literature'),
  ('The German company', 2, 'D', 'reduced its work'),
  ('The head of languages', 3, 'G', 'open a fifth, Chinese, as a one-year trial'),
 ]),
 sent(2, [
  ('The head of languages has kept records for ___ years.', ['ten', '10'], 'A', 'last ten years'),
  ('English is the language of the internet, science and international ___.', ['business'], 'B', 'international business'),
  ('Dr Petrova is a specialist in language ___.', ['education'], 'F', 'language education'),
  ('Restarting a programme is far more ___ than maintaining it.', ['expensive'], 'F', 'far more expensive'),
 ]),
 short(3, [
  ('How many native-speaker teachers does the lyceum employ?', ['two'], 'B', 'two teachers who are native speakers'),
  ('Why did students ask for Korean lessons?', ['music and films', 'korean music'], 'E', 'Korean music and films'),
  ('Which language will be a one-year trial?', ['chinese'], 'G', 'Chinese, as a one-year trial'),
 ]),
])
