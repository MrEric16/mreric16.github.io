from lib import *
from svgs import *
A = """Getting around a city is a matter of choice, and the choices that people make change over time as new services appear and old ones decline. The imaginary country of Calderia provides a useful example, because its transport authority has recorded the number of journeys by each type of transport since 1990. This passage looks at four of them: the metro, buses, bicycles and private cars. Each shows a different pattern, and each has a lesson for planners in other countries."""
B = """The metro is the most obvious success. The first line opened in 1995, and in the early years few people used it, since there were only a handful of stations. As new lines were added, the number of passengers has risen every year, and the system now carries more than a million people a day. Its trains are frequent, quiet and reliable, and a journey takes the same time whatever the traffic is like, which is the chief reason for its popularity."""
C = """Bus travel has moved in the opposite direction. In 1990, buses carried more passengers than any other form of public transport, but the number has fallen steadily ever since. Buses are slow in heavy traffic, and when the metro opened many routes were cut to save money, which made the network harder to use. The authority now plans to give buses their own lanes, so that they do not have to wait in queues of cars."""
D = """Cycling shows a pattern with a peak. The number of cyclists rose during the 1990s, when the city built its first cycle lanes, and it reached its highest point in 2008. After that, it fell, partly because a number of serious accidents made people afraid, and partly because the lanes were not connected and ended suddenly at busy junctions. Recently the fall has slowed, as the authority has begun to repair and link the lanes."""
E = """The use of private cars has behaved differently from the other three. Car journeys rose during the 1990s, as incomes grew, and then they levelled off. For the last fifteen years the number has stayed almost constant, even though the population has grown. Experts say that this is evidence that the metro has attracted drivers away from their cars, preventing a growth in traffic that would otherwise have taken place."""
F = """Dr Nadia Rahimova, a transport planner, believes that the lesson of the four cases is that people respond to quality and not to persuasion. The metro succeeded because it was fast and reliable, not because the government told people to use it. Cycling declined when it became unsafe. She argues that campaigns urging people to leave their cars at home will not work unless an attractive alternative is already available, and that planners must therefore build first and encourage afterwards. She adds that surveys of passengers in many cities show the same result: travellers rank speed, safety and reliability well above price, and they will pay more for a service that gets them to work on time every day. Where such a service does not yet exist, she says, even the best advertising will fail."""
G = """The authority hopes to learn from its experience. Its plan for the next decade includes two new metro lines, bus lanes on the busiest streets, and a connected network of protected cycle routes. It also plans to introduce a charge for cars entering the city centre, with the money used to improve public transport. If the plan succeeds, the number of car journeys may at last begin to fall, which would mean cleaner air, quieter streets and healthier citizens. The authority will publish figures every year, so that residents can judge for themselves whether the money is being well spent, and it has promised to change course if the results are disappointing."""
P = passage('p57', 'Getting Around Calderia', 'Society', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the trend for each type of transport described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('plateau'), 160, 120)], [
  ('the metro', 0, 'B', 'the number of passengers has risen every year'),
  ('buses', 1, 'C', 'the number has fallen steadily ever since'),
  ('bicycles', 2, 'D', 'it reached its highest point in 2008'),
  ('private cars', 3, 'E', 'they levelled off'),
 ]),
 tfng([
  ('The transport authority has recorded journeys since 1990.', 'T', 'A', 'since 1990'),
  ('Calderia is an imaginary country.', 'T', 'A', 'The imaginary country of Calderia'),
  ('The first metro line opened in 1995.', 'T', 'B', 'The first line opened in 1995'),
  ('Metro journey times depend on the traffic.', 'F', 'B', 'a journey takes the same time whatever the traffic is like'),
  ('Buses carried more passengers than any other public transport in 1990.', 'T', 'C', 'buses carried more passengers than any other form of public transport'),
  ('Bus routes were increased when the metro opened.', 'F', 'C', 'many routes were cut to save money'),
  ('Cycling numbers peaked in 2008.', 'T', 'D', 'highest point in 2008'),
  ('Cycle lanes were connected from the beginning.', 'F', 'D', 'the lanes were not connected'),
  ('Most people in Calderia now own two cars.', 'NG', 'E', 'The use of private cars', 'Car ownership figures are not given.'),
 ]),
 mcq([
  ('What is the chief reason for the popularity of the metro?', ['Cheap tickets.', 'A journey takes the same time whatever the traffic.', 'Good views.', 'Free food.'], 1, 'B', 'a journey takes the same time whatever the traffic is like'),
  ('Why did cycling decline?', ['Winters became colder.', 'Accidents and unconnected lanes.', 'The metro was free.', 'Bicycles became expensive.'], 1, 'D', 'a number of serious accidents made people afraid'),
  ('What does Dr Rahimova believe?', ['People respond to quality, not persuasion.', 'Cars should be banned.', 'Cycling is dangerous.', 'Buses are best.'], 0, 'F', 'people respond to quality and not to persuasion'),
 ]),
 multi('Which TWO reasons for the fall in cycling are given in paragraph D?', ['Serious accidents made people afraid.', 'The lanes were not connected.', 'Bicycles became too expensive.', 'The weather became worse.', 'The metro became cheaper.'], [0, 1], [('D', 'serious accidents made people afraid'), ('D', 'the lanes were not connected')]),
 head(['Choosing how to travel', 'An underground success', 'A service in decline', 'A rise and then a fall on two wheels', 'Cars hold steady', 'What the cases teach', 'Plans for the future', 'The history of the bicycle', 'How aeroplanes work'],
  [('A', 0, 'This passage looks at four of them'), ('B', 1, 'The metro is the most obvious success'), ('C', 2, 'Bus travel has moved in the opposite direction'), ('D', 3, 'Cycling shows a pattern with a peak'), ('E', 4, 'The use of private cars has behaved differently'), ('F', 5, 'the lesson of the four cases'), ('G', 6, 'The authority hopes to learn from its experience')]),
 info([
  ('a reference to frequent trains', 'B', 'frequent, quiet and reliable'),
  ('a plan to give buses their own lanes', 'C', 'their own lanes'),
  ('a reference to repairing and linking lanes', 'D', 'repair and link the lanes'),
  ('an explanation of why traffic did not grow', 'E', 'the metro has attracted drivers away from their cars'),
  ('a plan for a charge on cars', 'G', 'a charge for cars entering the city centre'),
 ]),
 ends(['has risen every year.', 'was cut to save money.', 'reached its highest point in 2008.', 'stayed almost constant.', 'is free for everyone.', 'was banned in 1990.', 'is not used in cities.'], [
  ('The number of metro passengers', 0, 'B', 'has risen every year'),
  ('Many bus routes', 1, 'C', 'many routes were cut to save money'),
  ('Cycling', 2, 'D', 'it reached its highest point in 2008'),
  ('The number of car journeys', 3, 'E', 'the number has stayed almost constant'),
 ]),
 sent(2, [
  ('The metro system now carries more than a ___ people a day.', ['million'], 'B', 'more than a million people a day'),
  ('The authority plans to give buses their own ___.', ['lanes'], 'C', 'their own lanes'),
  ('Dr Rahimova is a transport ___.', ['planner'], 'F', 'a transport planner'),
  ('The authority plans a charge for cars entering the city ___.', ['centre'], 'G', 'the city centre'),
 ]),
 short(3, [
  ('When did the first metro line open?', ['1995'], 'B', 'opened in 1995'),
  ('What did accidents make people feel?', ['afraid'], 'D', 'made people afraid'),
  ('What will the charge money improve?', ['public transport'], 'G', 'improve public transport'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'The metro has attracted more passengers every year, while bus use has [[1]]. Cycling reached a peak in 2008 and then fell because lanes were not [[2]]. Car use has been [[3]] for fifteen years, and Dr Rahimova says planners should [[4]] first.',
  [(['fallen'], 'C', 'has fallen steadily'), (['connected'], 'D', 'not connected'), (['constant'], 'E', 'almost constant'), (['build'], 'F', 'build first')], 1,
  bank=['fallen', 'connected', 'constant', 'build', 'risen', 'closed', 'cheap', 'persuade']),
])
