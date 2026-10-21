from lib import *
from svgs import *
A = """In 1800, the fastest way to travel over land was on horseback, and a journey of a few hundred kilometres took days. Seventy years later, a person could cross a continent by train in a week. The railway was one of the most powerful inventions in history, and it changed not only how people travelled but also how they worked, traded, told the time and thought about distance. Today, high-speed trains run at more than three hundred kilometres an hour and are among the cleanest forms of transport. This passage follows the story of the railway from the first rails to the modern era, and looks at its future."""
B = """Railways began long before the steam engine. In mines and quarries, wooden rails had been used for centuries to help horses pull heavy loads, since a wheel running on a smooth rail meets much less resistance than one on a rough road. In the eighteenth century, iron replaced wood. The missing element was a source of power. In 1804, Richard Trevithick built a steam locomotive in Wales which hauled ten tonnes of iron and seventy men along a track, but it was too heavy and broke the cast-iron rails. Several other engineers experimented in the following years."""
C = """The decisive step was taken by George Stephenson. His locomotive, Locomotion, pulled the first train on the Stockton and Darlington Railway in England in 1825, and in 1829 his son Robert's engine, the Rocket, won a competition by reaching a speed of about forty-eight kilometres an hour. The Liverpool and Manchester Railway, which opened in 1830, was the first line to rely entirely on steam locomotives and to carry both passengers and goods on a regular timetable. Its success sparked a boom, and within twenty years Britain had thousands of kilometres of track."""
D = """Railways spread rapidly across the world. In the United States, the first transcontinental line was completed in 1869, when two lines met at Promontory Summit in Utah and a ceremonial spike was driven in, reducing the journey from coast to coast from months to about a week. In Russia, the Trans-Siberian Railway, begun in 1891, eventually stretched over nine thousand kilometres from Moscow to Vladivostok. Central Asia was linked by the Trans-Caspian Railway, whose line reached Samarkand in 1888 and later extended to Tashkent, bringing the cities of the Silk Road into a new network."""
E = """The railway transformed society. Goods could be carried cheaply and quickly, so that fresh food reached the cities, factories sold their products to distant markets, and farmers could specialise in the crops best suited to their land. Cities grew around stations, and ordinary people could for the first time live in one town and work in another. The need for timetables forced towns to adopt a common time, which led to standard time zones. Railways also created large numbers of jobs, from engineers and drivers to ticket sellers and porters, and they brought news, letters and newspapers to places which had been isolated."""
F = """The steam locomotive reigned for more than a century, but its time came to an end. Steam engines were heavy, dirty and wasted most of their energy. From the early twentieth century, diesel and electric locomotives, which are cleaner and more efficient, began to replace them. Electric trains are especially suitable for busy lines since they produce no smoke where they run, and they can be powered from renewable sources. By the middle of the century, many countries were closing branch lines as cars and aeroplanes took passengers and freight, and some people believed that the railway had no future."""
G = """The railway has, however, made a comeback. Japan opened the first high-speed line, the Shinkansen, in 1964, and similar networks have since been built in France, Spain, China and many other countries. In Uzbekistan, the Afrosiyob high-speed train connects Tashkent with Samarkand and other cities in a fraction of the time that the journey once took. Dr Peter Lindqvist, a transport economist, argues that on distances between about two hundred and eight hundred kilometres, high-speed trains beat both planes and cars, because they run from city centre to city centre and release far less carbon dioxide per passenger. He expects a new golden age of rail, driven by concern for the climate."""
P = passage('p98', 'The Age of the Railway', 'History of technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('In 1800, horses were the fastest way to travel over land.', 'T', 'A', 'horseback'),
  ('High-speed trains run at more than three hundred kilometres an hour.', 'T', 'A', 'more than three hundred kilometres an hour'),
  ('Railways began with the steam engine.', 'F', 'B', 'long before the steam engine'),
  ('Trevithick\'s locomotive broke the rails.', 'T', 'B', 'broke the cast-iron rails'),
  ('The Rocket won a competition in 1829.', 'T', 'C', 'in 1829'),
  ('The Liverpool and Manchester Railway opened in 1830.', 'T', 'C', 'opened in 1830'),
  ('The first US transcontinental line was completed in 1869.', 'T', 'D', 'completed in 1869'),
  ('The Trans-Siberian Railway runs from Moscow to Saint Petersburg.', 'F', 'D', 'from Moscow to Vladivostok'),
  ('George Stephenson was born in a poor family.', 'NG', 'C', 'George Stephenson', 'His family background is not given.'),
 ]),
 mcq([
  ('Why did wooden rails help horses?', ['A wheel meets less resistance on a smooth rail.', 'They were cheaper.', 'They were soft.', 'They were longer.'], 0, 'B', 'much less resistance'),
  ('What was one effect of the railway on time?', ['Towns adopted a common time.', 'Days became longer.', 'Clocks were banned.', 'Watches stopped.'], 0, 'E', 'common time'),
  ('When does Dr Lindqvist say high-speed trains beat planes?', ['On distances of about 200 to 800 km.', 'On all distances.', 'Under 50 km.', 'Over 3000 km.'], 0, 'G', 'two hundred and eight hundred kilometres'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Year', 'Event'],
  [['1804', 'Trevithick built a steam [[1]]'], ['1830', 'Liverpool and Manchester Railway [[2]]'], ['1869', 'First [[3]] line completed in the USA'], ['1964', 'Japan opened the [[4]]']],
  [(['locomotive'], 'B', 'steam locomotive'), (['opened'], 'C', 'opened in 1830'), (['transcontinental'], 'D', 'transcontinental line'), (['shinkansen'], 'G', 'Shinkansen')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Wooden rails help horses pull [[1]] loads.', 'Iron replaced [[2]].', 'Locomotives run to a regular [[3]].', 'Cleaner locomotives replace [[4]] engines.'],
  [(['heavy'], 'B', 'heavy loads'), (['wood'], 'B', 'replaced wood'), (['timetable'], 'C', 'regular timetable'), (['steam'], 'F', 'Steam engines')], 1),
 feat('Match each statement with the correct item, A to D.', ['Trevithick', 'Stephenson', 'Promontory Summit', 'Afrosiyob'], [
  ('He built a steam locomotive in Wales.', 0, 'B', 'in Wales'),
  ('His engine pulled the first train on the Stockton and Darlington Railway.', 1, 'C', 'first train on the Stockton and Darlington Railway'),
  ('Two lines met there in Utah.', 2, 'D', 'Utah'),
  ('It connects Tashkent with Samarkand.', 3, 'G', 'Tashkent with Samarkand'),
 ]),
 multi('Which TWO effects of the railway on food and trade are mentioned in paragraph E?', ['Fresh food reached the cities.', 'Factories sold products to distant markets.', 'Food became free.', 'Markets closed.', 'Farms disappeared.'], [0, 1], [('E', 'fresh food reached the cities'), ('E', 'distant markets')]),
 head(['A revolution in travel', 'Rails before engines', 'Stephenson and the Rocket', 'Across continents', 'A changed society', 'The end of steam', 'A modern revival', 'The history of cars', 'Airports'],
  [('A', 0, 'one of the most powerful inventions in history'), ('B', 1, 'wooden rails had been used for centuries'), ('C', 2, 'The decisive step'), ('D', 3, 'Railways spread rapidly across the world'), ('E', 4, 'transformed society'), ('F', 5, 'its time came to an end'), ('G', 6, 'made a comeback')]),
 info([
  ('a reference to a ceremonial spike', 'D', 'ceremonial spike'),
  ('a reference to Samarkand in 1888', 'D', 'reached Samarkand in 1888'),
  ('a reference to jobs for porters', 'E', 'porters'),
  ('a reference to closing branch lines', 'F', 'closing branch lines'),
  ('a reference to carbon dioxide', 'G', 'carbon dioxide'),
 ]),
 ends(['used wooden rails.', 'won a competition.', 'reached Samarkand in 1888.', 'beat planes on mid distances.', 'were invented in 1990.', 'was run by horses.', 'ended in 1800.'], [
  ('Mines and quarries', 0, 'B', 'wooden rails'),
  ('The Rocket', 1, 'C', 'won a competition'),
  ('The Trans-Caspian Railway', 2, 'D', 'reached Samarkand in 1888'),
  ('High-speed trains', 3, 'G', 'beat both planes and cars'),
 ]),
 sent(2, [
  ('Trevithick\'s locomotive was built in ___.', ['1804'], 'B', 'In 1804'),
  ('The Trans-Siberian Railway was begun in ___.', ['1891'], 'D', 'begun in 1891'),
  ('Cities grew around ___.', ['stations'], 'E', 'around stations'),
  ('Dr Lindqvist is a transport ___.', ['economist'], 'G', 'transport economist'),
 ]),
 short(3, [
  ('How fast was the Rocket?', ['forty-eight kilometres', 'about forty-eight'], 'C', 'about forty-eight kilometres'),
  ('How long is the Trans-Siberian Railway?', ['nine thousand kilometres'], 'D', 'nine thousand kilometres'),
  ('What replaced steam locomotives?', ['diesel', 'electric'], 'F', 'diesel and electric locomotives'),
 ]),
])
