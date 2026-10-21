from lib import *
from svgs import *
A = """Every book on a shelf has made a long journey, and most readers never think about the many people who helped to bring it to them. An author may spend two years writing a manuscript, but the work of turning it into a finished book takes many more hands: editors, designers, printers, drivers and booksellers all play a part. This passage follows the path of a book from the author's desk to the bookshop and then looks at how the sales of four formats of books have changed in the imaginary country of Calderia, where the publishing industry has published detailed figures for the past four years."""
B = """The journey begins with the author, who writes the manuscript, often alone and over a long period. When it is finished, the author sends it to an agent, who offers it to publishers. A publisher who likes the book signs a contract, and the manuscript then goes to an editor. The editor reads it closely, suggests changes to the plot or the structure, and corrects errors of grammar and fact. This stage can take several months, and many authors say that a good editor improves a book more than any other person, even though the editor's name rarely appears on the cover."""
C = """Next comes design. A designer chooses the typeface, decides how the words will sit on the page, and prepares the cover, which is one of the most important parts of the whole project, since many people choose a book because of the way it looks. The pages are then checked by a proofreader, who looks for the last small mistakes, such as a missing comma or a repeated word. Only when the proofreader is satisfied does the book go to the printer, and by that time the publisher has usually decided how many copies to print, a decision that involves a good deal of guesswork."""
D = """At the printing works, huge machines print the pages on enormous sheets of paper, which are then folded, cut, gathered and bound together between covers. A modern printing press can produce thousands of copies in a single day. The finished books are packed into boxes and loaded on to lorries, and sent to a warehouse, where they are stored until the shops order them. Many publishers now print only small numbers at first and reprint if the book is popular, because unsold copies are expensive to store and are sometimes pulped, or recycled, at a loss to the company."""
E = """From the warehouse, books travel to shops by road, or to readers' homes if they have been ordered online. A bookshop owner decides which titles to stock, and a book that is not displayed has little chance of being noticed. For that reason, publishers pay for bookshops to put selected titles near the entrance, and they send sales representatives to persuade owners to order large quantities. A book that sells well in its first weeks is likely to stay on the shelf, whereas a book that sells slowly may be returned to the publisher within a few months."""
F = """The formats in which people buy books have changed in the last four years. According to figures from the Calderian publishers, paperback sales have stayed constant, while hardback sales have fallen each year, because the price is high. Sales of electronic books have risen steadily, helped by cheap reading devices, and audiobooks have shown the most dramatic change: they stayed small for two years and then jumped suddenly, after a popular app began to offer them to its subscribers. Dr Imran Sadiq, a publishing analyst, thinks that listening will continue to grow, as people use time on journeys for reading."""
G = """Despite these changes, many experts believe that the printed book will survive. Paper books need no battery, can be lent to friends and give pleasure as objects as well as stories. Dr Sadiq points out that every new format of the past hundred years, from the radio to the television, was supposed to replace the book, and none has done so. He expects that readers will use several formats according to the situation, reading a paperback at home, an electronic copy on holiday and listening to an audiobook in the car, and that publishers who understand this will thrive."""
S, PT, W, H = chain(5)
P = passage('p64', 'From Manuscript to Bookshop', 'Society', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which bar chart, A to D, shows the sales of each book format over four years?', [(bars([4, 4, 4, 4]), 160, 120), (bars([5, 4, 3, 2]), 160, 120), (bars([2, 3, 4, 5]), 160, 120), (bars([1, 1, 5, 5]), 160, 120)], [
  ('paperbacks', 0, 'F', 'paperback sales have stayed constant'),
  ('hardbacks', 1, 'F', 'hardback sales have fallen each year'),
  ('electronic books', 2, 'F', 'have risen steadily'),
  ('audiobooks', 3, 'F', 'stayed small for two years and then jumped suddenly'),
 ]),
 tfng([
  ('An author may spend two years writing a manuscript.', 'T', 'A', 'spend two years writing a manuscript'),
  ('An agent offers the manuscript to publishers.', 'T', 'B', 'who offers it to publishers'),
  ('The editor\'s name usually appears on the cover.', 'F', 'B', 'rarely appears on the cover'),
  ('A proofreader looks for small mistakes.', 'T', 'C', 'looks for the last small mistakes'),
  ('A modern printing press can produce thousands of copies in a day.', 'T', 'D', 'thousands of copies in a single day'),
  ('Unsold copies are never recycled.', 'F', 'D', 'pulped, or recycled'),
  ('Publishers pay for bookshops to display some titles.', 'T', 'E', 'publishers pay for bookshops to put selected titles near the entrance'),
  ('Audiobook sales jumped after an app began to offer them.', 'T', 'F', 'after a popular app began to offer them to its subscribers'),
  ('Dr Sadiq has written several novels.', 'NG', 'G', 'Dr Sadiq points out', 'His own writing is not mentioned.'),
 ]),
 mcq([
  ('Why is the cover important?', ['It protects the pages.', 'Many people choose a book for its look.', 'It is cheap to make.', 'It is printed first.'], 1, 'C', 'many people choose a book because of the way it looks'),
  ('Why do publishers print small numbers first?', ['Paper is scarce.', 'Unsold copies are expensive to store.', 'Machines are slow.', 'Authors request it.'], 1, 'D', 'unsold copies are expensive to store'),
  ('What does Dr Sadiq expect readers to do?', ['Stop reading.', 'Use several formats.', 'Buy only hardbacks.', 'Avoid apps.'], 1, 'G', 'readers will use several formats'),
 ]),
 diag('Label the people in the journey of a book, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['author'], 'B', 'begins with the author'), (['editor'], 'B', 'goes to an editor'), (['designer'], 'C', 'A designer chooses'), (['printer'], 'C', 'go to the printer'), (['bookshop'], 'E', 'A bookshop owner decides')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Editing', 'The editor suggests changes to the [[1]]'], ['Proofreading', 'The proofreader looks for a missing [[2]]'], ['Printing', 'Pages are printed on enormous sheets of [[3]]'], ['Selling', 'Publishers send sales [[4]]']],
  [(['plot'], 'B', 'changes to the plot'), (['comma'], 'C', 'a missing comma'), (['paper'], 'D', 'enormous sheets of paper'), (['representatives'], 'E', 'sales representatives')], 1),
 head(['A long journey', 'Writing and editing', 'Design and checking', 'Printing and storing', 'Reaching the reader', 'Changing formats', 'The future of paper', 'The history of the typewriter', 'How to learn a language'],
  [('A', 0, 'Every book on a shelf has made a long journey'), ('B', 1, 'The editor reads it closely'), ('C', 2, 'A designer chooses the typeface'), ('D', 3, 'huge machines print the pages'), ('E', 4, 'books travel to shops by road'), ('F', 5, 'The formats in which people buy books have changed'), ('G', 6, 'many experts believe that the printed book will survive')]),
 info([
  ('a reference to an agent', 'B', 'sends it to an agent'),
  ('a mention of the typeface', 'C', 'chooses the typeface'),
  ('a reference to pulping unsold books', 'D', 'pulped, or recycled'),
  ('a method publishers use to persuade owners', 'E', 'persuade owners to order large quantities'),
  ('a reference to listening in a car', 'G', 'audiobook in the car'),
 ]),
 ends(['prepares the cover.', 'fold, cut and bind the pages.', 'decides which titles to stock.', 'need no battery.', 'write the manuscript.', 'are sold only online.', 'cost nothing to print.'], [
  ('A designer', 0, 'C', 'prepares the cover'),
  ('Printing machines', 1, 'D', 'folded, cut, gathered and bound'),
  ('A bookshop owner', 2, 'E', 'decides which titles to stock'),
  ('Paper books', 3, 'G', 'need no battery'),
 ]),
 sent(2, [
  ('A publisher who likes a book signs a ___.', ['contract'], 'B', 'signs a contract'),
  ('A ___ checks the pages for the last small mistakes.', ['proofreader'], 'C', 'a proofreader'),
  ('Unsold copies are expensive to ___.', ['store'], 'D', 'expensive to store'),
  ('Dr Sadiq is a publishing ___.', ['analyst'], 'F', 'publishing analyst'),
 ]),
 short(3, [
  ('Who offers the manuscript to publishers?', ['an agent', 'agent'], 'B', 'an agent'),
  ('Where are books stored before shops order them?', ['a warehouse', 'warehouse'], 'D', 'a warehouse'),
  ('Which kind of book needs no battery?', ['paper', 'paper books'], 'G', 'Paper books need no battery'),
 ]),
])
