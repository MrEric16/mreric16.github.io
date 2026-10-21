from lib import *
from svgs import *
A = """An earthquake is a sudden shaking of the ground, caused by the release of energy in the Earth's crust. Millions of small earthquakes occur every year, and most are too weak to be felt. About once a year, however, a very large one strikes, shaking the ground violently, knocking down buildings and sometimes setting off giant sea waves. People have feared earthquakes since ancient times, and many cultures explained them as the movements of giant animals beneath the ground. Today scientists know much more about the causes, and they can measure the shaking with precision, although they still cannot predict exactly when the next one will come."""
B = """The Earth's outer shell is broken into huge pieces called tectonic plates, which move very slowly, at about the speed that fingernails grow. Where two plates meet, they may slide past each other, collide, or move apart. Often the edges stick together, and the pressure builds up over years or centuries, until the rock suddenly breaks and the plates jump forward. The place beneath the ground where the break begins is called the focus, and the point on the surface directly above it is the epicentre, where the shaking is usually strongest. Most earthquakes happen along the edges of plates, particularly around the Pacific Ocean, in a region called the Ring of Fire."""
C = """The energy released by the break travels outwards in waves. The fastest are called primary waves, or P-waves, which push and pull the rock like a spring and arrive first, often as a sudden jolt. They are followed by the slower secondary waves, or S-waves, which move the ground from side to side and cause most of the damage. Finally, surface waves, which roll along the top of the ground like waves on water, arrive and can shake buildings for a minute or more. The gap between the arrival of the P-waves and the S-waves allows scientists to calculate how far away the earthquake was."""
D = """The instrument used to record the waves is the seismograph. Inside it, a heavy weight hangs from a spring, and when the ground moves, the weight stays almost still and a pen attached to it draws a line on a moving roll of paper. On a quiet day, the line is almost flat. A weak tremor produces small, regular waves, while a strong earthquake produces tall waves that may fill the whole width of the paper. Aftershocks, which follow a large earthquake, appear as bursts of rapid, tightly packed wiggles. Modern seismographs are electronic and send their records to computers, but the traces still look very similar to the old ones."""
E = """The size of an earthquake is described by its magnitude. The scale is not ordinary, but logarithmic: each whole number represents a shaking about ten times larger, and an energy release about thirty-two times greater. An earthquake of magnitude seven therefore releases about a thousand times more energy than one of magnitude five. Earthquakes below magnitude three are rarely felt; those between four and five can break windows; and those above seven can destroy whole towns. The effects depend on more than size, however. Depth, the type of ground and the quality of the buildings all matter, and a moderate earthquake can kill thousands if buildings are weak."""
F = """Dr Keiko Tanaka, a seismologist, has spent her career studying how to protect people. She explains that the best way to save lives is not to predict earthquakes but to build safe buildings, which have deep foundations, flexible frames and heavy rubber supports that absorb shaking. In countries which have adopted strict building rules, a strong earthquake may cause little damage, whereas the same shaking can flatten a poor town where rules are ignored. Dr Tanaka also supports early-warning systems, which detect the first fast waves and send alerts to phones and trains a few seconds before the stronger waves arrive."""
G = """Ordinary people can also prepare. Experts advise families to choose a safe place in every room, such as under a strong table, to keep a bag of water, food and medicines ready, and to practise what to do when the shaking starts: drop to the hands and knees, take cover and hold on until the shaking stops. Schools in many earthquake zones hold regular drills, so that children learn to act calmly. If the shaking begins near the coast, people should move to high ground at once, since a tsunami may follow, and wait until the authorities say that the danger is over."""
P = passage('p72', 'When the Ground Shakes', 'Earth science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which seismograph trace, A to D, matches each description?', [(wave('flat'), 160, 120), (wave('sine'), 160, 120), (wave('tall'), 160, 120), (wave('tight'), 160, 120)], [
  ('a quiet day', 0, 'D', 'the line is almost flat'),
  ('a weak tremor', 1, 'D', 'small, regular waves'),
  ('a strong earthquake', 2, 'D', 'tall waves that may fill the whole width of the paper'),
  ('aftershocks', 3, 'D', 'rapid, tightly packed wiggles'),
 ]),
 tfng([
  ('Most earthquakes are too weak to be felt.', 'T', 'A', 'most are too weak to be felt'),
  ('A very large earthquake occurs about once a year.', 'T', 'A', 'About once a year'),
  ('Scientists can now predict exactly when the next earthquake will come.', 'F', 'A', 'still cannot predict exactly when'),
  ('Tectonic plates move very slowly.', 'T', 'B', 'move very slowly'),
  ('The epicentre is directly above the focus.', 'T', 'B', 'the point on the surface directly above it is the epicentre'),
  ('Most earthquakes occur far from the edges of plates.', 'F', 'B', 'Most earthquakes happen along the edges of plates'),
  ('P-waves arrive first.', 'T', 'C', 'arrive first'),
  ('S-waves cause most of the damage.', 'T', 'C', 'cause most of the damage'),
  ('The seismograph was invented in Japan.', 'NG', 'D', 'The instrument used to record the waves is the seismograph', 'Its origin is not given.'),
 ]),
 mcq([
  ('What allows scientists to calculate the distance of an earthquake?', ['The gap between P-waves and S-waves.', 'The colour of the sky.', 'The number of aftershocks.', 'The time of day.'], 0, 'C', 'The gap between the arrival of the P-waves and the S-waves'),
  ('How much more energy does magnitude seven release than magnitude five?', ['Ten times.', 'About a thousand times.', 'Twice.', 'The same.'], 1, 'E', 'about a thousand times more energy'),
  ('What is the best way to save lives, according to Dr Tanaka?', ['Predicting earthquakes.', 'Building safe buildings.', 'Leaving cities.', 'Digging shelters.'], 1, 'F', 'to build safe buildings'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The edges of the plates [[1]] together and pressure builds up.', 'The rock suddenly [[2]].', 'Waves travel outwards, and [[3]] waves arrive first.', 'Surface waves can shake buildings for a [[4]] or more.'],
  [(['stick'], 'B', 'edges stick together'), (['breaks'], 'B', 'the rock suddenly breaks'), (['primary'], 'C', 'primary waves'), (['minute'], 'C', 'a minute or more')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Magnitude', 'Effect'],
  [['Below three', 'Rarely [[1]]'], ['Four to five', 'Can break [[2]]'], ['Above seven', 'Can destroy whole [[3]]'], ['Seven', 'About a [[4]] times more energy than five']],
  [(['felt'], 'E', 'rarely felt'), (['windows'], 'E', 'break windows'), (['towns'], 'E', 'destroy whole towns'), (['thousand'], 'E', 'about a thousand times more energy')], 1),
 head(['A shaking Earth', 'Plates under pressure', 'Three kinds of wave', 'Recording the shaking', 'Measuring size', 'Building for safety', 'What families can do', 'The history of volcanoes', 'How to climb a mountain'],
  [('A', 0, 'a sudden shaking of the ground'), ('B', 1, 'the pressure builds up over years or centuries'), ('C', 2, 'primary waves'), ('D', 3, 'The instrument used to record the waves is the seismograph'), ('E', 4, 'described by its magnitude'), ('F', 5, 'build safe buildings'), ('G', 6, 'Ordinary people can also prepare')]),
 info([
  ('a comparison with fingernails', 'B', 'fingernails grow'),
  ('a reference to a region around the Pacific', 'B', 'Ring of Fire'),
  ('a reference to a sudden jolt', 'C', 'a sudden jolt'),
  ('a reference to electronic records', 'D', 'send their records to computers'),
  ('a reference to alerts on phones', 'F', 'alerts to phones and trains'),
 ]),
 ends(['records the waves.', 'move the ground from side to side.', 'hold regular drills.', 'absorb shaking.', 'predict earthquakes.', 'are found only on land.', 'measure temperature.'], [
  ('A seismograph', 0, 'D', 'used to record the waves'),
  ('S-waves', 1, 'C', 'move the ground from side to side'),
  ('Schools', 2, 'G', 'hold regular drills'),
  ('Rubber supports', 3, 'F', 'absorb shaking'),
 ]),
 sent(2, [
  ('The place where the break begins is called the ___.', ['focus'], 'B', 'called the focus'),
  ('Magnitude is measured on a ___ scale.', ['logarithmic'], 'E', 'logarithmic'),
  ('Dr Tanaka is a ___.', ['seismologist'], 'F', 'a seismologist'),
  ('After shaking near the coast, people should move to high ___.', ['ground'], 'G', 'high ground'),
 ]),
 short(3, [
  ('What are the fastest waves called?', ['primary waves', 'p-waves'], 'C', 'primary waves'),
  ('What hangs from a spring in a seismograph?', ['a heavy weight', 'heavy weight', 'weight'], 'D', 'a heavy weight'),
  ('What may follow an earthquake near the coast?', ['a tsunami', 'tsunami'], 'G', 'a tsunami may follow'),
 ]),
])
