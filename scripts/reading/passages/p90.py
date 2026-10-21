from lib import *
from svgs import *
A = """Alisher Navoi is one of the greatest figures in the literature of Central Asia. Born in 1441 in the city of Herat, now in Afghanistan, he was a poet, a statesman, a patron of the arts and a scholar, and he is remembered above all for raising the Turkic language of his time to the level of a great literary language. Today, his name is given to a city, a theatre, a state library and a prize in Uzbekistan, and his poems are learned by schoolchildren. This passage describes his life, his works and the reasons why people still read him more than five hundred years after his death."""
B = """Navoi grew up in a court family, and his father held a position at the court of the ruler of Herat. As a child he showed a gift for languages and poetry; according to tradition, he was already writing verse as a boy of fifteen. He studied in Herat and later in Samarkand and Mashhad, where he learned from famous teachers and scholars. In his youth he became friends with Husayn Bayqara, a prince who later became ruler of Herat. This friendship was to shape his career, as it brought him a position of influence when the prince took power in 1469."""
C = """For many years Navoi served as a minister at the court of Sultan Husayn. He was involved in the work of government, but he used his wealth and position to help others. He paid for the building of schools, hospitals, libraries, bridges, caravanserais and mosques, and according to historians he supported poets, painters and musicians. Many artists in Herat, including the famous miniature painter Behzad, are said to have enjoyed his protection. Navoi lived modestly himself and never married. In his later years he withdrew from public duties to devote himself to writing."""
D = """His literary output was enormous. He wrote in two languages: in Persian, under the pen name Fani, and in Chagatai, a Turkic language, under the name Navoi. His collections of lyric poetry contain thousands of verses on love, nature and the search for truth. His greatest work is the Khamsa, or Five Poems, five long poems completed in the 1480s, which tell stories of love, kingship and adventure. Among them is Layli and Majnun, an old tale of love, and Farhad and Shirin, the story of a sculptor who falls in love with a princess. Navoi was the first to write a complete Khamsa in a Turkic language."""
E = """Navoi was also a defender of his mother tongue. At that time, Persian was the language of poetry and culture at the courts of the region, and many believed that Turkic was too simple for serious literature. In a book called The Judgement of Two Languages, written near the end of his life, Navoi argued that Turkic had a rich vocabulary and was equal to Persian in every respect. He supported the claim with his own poetry, which showed what the language could do. Scholars see this work as an important step in the development of literary Uzbek, and for this reason Navoi is considered the founder of Uzbek literature."""
F = """Navoi died in Herat in 1501, at the age of about sixty, and was mourned by the whole city. After his death, his work spread far beyond Herat. Manuscripts of the Khamsa were copied by hand and illustrated with miniatures in the libraries of Persia, India, the Ottoman Empire and Central Asia. For centuries, poets imitated his style. In the twentieth century his works were printed in many editions and translated into dozens of languages, and in 1941, five hundred years after his birth, his anniversary was widely celebrated. Dr Laylo Karimova, a literary scholar in Tashkent, says that few writers have been so widely admired for so long."""
G = """Why do readers still turn to Navoi? Dr Karimova suggests three reasons. First, his poems deal with subjects which are timeless, such as love, loyalty, justice and the meaning of life. Second, the beauty of his language is such that many of his lines have become proverbs which people use in everyday speech. Third, his life offers an example of a person who held power and used it to help others. In Uzbekistan, his birthday is celebrated every February, when schools hold readings and competitions, and young people compete to recite his verses from memory."""
P = passage('p90', 'Alisher Navoi: Poet and Statesman', 'Literature and history', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Navoi was born in Herat.', 'T', 'A', 'in the city of Herat'),
  ('Navoi was born in 1441.', 'T', 'A', 'Born in 1441'),
  ('Navoi was born into a poor family of farmers.', 'F', 'B', 'a court family'),
  ('Navoi became friends with Husayn Bayqara in his youth.', 'T', 'B', 'friends with Husayn Bayqara'),
  ('Navoi never married.', 'T', 'C', 'never married'),
  ('Navoi wrote in Persian under the pen name Fani.', 'T', 'D', 'pen name Fani'),
  ('The Khamsa was completed in the 1480s.', 'T', 'D', 'completed in the 1480s'),
  ('The Judgement of Two Languages was written when Navoi was young.', 'F', 'E', 'near the end of his life'),
  ('Navoi wrote a book about astronomy.', 'NG', 'D', 'His literary output was enormous', 'Astronomy is not mentioned.'),
 ]),
 mcq([
  ('How did Navoi use his wealth?', ['He paid for schools, hospitals and libraries.', 'He bought land.', 'He built palaces.', 'He lent money.'], 0, 'C', 'schools, hospitals, libraries'),
  ('What did Navoi argue in The Judgement of Two Languages?', ['Turkic was equal to Persian.', 'Persian was better.', 'Arabic should be used.', 'Poetry was unnecessary.'], 0, 'E', 'equal to Persian in every respect'),
  ('What happened in 1941?', ['The 500th anniversary of his birth was celebrated.', 'His tomb was built.', 'The Khamsa was found.', 'A prize was created.'], 0, 'F', 'five hundred years after his birth'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Date', 'Event'],
  [['1441', 'Navoi was born in [[1]]'], ['1469', 'Husayn Bayqara took [[2]]'], ['1480s', 'The [[3]] was completed'], ['1501', 'Navoi died in [[4]]']],
  [(['herat'], 'A', 'Herat'), (['power'], 'B', 'took power'), (['khamsa'], 'D', 'Khamsa'), (['herat'], 'F', 'died in Herat')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Navoi studies in Herat, Samarkand and [[1]].', 'He becomes a [[2]] at the court of Sultan Husayn.', 'He pays for schools, hospitals and [[3]].', 'In later years he devotes himself to [[4]].'],
  [(['mashhad'], 'B', 'Mashhad'), (['minister'], 'C', 'minister'), (['libraries'], 'C', 'libraries'), (['writing'], 'C', 'writing')], 1),
 feat('Match each statement with the correct item, A to D.', ['Behzad', 'Fani', 'The Khamsa', 'Dr Karimova'], [
  ('He was a famous miniature painter.', 0, 'C', 'miniature painter'),
  ('It was Navoi\'s Persian pen name.', 1, 'D', 'pen name Fani'),
  ('It consists of five long poems.', 2, 'D', 'five long poems'),
  ('She is a literary scholar in Tashkent.', 3, 'F', 'literary scholar in Tashkent'),
 ]),
 multi('Which TWO places where Navoi studied are mentioned in paragraph B?', ['Samarkand.', 'Mashhad.', 'Baghdad.', 'Cairo.', 'Delhi.'], [0, 1], [('B', 'Samarkand'), ('B', 'Mashhad')]),
 head(['A giant of Central Asian literature', 'A gifted child at court', 'A minister who helped artists', 'Poems and the Khamsa', 'In defence of a language', 'A legacy across the world', 'Why he is still read', 'The history of Herat', 'A guide to Persian verse'],
  [('A', 0, 'one of the greatest figures'), ('B', 1, 'showed a gift for languages and poetry'), ('C', 2, 'supported poets, painters and musicians'), ('D', 3, 'His literary output was enormous'), ('E', 4, 'a defender of his mother tongue'), ('F', 5, 'spread far beyond Herat'), ('G', 6, 'Why do readers still turn to Navoi')]),
 info([
  ('a reference to a theatre named after him', 'A', 'a theatre'),
  ('a reference to a prince becoming ruler', 'B', 'became ruler of Herat'),
  ('a reference to a sculptor', 'D', 'a sculptor'),
  ('a reference to proverbs', 'G', 'become proverbs'),
  ('a reference to reciting from memory', 'G', 'recite his verses from memory'),
 ]),
 ends(['held a position at court.', 'served as a minister.', 'tells of a sculptor.', 'is celebrated every February.', 'was written in Latin.', 'was painted by Behzad.', 'was built in Herat.'], [
  ('Navoi\'s father', 0, 'B', 'held a position at the court'),
  ('Navoi', 1, 'C', 'served as a minister'),
  ('Farhad and Shirin', 2, 'D', 'a sculptor who falls in love'),
  ('His birthday', 3, 'G', 'celebrated every February'),
 ]),
 sent(2, [
  ('Navoi wrote his Turkic poetry in ___.', ['chagatai'], 'D', 'Chagatai'),
  ('The Khamsa means Five ___.', ['poems'], 'D', 'Five Poems'),
  ('Persian was the language of poetry at the ___ of the region.', ['courts'], 'E', 'courts of the region'),
  ('Dr Karimova gives ___ reasons.', ['three', '3'], 'G', 'three reasons'),
 ]),
 short(3, [
  ('How old was Navoi when he began writing verse, according to tradition?', ['fifteen'], 'B', 'fifteen'),
  ('When did Navoi die?', ['1501'], 'F', '1501'),
  ('Which languages were manuscripts translated into?', ['dozens of languages'], 'F', 'dozens of languages'),
 ]),
])
