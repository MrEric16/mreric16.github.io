from lib import *
from svgs import *
A = """Reading habits are changing across the world, and the imaginary country of Altonia offers a useful example. Every five years since 1990, its national statistics office has asked thousands of adults how they read, what they read and where they get their books. The results, taken together, show four quite different patterns, and each has a story behind it. This passage describes the main findings and the explanations that researchers have offered, and it asks what they may mean for the future of reading in the country. The study is unusual because the same questions have been asked in the same way for more than thirty years, so that the answers can be compared directly. Its authors stress that the figures describe adults only, and that children may behave quite differently from their parents."""
B = """The most dramatic change concerns electronic books. For almost two decades, hardly anyone in Altonia read them: the figure stayed close to zero because readers were expensive and the choice of titles was small. Then, in the early 2010s, cheap tablets and larger phone screens arrived, and the number jumped within a few years. Today, more than a third of adults say that they read at least one e-book each year, and the share is still climbing, although more slowly than before."""
C = """Printed newspapers tell a very different story. In 1990, nearly three-quarters of adults read one at least once a week. The figure has fallen at every survey since, and it is now below one in five. Readers say they prefer to find news online, where it is free and constantly updated. Several famous titles have closed, and others now publish only a few days a week, relying on their websites for most of their income."""
D = """Library visits followed a pattern with a peak. Numbers rose during the 1990s, when many new libraries opened and the government ran a campaign to encourage reading among children. They reached their highest point in 2005. After that they fell sharply, partly because many libraries cut their opening hours when budgets were reduced, and partly because people could now borrow e-books from home. Some libraries have since changed, offering computer classes, meeting rooms and cafes, and the decline seems to have slowed."""
E = """Audiobooks developed in yet another way. They began as a small market for blind readers and for long car journeys, and for years the audience was tiny. A rapid rise followed the arrival of music-streaming services, which taught people to listen on their phones, but the growth has now stopped. About one adult in ten listens to an audiobook each year, and the figure has stayed at that level for the last decade, which suggests that the market has found its natural size. Publishers say that the loyal audience for audiobooks is mostly made up of commuters and of people over fifty who find it hard to read small print."""
F = """What does all this mean for the reading of books in general? Surprisingly, the total time that adults spend reading has hardly changed. The researcher in charge of the survey, Dr Sven Ahlberg, says that people have not stopped reading; they have changed the way they do it. He adds that readers who use several formats tend to read more books than those who use only one, so that digital reading may actually help to keep the habit alive."""
G = """Looking to the future, the survey team expects the same pattern to continue: more reading on screens, fewer printed newspapers, and a gradual change in the role of the library. Publishers, meanwhile, are experimenting with new ways to sell stories, from monthly subscriptions to books that are published one chapter at a time. Whether these experiments succeed will depend on whether readers are willing to pay for what they can often find free elsewhere, a question that nobody can yet answer with confidence."""
P = passage('p32', 'How Altonia Reads', 'Society', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows each reading trend described in the passage?', [(graph('sharp'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('plateau'), 160, 120)], [
  ('e-book reading', 0, 'B', 'the number jumped within a few years'),
  ('weekly readers of printed newspapers', 1, 'C', 'The figure has fallen at every survey since'),
  ('library visits', 2, 'D', 'They reached their highest point in 2005'),
  ('audiobook listening', 3, 'E', 'the figure has stayed at that level for the last decade'),
 ]),
 tfng([
  ('Altonia is a real country.', 'F', 'A', 'the imaginary country of Altonia'),
  ('The survey has been carried out every five years since 1990.', 'T', 'A', 'Every five years since 1990'),
  ('E-readers were cheap in the early years.', 'F', 'B', 'readers were expensive'),
  ('More than a third of adults read an e-book each year.', 'T', 'B', 'more than a third of adults'),
  ('Three-quarters of adults read a newspaper weekly in 1990.', 'T', 'C', 'nearly three-quarters of adults'),
  ('Readers prefer online news because it is free.', 'T', 'C', 'where it is free and constantly updated'),
  ('Library visits fell because libraries were closed for ever.', 'F', 'D', 'cut their opening hours'),
  ('Audiobooks were first made for car drivers.', 'NG', 'E', 'a small market for blind readers and for long car journeys', 'Blind readers and long journeys are both mentioned; which came first is not stated.'),
  ('The total time adults spend reading has changed a great deal.', 'F', 'F', 'has hardly changed'),
 ]),
 mcq([
  ('What caused the jump in e-book reading?', ['Lower book prices.', 'Cheap tablets and larger phone screens.', 'A government campaign.', 'More libraries.'], 1, 'B', 'cheap tablets and larger phone screens'),
  ('Why do audiobook figures suggest a natural size?', ['They are falling.', 'They have stayed level.', 'They are very small.', 'They are rising fast.'], 1, 'E', 'the market has found its natural size'),
  ('What does Dr Ahlberg say about readers of several formats?', ['They read fewer books.', 'They read more books.', 'They prefer newspapers.', 'They visit libraries less.'], 1, 'F', 'tend to read more books'),
 ]),
 multi('Which TWO reasons for the fall in library visits are given in paragraph D?', ['Libraries cut their opening hours.', 'People could borrow e-books at home.', 'Many libraries were destroyed.', 'Books became cheaper.', 'Children lost interest in reading.'], [0, 1], [('D', 'cut their opening hours'), ('D', 'borrow e-books from home')]),
 head(['The aim of the study', 'A sudden surge', 'A steady decline', 'Rise, peak and fall', 'Growth that stopped', 'The overall picture', 'Predictions and experiments', 'The history of the printing press', 'The cost of paper'],
  [('A', 0, 'This passage describes the main findings'), ('B', 1, 'The most dramatic change concerns electronic books'), ('C', 2, 'Printed newspapers tell a very different story'), ('D', 3, 'Library visits followed a pattern with a peak'), ('E', 4, 'Audiobooks developed in yet another way'), ('F', 5, 'the total time that adults spend reading has hardly changed'), ('G', 6, 'Looking to the future')]),
 info([
  ('a reference to the aim of a government campaign', 'D', 'to encourage reading among children'),
  ('a description of new services offered by libraries', 'D', 'computer classes, meeting rooms and cafes'),
  ('a reference to the audience for early audiobooks', 'E', 'blind readers'),
  ('a mention of selling stories in instalments', 'G', 'one chapter at a time'),
  ('a mention of titles that have stopped publishing', 'C', 'Several famous titles have closed'),
 ]),
 sent(2, [
  ('The survey asks adults how they read and where they get their ___.', ['books'], 'A', 'where they get their books'),
  ('Many titles now rely on their ___ for most of their income.', ['websites'], 'C', 'relying on their websites'),
  ('The growth of audiobooks followed music-streaming ___.', ['services'], 'E', 'music-streaming services'),
  ('Readers may not want to pay for what they can find ___ elsewhere.', ['free'], 'G', 'find free elsewhere'),
 ]),
 short(3, [
  ('Who runs the survey?', ['statistics office'], 'A', 'its national statistics office'),
  ('When did the highest number of library visits occur?', ['2005'], 'D', 'in 2005'),
  ('What is Dr Ahlberg in charge of?', ['the survey'], 'F', 'in charge of the survey'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'E-books were almost unread until cheap [[1]] arrived. Printed newspapers have [[2]] at every survey, while library visits reached their [[3]] point in 2005 and then fell. Audiobook listening has stayed [[4]] for ten years.',
  [(['tablets'], 'B', 'cheap tablets'), (['fallen'], 'C', 'has fallen at every survey'), (['highest'], 'D', 'highest point'), (['level', 'steady'], 'E', 'stayed at that level')], 1,
  bank=['tablets', 'fallen', 'highest', 'level', 'phones', 'risen', 'cheaper', 'closed']),
])
