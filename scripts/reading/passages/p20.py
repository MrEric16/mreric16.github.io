from lib import *
A = """Every day the human body is attacked by bacteria and viruses, and most of the time we never notice, because the immune system defeats them. White blood cells find invaders by recognising antigens, which are molecules on the surface of a germ. When a new germ is met for the first time, the response is slow, and a person may be ill for days before the body wins. Without this defence, even a minor infection could be fatal, and for most of history, many of them were."""
B = """The key discovery was that the immune system has a memory. After an infection, some of the white blood cells survive as memory cells, which can recognise the same germ years later and react within hours. A second infection is therefore usually much milder than the first, or does not cause illness at all. A vaccine is a way of giving the immune system this memory without the illness, and it is one of the cheapest and most effective tools in the history of medicine."""
C = """The idea is older than the science. In 1796 the English doctor Edward Jenner noticed that milkmaids who had caught cowpox, a mild disease, did not catch smallpox. He tested his idea on a boy by injecting him with material from a cowpox sore, and later showed that the boy was protected. The word vaccine comes from vacca, the Latin for cow. In 1980, after a worldwide campaign, the World Health Organization announced that smallpox had been wiped out, the only human disease to be defeated in this way."""
D = """Vaccines work in different ways. Some contain a weakened form of the germ, which can still multiply but cannot cause serious illness. Others contain a killed germ, or only a harmless part of it, such as a protein from its surface. A newer type, the mRNA vaccine, carries instructions that tell the body's own cells to make one harmless protein, which the immune system then learns to recognise. In every case, the aim is to show the immune system an antigen without the danger of the real disease."""
E = """Vaccines protect not only the people who receive them. When enough people in a community are immune, the germ finds it hard to spread, and those who cannot be vaccinated, such as newborn babies, gain some protection too. This effect is called herd immunity. The level needed depends on how infectious the disease is. For a disease that spreads slowly, a smaller share is enough, but for measles, which is highly infectious, about ninety-five per cent of people must be immune."""
F = """Like any medicine, vaccines can have side effects, but these are usually mild, such as a sore arm or a slight fever. Serious reactions are extremely rare. Before a vaccine is approved, it is tested in several phases, starting with small groups and ending with tens of thousands of volunteers, and its safety continues to be monitored afterwards. Doctors also record every report of illness after vaccination, so that a rare problem can be noticed quickly and investigated. Despite this, some people distrust vaccines, and false stories spread online have led to falling vaccination rates in some countries, and to the return of measles outbreaks."""
G = """Researchers are now working on vaccines for diseases that have resisted every attempt, including malaria, which kills more than half a million people a year. In 2021 the World Health Organization recommended a malaria vaccine for children in Africa, a breakthrough after decades of research. Other teams are exploring vaccines against some kinds of cancer. Such work is slow and expensive, but the rewards are large, because a successful vaccine can protect millions of children for the cost of a few coins each. Many experts believe that the next decades will see the most important advances since Jenner."""
P = passage('p20', 'How Vaccines Work', 'Medicine', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Antigens are molecules on the surface of a germ.', 'T', 'A', 'molecules on the surface of a germ'),
  ('The immune system responds quickly to a germ it has never met.', 'F', 'A', 'the response is slow'),
  ('Memory cells can recognise a germ years after an infection.', 'T', 'B', 'recognise the same germ years later'),
  ('Jenner tested his idea on his own child.', 'NG', 'C', 'He tested his idea on a boy', 'The boy is not identified as Jenner\'s child.'),
  ('Smallpox was declared wiped out in 1980.', 'T', 'C', 'In 1980'),
  ('All vaccines contain a living germ.', 'F', 'D', 'Others contain a killed germ'),
  ('Newborn babies can be protected by herd immunity.', 'T', 'E', 'such as newborn babies, gain some protection too'),
  ('Serious reactions to vaccines are common.', 'F', 'F', 'Serious reactions are extremely rare'),
  ('A malaria vaccine was recommended by the WHO in 2021.', 'T', 'G', 'In 2021 the World Health Organization recommended a malaria vaccine'),
 ]),
 mcq([
  ('Why is a second infection usually milder?', ['The germ becomes weaker.', 'Memory cells react quickly.', 'Antibiotics are used.', 'White blood cells multiply slowly.'], 1, 'B', 'react within hours'),
  ('What does the word vaccine come from?', ['a Greek word for medicine', 'the Latin word for cow', 'the name of a doctor', 'an Arabic word for protection'], 1, 'C', 'vacca, the Latin for cow'),
  ('What has led to falling vaccination rates in some countries?', ['rising prices', 'false stories online', 'serious side effects', 'lack of doctors'], 1, 'F', 'false stories spread online'),
 ]),
 multi('Which TWO types of vaccine ingredient are mentioned in paragraph D?', ['A weakened germ.', 'A killed germ.', 'A synthetic metal.', 'A plant extract.', 'A fragment of a bacterium\'s DNA.'], [0, 1], [('D', 'a weakened form of the germ'), ('D', 'Others contain a killed germ')]),
 head(['How the body fights germs', 'The body\'s memory', 'From cows to the end of a disease', 'Different kinds of vaccine', 'Protecting a whole community', 'Safety and distrust', 'The search for new vaccines', 'The cost of a hospital', 'How germs spread by air'],
  [('A', 0, 'the immune system defeats them'), ('B', 1, 'the immune system has a memory'), ('C', 2, 'The idea is older than the science'), ('D', 3, 'Vaccines work in different ways'), ('E', 4, 'Vaccines protect not only the people who receive them'), ('F', 5, 'Like any medicine, vaccines can have side effects'), ('G', 6, 'Researchers are now working on vaccines')]),
 info([
  ('a definition of a type of molecule', 'A', 'molecules on the surface of a germ'),
  ('an observation about people who looked after cows', 'C', 'milkmaids who had caught cowpox'),
  ('an explanation of a newer kind of vaccine', 'D', 'tell the body\'s own cells to make one harmless protein'),
  ('a figure for the share of people who need to be immune to stop measles', 'E', 'about ninety-five per cent'),
  ('a description of testing stages', 'F', 'tested in several phases'),
 ]),
 ends(['can recognise a germ and react within hours.', 'was announced as wiped out in 1980.', 'tell the body\'s cells to make one harmless protein.', 'depends on how infectious the disease is.', 'is found only in children.', 'was invented by the World Health Organization.', 'always causes a serious illness.'], [
  ('A memory cell', 0, 'B', 'react within hours'),
  ('Smallpox', 1, 'C', 'had been wiped out'),
  ('An mRNA vaccine carries instructions that', 2, 'D', 'tell the body\'s own cells to make one harmless protein'),
  ('The level of immunity needed', 3, 'E', 'depends on how infectious the disease is'),
 ]),
 sent(2, [
  ('Jenner was an ___ doctor.', ['english'], 'C', 'the English doctor Edward Jenner'),
  ('A weakened germ cannot cause ___ illness.', ['serious'], 'D', 'cannot cause serious illness'),
  ('Herd immunity protects people who cannot be ___.', ['vaccinated'], 'E', 'who cannot be vaccinated'),
  ('Malaria kills more than half a ___ people a year.', ['million'], 'G', 'more than half a million people a year'),
 ]),
 short(3, [
  ('Besides a slight fever, what side effect is mentioned?', ['sore arm', 'a sore arm'], 'F', 'a sore arm or a slight fever'),
  ('What kind of disease did Jenner\'s milkmaids catch?', ['cowpox'], 'C', 'caught cowpox'),
  ('Who recommended the malaria vaccine?', ['world health organization', 'who'], 'G', 'the World Health Organization recommended'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['A vaccine shows the immune system an [[1]] without the danger of the real disease.', 'Some white blood cells survive as [[2]] cells.', 'If the real germ arrives, these cells react within [[3]].', 'The illness is much [[4]] or does not occur.'],
  [(['antigen'], 'D', 'show the immune system an antigen'), (['memory'], 'B', 'survive as memory cells'), (['hours'], 'B', 'react within hours'), (['milder'], 'B', 'usually much milder than the first')], 1),
])
