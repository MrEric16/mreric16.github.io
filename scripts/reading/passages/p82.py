from lib import *
from svgs import *
A = """In just over half a century, the internet has changed from an experiment connecting a handful of computers into a network used by more than five billion people, about two thirds of the world's population. It has altered the way we work, learn, shop, travel and communicate with friends. Many people use it every hour without knowing how it works, or that it was created by a small group of scientists who could not have imagined its size. This passage describes the main steps in its development, explains the difference between the internet and the web and considers some of the problems that it has created."""
B = """The story begins in 1969, when American researchers connected four university computers in a project called ARPANET. The aim was to let scientists share expensive machines and to build a network that would continue to work even if part of it were damaged. On 29 October, a student in California tried to send the first message to a computer at Stanford, 560 kilometres away. He typed only two letters before the system crashed, so the first message sent across the network was lo, as in lo and behold. An hour later, the full message was transmitted successfully."""
C = """The network grew slowly. In 1971 an engineer, Ray Tomlinson, sent the first email between two computers and chose the symbol @ to separate the name of the user from the name of the machine, a choice that has lasted to the present day. Within a few years, email was the most popular use of the network, far more than the sharing of machines that its creators had intended. In 1983, the separate networks adopted a common set of rules, called TCP/IP, which allowed them to exchange data. This date is often regarded as the birth of the internet, which means a network of networks."""
D = """Most people today confuse the internet with the web, but they are different things. The internet is the global system of cables, wireless links and computers that carries data. The World Wide Web is a service that runs on top of it, consisting of pages linked together and viewed by a browser. It was invented in 1989 by a British scientist, Tim Berners-Lee, who was working at CERN, the European laboratory for particle physics, and wanted a simple way for researchers to share documents. The first website went online in 1991, and in 1993 CERN announced that the technology would be free for everyone to use, a decision that made rapid growth possible."""
E = """After that, change was rapid. Easy-to-use browsers appeared in the 1990s, and search engines made it possible to find information among millions of pages. Online shops, video calls and social networks followed. In 2007 the first modern smartphones put the internet in people's pockets, and today most people reach it through a phone, not a computer. Speeds have increased enormously: a film that took hours to download in the year 2000 can now be received in seconds. At the same time, the cost has fallen, so that in many countries a connection is considered as essential as electricity or water."""
F = """The internet has also created problems. Dr Sven Lindgren, a researcher in digital society, identifies three of the most serious. First, privacy: companies collect huge amounts of data about what people read, buy and say, often without their full understanding. Second, false information: a rumour can spread around the world in minutes, long before it can be corrected. Third, inequality: about a third of humanity still has no access, especially in poor and remote regions, and they risk being left behind in education and work. He adds that the dangers are greatest for the young, who spend many hours online."""
G = """Dr Lindgren argues that the answer is not to leave the internet but to learn to use it wisely. Students should check where a piece of information comes from, compare several sources and ask who benefits from a claim before they share it. They should use strong passwords, think carefully before posting photographs and take regular breaks from screens. Many schools now teach digital literacy as a subject, alongside reading and mathematics. Dr Lindgren compares the internet to a city: it offers wonderful opportunities, but a person who walks through it without knowing the rules is likely to be hurt."""
S, PT, W, H = chain(5)
P = passage('p82', 'From ARPANET to the Web', 'Technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('More than five billion people use the internet.', 'T', 'A', 'more than five billion people'),
  ('The internet was created by a large company.', 'F', 'A', 'a small group of scientists'),
  ('ARPANET connected four university computers.', 'T', 'B', 'four university computers'),
  ('The first message was sent in full at the first attempt.', 'F', 'B', 'the system crashed'),
  ('Ray Tomlinson sent the first email.', 'T', 'C', 'Ray Tomlinson, sent the first email'),
  ('The internet and the web are the same thing.', 'F', 'D', 'they are different things'),
  ('The web was invented at CERN.', 'T', 'D', 'working at CERN'),
  ('The first modern smartphones appeared in 2007.', 'T', 'E', 'In 2007 the first modern smartphones'),
  ('Tim Berners-Lee became a millionaire.', 'NG', 'D', 'Tim Berners-Lee', 'His wealth is not discussed.'),
 ]),
 mcq([
  ('Why did the creators want a network that could survive damage?', ['To keep working if part was damaged.', 'To save money.', 'To save paper.', 'To speed up mail.'], 0, 'B', 'continue to work even if part of it were damaged'),
  ('How is the web different from the internet?', ['It is a service that runs on top of it.', 'It is older.', 'It is a cable.', 'It is a phone.'], 0, 'D', 'a service that runs on top of it'),
  ('What does Dr Lindgren advise?', ['Learn to use the internet wisely.', 'Leave the internet.', 'Use it only at night.', 'Buy more devices.'], 0, 'G', 'learn to use it wisely'),
 ]),
 diag('Label the steps in the development of the internet, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['arpanet'], 'B', 'called ARPANET'), (['email'], 'C', 'the first email'), (['web'], 'D', 'The World Wide Web is a service'), (['browsers'], 'E', 'Easy-to-use browsers appeared'), (['smartphones'], 'E', 'modern smartphones')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Researchers connect four [[1]] computers.', 'A student types two letters before the system [[2]].', 'The separate networks adopt a common set of [[3]].', 'CERN announces that the web is free for [[4]] to use.'],
  [(['university'], 'B', 'four university computers'), (['crashed'], 'B', 'the system crashed'), (['rules'], 'C', 'common set of rules'), (['everyone'], 'D', 'free for everyone to use')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Year', 'Event'],
  [['1969', 'Four university computers joined in [[1]]'], ['1971', 'The first [[2]] was sent'], ['1991', 'The first [[3]] went online'], ['1993', 'CERN made the technology [[4]]']],
  [(['arpanet'], 'B', 'called ARPANET'), (['email'], 'C', 'the first email'), (['website'], 'D', 'The first website went online'), (['free'], 'D', 'would be free for everyone')], 1),
 feat('Match each statement with the correct person or organisation, A to D.', ['Ray Tomlinson', 'Tim Berners-Lee', 'Dr Lindgren', 'CERN'], [
  ('He chose the @ symbol.', 0, 'C', 'chose the symbol @'),
  ('He wanted researchers to share documents easily.', 1, 'D', 'a simple way for researchers to share documents'),
  ('He compares the internet to a city.', 2, 'G', 'compares the internet to a city'),
  ('It announced that the technology would be free.', 3, 'D', 'CERN announced'),
 ]),
 multi('Which TWO problems of the internet are mentioned in paragraph F?', ['Privacy.', 'False information.', 'High cost.', 'Noise.', 'Bad weather.'], [0, 1], [('F', 'privacy'), ('F', 'false information')]),
 head(['A network that spans the globe', 'The first message', 'Email and common rules', 'Web and internet are different', 'Faster and cheaper', 'Three dangers', 'Using it wisely', 'The history of the telephone', 'How computers are made'],
  [('A', 0, 'used by more than five billion people'), ('B', 1, 'the first message sent across the network was lo'), ('C', 2, 'adopted a common set of rules'), ('D', 3, 'they are different things'), ('E', 4, 'change was rapid'), ('F', 5, 'identifies three of the most serious'), ('G', 6, 'learn to use it wisely')]),
 info([
  ('a reference to a crashed system', 'B', 'the system crashed'),
  ('a reference to a symbol separating user and machine', 'C', 'separate the name of the user from the name of the machine'),
  ('a reference to a European laboratory', 'D', 'European laboratory for particle physics'),
  ('a comparison of download times', 'E', 'hours to download in the year 2000'),
  ('a comparison with a city', 'G', 'compares the internet to a city'),
 ]),
 ends(['connected four university computers.', 'became the most popular use of the network.', 'runs on top of the internet.', 'advises checking sources.', 'was invented in 1800.', 'carries only films.', 'has no users.'], [
  ('ARPANET', 0, 'B', 'four university computers'),
  ('Email', 1, 'C', 'most popular use of the network'),
  ('The web', 2, 'D', 'runs on top of it'),
  ('Dr Lindgren', 3, 'G', 'check where a piece of information comes from'),
 ]),
 sent(2, [
  ('The first message sent over ARPANET was ___.', ['lo'], 'B', 'was lo'),
  ('Email was invented by Ray ___.', ['tomlinson'], 'C', 'Ray Tomlinson'),
  ('The web was invented by Tim ___.', ['berners-lee'], 'D', 'Tim Berners-Lee'),
  ('Dr Lindgren is a researcher in ___ society.', ['digital'], 'F', 'digital society'),
 ]),
 short(3, [
  ('Where was Berners-Lee working?', ['cern'], 'D', 'CERN'),
  ('What do many schools now teach?', ['digital literacy'], 'G', 'digital literacy'),
  ('How much of humanity has no access?', ['a third', 'about a third'], 'F', 'about a third of humanity'),
 ]),
])
