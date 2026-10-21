from lib import *
from svgs import *
A = """When it is noon in Tashkent, it is seven in the morning in London in winter, ten in the morning in Moscow, and three in the afternoon in Beijing. These differences are caused by the rotation of the Earth, which turns once every twenty-four hours, so that the sun rises in the east before it rises in the west. For most of history, nobody needed to worry about the difference. Each town set its clocks by the sun, with noon defined as the moment when the sun was highest in the sky. The coming of the railway, however, made this system impossible, and led to the creation of the time zones that we use today."""
B = """In the early nineteenth century, a traveller going from one town to another found that the local time changed with every few kilometres: if he travelled west, noon arrived later, and if he travelled east, it arrived earlier. This was only a small difficulty for people on horseback, but for the railways it was a nightmare. A timetable that listed the departure of a train at ten o'clock had to say in whose time. In Britain, railway companies solved the problem in the 1840s by using a single time, which was London time, throughout their network, and soon most towns adopted it for everything."""
C = """The problem was even greater in North America, which is wider than Britain, and where there were hundreds of local times in use in the 1870s. Railway companies used more than fifty different times, and passengers had to change their watches again and again. In 1883, the American railways introduced four standard time zones, each one hour apart, and almost all of the country adopted them within a year. By dividing the country into broad belts, they solved the problem without going to the extreme of using a single time for the entire continent."""
D = """The world followed. In 1884, delegates from twenty-five countries met in Washington to agree on a prime meridian, a line of zero longitude from which all others would be measured. They chose the line which passes through the Royal Observatory at Greenwich, near London, partly because most of the world's shipping already used it on charts. The Earth was divided into twenty-four zones, each fifteen degrees of longitude wide, since the sun appears to move through fifteen degrees every hour. Time in each zone is set by counting hours ahead of or behind Greenwich Mean Time, which is today replaced by Coordinated Universal Time."""
E = """In practice, zones are not straight lines on the map. Countries draw the boundaries to suit themselves, so that a region does not have two times. China, which is as wide as the continental United States, uses a single time throughout the country, and in winter the sun rises in the far west of China at about ten in the morning by official time. Russia, the largest country, has eleven zones. Some countries use zones that differ from their neighbours' by half an hour or forty-five minutes: India is five and a half hours ahead of Greenwich, and Nepal is five hours and forty-five minutes ahead."""
F = """Uzbekistan lies in a single zone, five hours ahead of Greenwich, and it does not change its clocks in summer. Many other countries put the clocks forward by an hour in spring to take advantage of longer evenings, a practice called daylight saving time, although its benefits are disputed and a number of countries have abandoned it. The zones also meet at the International Date Line, which runs roughly along the line of 180 degrees of longitude in the Pacific. A traveller who crosses it from west to east repeats a day; one who crosses it from east to west loses a day."""
G = """Dr Anton Weiss, a historian of science, says that the time zones are a good example of how technology forces people to cooperate. Before the railways and telegraph, nobody saw any reason to agree on the time; afterwards, the advantages were so great that countries accepted a single system. Today the internet and global trade are creating a need for still greater co-ordination. Computer systems around the world use Coordinated Universal Time to record events, so that a transaction in Tashkent and one in Toronto can be placed in order. Dr Weiss adds that although the time is a human invention, the Earth's rotation, which makes the day, is not."""
P = passage('p85', 'Why the World Has Time Zones', 'Geography', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Earth turns once every twenty-four hours.', 'T', 'A', 'once every twenty-four hours'),
  ('Towns once set their clocks by the sun.', 'T', 'A', 'set its clocks by the sun'),
  ('British railway companies used London time.', 'T', 'B', 'London time'),
  ('North American railways introduced four time zones in 1883.', 'T', 'C', 'four standard time zones'),
  ('Delegates from twenty-five countries met in Washington.', 'T', 'D', 'delegates from twenty-five countries'),
  ('The prime meridian passes through Moscow.', 'F', 'D', 'Royal Observatory at Greenwich'),
  ('China uses a single time zone.', 'T', 'E', 'single time throughout the country'),
  ('Nepal is five hours ahead of Greenwich.', 'F', 'E', 'five hours and forty-five minutes'),
  ('Uzbekistan introduced its time zone in 1991.', 'NG', 'F', 'Uzbekistan lies in a single zone', 'The date is not given.'),
 ]),
 mcq([
  ('Why were local times a problem for railways?', ['A timetable had to say in whose time.', 'Trains were slow.', 'Clocks were expensive.', 'Stations were small.'], 0, 'B', 'had to say in whose time'),
  ('Why was Greenwich chosen?', ['Most shipping already used it on charts.', 'It was the highest place.', 'It was the oldest city.', 'It was near the sea.'], 0, 'D', 'most of the world\'s shipping already used it on charts'),
  ('What does Dr Weiss say about technology?', ['It forces people to cooperate.', 'It is too fast.', 'It is harmful.', 'It is dull.'], 0, 'G', 'technology forces people to cooperate'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The Earth turns once every twenty-four [[1]].', 'Each zone is fifteen degrees of [[2]] wide.', 'Times are counted ahead of or behind Greenwich Mean [[3]].', 'A traveller crossing the date line from west to east repeats a [[4]].'],
  [(['hours'], 'A', 'every twenty-four hours'), (['longitude'], 'D', 'degrees of longitude wide'), (['time'], 'D', 'Greenwich Mean Time'), (['day'], 'F', 'repeats a day')], 1),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Place', 'Detail'],
  [['Britain', 'Railways used [[1]] time'], ['North America', 'Four standard [[2]] adopted in 1883'], ['China', 'Uses a [[3]] time throughout'], ['India', 'Five and a half hours [[4]] of Greenwich']],
  [(['london'], 'B', 'London time'), (['time zones'], 'C', 'four standard time zones'), (['single'], 'E', 'single time throughout the country'), (['ahead'], 'E', 'hours ahead of Greenwich')], 2),
 feat('Match each statement with the correct place, A to D.', ['Britain', 'North America', 'China', 'Russia'], [
  ('Railway companies adopted London time.', 0, 'B', 'London time'),
  ('Passengers had to change their watches again and again.', 1, 'C', 'change their watches again and again'),
  ('It uses one time throughout the country.', 2, 'E', 'single time throughout the country'),
  ('It has eleven zones.', 3, 'E', 'eleven zones'),
 ]),
 multi('Which TWO countries with unusual time differences are mentioned in paragraph E?', ['India.', 'Nepal.', 'Japan.', 'Brazil.', 'Egypt.'], [0, 1], [('E', 'India is five and a half hours'), ('E', 'Nepal is five hours and forty-five minutes')]),
 head(['A turning Earth', 'Trains and timetables', 'A bigger problem across a continent', 'A world meeting', 'Zones that bend', 'Summer clocks and a line in the Pacific', 'Cooperation by necessity', 'The history of watches', 'Famous trains'],
  [('A', 0, 'caused by the rotation of the Earth'), ('B', 1, 'for the railways it was a nightmare'), ('C', 2, 'The problem was even greater in North America'), ('D', 3, 'delegates from twenty-five countries met in Washington'), ('E', 4, 'zones are not straight lines on the map'), ('F', 5, 'daylight saving time'), ('G', 6, 'technology forces people to cooperate')]),
 info([
  ('a reference to a difficulty for railways', 'B', 'a nightmare'),
  ('a reference to hundreds of local times', 'C', 'hundreds of local times'),
  ('a reference to shipping charts', 'D', 'shipping already used it on charts'),
  ('a reference to the sun rising late in western China', 'E', 'far west of China'),
  ('a reference to recording events by computer', 'G', 'record events'),
 ]),
 ends(['were set by the sun.', 'made local times impossible.', 'was chosen in 1884.', 'runs through the Pacific.', 'divides China.', 'was invented by Dr Weiss.', 'ends at Moscow.'], [
  ('Local times', 0, 'A', 'set its clocks by the sun'),
  ('The railways', 1, 'A', 'made this system impossible'),
  ('The Greenwich meridian', 2, 'D', 'In 1884'),
  ('The International Date Line', 3, 'F', 'in the Pacific'),
 ]),
 sent(2, [
  ('Noon was the moment when the sun was ___ in the sky.', ['highest'], 'A', 'highest in the sky'),
  ('The railways of Britain adopted ___ time.', ['london'], 'B', 'London time'),
  ('Russia, the largest country, has ___ zones.', ['eleven', '11'], 'E', 'eleven zones'),
  ('Dr Weiss is a historian of ___.', ['science'], 'G', 'historian of science'),
 ]),
 short(3, [
  ('How wide is each zone?', ['fifteen degrees'], 'D', 'fifteen degrees'),
  ('What is moving the clocks forward in spring called?', ['daylight saving time', 'daylight saving'], 'F', 'daylight saving time'),
  ('Which time do computers use to record events?', ['coordinated universal time', 'universal time'], 'G', 'Coordinated Universal Time'),
 ]),
])
