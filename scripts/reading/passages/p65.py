from lib import *
from svgs import *
A = """How do students get to school? The answer depends on where they live, how far they must travel and what services are available, and it has important consequences for health, for traffic and for the environment. In the imaginary country of Altonia, the Ministry of Education surveyed students in four very different towns to find out how they travel, and published the results as pie charts. The towns were chosen to represent four types of community: a mountain village, a big city, an island and a farming district. This passage describes the findings and considers what other countries can learn from them."""
B = """In the mountain village, half of the students walk to school and the other half go by school bus. The village is small, so many children live within a kilometre of the school, and the steep roads make cycling difficult. Those who live higher up the valley, however, would have to walk for more than an hour, and so the council provides a bus for them. Parents in the village say that the walk is one of the pleasures of the day, since the children meet their friends on the way and arrive at school awake and ready to learn, although in winter the snow can make the journey hard."""
C = """The big city offers four main choices, and students use them in almost equal numbers: a quarter walk, a quarter cycle, a quarter take the bus or metro, and a quarter travel by car. This is the result of a deliberate policy. The city has built safe cycle lanes, made public transport cheap for students and limited parking near schools, so that parents have less reason to drive. City officials say that the aim is not to ban cars but to make other choices equally attractive, and that the policy has reduced the traffic jams outside schools every morning."""
D = """On the island, the picture is very different: nine out of ten students travel by boat. Villages are separated by water, and there are almost no roads, so a ferry is the only practical way to reach the school on the neighbouring island, and the remaining tenth live close enough to walk. The boat journey takes about twenty minutes, and students use it to do their homework or to chat. The island's ferry service is expensive to run, and the Ministry pays almost the whole cost, because it believes that no child should miss an education because of the sea."""
E = """In the farming district, the figures divide into three almost equal parts. About a third of the students are driven to school by their parents, a third come on a school bus, and a third cycle along quiet country roads. Distances are long, and farms are scattered across a wide area, so no single method is suitable for everyone. The district has the highest proportion of students who arrive late, because buses are sometimes delayed by mud in the wet season, and local officials have asked the Ministry for money to pave the worst roads."""
F = """Dr Katarzyna Nowak, a health researcher who analysed the survey, observes that students who walk or cycle are more active and more alert in morning lessons than those who arrive by car. She recommends that every school should encourage active travel where distances allow, and that governments should make the routes safe. According to her calculations, a child who cycles three kilometres to school and back each day gains the equivalent of the exercise recommended for the whole day, without any additional time spent in a gym or on a sports field. She also notes that parents often drive their children only because the roads feel dangerous, and that cheap measures such as crossings, lights and traffic calming can change that feeling."""
G = """The Ministry has not yet decided what to do. It is considering a plan to pay for crossing guards and bicycle sheds in schools throughout the country, which would cost relatively little. It is also considering a scheme in which groups of parents would take turns to walk with children to school, an idea known as a walking bus. Both measures have been tried with success in other countries. The Ministry says that it will make a decision after a second survey, to be carried out in two years, which will show whether the habits of students are changing as roads and services improve."""
P = passage('p65', 'The Way to School', 'Society', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which pie chart, A to D, shows how students travel to school in each place?', [(pie([50, 50]), 160, 120), (pie([25, 25, 25, 25]), 160, 120), (pie([90, 10]), 160, 120), (pie([34, 33, 33]), 160, 120)], [
  ('the mountain village', 0, 'B', 'half of the students walk'),
  ('the big city', 1, 'C', 'in almost equal numbers'),
  ('the island', 2, 'D', 'nine out of ten students travel by boat'),
  ('the farming district', 3, 'E', 'three almost equal parts'),
 ]),
 tfng([
  ('The Ministry surveyed students in four towns.', 'T', 'A', 'four very different towns'),
  ('Altonia is an imaginary country.', 'T', 'A', 'imaginary country of Altonia'),
  ('Half the students in the village go by bus.', 'T', 'B', 'the other half go by school bus'),
  ('Cycling is easy on the village roads.', 'F', 'B', 'steep roads make cycling difficult'),
  ('The city limited parking near schools.', 'T', 'C', 'limited parking near schools'),
  ('City officials want to ban cars.', 'F', 'C', 'not to ban cars'),
  ('The Ministry pays almost the whole cost of the ferry.', 'T', 'D', 'pays almost the whole cost'),
  ('Buses in the farming district are delayed by mud.', 'T', 'E', 'delayed by mud in the wet season'),
  ('The island ferry was built twenty years ago.', 'NG', 'D', 'ferry service is expensive to run', 'Its age is not given.'),
 ]),
 mcq([
  ('Why does the village provide a bus?', ['The roads are flat.', 'Some students live too far to walk.', 'Parents ask for it.', 'The school is new.'], 1, 'B', 'would have to walk for more than an hour'),
  ('Why is no single method suitable in the farming district?', ['Distances are long.', 'There are no roads.', 'Students dislike buses.', 'Schools are closed.'], 0, 'E', 'Distances are long'),
  ('What is a walking bus?', ['A school bus that is slow.', 'Groups of parents walking with children.', 'A bus with no engine.', 'A cycle lane.'], 1, 'G', 'groups of parents would take turns to walk with children'),
 ]),
 feat('Match each statement with the correct place, A to D.', ['Mountain village', 'Big city', 'Island', 'Farming district'], [
  ('The council provides a bus for children who live higher up.', 0, 'B', 'the council provides a bus for them'),
  ('Parking near schools is limited.', 1, 'C', 'limited parking near schools'),
  ('Students sometimes do homework on the way.', 2, 'D', 'use it to do their homework'),
  ('Local officials want money to pave roads.', 3, 'E', 'pave the worst roads'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Place', 'Detail'],
  [['Village', 'Children meet friends on the [[1]]'], ['City', 'Safe [[2]] lanes were built'], ['Island', 'The journey takes about twenty [[3]]'], ['Farming district', 'Buses are delayed by [[4]]']],
  [(['way'], 'B', 'on the way'), (['cycle'], 'C', 'safe cycle lanes'), (['minutes'], 'D', 'twenty minutes'), (['mud'], 'E', 'delayed by mud')], 1),
 multi('Which TWO measures does the Ministry consider in paragraph G?', ['Crossing guards and bicycle sheds.', 'A walking bus.', 'Free cars for families.', 'New schools.', 'Longer holidays.'], [0, 1], [('G', 'pay for crossing guards and bicycle sheds'), ('G', 'groups of parents would take turns to walk with children')]),
 head(['Asking how students travel', 'Walking in the mountains', 'A balanced city', 'Crossing the water', 'Three equal ways', 'Health benefits', 'Plans for change', 'The history of the bus', 'Learning to swim'],
  [('A', 0, 'surveyed students in four very different towns'), ('B', 1, 'half of the students walk to school'), ('C', 2, 'almost equal numbers'), ('D', 3, 'nine out of ten students travel by boat'), ('E', 4, 'three almost equal parts'), ('F', 5, 'more active and more alert in morning lessons'), ('G', 6, 'The Ministry has not yet decided what to do')]),
 info([
  ('a reference to meeting friends on the way', 'B', 'meet their friends on the way'),
  ('a statement of the aim of city policy', 'C', 'make other choices equally attractive'),
  ('a reference to the cost of a boat service', 'D', 'expensive to run'),
  ('a request for help with roads', 'E', 'asked the Ministry for money to pave the worst roads'),
  ('a reference to a later survey', 'G', 'second survey'),
 ]),
 ends(['has built safe cycle lanes.', 'travel by boat.', 'recommends active travel.', 'will carry out a second survey.', 'bans cycling.', 'closes the ferry.', 'builds new schools.'], [
  ('The city', 0, 'C', 'built safe cycle lanes'),
  ('Island students', 1, 'D', 'travel by boat'),
  ('Dr Nowak', 2, 'F', 'encourage active travel'),
  ('The Ministry', 3, 'G', 'a second survey, to be carried out in two years'),
 ]),
 sent(2, [
  ('The Ministry of ___ carried out the survey.', ['education'], 'A', 'Ministry of Education'),
  ('On the island, ___ out of ten students travel by boat.', ['nine', '9'], 'D', 'nine out of ten'),
  ('Dr Nowak is a health ___.', ['researcher'], 'F', 'a health researcher'),
  ('An idea in which parents walk children to school is called a ___ bus.', ['walking'], 'G', 'walking bus'),
 ]),
 short(3, [
  ('How long is the boat journey?', ['twenty minutes', 'about twenty minutes'], 'D', 'about twenty minutes'),
  ('Who drives about a third of farming students?', ['parents', 'their parents'], 'E', 'driven to school by their parents'),
  ('How far does the cycling child travel to school?', ['three kilometres'], 'F', 'three kilometres'),
 ]),
])
