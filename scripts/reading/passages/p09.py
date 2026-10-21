from lib import *
A = """For centuries, sailors who lost sight of land could not say exactly where they were. Finding latitude, their position north or south of the equator, was relatively easy: a navigator measured the height of the sun at noon, or of the pole star at night, and consulted a table. Longitude, the position east or west, was a far harder problem. The Earth turns through fifteen degrees every hour, so a navigator who knew the time at his home port, and who could tell when it was noon where he was, could work out how far east or west he had travelled. The difficulty was knowing the time at home. The pendulum clocks of the period lost or gained minutes on a rolling ship, and changes in temperature and humidity made them still less reliable."""
B = """The cost of this ignorance was terrible. In 1707 a fleet of British warships returning from the Mediterranean misjudged its position in thick fog, and four ships were wrecked on the rocks of the Isles of Scilly with the loss of more than a thousand sailors. Public anger forced the government to act. In 1714 Parliament passed the Longitude Act, which offered a prize of up to twenty thousand pounds, a fortune at the time, to anyone who could find a way of determining longitude at sea to within half a degree."""
C = """Two approaches competed for the prize. The first was astronomical. Because the Moon moves across the sky against the background of the stars in a predictable way, a navigator could measure its position, compare it with printed tables, and so calculate the time at Greenwich. The method worked in principle, but the calculations were long and difficult, and they could take a sailor several hours. The second approach was to build a clock accurate enough to keep the time of the home port through a long voyage. Many leading scientists, including Isaac Newton, doubted that such a machine could ever be made, and most of them favoured the astronomical method."""
D = """The man who proved them wrong was John Harrison, a self-taught carpenter and clockmaker from Yorkshire. Harrison understood that the problem lay in the mechanism's sensitivity to its surroundings, and he set about removing each cause of error in turn. He made parts of his clocks from a hard wood that needed no oil, and he combined strips of brass and steel in a way that cancelled out the effect of temperature on the pendulum. In 1730 he travelled to London with his designs, and his first sea clock was tested on a voyage to Lisbon in 1736. It performed well enough for him to receive money to continue."""
E = """Harrison's first three clocks were large and heavy, and he spent nearly thirty years improving them. His fourth machine, finished in 1759, was completely different: it looked like an oversized pocket watch, only about thirteen centimetres across. In 1761 it crossed the Atlantic to Jamaica, and on arrival it had lost just five seconds in eighty-one days, which was well within the standard that the prize required. Yet the Board of Longitude, the committee responsible for the award, refused to pay in full. It demanded further trials and insisted that Harrison hand over the watch and its designs so that copies could be made."""
F = """Some members of the Board were astronomers, and they had a natural preference for their own method. One of them, the Astronomer Royal, Nevil Maskelyne, was involved in judging the tests, and Harrison believed that he could not be impartial. After years of delay, Harrison, by then an old man, appealed to King George III. The king tested a later watch himself and found it excellent, and in 1773 Parliament awarded Harrison a large payment, though never the prize itself. In the writer's view, a man who had solved the problem so convincingly deserved to be rewarded far sooner."""
G = """The new instruments soon proved their worth. Captain James Cook took a copy of Harrison's fourth watch on his second voyage and described it in glowing terms, and within a few decades ships' chronometers had become cheap enough to be carried by most vessels. Navigators could at last fix their position with confidence, and voyages became shorter and safer. The idea that time and place are connected has not gone out of date: modern satellite navigation systems also work by comparing the precise time signals that reach a receiver from space."""
P = passage('p09', 'The Problem of Longitude', 'History of science', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Finding latitude at sea was easier than finding longitude.', 'T', 'A', 'Longitude, the position east or west, was a far harder problem'),
  ('The Earth turns through fifteen degrees every hour.', 'T', 'A', 'The Earth turns through fifteen degrees every hour'),
  ('Pendulum clocks kept accurate time on rolling ships.', 'F', 'A', 'lost or gained minutes on a rolling ship'),
  ('The 1707 disaster happened in fine weather.', 'F', 'B', 'misjudged its position in thick fog'),
  ('The Longitude Act offered a prize to the first person to cross the Atlantic.', 'F', 'B', 'a way of determining longitude at sea to within half a degree'),
  ('Navigators using the Moon had to make long calculations.', 'T', 'C', 'the calculations were long and difficult'),
  ('Isaac Newton believed that an accurate sea clock could be built.', 'F', 'C', 'including Isaac Newton, doubted that such a machine could ever be made'),
  ('Harrison made his first sea clock without any training.', 'NG', 'D', 'a self-taught carpenter and clockmaker', 'He is described as self-taught, but the passage does not say that about his first clock specifically.'),
  ('Harrison\'s fourth machine was about the size of a large pocket watch.', 'T', 'E', 'it looked like an oversized pocket watch'),
  ('The watch lost more than a minute during the voyage to Jamaica.', 'F', 'E', 'it had lost just five seconds in eighty-one days'),
  ('Harrison received the full prize in 1773.', 'F', 'F', 'though never the prize itself'),
  ('Cook\'s first voyage used a copy of Harrison\'s watch.', 'NG', 'G', 'Captain James Cook took a copy of Harrison\'s fourth watch on his second voyage', 'The passage says a copy was taken on the second voyage; it says nothing about the first.'),
 ]),
 tfng([
  ('Harrison should have been rewarded sooner than he was.', 'Y', 'F', 'deserved to be rewarded far sooner'),
  ('The astronomical method was easier to use than the clock method.', 'N', 'C', 'the calculations were long and difficult'),
  ('The Board of Longitude made a sensible decision when it demanded more trials.', 'NG', 'E', 'It demanded further trials', 'The writer reports the demand without judging it.'),
  ('Ships at sea became safer once accurate chronometers were widely used.', 'Y', 'G', 'voyages became shorter and safer'),
  ('Satellite navigation is unrelated to the problem of longitude.', 'N', 'G', 'modern satellite navigation systems also work by comparing the precise time signals'),
  ('Harrison\'s success was achieved by removing causes of error one at a time.', 'Y', 'D', 'removing each cause of error in turn'),
 ], yn=True),
 feat('Which method does each statement describe? Choose A or B. You may use either letter more than once.', ['The astronomical method', 'The sea clock'], [
  ('It involved measuring the position of the Moon.', 0, 'C', 'a navigator could measure its position'),
  ('It required a machine that kept the time of the home port.', 1, 'C', 'keep the time of the home port through a long voyage'),
  ('It involved comparing observations with printed tables.', 0, 'C', 'compare it with printed tables'),
  ('Most leading scientists thought it was more promising.', 0, 'C', 'most of them favoured the astronomical method'),
  ('It was tested on a voyage to Lisbon in 1736.', 1, 'D', 'his first sea clock was tested on a voyage to Lisbon in 1736'),
 ], cls=True),
 ends(['could take a sailor several hours.', 'cancelled the effect of temperature on the pendulum.', 'lost only five seconds in eighty-one days.', 'was a fortune at the time.', 'were wrecked on the rocks off the Isles of Scilly.', 'became cheap enough for most ships to carry.', 'was awarded to the Astronomer Royal.', 'was written by Isaac Newton.'],
  [('The calculations for the astronomical method', 0, 'C', 'they could take a sailor several hours'), ('Harrison\'s combination of brass and steel', 1, 'D', 'cancelled out the effect of temperature on the pendulum'), ('Harrison\'s fourth watch', 2, 'E', 'it had lost just five seconds in eighty-one days'), ('The prize offered by the Longitude Act', 3, 'B', 'a fortune at the time'), ('Four British warships', 4, 'B', 'four ships were wrecked on the rocks of the Isles of Scilly'), ('Ships\' chronometers', 5, 'G', 'ships\' chronometers had become cheap enough to be carried by most vessels')]),
 mcq([
  ('What was the main problem with pendulum clocks at sea?', ['They were too heavy to carry.', 'They stopped working in fog.', 'They were affected by the ship\'s movement and the weather.', 'They could not be read by sailors.'], 2, 'A', 'The pendulum clocks of the period lost or gained minutes on a rolling ship'),
  ('Why did Harrison distrust Nevil Maskelyne?', ['He had copied Harrison\'s designs.', 'He was a supporter of the astronomical method.', 'He had refused to meet the king.', 'He wanted the prize for himself.'], 1, 'F', 'Harrison believed that he could not be impartial'),
  ('What does the writer say about the end of Harrison\'s story?', ['He was paid the prize in full.', 'He regretted submitting the watch.', 'He was rewarded but not by the prize.', 'He was helped by the king to build a clock.'], 2, 'F', 'though never the prize itself'),
 ]),
 head(['The reason why longitude was hard to find', 'A disaster and a reward', 'Two rival ideas', 'A clockmaker with a new approach', 'A watch that passed the test', 'A bitter dispute', 'A lasting influence', 'Why latitude is measured from the equator', 'How the Moon moves around the Earth'],
  [('A', 0, 'Longitude, the position east or west, was a far harder problem'), ('B', 1, 'Public anger forced the government to act'), ('C', 2, 'Two approaches competed for the prize'), ('D', 3, 'The man who proved them wrong was John Harrison'), ('E', 4, 'on arrival it had lost just five seconds in eighty-one days'), ('F', 5, 'Harrison believed that he could not be impartial'), ('G', 6, 'The new instruments soon proved their worth')]),
 info([
  ('an explanation of how a navigator could calculate how far east or west he had travelled', 'A', 'could work out how far east or west he had travelled'),
  ('a description of a naval disaster', 'B', 'four ships were wrecked'),
  ('a reason why scientists doubted the clock method', 'C', 'doubted that such a machine could ever be made'),
  ('a description of how Harrison dealt with temperature changes', 'D', 'combined strips of brass and steel'),
  ('a demand that Harrison hand over his designs', 'E', 'insisted that Harrison hand over the watch and its designs'),
  ('a mention of a famous explorer\'s opinion of the watch', 'G', 'described it in glowing terms'),
 ]),
 sent(3, [
  ('Navigators found latitude by measuring the height of the sun at ___.', ['noon'], 'A', 'the height of the sun at noon'),
  ('The Longitude Act was passed in ___.', ['1714'], 'B', 'In 1714 Parliament passed the Longitude Act'),
  ('Harrison came from the English county of ___.', ['yorkshire'], 'D', 'clockmaker from Yorkshire'),
  ('Harrison made parts of his clocks from a hard wood that needed no ___.', ['oil'], 'D', 'a hard wood that needed no oil'),
  ('Harrison\'s fourth machine was about ___ centimetres across.', ['thirteen', '13'], 'E', 'only about thirteen centimetres across'),
  ('In 1773 Parliament gave Harrison a large ___.', ['payment'], 'F', 'awarded Harrison a large payment'),
 ]),
 short(3, [
  ('Where did the fleet that was wrecked in 1707 go aground?', ['isles of scilly', 'scilly'], 'B', 'the rocks of the Isles of Scilly'),
  ('Who did Harrison appeal to after years of delay?', ['king george iii', 'george iii', 'the king', 'king'], 'F', 'appealed to King George III'),
  ('Which committee was responsible for the award?', ['board of longitude'], 'E', 'the Board of Longitude'),
  ('Whose second voyage used a copy of the watch?', ['captain james cook', 'james cook', 'cook', 'captain cook'], 'G', 'Captain James Cook took a copy'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['The navigator works out when it is [[1]] where he is.', 'He compares this with the time at his [[2]].', 'The Earth turns through fifteen [[3]] every hour.', 'The difference in time shows how far [[4]] or west he has travelled.'],
  [(['noon'], 'A', 'tell when it was noon where he was'), (['home port'], 'A', 'the time at his home port'), (['degrees'], 'A', 'fifteen degrees every hour'), (['east'], 'A', 'how far east or west he had travelled')], 2),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Year', 'Event'],
  [['1707', 'Four ships are wrecked off the [[1]]'], ['1714', 'Parliament passes the [[2]]'], ['1736', 'Harrison\'s first sea clock is tested on a voyage to [[3]]'], ['1761', 'Harrison\'s fourth machine crosses the Atlantic to [[4]]']],
  [(['isles of scilly', 'scilly'], 'B', 'the Isles of Scilly'), (['longitude act'], 'B', 'passed the Longitude Act'), (['lisbon'], 'D', 'voyage to Lisbon in 1736'), (['jamaica'], 'E', 'to Jamaica')], 3),
])
