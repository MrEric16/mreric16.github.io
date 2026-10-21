from lib import *
A = """Before the fifteenth century, every book in Europe had to be copied by hand. A skilled monk might spend a year on a single Bible, so books were rare and extremely expensive, and only the Church, the nobility and a few wealthy scholars could afford them. Most people could not read, and ideas travelled slowly, usually by word of mouth. The invention of the printing press changed all this, and many historians regard it as the most important invention of the last thousand years, whatever their own special interests may be. Without cheap and exact copies of the same text, modern science, law and education would be very difficult to imagine."""
B = """The inventor was Johannes Gutenberg, a goldsmith from the German city of Mainz. Around 1450, he combined several existing ideas into a single system. The first was movable type: instead of carving a whole page on a block of wood, he cast each letter separately in metal, so that the letters could be arranged into words, printed, and then used again. The second was a press, adapted from the machines used to squeeze grapes. The third was an oil-based ink, which stuck to metal better than the water-based inks used by scribes."""
C = """Printing was not entirely new. The Chinese had been printing from carved wooden blocks since about the eighth century, and a Chinese craftsman named Bi Sheng invented movable type made of clay around 1040. In Korea, metal type was in use by the thirteenth century. However, the Chinese and Korean languages use thousands of different characters, which made movable type slow and impractical. Gutenberg's alphabet had only a few dozen letters, and for this reason his system worked much better for European languages."""
D = """Gutenberg's most famous work was a Bible, completed in about 1455, of which roughly 180 copies were printed. It took years to produce, and Gutenberg himself ran into financial difficulties, losing his workshop to a creditor. Nevertheless, the new technology spread quickly. By 1500, printing presses were operating in more than two hundred cities of Europe, and printers had produced about twenty million books, more than all the scribes of Europe had made in the previous thousand years."""
E = """The effects were enormous. As the cost of books fell, more people learned to read, and literacy slowly rose. Scientists could publish their results and compare them with those of others, so that knowledge accumulated more quickly. The Protestant Reformation, begun by Martin Luther in 1517, spread across Germany in a few years because his pamphlets were printed by the thousand. Standard spellings and grammar also developed, since a printer had to choose one spelling for each word and keep to it."""
F = """Not everyone welcomed the new technology. Some authorities feared that cheap books would spread dangerous ideas, and they tried to control printing by licensing the printers and by banning certain works. Some scribes feared for their jobs, and a few scholars argued that printed books were inferior, since they lacked the beauty of the hand-lettered page. Dr Ingrid Lang, a historian of books, points out that similar arguments are made about every new form of communication, including the internet."""
G = """Today, printing is taken for granted, yet its basic principle has not changed: a pattern is transferred from a master copy to many sheets of paper. Modern presses can print thousands of pages a minute, and digital printers allow a single copy of a book to be produced on demand. Even so, many people still enjoy the feel of a printed book, and sales of printed books have remained steady in many countries despite the growth of electronic reading, which suggests that the two forms can live together."""
P = passage('p43', 'The Printing Revolution', 'History of technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Books were cheap in Europe before 1400.', 'F', 'A', 'rare and extremely expensive'),
  ('Most people in Europe could read before Gutenberg.', 'F', 'A', 'Most people could not read'),
  ('Gutenberg was a goldsmith.', 'T', 'B', 'a goldsmith from the German city of Mainz'),
  ('Gutenberg\'s press was adapted from a machine used for squeezing grapes.', 'T', 'B', 'adapted from the machines used to squeeze grapes'),
  ('Bi Sheng\'s type was made of metal.', 'F', 'C', 'movable type made of clay'),
  ('Gutenberg printed his Bible in Latin.', 'NG', 'D', 'Gutenberg\'s most famous work was a Bible', 'The language of the Bible is not given.'),
  ('About 180 copies of the Gutenberg Bible were printed.', 'T', 'D', 'roughly 180 copies'),
  ('Luther\'s pamphlets were printed in large numbers.', 'T', 'E', 'printed by the thousand'),
  ('Printing had no effect on spelling.', 'F', 'E', 'Standard spellings and grammar also developed'),
 ]),
 mcq([
  ('Why was movable type unsuited to Chinese?', ['Chinese paper was poor.', 'There are thousands of characters.', 'Chinese ink was weak.', 'There was no demand.'], 1, 'C', 'thousands of different characters'),
  ('What happened to Gutenberg?', ['He became rich.', 'He lost his workshop.', 'He moved to China.', 'He stopped printing.'], 1, 'D', 'losing his workshop to a creditor'),
  ('What does Dr Lang point out?', ['Printing was a failure.', 'New communication forms always meet similar objections.', 'The internet will replace books.', 'Scribes were better.'], 1, 'F', 'similar arguments are made about every new form of communication'),
 ]),
 multi('Which TWO of Gutenberg\'s three ideas are described in paragraph B as parts of his system?', ['Movable metal type.', 'An oil-based ink.', 'Colour printing.', 'A paper mill.', 'A steam engine.'], [0, 1], [('B', 'cast each letter separately in metal'), ('B', 'an oil-based ink')]),
 head(['The age of the scribe', 'A new system in Mainz', 'Printing before Gutenberg', 'The first great book and its spread', 'How printing changed society', 'Opposition to the new technology', 'Printing today', 'The history of paper', 'How ink is made'],
  [('A', 0, 'every book in Europe had to be copied by hand'), ('B', 1, 'combined several existing ideas into a single system'), ('C', 2, 'Printing was not entirely new'), ('D', 3, 'By 1500, printing presses were operating in more than two hundred cities'), ('E', 4, 'The effects were enormous'), ('F', 5, 'Not everyone welcomed the new technology'), ('G', 6, 'Today, printing is taken for granted')]),
 info([
  ('a comparison between the output of printers and scribes', 'D', 'more than all the scribes of Europe had made in the previous thousand years'),
  ('a reference to a religious movement helped by printing', 'E', 'The Protestant Reformation'),
  ('a reason why some scholars disliked printed books', 'F', 'they lacked the beauty of the hand-lettered page'),
  ('a mention of printing on demand', 'G', 'produced on demand'),
  ('a mention of a craftsman who used clay', 'C', 'Bi Sheng'),
 ]),
 ends(['could afford books before the fifteenth century.', 'cast each letter separately in metal.', 'was used in Korea by the thirteenth century.', 'were operating in more than two hundred cities by 1500.', 'was invented in the twentieth century.', 'was written by a monk in Mainz.', 'is no longer sold anywhere.'], [
  ('Only the Church, the nobility and a few scholars', 0, 'A', 'only the Church, the nobility and a few wealthy scholars could afford them'),
  ('Gutenberg', 1, 'B', 'he cast each letter separately in metal'),
  ('Metal type', 2, 'C', 'metal type was in use by the thirteenth century'),
  ('Printing presses', 3, 'D', 'printing presses were operating in more than two hundred cities of Europe'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Person or place', 'Contribution'],
  [['Gutenberg', 'Combined movable type, a press and [[1]] ink'], ['Bi Sheng', 'Invented movable type from [[2]]'], ['Korea', 'Used [[3]] type by the thirteenth century'], ['Martin Luther', 'Printed [[4]] spread his ideas']],
  [(['oil-based'], 'B', 'an oil-based ink'), (['clay'], 'C', 'made of clay'), (['metal'], 'C', 'metal type'), (['pamphlets'], 'E', 'his pamphlets')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Each letter is cast separately in [[1]].', 'The letters are arranged into [[2]] and printed.', 'The letters are then [[3]].', 'The cost of books falls and more people learn to [[4]].'],
  [(['metal'], 'B', 'cast each letter separately in metal'), (['words'], 'B', 'arranged into words'), (['used again', 'reused'], 'B', 'used again'), (['read'], 'E', 'more people learned to read')], 2),
 sent(2, [
  ('Gutenberg was from the German city of ___.', ['mainz'], 'B', 'the German city of Mainz'),
  ('Gutenberg\'s alphabet had only a few ___ letters.', ['dozen'], 'C', 'only a few dozen letters'),
  ('The Reformation was begun by Martin ___.', ['luther'], 'E', 'begun by Martin Luther'),
  ('Some authorities tried to control printing by ___ printers.', ['licensing'], 'F', 'licensing the printers'),
 ]),
 short(3, [
  ('In which year was Gutenberg\'s Bible completed?', ['1455', 'about 1455'], 'D', 'completed in about 1455'),
  ('What is Dr Lang\'s profession?', ['historian of books'], 'F', 'a historian of books'),
  ('How many books had been printed by 1500?', ['twenty million', 'about twenty million'], 'D', 'about twenty million books'),
 ]),
])
