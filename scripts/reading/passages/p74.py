from lib import *
from svgs import *
A = """A desert is a region that receives less than about two hundred and fifty millimetres of rain a year. Deserts cover roughly a third of the Earth's land surface, and they are not all hot and sandy: some, like parts of Antarctica, are cold, and many are stony rather than sandy. Uzbekistan has its own, the Kyzylkum, whose name means red sand. Life in a desert seems impossible, yet thousands of species live there. They have solved the two great problems of the desert, which are the shortage of water and the extremes of temperature, in ways that are often ingenious. This passage describes four of these solutions and the lessons that they offer."""
B = """The camel is the most famous desert animal. Contrary to popular belief, its hump does not hold water but fat, which can be used as a store of energy when food is scarce. The camel's real secret is its ability to cope with thirst. It can lose a quarter of its body weight in water without serious harm, an amount that would kill most mammals, and when it finds a well it can drink more than a hundred litres in a few minutes. Its wide, flat feet spread its weight on soft sand, its thick eyelashes and closing nostrils keep out blowing dust, and its thick coat protects it from the heat."""
C = """The fennec fox, the smallest fox in the world, lives in the Sahara. Its enormous ears, which may be fifteen centimetres long, serve two purposes: they give the fox a sharp sense of hearing for finding insects underground, and they act like radiators, releasing heat from the blood vessels near the surface of the skin. The fox sleeps in a burrow during the heat of the day and hunts only at night, when the desert is cool. Its pale colour reflects the sunlight, and the thick fur on its feet protects them from the burning sand. It can survive with very little water, gaining most of what it needs from its food."""
D = """Some animals never drink at all. The kangaroo rat of the North American desert gets all its water from the seeds that it eats, and from the chemical processes in its own body. It loses very little: its kidneys produce a highly concentrated urine, its droppings are dry, and it spends the day in a cool, humid burrow, which it seals with earth. It does not sweat. Scientists have studied the animal closely to learn how it saves water, and some of their findings have been used in the design of equipment that recycles water in places where it is scarce."""
E = """Desert plants face the same problems. Cacti have swollen stems in which they store water, and their leaves have evolved into spines, which reduce the loss of water and protect against animals. Their roots spread wide just below the surface, so that they can absorb a brief shower before it evaporates. Other plants avoid the drought altogether. Their seeds lie in the sand for years, sometimes for decades, and germinate only when heavy rain falls. Within days, the plants flower, produce new seeds and die, so that a barren plain can turn into a carpet of colour for a few weeks, an event that attracts visitors from around the world."""
F = """A common solution is to avoid the day. Most desert animals are nocturnal, which means that they are active at night, when the temperature may be as much as thirty degrees lower than at midday. Insects, snakes, lizards and small mammals shelter underground or under rocks, where the temperature is much more stable. Even a few centimetres below the surface of the sand, the heat is far less severe. Some beetles collect drinking water from the morning fog by standing with their bodies tilted and letting the droplets run down to their mouths."""
G = """Dr Amir Nazarov, a desert ecologist, believes that humans can learn from these adaptations. Architects are copying the thick walls and shaded courtyards of desert towns, engineers are designing nets to catch water from fog, and farmers are testing crops that need little water. At the same time, he warns that deserts are growing. Overgrazing, the cutting of trees and the changing climate are turning dry grassland into desert, a process called desertification, which threatens the homes of hundreds of millions of people. The solution, he says, is to plant trees and protect the soil, before the land is lost."""
P = passage('p74', 'Surviving in the Desert', 'Ecology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Deserts receive less than about 250 millimetres of rain a year.', 'T', 'A', 'less than about two hundred and fifty millimetres'),
  ('All deserts are hot and sandy.', 'F', 'A', 'not all hot and sandy'),
  ('Kyzylkum means red sand.', 'T', 'A', 'means red sand'),
  ('A camel\'s hump holds water.', 'F', 'B', 'does not hold water but fat'),
  ('A camel can drink over a hundred litres in a few minutes.', 'T', 'B', 'more than a hundred litres in a few minutes'),
  ('The fennec fox hunts during the day.', 'F', 'C', 'hunts only at night'),
  ('The kangaroo rat gets water from seeds.', 'T', 'D', 'water from the seeds that it eats'),
  ('Some desert seeds wait for decades before germinating.', 'T', 'E', 'sometimes for decades'),
  ('Cacti are native to Asia.', 'NG', 'E', 'Cacti have swollen stems', 'Their origin is not given.'),
 ]),
 mcq([
  ('What is the camel\'s real secret?', ['Its hump of water.', 'Its ability to cope with thirst.', 'Its speed.', 'Its colour.'], 1, 'B', 'its ability to cope with thirst'),
  ('Why does the kangaroo rat seal its burrow?', ['To keep it cool and humid.', 'To hide food.', 'To keep out snow.', 'To sleep longer.'], 0, 'D', 'a cool, humid burrow, which it seals with earth'),
  ('What causes desertification?', ['Overgrazing, tree cutting and climate change.', 'Floods.', 'Volcanoes.', 'Earthquakes.'], 0, 'G', 'Overgrazing, the cutting of trees and the changing climate'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The camel stores [[1]] in its hump.', 'The fennec fox releases heat through its [[2]].', 'The kangaroo rat seals its burrow with [[3]].', 'Cactus leaves have evolved into [[4]].'],
  [(['fat'], 'B', 'but fat'), (['ears'], 'C', 'enormous ears'), (['earth'], 'D', 'seals with earth'), (['spines'], 'E', 'into spines')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Animal or plant', 'Detail'],
  [['Camel', 'Can drink more than a hundred [[1]] in minutes'], ['Fennec fox', 'Hunts only at [[2]]'], ['Cactus', 'Roots spread wide just below the [[3]]'], ['Beetle', 'Collects water from morning [[4]]']],
  [(['litres'], 'B', 'a hundred litres'), (['night'], 'C', 'hunts only at night'), (['surface'], 'E', 'just below the surface'), (['fog'], 'F', 'morning fog')], 1),
 feat('Match each statement with the correct species, A to D.', ['Camel', 'Fennec fox', 'Kangaroo rat', 'Cactus'], [
  ('It does not sweat.', 2, 'D', 'It does not sweat'),
  ('Its ears act like radiators.', 1, 'C', 'act like radiators'),
  ('It has wide, flat feet.', 0, 'B', 'wide, flat feet'),
  ('It stores water in its stem.', 3, 'E', 'in which they store water'),
 ]),
 multi('Which TWO uses of the fennec fox\'s ears are given in paragraph C?', ['Sharp hearing.', 'Releasing heat.', 'Storing fat.', 'Digging burrows.', 'Attracting mates.'], [0, 1], [('C', 'a sharp sense of hearing'), ('C', 'releasing heat from the blood vessels')]),
 head(['Life where water is scarce', 'A tolerance for thirst', 'Ears that cool', 'An animal that never drinks', 'Plants that wait', 'Avoiding the day', 'Lessons and warnings', 'The history of oil', 'Crossing the ocean'],
  [('A', 0, 'the shortage of water and the extremes of temperature'), ('B', 1, 'its ability to cope with thirst'), ('C', 2, 'they act like radiators'), ('D', 3, 'Some animals never drink at all'), ('E', 4, 'germinate only when heavy rain falls'), ('F', 5, 'A common solution is to avoid the day'), ('G', 6, 'humans can learn from these adaptations')]),
 info([
  ('a reference to closing nostrils', 'B', 'closing nostrils'),
  ('a reference to protective fur on the feet', 'C', 'thick fur on its feet'),
  ('a reference to a sealed burrow', 'D', 'seals with earth'),
  ('a reference to a carpet of colour', 'E', 'carpet of colour'),
  ('a reference to tilted bodies', 'F', 'bodies tilted'),
 ]),
 ends(['drinks over a hundred litres in minutes.', 'sleeps in a burrow by day.', 'germinate only after heavy rain.', 'warns that deserts are growing.', 'live only in Antarctica.', 'dig wells.', 'eat cacti.'], [
  ('The camel', 0, 'B', 'more than a hundred litres'),
  ('The fennec fox', 1, 'C', 'sleeps in a burrow during the heat of the day'),
  ('Desert seeds', 2, 'E', 'germinate only when heavy rain falls'),
  ('Dr Nazarov', 3, 'G', 'deserts are growing'),
 ]),
 sent(2, [
  ('The Kyzylkum is a desert in ___.', ['uzbekistan'], 'A', 'Uzbekistan'),
  ('A camel\'s hump holds ___, not water.', ['fat'], 'B', 'but fat'),
  ('The fennec fox is the smallest fox in the ___.', ['world'], 'C', 'in the world'),
  ('Dr Nazarov is a desert ___.', ['ecologist'], 'G', 'desert ecologist'),
 ]),
 short(3, [
  ('How long can a fennec fox\'s ears be?', ['fifteen centimetres'], 'C', 'fifteen centimetres'),
  ('What have cactus leaves become?', ['spines'], 'E', 'into spines'),
  ('What is the process of land turning into desert called?', ['desertification'], 'G', 'desertification'),
 ]),
])
