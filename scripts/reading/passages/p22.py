from lib import *
A = """Chess is one of the oldest games still played today. Its ancestor, a game called chaturanga, appeared in India around the sixth century. The name means 'four divisions', a reference to the four parts of an Indian army: infantry, cavalry, elephants and chariots, which later became the pawn, the knight, the bishop and the rook. The game was played on an eight-by-eight board, and it was valued as a way of teaching the art of war to young princes. Pieces were carved from wood, ivory and stone, and sets made for kings were often works of art."""
B = """From India the game spread to Persia, where it was called shatranj, and the Persians introduced the call 'shah', meaning king, which survives in our word 'check'. After the Arab conquest of Persia in the seventh century, Muslim players carried the game across North Africa to Spain, and by about the year 1000 it was being played in most of Europe. Travelling merchants, soldiers and pilgrims all helped to spread it, and so, many historians believe, did the trade routes of Central Asia."""
C = """The rules changed as the game moved west. In the early game the queen, then called the counsellor, could move only one square at a time, and the bishop could jump only two squares diagonally. Around 1475, in Spain or Italy, the two pieces gained their modern powers, and the game became much faster and more exciting. Other rules, such as castling and the first move of two squares for a pawn, were added over the following century, until the game looked very much as it does today. For a time, in some countries, it was known as 'the mad queen's chess'."""
D = """Chess grew into a serious competition in the nineteenth century. The first international tournament was held in London in 1851, and in 1886 Wilhelm Steinitz became the first official world champion. In 1924, an international federation, FIDE, was founded in Paris to organise tournaments and to agree the rules. Today it has about two hundred member countries, and the best players travel the world to compete for prizes, titles and fame."""
E = """The mathematics of the game is astonishing. After only a few moves each, there are millions of possible positions, and the number of possible games is estimated to be greater than the number of atoms in the observable universe. No player, however gifted, can calculate everything, so players rely on pattern recognition, which they develop through years of study. Research suggests that a strong player may recognise around fifty thousand patterns at a glance. This is why a master can often take in a position in seconds, while a beginner sees only a crowd of pieces and has to count each one."""
F = """Computers have changed chess completely. In 1997, an IBM computer called Deep Blue defeated the world champion, Garry Kasparov, in a match in New York, the first time that a machine had beaten a reigning champion in a match under tournament conditions. Today, a free program on a mobile phone plays better than any human. Instead of ending the game, however, the machines have become teachers: young players use them to analyse their games and to find ideas that no coach had imagined."""
G = """Interest in chess has grown rapidly in recent years. During the lockdowns of 2020, millions of people learned the game online, helped by the popularity of a television series, The Queen's Gambit. Schools in many countries, including Armenia, now teach chess as a lesson, because teachers believe that it improves concentration and logical thinking. The evidence for this is mixed, but nobody doubts that the game is a pleasure to play, and that it can be learned at any age."""
P = passage('p22', 'The Story of Chess', 'Games and history', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Chess is older than the Roman Empire.', 'NG', 'A', 'one of the oldest games still played today', 'The passage gives no date for the Roman Empire.'),
  ('Chaturanga appeared in India.', 'T', 'A', 'appeared in India around the sixth century'),
  ('Chaturanga was played on a board with sixty-four squares.', 'T', 'A', 'an eight-by-eight board'),
  ('The word check comes from a Persian word.', 'T', 'B', 'the call \'shah\', meaning king, which survives in our word \'check\''),
  ('Chess reached most of Europe by about the year 1000.', 'T', 'B', 'by about the year 1000 it was being played in most of Europe'),
  ('In the early game the queen could move across the whole board.', 'F', 'C', 'could move only one square at a time'),
  ('The first international tournament took place in Paris.', 'F', 'D', 'held in London in 1851'),
  ('Deep Blue lost its match against Kasparov.', 'F', 'F', 'defeated the world champion'),
  ('Armenia\'s schools teach chess.', 'T', 'G', 'Schools in many countries, including Armenia, now teach chess'),
 ]),
 mcq([
  ('What does chaturanga mean?', ['four divisions', 'the king\'s game', 'war and peace', 'eight squares'], 0, 'A', 'The name means \'four divisions\''),
  ('When did the queen and bishop gain their modern powers?', ['around 1000', 'around 1475', 'in 1851', 'in 1924'], 1, 'C', 'Around 1475'),
  ('How have computers affected chess teaching?', ['They have stopped young players.', 'They are used to analyse games.', 'They are banned from competitions.', 'They have replaced coaches entirely.'], 1, 'F', 'young players use them to analyse their games'),
 ]),
 head(['The Indian beginnings', 'A journey west', 'A faster and stronger game', 'The age of competition', 'The numbers behind the game', 'Humans against machines', 'A new wave of players', 'The best chess pieces to buy', 'How to win in ten moves'],
  [('A', 0, 'Its ancestor, a game called chaturanga'), ('B', 1, 'From India the game spread to Persia'), ('C', 2, 'The rules changed as the game moved west'), ('D', 3, 'Chess grew into a serious competition'), ('E', 4, 'The mathematics of the game is astonishing'), ('F', 5, 'Computers have changed chess completely'), ('G', 6, 'Interest in chess has grown rapidly in recent years')]),
 info([
  ('a list of four parts of an army', 'A', 'infantry, cavalry, elephants and chariots'),
  ('the century in which Muslim players spread the game', 'B', 'seventh century'),
  ('a nickname for a version of the game', 'C', 'the mad queen\'s chess'),
  ('an organisation founded in a European capital', 'D', 'FIDE, was founded in Paris'),
  ('the name of a television series', 'G', 'The Queen\'s Gambit'),
 ]),
 sent(2, [
  ('Chaturanga was a way of teaching young princes the art of ___.', ['war'], 'A', 'the art of war to young princes'),
  ('Persians called the game ___.', ['shatranj'], 'B', 'it was called shatranj'),
  ('Wilhelm Steinitz became world champion in ___.', ['1886'], 'D', 'in 1886'),
  ('A strong player may recognise around fifty thousand ___.', ['patterns'], 'E', 'fifty thousand patterns'),
 ]),
 short(3, [
  ('In which city did Deep Blue play Kasparov?', ['new york'], 'F', 'in a match in New York'),
  ('What was the queen originally called?', ['the counsellor', 'counsellor'], 'C', 'then called the counsellor'),
  ('What can chess be learned at, according to the passage?', ['any age'], 'G', 'learned at any age'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Stage', 'Detail'],
  [['India', 'The game was called [[1]]'], ['Persia', 'The game was called [[2]]'], ['1851', 'The first international [[3]] was held in London'], ['1997', 'Deep Blue beat the world [[4]]']],
  [(['chaturanga'], 'A', 'a game called chaturanga'), (['shatranj'], 'B', 'it was called shatranj'), (['tournament'], 'D', 'The first international tournament'), (['champion'], 'F', 'defeated the world champion')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Chaturanga appears in [[1]] around the sixth century.', 'It spreads to Persia as [[2]].', 'Muslim players carry it to [[3]] by way of North Africa.', 'By about the year [[4]], most of Europe plays it.'],
  [(['india'], 'A', 'appeared in India'), (['shatranj'], 'B', 'it was called shatranj'), (['spain'], 'B', 'across North Africa to Spain'), (['1000'], 'B', 'by about the year 1000')], 1),
])
