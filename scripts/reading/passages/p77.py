from lib import *
from svgs import *
A = """Few words in the modern world are used as often as algorithm and algebra, and both come from a single man who lived more than twelve hundred years ago. Muhammad ibn Musa al-Khwarizmi was a mathematician, astronomer and geographer, and he is often called the father of algebra. He was born around the year 780, probably in Khwarazm, a region which today lies partly in Uzbekistan, and the name al-Khwarizmi simply means from Khwarazm. Little is known about his private life, but his work was so influential that it shaped the way in which people in many countries have calculated ever since."""
B = """Al-Khwarizmi spent most of his career in Baghdad, then the largest city in the world and the capital of the Islamic empire. The ruler, Caliph al-Ma'mun, had founded a great centre of learning, known as the House of Wisdom, where scholars gathered from many countries to translate Greek, Persian and Indian books into Arabic and to carry out new research. Al-Khwarizmi worked there as a scholar, supported by the Caliph, and he studied mathematics, astronomy and geography. The House of Wisdom produced a flood of discoveries, and historians sometimes call this period the Golden Age of Islamic science."""
C = """His most famous book was written around the year 820, with the title The Compendious Book on Calculation by Completion and Balancing. Its purpose was practical: the Caliph wanted a guide to the problems that ordinary people faced, such as dividing an inheritance, measuring land and calculating the amount of a tax. Al-Khwarizmi showed how such problems could be turned into equations and solved by clear, step-by-step rules. He described six types of equation, and for each he explained a method of solution, using diagrams to show why the method worked. The book contained no symbols; the equations were written in words, and the reader had to follow the argument in sentences."""
D = """The word algebra comes from the title of the book. In Arabic, the process of completion, which means moving a quantity from one side of an equation to the other, was called al-jabr. When the book was translated into Latin in the twelfth century, the word became algebra, and it has been used in this sense in European languages ever since. The second part of the title, balancing, refers to the idea that an equation must remain balanced like a pair of scales: whatever is done to one side must be done to the other. This simple principle, which students learn at school today, is the foundation of all algebra."""
E = """Al-Khwarizmi also wrote a book explaining the number system that had been invented in India, with the nine digits and zero. Before it, many people used Roman numerals or counting boards, which made large calculations slow and difficult. The Latin translation of the book, which began with the words Dixit Algorismi, meaning Al-Khwarizmi said, spread the new numbers across Europe. His name, in its Latin form Algorismi, became the word algorithm, which today means any set of step-by-step rules for solving a problem, from a recipe to the programs in a computer."""
F = """His interests were wide. He compiled astronomical tables, which gave the positions of the sun, moon and planets, and they were used by astronomers for centuries. He also wrote a work on geography, listing the coordinates of hundreds of cities and rivers, and he helped to prepare a map of the known world for the Caliph. Some historians believe that he took part in an expedition to measure the size of the Earth. Dr Farida Yusupova, a historian of mathematics, says that his greatest gift was clarity: he took ideas that were scattered and complicated and presented them in a form that anybody could use."""
G = """Today al-Khwarizmi is remembered in many ways. A statue of him stands in the old city of Khiva, near the place where he is thought to have been born, and a university in Urgench carries his name. Dr Yusupova points out that every time someone solves an equation, searches the internet or follows a recipe, he or she is using an idea that goes back to the scholar of Khwarazm. She hopes that young people in Central Asia will take pride in this heritage, and she adds that the best way to honour him is not to admire his statue but to study the subject that he loved."""
P = passage('p77', 'Al-Khwarizmi and the Birth of Algebra', 'History of science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Algebra and algorithm both come from the work of al-Khwarizmi.', 'T', 'A', 'come from a single man'),
  ('Al-Khwarizmi was born around the year 780.', 'T', 'A', 'around the year 780'),
  ('Khwarazm lies partly in Uzbekistan today.', 'T', 'A', 'partly in Uzbekistan'),
  ('Baghdad was then the largest city in the world.', 'T', 'B', 'the largest city in the world'),
  ('The House of Wisdom translated books into Arabic.', 'T', 'B', 'into Arabic'),
  ('His famous book was written for scholars only.', 'F', 'C', 'ordinary people faced'),
  ('The book contained many symbols.', 'F', 'C', 'contained no symbols'),
  ('The word algebra comes from al-jabr.', 'T', 'D', 'al-jabr'),
  ('Al-Khwarizmi had many children.', 'NG', 'A', 'Little is known about his private life', 'His family is not mentioned.'),
 ]),
 mcq([
  ('What was the purpose of his famous book?', ['To solve practical problems of ordinary people.', 'To teach Greek.', 'To describe animals.', 'To map the stars.'], 0, 'C', 'a guide to the problems that ordinary people faced'),
  ('What does balancing refer to?', ['An equation must remain balanced.', 'A diet.', 'A scale of music.', 'A tax.'], 0, 'D', 'an equation must remain balanced'),
  ('What problem did Roman numerals cause?', ['Large calculations were slow and difficult.', 'They were secret.', 'They had no zero.', 'They were too small.'], 0, 'E', 'made large calculations slow and difficult'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The Latin translation of his book began with the words Dixit [[1]].', 'The Latin form of his name became the word [[2]].', 'The word algebra comes from al-[[3]].', 'The book was translated into Latin in the [[4]] century.'],
  [(['algorismi'], 'E', 'Dixit Algorismi'), (['algorithm'], 'E', 'became the word algorithm'), (['jabr'], 'D', 'al-jabr'), (['twelfth'], 'D', 'in the twelfth century')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Work', 'Detail'],
  [['Book on calculation', 'Written around the year [[1]]'], ['Book on numbers', 'Explained the system invented in [[2]]'], ['Astronomical tables', 'Gave positions of the sun, moon and [[3]]'], ['Geography', 'Listed coordinates of hundreds of [[4]]']],
  [(['820'], 'C', 'around the year 820'), (['india'], 'E', 'invented in India'), (['planets'], 'F', 'moon and planets'), (['cities'], 'F', 'cities and rivers')], 1),
 feat('Match each statement with the correct person or place, A to D.', ['Caliph al-Ma\'mun', 'Al-Khwarizmi', 'Dr Yusupova', 'The House of Wisdom'], [
  ('It was a centre of learning where scholars translated books.', 3, 'B', 'a great centre of learning'),
  ('He wanted a guide to practical problems.', 0, 'C', 'the Caliph wanted a guide'),
  ('She believes his greatest gift was clarity.', 2, 'F', 'his greatest gift was clarity'),
  ('He compiled astronomical tables.', 1, 'F', 'compiled astronomical tables'),
 ]),
 multi('Which TWO practical problems are mentioned in paragraph C?', ['Dividing an inheritance.', 'Measuring land.', 'Building ships.', 'Making maps.', 'Predicting weather.'], [0, 1], [('C', 'dividing an inheritance'), ('C', 'measuring land')]),
 head(['Words we still use', 'A city of learning', 'A book of practical solutions', 'The origin of a word', 'Numbers and a new word', 'A wide range of interests', 'A heritage to be proud of', 'The history of the compass', 'Persian poetry'],
  [('A', 0, 'Few words in the modern world are used as often as algorithm and algebra'), ('B', 1, 'a great centre of learning'), ('C', 2, 'a guide to the problems that ordinary people faced'), ('D', 3, 'The word algebra comes from the title of the book'), ('E', 4, 'became the word algorithm'), ('F', 5, 'His interests were wide'), ('G', 6, 'Today al-Khwarizmi is remembered in many ways')]),
 info([
  ('a reference to the meaning of his name', 'A', 'means from Khwarazm'),
  ('a reference to support from the ruler', 'B', 'supported by the Caliph'),
  ('a reference to the use of diagrams', 'C', 'using diagrams'),
  ('a comparison with scales', 'D', 'pair of scales'),
  ('a reference to Roman numerals', 'E', 'Roman numerals'),
 ]),
 ends(['founded the House of Wisdom.', 'contained no symbols.', 'comes from his name.', 'carries his name.', 'was built in Baghdad.', 'was written in Latin.', 'uses Roman numerals.'], [
  ('Caliph al-Ma\'mun', 0, 'B', 'had founded a great centre of learning'),
  ('The book on calculation', 1, 'C', 'contained no symbols'),
  ('The word algorithm', 2, 'E', 'His name, in its Latin form'),
  ('A university in Urgench', 3, 'G', 'carries his name'),
 ]),
 sent(2, [
  ('Al-Khwarizmi is often called the father of ___.', ['algebra'], 'A', 'father of algebra'),
  ('The House of Wisdom was in ___.', ['baghdad'], 'B', 'in Baghdad'),
  ('He described ___ types of equation.', ['six', '6'], 'C', 'six types of equation'),
  ('Dr Yusupova is a historian of ___.', ['mathematics'], 'F', 'historian of mathematics'),
 ]),
 short(3, [
  ('What were the equations written in?', ['words'], 'C', 'written in words'),
  ('Where does a statue of him stand?', ['khiva'], 'G', 'old city of Khiva'),
  ('What does Dixit Algorismi mean?', ['al-khwarizmi said'], 'E', 'Al-Khwarizmi said'),
 ]),
])
