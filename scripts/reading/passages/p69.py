from lib import *
from svgs import *
A = """Mount Zandra, the highest peak of the imaginary island of Zendia, has had a weather station on its summit ridge for thirty years. The station was built by a small team of scientists who wanted to understand how conditions change through the year in a mountain environment, and it has been staffed by volunteers ever since. Every day they record the temperature, the depth of snow, the speed of the wind and the number of climbers who pass the station on their way to the top. The records are valuable not only for science but also for the mountain guides, who use them to decide when it is safe to take visitors up."""
B = """The temperature on the ridge follows the shape of the year. In January the average is more than twenty degrees below freezing, and then it rises through spring until it reaches its highest point in July, when it climbs to just above zero. After July it falls again as the days shorten. The pattern is regular, and the volunteers can predict it within a few degrees, but the changes from week to week can be dramatic, and the temperature has been known to fall by fifteen degrees in an afternoon when a storm arrives from the west."""
C = """Snow depth shows a reverse pattern. In January the snow on the ridge is deep, often reaching three metres, but as the temperature rises the snow begins to melt, and the depth decreases until in July and August the ground is almost clear. It then deepens again as autumn storms arrive. The melting snow is the main source of the water that flows in the valley rivers, and the farmers below the mountain watch the depth anxiously, since a thin winter snowfall can mean a dry summer for their fields."""
D = """Wind speed behaves in the most unpredictable way of all. It goes up and down from day to day and even from hour to hour, with no seasonal pattern that the volunteers have been able to find. A calm morning can be followed by a gale in the afternoon, with gusts that knock a person off his feet, and then by calm again at night. The unpredictability is one reason why the mountain is dangerous. Guides check the wind speed every hour, and they turn back groups if the gusts exceed sixty kilometres an hour, however good the view or the weather may seem at lower levels."""
E = """The number of climbers shows an altogether different pattern. For most of the thirty years it stayed at a low level, with only a few hundred people a year, mainly experienced mountaineers. Then, about eight years ago, a documentary film about the mountain was shown on television around the world, and within two seasons the numbers jumped, and they have remained high. Today more than ten thousand people try to reach the summit every year, and the rangers say that this is too many for the narrow path, which is wearing away, and for the small mountain huts, which are often full."""
F = """Dr Lars Eklund, the scientist who runs the station, believes that the four sets of records show that natural and human influences can be separated. The temperature and snow follow the seasons, the wind follows no rule, and the number of climbers depends on the decisions of people, which are influenced by fashions and by films. He says that the first three can only be observed, while the last can be controlled, and he urges the authorities to introduce a limit on the number of climbers each day, as has been done on some other famous mountains."""
G = """The authorities are considering his proposal. A daily limit would protect the path and the huts, and would make the mountain safer, since crowded paths cause accidents. But local businesses fear that a limit would reduce their income, and some climbers say that nobody should be prevented from enjoying a mountain. The rangers suggest a compromise, in which climbers would book a place online, with a higher number permitted at weekends. A decision is expected after the next summer season, when the station will have another year of records to show how the numbers are changing."""
P = passage('p69', 'The Weather Station on Mount Zandra', 'Geography', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows each type of record from Mount Zandra?', [(graph('peak'), 160, 120), (graph('dip'), 160, 120), (graph('fluct'), 160, 120), (graph('sharp'), 160, 120)], [
  ('temperature through the year', 0, 'B', 'its highest point in July'),
  ('snow depth through the year', 1, 'C', 'the ground is almost clear'),
  ('wind speed', 2, 'D', 'goes up and down from day to day'),
  ('the number of climbers', 3, 'E', 'within two seasons the numbers jumped'),
 ]),
 tfng([
  ('Mount Zandra is on an imaginary island.', 'T', 'A', 'imaginary island of Zendia'),
  ('The station has operated for thirty years.', 'T', 'A', 'for thirty years'),
  ('Volunteers staff the station.', 'T', 'A', 'staffed by volunteers'),
  ('The average January temperature is above freezing.', 'F', 'B', 'more than twenty degrees below freezing'),
  ('The temperature has fallen by fifteen degrees in an afternoon.', 'T', 'B', 'fall by fifteen degrees in an afternoon'),
  ('The snow can reach three metres in January.', 'T', 'C', 'often reaching three metres'),
  ('Guides turn back groups if gusts exceed sixty kilometres an hour.', 'T', 'D', 'exceed sixty kilometres an hour'),
  ('A documentary film was followed by a jump in the number of climbers.', 'T', 'E', 'a documentary film about the mountain was shown on television'),
  ('Dr Eklund has climbed the mountain many times.', 'NG', 'F', 'Dr Lars Eklund', 'His climbing is not mentioned.'),
 ]),
 mcq([
  ('Why do farmers watch the snow depth?', ['Thin snow can mean a dry summer.', 'Snow kills crops.', 'They sell snow.', 'They ski.'], 0, 'C', 'a thin winter snowfall can mean a dry summer'),
  ('Why is the wind a danger?', ['It is always strong.', 'It is unpredictable.', 'It is warm.', 'It is silent.'], 1, 'D', 'The unpredictability is one reason why the mountain is dangerous'),
  ('What does Dr Eklund propose?', ['A daily limit on climbers.', 'A new weather station.', 'Closing the mountain.', 'More huts.'], 0, 'F', 'a limit on the number of climbers each day'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Record', 'Detail'],
  [['Temperature', 'Highest in [[1]]'], ['Snow depth', 'Often reaches three [[2]]'], ['Wind', 'Guides check it every [[3]]'], ['Climbers', 'More than ten thousand try to reach the [[4]]']],
  [(['july'], 'B', 'highest point in July'), (['metres'], 'C', 'three metres'), (['hour'], 'D', 'every hour'), (['summit'], 'E', 'reach the summit')], 1),
 feat('Match each statement with the correct record, A to D.', ['Temperature', 'Snow depth', 'Wind speed', 'Climbers'], [
  ('It can fall suddenly when a storm arrives.', 0, 'B', 'when a storm arrives from the west'),
  ('Farmers watch it anxiously.', 1, 'C', 'watch the depth anxiously'),
  ('It follows no seasonal pattern.', 2, 'D', 'no seasonal pattern'),
  ('Its rise followed a television film.', 3, 'E', 'documentary film'),
 ]),
 multi('Which TWO problems caused by the large number of climbers are mentioned in paragraph E?', ['The narrow path is wearing away.', 'The mountain huts are often full.', 'The rivers are polluted.', 'Avalanches are more common.', 'The weather is warmer.'], [0, 1], [('E', 'the narrow path, which is wearing away'), ('E', 'the small mountain huts, which are often full')]),
 head(['A weather station on a peak', 'Warmth through the year', 'Snow that comes and goes', 'A wind with no pattern', 'A sudden rush of visitors', 'What can be controlled', 'Considering a limit', 'The history of skiing', 'Packing for a journey'],
  [('A', 0, 'has had a weather station on its summit ridge'), ('B', 1, 'follows the shape of the year'), ('C', 2, 'Snow depth shows a reverse pattern'), ('D', 3, 'Wind speed behaves in the most unpredictable way of all'), ('E', 4, 'The number of climbers shows an altogether different pattern'), ('F', 5, 'the last can be controlled'), ('G', 6, 'The authorities are considering his proposal')]),
 info([
  ('a reference to a storm arriving from the west', 'B', 'a storm arrives from the west'),
  ('a reference to the source of river water', 'C', 'main source of the water that flows in the valley rivers'),
  ('a reference to gusts that knock people down', 'D', 'knock a person off his feet'),
  ('a reference to a television film', 'E', 'documentary film'),
  ('a suggestion that climbers book online', 'G', 'book a place online'),
 ]),
 ends(['turn back groups in strong gusts.', 'was shown on television around the world.', 'wants a limit on climbers.', 'fear a limit would reduce their income.', 'built the path.', 'live on the summit.', 'measure the snow.'], [
  ('Guides', 0, 'D', 'turn back groups'),
  ('The documentary film', 1, 'E', 'shown on television around the world'),
  ('Dr Eklund', 2, 'F', 'a limit on the number of climbers each day'),
  ('Local businesses', 3, 'G', 'reduce their income'),
 ]),
 sent(2, [
  ('The weather station is on the summit ___.', ['ridge'], 'A', 'summit ridge'),
  ('Melting snow is the main source of water in the ___ rivers.', ['valley'], 'C', 'valley rivers'),
  ('Dr Eklund runs the ___.', ['station'], 'F', 'runs the station'),
  ('A decision is expected after the next ___ season.', ['summer'], 'G', 'next summer season'),
 ]),
 short(3, [
  ('How deep can the snow be?', ['three metres'], 'C', 'three metres'),
  ('Who uses the records to decide when it is safe?', ['mountain guides', 'the mountain guides'], 'A', 'the mountain guides'),
  ('When did the film make climber numbers jump?', ['eight years ago'], 'E', 'about eight years ago'),
 ]),
])
