from lib import *
A = """Before paper, people wrote on whatever they could find. The ancient Egyptians used papyrus, made by splitting the stems of a river reed into strips and pressing them together. In Europe, scribes used parchment, which was made from animal skin. Parchment lasted for centuries, but it was costly: a single large book might require the skins of a whole flock of sheep. For most of history, therefore, writing belonged to a small number of people who could afford it."""
B = """In China, early writers used strips of bamboo, which were heavy and awkward to store, or silk, which was light but very expensive. According to tradition, in the year 105 an official named Cai Lun presented the emperor with a new material made from tree bark, hemp waste, old rags and fishing nets. Archaeologists have since found fragments of paper that are older than his date, so he probably improved the method rather than invented it. Whoever deserves the credit, the new material was lighter than bamboo and far cheaper than silk, and its use spread quickly through the empire. His achievement was to make paper cheap enough for ordinary use."""
C = """The process was simple, which was one reason why it spread so widely. The raw materials were soaked in water for several days and then beaten into a soft pulp. The pulp was mixed with water in a large vat. A worker dipped a screen made of fine bamboo strips into the vat and lifted it out, leaving a thin layer of fibres on the screen as the water drained away. The wet sheets were stacked and pressed to squeeze out the remaining water, and finally they were hung up to dry."""
D = """For several centuries the Chinese guarded the secret of papermaking. It moved west along the Silk Road, the network of trade routes that linked China with the Mediterranean, and by the eighth century paper was being made in Samarkand and Baghdad. A popular story claims that Chinese prisoners taught the craft after a battle in 751, but historians doubt this, since merchants had been carrying paper along the same routes for years and local workers could have learned from them."""
E = """In the Islamic world, paper had an enormous effect. Mills in Baghdad produced it in large quantities, and cheap paper encouraged the growth of libraries, bookshops and schools. Scholars copied and translated works of mathematics, medicine and astronomy, and many of these texts later reached Europe. Europeans were slower to accept the new material. Some officials distrusted it as flimsy and refused to accept important documents written on paper, and the first European mills did not appear until the twelfth century, in Spain. Once people saw how cheap and convenient the material was, however, resistance faded, and by the end of the Middle Ages paper was in everyday use in most of Europe."""
F = """The arrival of the printing press in the middle of the fifteenth century changed the situation completely. Printers needed large amounts of paper, and demand soon outran the supply of rags, which were still the main raw material. By the nineteenth century the shortage was so serious that manufacturers were searching for alternatives. The solution, discovered in the 1840s, was to make pulp from wood. It was far cheaper than rag, and it made possible the mass-produced newspapers and cheap books that had once been unimaginable."""
G = """Predictions that computers would create a paperless world have not come true, and the world uses more paper today than it did fifty years ago. Environmental groups have criticised the industry for cutting down forests, and manufacturers have responded by planting new trees and by recycling. In many countries more than half of the paper produced now comes from used paper, so the fibres that Cai Lun's workers beat into pulp nearly two thousand years ago are still being reused."""
P = passage('p05', 'The Story of Paper', 'History', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Parchment was made from the skins of animals.', 'T', 'A', 'parchment, which was made from animal skin'),
  ('Papyrus was cheaper to produce than parchment.', 'NG', 'A', 'The ancient Egyptians used papyrus', 'The passage does not compare the cost of the two materials.'),
  ('Silk was a cheap writing material in China.', 'F', 'B', 'silk, which was light but very expensive'),
  ('Cai Lun was the first person ever to make paper.', 'F', 'B', 'he probably improved the method rather than invented it'),
  ('Cai Lun made paper from materials that included old fishing nets.', 'T', 'B', 'tree bark, hemp waste, old rags and fishing nets'),
  ('The pulp was dried before it was mixed with water.', 'F', 'C', 'The pulp was mixed with water in a large vat'),
  ('Historians accept the story that prisoners taught papermaking in 751.', 'F', 'D', 'historians doubt this'),
  ('Paper was being made in Baghdad by the eighth century.', 'T', 'D', 'by the eighth century paper was being made in Samarkand and Baghdad'),
  ('Paper mills opened in Spain before they opened elsewhere in Europe.', 'NG', 'E', 'the first European mills did not appear until the twelfth century, in Spain', 'The passage says the first mills were in Spain but does not say what came next.'),
  ('Wood pulp replaced rags as the main raw material in the nineteenth century.', 'T', 'F', 'The solution, discovered in the 1840s, was to make pulp from wood'),
 ]),
 feat('Which writing material does each statement describe? Choose the correct letter, A to E. You may use any letter more than once.', ['Papyrus', 'Parchment', 'Bamboo', 'Silk', 'Paper'], [
  ('It was made from the stems of a river reed.', 0, 'A', 'splitting the stems of a river reed into strips'),
  ('A single large book could use up the skins of a flock of sheep.', 1, 'A', 'the skins of a whole flock of sheep'),
  ('It was heavy and awkward to store.', 2, 'B', 'heavy and awkward to store'),
  ('It was light but very expensive.', 3, 'B', 'light but very expensive'),
  ('It encouraged the growth of libraries and bookshops.', 4, 'E', 'cheap paper encouraged the growth of libraries, bookshops and schools'),
 ], cls=True),
 mcq([
  ('What does the writer suggest about Cai Lun?', ['He kept papermaking secret.', 'He made paper widely affordable.', 'He taught the Arabs to make paper.', 'He discovered wood pulp.'], 1, 'B', 'His achievement was to make paper cheap enough for ordinary use'),
  ('Why did some Europeans refuse to accept paper documents?', ['They thought paper was too expensive.', 'They could not read the text.', 'They believed it was not strong enough.', 'They preferred printed books.'], 2, 'E', 'Some officials distrusted it as flimsy'),
  ('What caused the rag shortage described in paragraph F?', ['a rise in the demand from printers', 'the closure of old paper mills', 'a decline in the cloth trade', 'competition from parchment makers'], 0, 'F', 'demand soon outran the supply of rags'),
 ]),
 head(['The high cost of early writing materials', 'A cheaper material from China', 'How paper was made', 'The route paper took to the West', 'A great stimulus to learning', 'The problem of finding enough raw material', 'Paper use in the modern world', 'The invention of the printing press'],
  [('A', 0, 'it was costly'), ('B', 1, 'make paper cheap enough for ordinary use'), ('C', 2, 'The process was simple'), ('D', 3, 'It moved west along the Silk Road'), ('E', 4, 'cheap paper encouraged the growth of libraries'), ('F', 5, 'demand soon outran the supply of rags')]),
 info([
  ('a reason why the papermaking process spread so widely', 'C', 'The process was simple, which was one reason why it spread so widely'),
  ('a description of how the first European paper mills were located', 'E', 'the first European mills did not appear until the twelfth century, in Spain'),
  ('a statement that people had previously thought computers would replace paper', 'G', 'Predictions that computers would create a paperless world'),
  ('an explanation of why a popular story is doubted', 'D', 'merchants had been carrying paper along the same routes for years'),
  ('a comparison between the cost of wood pulp and rag', 'F', 'It was far cheaper than rag'),
  ('a reference to people who could afford to write', 'A', 'writing belonged to a small number of people who could afford it'),
 ]),
 sent(3, [
  ('Papyrus was made by pressing together strips of a river ___.', ['reed'], 'A', 'stems of a river reed'),
  ('Cai Lun gave the emperor a new material in the year ___.', ['105'], 'B', 'in the year 105'),
  ('Raw materials were soaked in water and then beaten into ___.', ['pulp', 'a soft pulp', 'soft pulp'], 'C', 'beaten into a soft pulp'),
  ('Paper moved west along the ___ Road.', ['silk'], 'D', 'along the Silk Road'),
  ('Scholars in the Islamic world translated works of mathematics, medicine and ___.', ['astronomy'], 'E', 'mathematics, medicine and astronomy'),
  ('The press arrived in the middle of the ___ century.', ['fifteenth', '15th'], 'F', 'middle of the fifteenth century'),
 ]),
 short(3, [
  ('What did a worker dip into the vat?', ['a screen', 'screen'], 'C', 'dipped a screen made of fine bamboo strips'),
  ('In which city was paper produced in large quantities in the Islamic world?', ['baghdad'], 'E', 'Mills in Baghdad'),
  ('What did the new raw material of the 1840s come from?', ['wood'], 'F', 'make pulp from wood'),
  ('What have manufacturers planted to answer environmental criticism?', ['new trees', 'trees'], 'G', 'planting new trees'),
 ]),
 flow('Complete the flow chart. Write ONE WORD ONLY from the passage for each answer.',
  ['The raw materials are soaked in [[1]] for several days.', 'They are beaten into a soft [[2]].', 'A screen is dipped into the vat and lifted out, leaving a thin layer of [[3]].', 'The wet sheets are stacked and [[4]] to remove water.', 'The sheets are hung up to [[5]].'],
  [(['water'], 'C', 'soaked in water'), (['pulp'], 'C', 'beaten into a soft pulp'), (['fibres'], 'C', 'a thin layer of fibres'), (['pressed'], 'C', 'stacked and pressed'), (['dry'], 'C', 'hung up to dry')], 1),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Period', 'Event'],
  [['The year 105', 'Cai Lun presents the emperor with paper made partly from [[1]]'], ['The eighth century', 'Paper is made in Samarkand and [[2]]'], ['The twelfth century', 'The first [[3]] in Europe appear, in Spain'], ['The 1840s', '[[4]] is used to make pulp']],
  [(['old rags', 'rags', 'fishing nets', 'tree bark', 'hemp waste'], 'B', 'tree bark, hemp waste, old rags and fishing nets'), (['baghdad'], 'D', 'Samarkand and Baghdad'), (['mills', 'paper mills'], 'E', 'the first European mills'), (['wood'], 'F', 'pulp from wood')], 2),
])
