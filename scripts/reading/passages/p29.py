from lib import *
A = """Origami is the Japanese art of folding paper into shapes without cutting or gluing it. The word comes from two Japanese words, ori, meaning folding, and kami, meaning paper. Although it is now thought of as a Japanese tradition, paper folding was practised in China and Europe too, and historians still disagree about where the first models were made. What is certain is that the craft became popular in Japan during the seventeenth century, when paper became cheap enough for ordinary families to buy."""
B = """Early origami served ceremonial purposes. At Shinto weddings, two paper butterflies were used to decorate bottles of rice wine, and folded paper strips called noshi were attached to gifts as a sign of good wishes. Samurai exchanged them too. Because paper was expensive and precious, these models were treated with respect, and the patterns were passed from parent to child by memory, not written down. The first printed book of instructions, published in 1797, showed how to fold the famous crane."""
C = """The crane has a special meaning for the Japanese. According to a popular belief, a person who folds a thousand paper cranes will be granted a wish, often for good health or long life. After the Second World War, a girl named Sadako Sasaki, who was ill after the atomic bombing of Hiroshima, set out to fold a thousand cranes. Her story is told in a book read by children around the world, and every year thousands of paper cranes are sent to a monument in Hiroshima as a symbol of peace."""
D = """Modern origami began in the twentieth century with the work of Akira Yoshizawa, who invented a system of symbols, lines and arrows to show each fold. Before this, there was no common language for describing a model. His system, still in use, allows a folder in Brazil to follow instructions from a book written in Japan. Yoshizawa also invented wet-folding, in which the paper is dampened so that it can be shaped into curved forms that look more like living animals."""
E = """Origami has become a subject of serious mathematics. In the 1990s, mathematicians showed that certain rules govern every fold pattern, and that any shape with straight edges can in theory be made from a single square of paper. Engineers have since used these ideas to solve practical problems. A Japanese team designed a large solar panel that is folded flat for launch into space and then opens in orbit, and doctors have developed a tube for repairing blood vessels that is folded small to pass through a narrow artery before it opens."""
F = """Folding paper also has benefits for the mind. Teachers use origami in mathematics lessons to explain angles, symmetry and fractions, because pupils can see and touch each idea. Many of them report that children who fold models understand these ideas better. Dr Mei Lin Chan, an educational researcher, says that this is plausible, but she cautions that careful research is still needed before schools change their lessons, since pupils who enjoy folding may simply be the ones who were already good at mathematics."""
G = """For beginners, the best advice is to start simply. A square of paper, a flat table and a little patience are all that is needed. The first folds, the valley fold, in which the paper is folded towards you, and the mountain fold, in which it is folded away, are the basis of almost every model. Learners should crease each fold sharply with a fingernail, because a careless fold will spoil everything that follows. Many people find that, after the first few models, the craft becomes a relaxing way to end a long day."""
P = passage('p29', 'Origami: Folding Paper into Art', 'Arts and craft', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Origami involves cutting and gluing paper.', 'F', 'A', 'without cutting or gluing it'),
  ('Paper folding was practised only in Japan.', 'F', 'A', 'practised in China and Europe too'),
  ('Origami became popular in Japan in the seventeenth century.', 'T', 'A', 'popular in Japan during the seventeenth century'),
  ('Early patterns were usually written down.', 'F', 'B', 'passed from parent to child by memory, not written down'),
  ('The first printed instruction book was published in 1797.', 'T', 'B', 'published in 1797'),
  ('Folding a thousand cranes is believed to grant a wish.', 'T', 'C', 'a person who folds a thousand paper cranes will be granted a wish'),
  ('Sadako Sasaki finished folding her cranes.', 'NG', 'C', 'set out to fold a thousand cranes', 'The passage says she set out to do it, but not whether she completed it.'),
  ('Yoshizawa invented a system of symbols for folds.', 'T', 'D', 'a system of symbols, lines and arrows'),
  ('Wet-folding makes it possible to create curved forms.', 'T', 'D', 'shaped into curved forms'),
 ]),
 mcq([
  ('Why were early paper models treated with respect?', ['They were used in battle.', 'Paper was expensive and precious.', 'They were made by priests.', 'They were never given as gifts.'], 1, 'B', 'Because paper was expensive and precious'),
  ('What does the mathematics of origami show?', ['Only square paper can be used.', 'Any straight-edged shape can in theory be made from one square.', 'Curved forms are impossible.', 'Folds must be counted.'], 1, 'E', 'any shape with straight edges can in theory be made from a single square of paper'),
  ('What is Dr Chan\'s opinion of the claims about origami in lessons?', ['They are false.', 'They are plausible but need more research.', 'They are proved.', 'They are unimportant.'], 1, 'F', 'this is plausible, but she cautions that careful research is still needed'),
 ]),
 multi('Which TWO practical uses of origami ideas are mentioned in paragraph E?', ['A folding solar panel.', 'A tube for blood vessels.', 'A folding bridge.', 'A paper aeroplane.', 'A foldable tent.'], [0, 1], [('E', 'a large solar panel that is folded flat'), ('E', 'a tube for repairing blood vessels')]),
 head(['The meaning of a word and a craft', 'Models for ceremonies', 'A symbol of hope and peace', 'A universal language of folds', 'From art to science', 'Learning through paper', 'How to begin', 'The history of printing', 'A guide to rice wine'],
  [('A', 0, 'The word comes from two Japanese words'), ('B', 1, 'Early origami served ceremonial purposes'), ('C', 2, 'The crane has a special meaning'), ('D', 3, 'invented a system of symbols, lines and arrows'), ('E', 4, 'Origami has become a subject of serious mathematics'), ('F', 5, 'Teachers use origami in mathematics lessons'), ('G', 6, 'the best advice is to start simply')]),
 info([
  ('a reference to the meaning of two words', 'A', 'ori, meaning folding, and kami, meaning paper'),
  ('an example of decorations for bottles', 'B', 'two paper butterflies'),
  ('a mention of a monument', 'C', 'a monument in Hiroshima'),
  ('a suggestion that pupils who like folding may already be good at mathematics', 'F', 'may simply be the ones who were already good at mathematics'),
  ('a description of two basic folds', 'G', 'the valley fold'),
 ]),
 ends(['to decorate bottles of rice wine.', 'is said to bring good health.', 'to show each fold.', 'folded flat for launch into space.', 'was invented in Brazil.', 'is made from rice.', 'is the most expensive paper.'], [
  ('Paper butterflies were used', 0, 'B', 'to decorate bottles of rice wine'),
  ('Folding a thousand cranes', 1, 'C', 'will be granted a wish, often for good health'),
  ('Yoshizawa invented symbols', 2, 'D', 'to show each fold'),
  ('A solar panel was designed to be', 3, 'E', 'folded flat for launch into space'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Begin with a [[1]] of paper on a flat table.', 'Make a valley fold, in which the paper is folded [[2]] you.', 'Make a [[3]] fold, in which the paper is folded away.', '[[4]] each fold sharply with a fingernail.'],
  [(['square'], 'G', 'A square of paper'), (['towards'], 'G', 'folded towards you'), (['mountain'], 'G', 'the mountain fold'), (['crease'], 'G', 'crease each fold sharply')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Topic', 'Detail'],
  [['17th century', 'Paper became [[1]] for ordinary families'], ['1797', 'First printed [[2]] shows how to fold a crane'], ['Akira Yoshizawa', 'Invented [[3]] to show each fold'], ['1990s', 'Mathematicians found [[4]] that govern fold patterns']],
  [(['cheap'], 'A', 'cheap enough'), (['book'], 'B', 'The first printed book'), (['symbols'], 'D', 'a system of symbols'), (['rules'], 'E', 'certain rules govern')], 1),
 sent(2, [
  ('The folded paper strips attached to gifts were called ___.', ['noshi'], 'B', 'called noshi'),
  ('Sadako Sasaki was ill after the bombing of ___.', ['hiroshima'], 'C', 'bombing of Hiroshima'),
  ('Yoshizawa dampened paper to shape ___ forms.', ['curved'], 'D', 'curved forms'),
  ('Learners should crease each fold with a ___.', ['fingernail'], 'G', 'with a fingernail'),
 ]),
 short(3, [
  ('What did Samurai do with noshi?', ['exchanged them'], 'B', 'Samurai exchanged them too'),
  ('What is Dr Chan\'s profession?', ['educational researcher', 'an educational researcher'], 'F', 'an educational researcher'),
  ('What can a careless fold do?', ['spoil everything'], 'G', 'spoil everything that follows'),
 ]),
])
