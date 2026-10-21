from lib import *
A = """Money seems so natural that it is hard to imagine life without it. Yet for most of human history, people lived without coins or notes, and they obtained what they needed by barter, that is, by exchanging goods directly. Barter has a serious weakness: it works only when each person has something that the other wants. A farmer with a spare sheep who needs shoes must find a shoemaker who happens to need a sheep. Economists call this the problem of the double coincidence of wants, and money was invented to solve it."""
B = """The earliest forms of money were ordinary objects that people agreed to accept. In different times and places, shells, salt, cattle, beads and bricks of tea have all been used. A good form of money must be easy to carry, hard to copy, divisible into small parts, and durable. Cattle fail the test of portability and shells the test of durability. Metals such as gold, silver and bronze met all the conditions, and by about 3000 BC, merchants in Mesopotamia were using weighed pieces of silver as a standard of value."""
C = """The first true coins were made in the kingdom of Lydia, in what is now western Turkey, around 600 BC. Each coin was a lump of a natural mixture of gold and silver, stamped with a picture to guarantee its weight and purity. The idea spread quickly. Greek cities issued their own coins, and the Romans, who built a huge empire, used coins to pay their soldiers and to collect taxes, so that the same money circulated from Britain to Syria."""
D = """Paper money appeared in China during the Tang and Song dynasties, as a convenient alternative to carrying heavy strings of copper coins. Merchants first left their coins with a trusted shop in return for a receipt, and the receipts began to be accepted in place of the coins. The government soon took control of the system and printed official notes. When the Italian traveller Marco Polo described this in the thirteenth century, many of his readers found it hard to believe that paper could be worth anything."""
E = """In Europe, the next great change came with banks. Merchants in Italian cities such as Florence and Venice held accounts for their customers and let them make payments by a written order, an ancestor of the cheque. Banks also discovered that most depositors did not ask for their money at the same time, so they could lend part of it out and charge interest. This practice made trade easier, but it created the risk of a bank run, in which many customers demand their money at once, and the bank fails."""
F = """In the twentieth century, money lost its last connection with precious metal. Until the 1970s, many countries promised that their notes could be exchanged for a fixed amount of gold. When they abandoned this promise, money came to depend only on trust in the government that issued it. Today most money exists only as numbers in computer systems; coins and notes make up a small part of the total in wealthy countries, and in some, a growing share of shops no longer accept cash."""
G = """The newest form of money is digital currency. Cryptocurrencies, of which Bitcoin is the best known, are not issued by any government; they are created and recorded by a network of computers. Supporters say that they offer freedom from control by banks. Critics reply that their prices change wildly, that they are used by criminals, and that the computers which create them consume huge amounts of electricity. Dr Lucia Ferraro, a monetary historian, believes that money will continue to change, as it has always done, but that trust will remain its foundation."""
P = passage('p40', 'The Story of Money', 'History', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('People lived without money for most of human history.', 'T', 'A', 'for most of human history, people lived without coins or notes'),
  ('Barter works whenever two people meet.', 'F', 'A', 'it works only when each person has something that the other wants'),
  ('Cattle are easy to carry.', 'F', 'B', 'Cattle fail the test of portability'),
  ('Merchants in Mesopotamia used weighed silver by about 3000 BC.', 'T', 'B', 'by about 3000 BC'),
  ('The first true coins were made in Lydia.', 'T', 'C', 'made in the kingdom of Lydia'),
  ('Roman soldiers were paid in gold bars.', 'NG', 'C', 'used coins to pay their soldiers', 'The metal of the coins is not specified.'),
  ('Roman coins were used only in Italy.', 'F', 'C', 'from Britain to Syria'),
  ('Paper money first appeared in Europe.', 'F', 'D', 'appeared in China'),
  ('Marco Polo invented paper money.', 'F', 'D', 'described this'),
  ('Most people in wealthy countries now pay only in cash.', 'F', 'F', 'coins and notes make up a small part of the total in wealthy countries'),
 ]),
 mcq([
  ('What problem was money invented to solve?', ['Theft.', 'The double coincidence of wants.', 'Rising prices.', 'Lack of gold.'], 1, 'A', 'money was invented to solve it'),
  ('Why did merchants in China use receipts?', ['Coins were forbidden.', 'Copper coins were heavy.', 'Banks asked for them.', 'The emperor wanted paper.'], 1, 'D', 'carrying heavy strings of copper coins'),
  ('What does the passage say money now depends on?', ['Gold.', 'Silver.', 'Trust in the government.', 'Salt.'], 2, 'F', 'depend only on trust in the government'),
 ]),
 feat('Match each development with the correct place, A to D.', ['Lydia', 'China', 'Italian cities', 'Mesopotamia'], [
  ('Weighed pieces of silver served as a standard of value.', 3, 'B', 'weighed pieces of silver as a standard of value'),
  ('The first true coins were made there.', 0, 'C', 'The first true coins were made in the kingdom of Lydia'),
  ('Receipts replaced heavy copper coins.', 1, 'D', 'receipts began to be accepted in place of the coins'),
  ('Accounts and written orders were offered to customers.', 2, 'E', 'held accounts for their customers'),
 ]),
 multi('Which TWO qualities of a good form of money are given in paragraph B?', ['Easy to carry.', 'Hard to copy.', 'Bright in colour.', 'Made of paper.', 'Cheap to produce.'], [0, 1], [('B', 'easy to carry, hard to copy'), ('B', 'easy to carry, hard to copy')]),
 head(['Exchange without money', 'Early forms of money', 'The arrival of coins', 'Notes in the East', 'Lending and banking', 'The end of the gold link', 'Money without governments', 'The history of tea', 'How to save money'],
  [('A', 0, 'obtained what they needed by barter'), ('B', 1, 'The earliest forms of money were ordinary objects'), ('C', 2, 'The first true coins were made'), ('D', 3, 'Paper money appeared in China'), ('E', 4, 'the next great change came with banks'), ('F', 5, 'money lost its last connection with precious metal'), ('G', 6, 'The newest form of money is digital currency')]),
 info([
  ('an example of a problem facing a farmer', 'A', 'A farmer with a spare sheep who needs shoes'),
  ('a list of objects once used as money', 'B', 'shells, salt, cattle, beads and bricks of tea'),
  ('a reason why coins were stamped', 'C', 'to guarantee its weight and purity'),
  ('a description of the risk of a bank run', 'E', 'many customers demand their money at once'),
  ('a criticism relating to electricity', 'G', 'consume huge amounts of electricity'),
 ]),
 ends(['could be exchanged for gold until the 1970s.', 'was used by the Romans to pay soldiers.', 'was stamped with a picture.', 'made it risky for a bank to lend out deposits.', 'was invented in Venice in 1970.', 'is issued by every government.', 'was made of salt.'], [
  ('Many countries\' notes', 0, 'F', 'could be exchanged for a fixed amount of gold'),
  ('Roman money', 1, 'C', 'used coins to pay their soldiers'),
  ('A Lydian coin', 2, 'C', 'stamped with a picture'),
  ('The practice of lending out deposits', 3, 'E', 'it created the risk of a bank run'),
 ]),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Period', 'Detail'],
  [['Barter', 'Works only if each person has something the other [[1]]'], ['About 3000 BC', 'Mesopotamian merchants used weighed [[2]]'], ['About 600 BC', 'Lydian coins were stamped with a [[3]]'], ['13th century', 'Marco Polo described paper [[4]] in China']],
  [(['wants'], 'A', 'something that the other wants'), (['silver'], 'B', 'weighed pieces of silver'), (['picture'], 'C', 'stamped with a picture'), (['money'], 'D', 'Paper money appeared in China'.replace('Paper money appeared in China','Paper money'))], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Merchants leave their coins with a trusted [[1]] in return for a receipt.', 'The receipts are accepted in place of the [[2]].', 'The government takes control and prints official [[3]].', 'Marco Polo describes the system in the [[4]] century.'],
  [(['shop'], 'D', 'a trusted shop'), (['coins'], 'D', 'in place of the coins'), (['notes'], 'D', 'printed official notes'), (['thirteenth'], 'D', 'in the thirteenth century')], 1),
 sent(2, [
  ('Lydia was in what is now western ___.', ['turkey'], 'C', 'western Turkey'),
  ('Banks lend part of deposits and charge ___.', ['interest'], 'E', 'charge interest'),
  ('Bitcoin is the best known of the ___.', ['cryptocurrencies'], 'G', 'Cryptocurrencies, of which Bitcoin is the best known'),
  ('Dr Ferraro is a monetary ___.', ['historian'], 'G', 'a monetary historian'),
 ]),
 short(3, [
  ('What did Roman soldiers receive as pay?', ['coins'], 'C', 'used coins to pay their soldiers'),
  ('What does the cheque come from?', ['a written order', 'written order'], 'E', 'a written order, an ancestor of the cheque'),
  ('What will remain the foundation of money?', ['trust'], 'G', 'trust will remain its foundation'),
 ]),
])
