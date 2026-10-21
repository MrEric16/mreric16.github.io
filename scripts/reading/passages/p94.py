from lib import *
from svgs import *
A = """The blue whale is the largest animal that has ever lived. An adult can reach thirty metres in length, longer than three buses parked in a row, and weigh up to one hundred and fifty tonnes, which is more than twenty-five elephants. Its heart is the size of a small car, and its tongue alone weighs as much as an elephant. Yet this giant feeds on some of the smallest animals in the sea. Hunted almost to extinction in the twentieth century, the blue whale is now slowly recovering. This passage describes how it lives, feeds and communicates, and how people are trying to save it."""
B = """Blue whales belong to a group called baleen whales. Instead of teeth, they have long plates of a hornlike material called baleen hanging from the upper jaw, which work like a giant comb. The whale takes a huge mouthful of water, which may contain krill, small shrimp-like animals about the length of a finger. It then pushes the water out through the baleen with its tongue, leaving the krill trapped inside to be swallowed. At the peak of the feeding season, a blue whale can eat around four tonnes of krill a day, and it may swallow forty million of them."""
C = """The whales feed mainly in cold, rich waters near the poles in summer, where krill are abundant. In winter, many migrate to warmer seas near the equator, to give birth. A calf is born tail first after a pregnancy of about eleven months, and it is already about seven metres long and weighs around two tonnes. It drinks several hundred litres of its mother's milk a day, which is so rich in fat that the baby gains about ninety kilograms every day. After about six months the calf is weaned, by which time it has more than doubled in length."""
D = """Like all whales, blue whales are mammals, not fish. They are warm-blooded, give birth to live young and feed them with milk, and they breathe air through lungs. When a whale surfaces, it blows out a spout of warm, moist air through two blowholes on the top of its head. The spout of a blue whale can rise nine metres into the air, and it can be seen from a great distance. A whale can stay underwater for twenty minutes or more, and dives to depths of around two hundred metres to find food, although it usually stays closer to the surface."""
E = """Blue whales are among the loudest animals on the planet. They produce low-frequency moans, groans and pulses, which can reach 188 decibels, louder than a jet engine at close range. The sounds are so low that they are partly below the range of human hearing, and they can travel for hundreds of kilometres through the water. Scientists believe that whales use these calls to find one another across the vast ocean, and males may also use them to attract mates. Recently, researchers have noticed that the pitch of the calls of blue whales in many parts of the world has been slowly falling, and nobody is sure why."""
F = """In the early twentieth century, whalers armed with explosive harpoons and fast steam-powered ships hunted blue whales in huge numbers. As many as 350,000 were killed in the Southern Ocean alone, and by the 1960s, the population had fallen to a few thousand. An international ban on hunting blue whales was introduced in 1966, and numbers have since recovered slowly. Today, there are thought to be between ten and twenty-five thousand blue whales in the world, but this is a small fraction of the original population. Whales breed slowly, producing a single calf every two or three years, so recovery will take many decades."""
G = """Today the threats are different. Ships sometimes collide with whales, particularly in busy shipping lanes, and noise from engines and sonar may interfere with their calls. Whales can become tangled in fishing nets, and the warming of the oceans may reduce the supply of krill. Dr Ana Reyes, a marine biologist who studies whales from small boats, says that simple measures can help: ships can slow down in areas where whales are common, and shipping lanes can be moved. She believes that the recovery of the blue whale will be one of the great success stories of conservation, provided that people continue to protect it."""
P = passage('p94', 'The Blue Whale', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The blue whale is the largest animal that has ever lived.', 'T', 'A', 'largest animal that has ever lived'),
  ('An adult blue whale can reach thirty metres.', 'T', 'A', 'thirty metres in length'),
  ('Blue whales have teeth.', 'F', 'B', 'Instead of teeth'),
  ('Krill are about the length of a finger.', 'T', 'B', 'length of a finger'),
  ('A newborn calf is about seven metres long.', 'T', 'C', 'about seven metres long'),
  ('Blue whales are fish.', 'F', 'D', 'mammals, not fish'),
  ('The spout can rise nine metres.', 'T', 'D', 'nine metres into the air'),
  ('Blue whale calls can travel for hundreds of kilometres.', 'T', 'E', 'hundreds of kilometres'),
  ('Blue whales live in groups of fifty.', 'NG', 'C', 'feed mainly in cold, rich waters', 'Group size is not mentioned.'),
 ]),
 mcq([
  ('How does a blue whale feed?', ['It filters krill through baleen.', 'It bites fish with teeth.', 'It eats seaweed.', 'It hunts seals.'], 0, 'B', 'leaving the krill trapped inside'),
  ('When was the ban on hunting introduced?', ['1966.', '1900.', '1930.', '2000.'], 0, 'F', '1966'),
  ('What does Dr Reyes suggest?', ['Ships can slow down where whales are common.', 'Ban all ships.', 'Stop fishing.', 'Feed the whales.'], 0, 'G', 'ships can slow down'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Length', 'Up to thirty [[1]]'], ['Food', 'Around four [[2]] of krill a day'], ['Pregnancy', 'About eleven [[3]]'], ['Calf growth', 'Gains about ninety [[4]] a day']],
  [(['metres'], 'A', 'thirty metres'), (['tonnes'], 'B', 'four tonnes'), (['months'], 'C', 'eleven months'), (['kilograms'], 'C', 'ninety kilograms')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The whale takes a mouthful of [[1]].', 'It pushes the water out through the [[2]].', 'The krill are trapped [[3]].', 'The krill are [[4]].'],
  [(['water'], 'B', 'mouthful of water'), (['baleen'], 'B', 'through the baleen'), (['inside'], 'B', 'trapped inside'), (['swallowed'], 'B', 'swallowed')], 1),
 feat('Match each statement with the correct item, A to D.', ['Baleen', 'Blowholes', 'Moans and pulses', 'Dr Reyes'], [
  ('It works like a giant comb.', 0, 'B', 'giant comb'),
  ('There are two of them on the head.', 1, 'D', 'two blowholes'),
  ('They are louder than a jet engine.', 2, 'E', 'louder than a jet engine'),
  ('She is a marine biologist.', 3, 'G', 'marine biologist'),
 ]),
 multi('Which TWO threats to whales today are mentioned in paragraph G?', ['Collisions with ships.', 'Fishing nets.', 'Sharks.', 'Disease.', 'Volcanoes.'], [0, 1], [('G', 'collide with whales'), ('G', 'fishing nets')]),
 head(['The biggest animal ever', 'Feeding on the smallest', 'Birth in warm seas', 'A mammal of the sea', 'Voices across the ocean', 'From hunting to ban', 'Dangers that remain', 'The history of ships', 'Dolphins in captivity'],
  [('A', 0, 'largest animal that has ever lived'), ('B', 1, 'Instead of teeth'), ('C', 2, 'to give birth'), ('D', 3, 'mammals, not fish'), ('E', 4, 'loudest animals on the planet'), ('F', 5, 'An international ban'), ('G', 6, 'Today the threats are different')]),
 info([
  ('a comparison with buses', 'A', 'three buses'),
  ('a reference to explosive harpoons', 'F', 'explosive harpoons'),
  ('a reference to the size of the heart', 'A', 'size of a small car'),
  ('a reference to a fall in pitch', 'E', 'slowly falling'),
  ('a reference to sonar', 'G', 'sonar'),
 ]),
 ends(['hangs from the upper jaw.', 'are born tail first.', 'were hunted by steam ships.', 'can slow down for whales.', 'have teeth.', 'live in rivers.', 'eat fish.'], [
  ('Baleen', 0, 'B', 'upper jaw'),
  ('Calves', 1, 'C', 'born tail first'),
  ('Blue whales', 2, 'F', 'steam-powered ships'),
  ('Ships', 3, 'G', 'slow down'),
 ]),
 sent(2, [
  ('Blue whales feed on small animals called ___.', ['krill'], 'B', 'krill'),
  ('A calf is weaned after about six ___.', ['months'], 'C', 'six months'),
  ('Whales breathe air through ___.', ['lungs'], 'D', 'through lungs'),
  ('Whales produce a single ___ every two or three years.', ['calf'], 'F', 'single calf'),
 ]),
 short(3, [
  ('How long can a whale stay underwater?', ['twenty minutes'], 'D', 'twenty minutes'),
  ('How many blue whales are there today?', ['twenty-five thousand'], 'F', 'between ten and twenty-five thousand'),
  ('What may reduce the supply of krill?', ['warming'], 'G', 'warming of the oceans'),
 ]),
])
