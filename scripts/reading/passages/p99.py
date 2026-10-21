from lib import *
from svgs import *
A = """Owls have fascinated people for thousands of years. In some cultures they are symbols of wisdom, while in others they are signs of bad luck, and they appear in stories from ancient Greece to modern children's books. There are over two hundred species, found on every continent except Antarctica, from tiny owls the size of a sparrow to great horned owls that can carry off a rabbit. What unites them is the way they hunt: silently, at night, using senses that are among the most remarkable in the animal kingdom. This passage explains how the bodies of owls are adapted to their way of life."""
B = """The first adaptation is vision. An owl's eyes are huge in proportion to its head: if human eyes were the same relative size, they would be as big as grapefruits. Their shape is tubular, rather like a pair of binoculars, and this gives excellent sight in dim light, because a large lens gathers more light. The price is that the eyes are fixed in their sockets and cannot move. An owl must turn its whole head to look around. To do this, it has fourteen neck bones, twice as many as a human, and can rotate its head up to two hundred and seventy degrees in either direction."""
C = """The second adaptation is hearing. In many species, the face is a flat disc of feathers, shaped like a dish, which collects sound and directs it to the ears. The ears themselves are placed at slightly different heights on the sides of the head, so that a sound reaches one ear a fraction of a second before the other, and the owl can work out exactly where it came from, both left and right and up and down. A barn owl can catch a mouse in total darkness by sound alone, in conditions in which it could not see its prey at all."""
D = """The third adaptation is silent flight. Most birds make a swishing noise as their wings beat the air, but owls glide almost without a sound. The leading edge of their main wing feathers has a comb-like fringe, which breaks up the flow of air into small streams and reduces turbulence. The upper surface of the feathers is covered with a soft down, like velvet, and the trailing edge is fringed. As a result, the prey does not hear the owl approaching, and the owl, in turn, can listen for its prey without the noise of its own wings. Engineers have studied these feathers in order to design quieter fans and aircraft."""
E = """Owls are carnivores, feeding mainly on small mammals, such as mice and voles, but also on insects, fish and birds. Some species can take surprisingly large prey. The hunting method is usually to wait on a perch and listen, then swoop down on the target with talons spread. Owls swallow small prey whole, and since they cannot digest the bones, fur or feathers, they cough these up some hours later in the form of a compact pellet. Scientists collect and dissect the pellets to learn what the owl has eaten, and from this they can measure the numbers of small mammals in an area."""
F = """Most owls nest in holes in trees, old buildings or abandoned nests of other birds, and some, like the burrowing owl, nest underground. The female lays between two and eight eggs, depending on the species and the supply of food. In years when mice and voles are plentiful, owls may raise large broods; in lean years, they may not breed at all. The chicks are covered in white down and are fed by both parents. They leave the nest after about five to ten weeks but depend on their parents for food for some time afterwards. Many young owls die in their first winter."""
G = """Some owl species are in trouble. The destruction of forests and old trees removes nesting sites, and poisons used to kill rats and mice can pass up the food chain to the owls that eat them. Dr Rosa Lindgren, a conservation biologist, has shown that putting up nest boxes in farmland can double the number of barn owls in an area within a few years, and that the owls in turn reduce the number of rodents which damage crops. Farmers who put up boxes, she says, get free pest control. Her work is a reminder that, in nature, even the creature that works at night can help us in the day."""
P = passage('p99', 'The Silent Hunters: Owls', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('There are over two hundred species of owl.', 'T', 'A', 'over two hundred species'),
  ('Owls are found on every continent.', 'F', 'A', 'except Antarctica'),
  ('Owls hunt mainly at night.', 'T', 'A', 'at night'),
  ('An owl\'s eyes can move freely in their sockets.', 'F', 'B', 'fixed in their sockets'),
  ('Owls have fourteen neck bones.', 'T', 'B', 'fourteen neck bones'),
  ('An owl can rotate its head up to 270 degrees.', 'T', 'B', 'two hundred and seventy degrees'),
  ('A barn owl can catch a mouse by sound alone.', 'T', 'C', 'by sound alone'),
  ('Owls make a loud swishing noise in flight.', 'F', 'D', 'glide almost without a sound'),
  ('Owls live longer than eagles.', 'NG', 'F', 'Many young owls die in their first winter', 'No comparison with eagles is made.'),
 ]),
 mcq([
  ('Why do owls need to turn their heads?', ['Their eyes cannot move.', 'They are blind.', 'Their necks are short.', 'They are scared.'], 0, 'B', 'cannot move'),
  ('How does the facial disc help?', ['It collects sound.', 'It keeps the owl warm.', 'It scares prey.', 'It improves sight.'], 0, 'C', 'collects sound'),
  ('Why do engineers study owl feathers?', ['To design quieter fans and aircraft.', 'To make warm clothes.', 'To build bridges.', 'To make paper.'], 0, 'D', 'quieter fans and aircraft'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Adaptation', 'Detail'],
  [['Vision', 'Eyes are tubular, like [[1]]'], ['Hearing', 'Face is a flat [[2]] of feathers'], ['Flight', 'Comb-like [[3]] on the wing edge'], ['Diet', 'Cough up a [[4]]']],
  [(['binoculars'], 'B', 'binoculars'), (['disc'], 'C', 'flat disc'), (['fringe'], 'D', 'fringe'), (['pellet'], 'E', 'pellet')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The owl waits on a [[1]].', 'It swoops down with talons [[2]].', 'It swallows small prey [[3]].', 'It coughs up a [[4]] later.'],
  [(['perch'], 'E', 'on a perch'), (['spread'], 'E', 'talons spread'), (['whole'], 'E', 'swallow small prey whole'), (['pellet'], 'E', 'compact pellet')], 1),
 feat('Match each statement with the correct item, A to D.', ['Eyes', 'Facial disc', 'Wing feathers', 'Nest boxes'], [
  ('They are huge in proportion to the head.', 0, 'B', 'huge in proportion to its head'),
  ('It directs sound to the ears.', 1, 'C', 'directs it to the ears'),
  ('They have a comb-like fringe.', 2, 'D', 'comb-like fringe'),
  ('They can double the number of barn owls.', 3, 'G', 'double the number of barn owls'),
 ]),
 multi('Which TWO threats to owls are mentioned in paragraph G?', ['Loss of nesting sites.', 'Poisons passing up the food chain.', 'Hunting for sport.', 'Floods.', 'Noise.'], [0, 1], [('G', 'removes nesting sites'), ('G', 'pass up the food chain')]),
 head(['Symbols of the night', 'Eyes like binoculars', 'Hearing the invisible', 'Wings without noise', 'What owls eat', 'Nests and chicks', 'Helping owls and farmers', 'The history of flight', 'Owls in literature'],
  [('A', 0, 'hunt: silently, at night'), ('B', 1, 'tubular, rather like a pair of binoculars'), ('C', 2, 'collects sound'), ('D', 3, 'glide almost without a sound'), ('E', 4, 'feeding mainly on small mammals'), ('F', 5, 'nest in holes in trees'), ('G', 6, 'Some owl species are in trouble')]),
 info([
  ('a reference to the size of a sparrow', 'A', 'size of a sparrow'),
  ('a comparison with grapefruits', 'B', 'grapefruits'),
  ('a reference to velvet', 'D', 'like velvet'),
  ('a reference to dissecting pellets', 'E', 'dissect the pellets'),
  ('a reference to free pest control', 'G', 'free pest control'),
 ]),
 ends(['are fixed in their sockets.', 'collects sound.', 'reduces turbulence.', 'nests underground.', 'sings in the day.', 'eats only fruit.', 'is blind.'], [
  ('An owl\'s eyes', 0, 'B', 'fixed in their sockets'),
  ('The facial disc', 1, 'C', 'collects sound'),
  ('The wing fringe', 2, 'D', 'reduces turbulence'),
  ('The burrowing owl', 3, 'F', 'nest underground'),
 ]),
 sent(2, [
  ('An owl has fourteen ___ bones.', ['neck'], 'B', 'neck bones'),
  ('Owls cough up the bones and fur as a ___.', ['pellet'], 'E', 'compact pellet'),
  ('Chicks are covered in white ___.', ['down'], 'F', 'white down'),
  ('Dr Lindgren is a conservation ___.', ['biologist'], 'G', 'conservation biologist'),
 ]),
 short(3, [
  ('What is the largest number of eggs a female may lay?', ['eight'], 'F', 'two and eight eggs'),
  ('What do owls mainly eat?', ['small mammals'], 'E', 'small mammals'),
  ('What is the longest time chicks stay in the nest?', ['ten weeks'], 'F', 'ten weeks'),
 ]),
])
