from lib import *
from svgs import *
A = """The emperor penguin is the largest of the world's eighteen or so penguin species and the only one that breeds during the Antarctic winter. Adults stand about a metre and ten centimetres tall and weigh between twenty-two and forty-five kilograms, depending on the season. They cannot fly, but their wings have become flippers, and in the water they move with the grace of a bird in the air. Their lives are shaped by one of the harshest environments on Earth, where temperatures fall to minus sixty degrees and the wind blows at more than a hundred and fifty kilometres an hour. This passage explains how they survive."""
B = """In March, as the Antarctic autumn begins, emperor penguins walk up to a hundred and twenty kilometres across the ice from the sea to their breeding grounds, in groups of thousands. They walk upright or slide on their bellies, a method called tobogganing. Once there, each pair mates, and in May the female lays a single egg. Then comes the most extraordinary part of the story. She passes the egg carefully to her mate, who balances it on his feet and covers it with a warm fold of skin called the brood pouch, and she walks back to the sea to feed."""
C = """The males now face the worst of the winter. For about two months, and without eating anything, they stand on the ice with the egg on their feet. They survive by huddling together in dense groups of thousands, taking turns to stand in the warm centre, and the huddle slowly rotates so that no bird stays at the cold edge for long. Inside the group, the temperature can be thirty-five degrees warmer than outside. Each male may lose almost half of his body weight while waiting. If the egg touches the ice for even a minute, the chick inside will die."""
D = """At the end of July, around the time when the chick hatches, the females return, fat from feeding on fish and squid. Each recognises her mate among thousands by his call, and she takes over the care of the chick, feeding it with food that she has brought back in her stomach. Then it is the turn of the hungry males to walk to the sea. For the next few months, the parents take turns to feed the chick, which stays warm on their feet until it grows a coat of thick grey feathers. By December, when the ice begins to break up, the young birds are ready to go to sea."""
E = """Emperor penguins are among the finest divers of all birds. They can reach depths of more than five hundred metres, deeper than any other bird, and they can stay under water for over twenty minutes. Their bones are solid, not hollow like those of flying birds, which helps them to sink, and their blood and muscles store extra oxygen. When swimming fast, they can leap out of the water on to the ice, a skill which allows them to escape from leopard seals, their main enemy at sea, as well as from orcas."""
F = """Dr Marina Volkova, a polar biologist, has visited emperor penguin colonies for fifteen years. She says that the birds are among the most reliable indicators of change in Antarctica. The colonies depend on sea ice that remains solid until the chicks have grown their feathers; if the ice breaks up too early, the chicks fall into the water and drown. In recent years, some colonies have had almost no chicks surviving, and satellite photographs of the ice show that a few colonies have disappeared. Dr Volkova argues that the penguins' future depends on how quickly the world reduces the gases that warm the planet."""
G = """Counting penguins is difficult, since the colonies are remote and the weather is dangerous. Scientists now use satellites, which can detect the brown stains of penguin droppings on white ice, and they have found colonies that nobody knew existed. Drones with cameras, which fly over the birds without disturbing them, also help. Volunteers can join the work from their own homes by counting penguins in photographs. Dr Volkova hopes that these methods will give a clear picture, so that governments can protect the most important breeding grounds with new marine reserves and limits on fishing."""
P = passage('p79', 'The Emperor Penguin', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Emperor penguins breed during the Antarctic winter.', 'T', 'A', 'breeds during the Antarctic winter'),
  ('Emperor penguins can fly short distances.', 'F', 'A', 'They cannot fly'),
  ('Penguins walk up to a hundred and twenty kilometres to breed.', 'T', 'B', 'up to a hundred and twenty kilometres'),
  ('The female carries the egg on her feet.', 'F', 'B', 'passes the egg carefully to her mate'),
  ('The males do not eat for about two months.', 'T', 'C', 'about two months'),
  ('The huddle can be thirty-five degrees warmer than the outside.', 'T', 'C', 'thirty-five degrees warmer than outside'),
  ('The females recognise their mates by their calls.', 'T', 'D', 'by his call'),
  ('Emperor penguins can dive deeper than five hundred metres.', 'T', 'E', 'more than five hundred metres'),
  ('Penguin chicks learn to swim in January.', 'NG', 'D', 'ready to go to sea', 'The month they swim is not given.'),
 ]),
 mcq([
  ('How do the males survive the winter?', ['By huddling together.', 'By hunting.', 'By sleeping in caves.', 'By flying south.'], 0, 'C', 'huddling together in dense groups'),
  ('Why do penguins have solid bones?', ['It helps them to sink.', 'It keeps them warm.', 'It makes them fast.', 'It helps them to walk.'], 0, 'E', 'which helps them to sink'),
  ('Why do scientists use satellites?', ['To detect stains of droppings.', 'To feed penguins.', 'To measure the wind.', 'To catch fish.'], 0, 'G', 'detect the brown stains of penguin droppings'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['The female lays a single [[1]].', 'The male balances it on his [[2]].', 'The males huddle together in groups of [[3]].', 'The females return at the end of [[4]].'],
  [(['egg'], 'B', 'a single egg'), (['feet'], 'B', 'on his feet'), (['thousands'], 'C', 'groups of thousands'), (['july'], 'D', 'end of July')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Month', 'Event'],
  [['March', 'Penguins walk to the [[1]] grounds'], ['May', 'The female lays a single [[2]]'], ['July', 'The females return, fat from feeding on fish and [[3]]'], ['December', 'The [[4]] begins to break up']],
  [(['breeding'], 'B', 'their breeding grounds'), (['egg'], 'B', 'a single egg'), (['squid'], 'D', 'fish and squid'), (['ice'], 'D', 'the ice begins to break up')], 1),
 feat('Match each statement with the correct animal, A to D.', ['The male', 'The female', 'The chick', 'The leopard seal'], [
  ('It keeps the egg warm on its feet.', 0, 'B', 'balances it on his feet'),
  ('It brings food back in its stomach.', 1, 'D', 'brought back in her stomach'),
  ('It grows a coat of thick grey feathers.', 2, 'D', 'thick grey feathers'),
  ('It is the main enemy of penguins at sea.', 3, 'E', 'main enemy at sea'),
 ]),
 multi('Which TWO methods of counting penguins are mentioned in paragraph G?', ['Using satellites.', 'Using drones with cameras.', 'Using helicopters.', 'Tagging every bird.', 'Using fishing nets.'], [0, 1], [('G', 'use satellites'), ('G', 'Drones with cameras')]),
 head(['Life at the edge of the world', 'A long walk to the ice', 'Two months without food', 'The return of the females', 'Masters of the deep', 'A warning from the ice', 'New ways of counting', 'The history of Antarctica', 'Penguins in zoos'],
  [('A', 0, 'one of the harshest environments on Earth'), ('B', 1, 'walk up to a hundred and twenty kilometres across the ice'), ('C', 2, 'without eating anything'), ('D', 3, 'the females return'), ('E', 4, 'among the finest divers of all birds'), ('F', 5, 'among the most reliable indicators of change in Antarctica'), ('G', 6, 'Counting penguins is difficult')]),
 info([
  ('a method of travelling on the belly', 'B', 'slide on their bellies'),
  ('a reference to a rotating huddle', 'C', 'huddle slowly rotates'),
  ('a reference to recognition by sound', 'D', 'by his call'),
  ('a contrast with the bones of flying birds', 'E', 'hollow like those of flying birds'),
  ('a reference to lost colonies', 'F', 'a few colonies have disappeared'),
 ]),
 ends(['lose almost half their body weight.', 'turns slowly.', 'are the main enemy at sea.', 'fly over birds without disturbing them.', 'lay four eggs.', 'live in forests.', 'can fly.'], [
  ('Male penguins', 0, 'C', 'almost half of his body weight'),
  ('The huddle', 1, 'C', 'slowly rotates'),
  ('Leopard seals', 2, 'E', 'main enemy at sea'),
  ('Drones', 3, 'G', 'without disturbing them'),
 ]),
 sent(2, [
  ('Sliding on the belly is called ___.', ['tobogganing'], 'B', 'called tobogganing'),
  ('The warm fold of skin is called the ___ pouch.', ['brood'], 'B', 'brood pouch'),
  ('Dr Volkova is a polar ___.', ['biologist'], 'F', 'polar biologist'),
  ('Satellites detect the brown stains of penguin ___.', ['droppings'], 'G', 'penguin droppings'),
 ]),
 short(3, [
  ('How long can they stay under water?', ['twenty minutes', 'over twenty minutes'], 'E', 'over twenty minutes'),
  ('What do the females feed on at sea?', ['fish and squid'], 'D', 'fish and squid'),
  ('For how many years has Dr Volkova visited colonies?', ['fifteen years', 'fifteen'], 'F', 'fifteen years'),
 ]),
])
