from lib import *
A = """Until the middle of the nineteenth century, very few buildings rose above six storeys. The reason was simple: in a traditional building the walls carry the weight, so the taller the building, the thicker the walls must be at the bottom. The Monadnock Building in Chicago, completed in 1891 with sixteen storeys, needed walls about two metres thick at its base, and the lower rooms were dark and cramped. There was a practical limit as well, since few people wished to climb more than a few flights of stairs."""
B = """The first problem was solved by the lift. Mechanical lifts already existed, but nobody trusted them, because a broken rope meant a fatal fall. In 1854, at an exhibition in New York, Elisha Otis stood on a platform raised high above the crowd and ordered the rope to be cut. A safety brake held the platform in place. The demonstration persuaded the public, and within a few years passenger lifts were being installed in hotels and department stores."""
C = """The second problem was the weight of the walls, and it was solved by steel. After the invention of a cheap way of making steel in the 1850s, builders could use it to make a rigid skeleton for a building. The Home Insurance Building in Chicago, finished in 1885, is often described as the first skyscraper. It had only ten storeys, but its weight was carried by an iron and steel frame, and the outer walls were no more than a covering. Without the need to support the building, the walls could be thin, the windows could be large, and the structure could be built much faster."""
D = """Competition for height soon followed. In New York, the Chrysler Building and the Empire State Building were built within a year of each other, and the Empire State Building, completed in 1931, was the tallest building in the world for about forty years. It was built in little more than a year, with thousands of workers on site at the same time. Such buildings were symbols of the confidence and wealth of their owners, as well as practical answers to the high price of land in crowded city centres."""
E = """Height created new difficulties, and the greatest of these was wind. A tall building sways, and although the movement is not dangerous, it can make the people on the upper floors feel unwell. In Taipei, the 101 tower has a steel ball weighing about six hundred tonnes hung near the top; the ball swings in the opposite direction to the building and so reduces the motion. Designers of the Burj Khalifa in Dubai, which opened in 2010 and rises 828 metres, tackled the problem in another way. They gave the tower a Y-shaped plan that steps back as it climbs, so that the wind never has a flat surface on which to build up its force."""
F = """Not everyone admires the skyscraper. Dr Nadia Farouk, an urban planner, points out that tall buildings use large amounts of energy for lifts, heating and air conditioning, and that they cast long shadows on the streets around them. Supporters answer that a city of tall buildings covers less land than a city of low ones, and that it makes public transport more practical, since so many people live and work close together. The argument, like the towers themselves, is likely to continue to rise."""
G = """A modern skyscraper is built from the ground up in a definite order. Deep foundations, made from concrete piles that reach down to solid rock, support the weight of the whole structure. On top of them, workers raise the steel frame, which forms the skeleton. At the centre, a concrete core contains the lift shafts and the stairs. The outer skin is a curtain wall of glass, hung from the frame like a curtain from a rail, and a damper near the top reduces the swaying. Each floor is completed in a few days, and a tall tower may rise by a storey every week."""
SVG = ('<rect class="s" x="200" y="20" width="120" height="205"/>' + ''.join('<path class="l" d="M200 %dH320"/>' % y for y in range(55, 225, 35)) +
 '<path class="l" style="stroke-width:5" d="M205 20V225M315 20V225"/><rect class="f" x="245" y="60" width="30" height="165"/><rect class="c" x="249" y="150" width="22" height="30"/>'
 '<path class="l" d="M260 20V44"/><circle class="c" cx="260" cy="52" r="9"/><path class="l" d="M215 225V255M240 225V255M265 225V255M290 225V255M310 225V255M190 225H330"/>'
 '<path class="l" d="M276 52H387M320 100H387M200 100H143M245 150H143M215 240H143"/>')
P = passage('p14', 'The Rise of the Skyscraper', 'Architecture', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Before the 1850s, very few buildings had more than six storeys.', 'T', 'A', 'very few buildings rose above six storeys'),
  ('The Monadnock Building had walls about two metres thick at its base.', 'T', 'A', 'walls about two metres thick at its base'),
  ('Mechanical lifts did not exist before 1854.', 'F', 'B', 'Mechanical lifts already existed'),
  ('Otis demonstrated his safety brake at an exhibition in New York.', 'T', 'B', 'at an exhibition in New York'),
  ('Otis was injured during his demonstration.', 'NG', 'B', 'A safety brake held the platform in place', 'The platform held; the passage does not mention any injury.'),
  ('Cheap steel could be made by the 1850s.', 'T', 'C', 'a cheap way of making steel in the 1850s'),
  ('The Home Insurance Building had more than ten storeys when it was finished.', 'F', 'C', 'It had only ten storeys'),
  ('A steel frame allowed walls to be thin and windows to be large.', 'T', 'C', 'the walls could be thin, the windows could be large'),
  ('The Chrysler Building was taller than the Empire State Building.', 'NG', 'D', 'the Chrysler Building and the Empire State Building were built within a year of each other', 'Their heights are not compared.'),
  ('The Empire State Building took more than five years to build.', 'F', 'D', 'built in little more than a year'),
  ('The Burj Khalifa has a Y-shaped plan.', 'T', 'E', 'a Y-shaped plan'),
 ]),
 mcq([
  ('Why did early tall buildings have dark, cramped lower rooms?', ['Windows were not yet invented.', 'The walls had to be very thick.', 'Lifts took up too much space.', 'Steel was too expensive.'], 1, 'A', 'the taller the building, the thicker the walls must be at the bottom'),
  ('What was the effect of Otis\'s demonstration?', ['It showed how to cut ropes.', 'It made lifts cheaper.', 'It made the public trust lifts.', 'It gave him a job in a hotel.'], 2, 'B', 'The demonstration persuaded the public'),
  ('What does the steel ball in the Taipei tower do?', ['It supports the weight of the building.', 'It reduces the swaying.', 'It stores energy.', 'It measures the wind speed.'], 1, 'E', 'reduces the motion'),
 ]),
 head(['Why buildings could not grow taller', 'Making the stairs unnecessary', 'A skeleton of steel', 'A race for height', 'Dealing with wind', 'Arguments for and against', 'How a skyscraper is built', 'The cost of building materials', 'The life of a famous architect'],
  [('A', 0, 'Until the middle of the nineteenth century'), ('B', 1, 'The first problem was solved by the lift'), ('C', 2, 'The second problem was the weight of the walls'), ('D', 3, 'Competition for height soon followed'), ('E', 4, 'Height created new difficulties'), ('F', 5, 'Not everyone admires the skyscraper'), ('G', 6, 'A modern skyscraper is built from the ground up')]),
 info([
  ('an example of a demonstration of safety', 'B', 'stood on a platform raised high above the crowd'),
  ('a reason for the speed of construction of the first steel buildings', 'C', 'the structure could be built much faster'),
  ('a reference to the high price of land', 'D', 'the high price of land in crowded city centres'),
  ('an unusual way of reducing the effect of wind', 'E', 'a steel ball weighing about six hundred tonnes'),
  ('a criticism relating to shadows', 'F', 'they cast long shadows on the streets'),
  ('a description of the order of building', 'G', 'built from the ground up in a definite order'),
 ]),
 sent(2, [
  ('The Monadnock Building was completed in ___.', ['1891'], 'A', 'completed in 1891'),
  ('Elisha Otis ordered the ___ to be cut.', ['rope'], 'B', 'ordered the rope to be cut'),
  ('The Home Insurance Building is often called the first ___.', ['skyscraper'], 'C', 'the first skyscraper'),
  ('The Empire State Building was completed in ___.', ['1931'], 'D', 'completed in 1931'),
  ('The Burj Khalifa is ___ metres tall.', ['828'], 'E', 'rises 828 metres'),
  ('Supporters say tall buildings make public ___ more practical.', ['transport'], 'F', 'makes public transport more practical'),
 ]),
 short(3, [
  ('Where did Otis give his demonstration?', ['new york'], 'B', 'an exhibition in New York'),
  ('What did the Taipei tower have hung near its top?', ['a steel ball', 'steel ball'], 'E', 'a steel ball weighing about six hundred tonnes'),
  ('What kind of planner is Dr Farouk?', ['urban', 'an urban planner', 'urban planner'], 'F', 'an urban planner'),
  ('What do the concrete piles of the foundations reach down to?', ['solid rock', 'rock'], 'G', 'reach down to solid rock'),
 ]),
 diag('Label the diagram of a skyscraper. Write NO MORE THAN TWO WORDS from the passage for each answer.', 520, 260, SVG, [[400, 52], [400, 100], [130, 100], [130, 150], [130, 240]],
  [(['damper'], 'G', 'a damper near the top'), (['curtain wall', 'glass'], 'G', 'a curtain wall of glass'), (['steel frame', 'frame'], 'G', 'the steel frame'), (['lift shafts', 'lift shaft', 'core'], 'G', 'the lift shafts and the stairs'), (['foundations', 'deep foundations'], 'G', 'Deep foundations')], 2),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Early tall buildings needed very [[1]] walls. Otis made lifts safe, and later [[2]] allowed builders to make a rigid skeleton, so that the walls became a thin [[3]]. Tall buildings sway in the wind, so engineers hang a [[4]] near the top to reduce the movement.',
  [(['thick'], 'A', 'the thicker the walls'.replace('the thicker the walls','thicker')), (['steel'], 'C', 'a rigid skeleton'.replace('a rigid skeleton','steel')), (['covering'], 'C', 'no more than a covering'), (['ball'], 'E', 'a steel ball')], 1,
  bank=['thick', 'steel', 'covering', 'ball', 'thin', 'glass', 'brick', 'rope']),
])
