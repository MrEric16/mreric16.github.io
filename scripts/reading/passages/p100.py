from lib import *
from svgs import *
A = """Sharks have lived in the oceans for more than four hundred million years, which is longer than trees have existed on land and about two hundred million years before the first dinosaurs. There are over five hundred species, ranging from the dwarf lanternshark, which would fit in a human hand, to the whale shark, which can reach twelve metres in length. In films, sharks are shown as man-eating monsters, but in reality they are mostly shy animals, and fewer than a dozen people die from shark attacks in a typical year. In contrast, humans kill tens of millions of sharks annually. This passage describes how sharks live and why they need our protection."""
B = """Sharks differ from most fish in having a skeleton made of cartilage, the flexible material of which our ears and noses are made, rather than bone. Cartilage is lighter than bone, which helps a shark to float. Its skin is covered with tiny tooth-like scales, called denticles, which make it rough to the touch, like sandpaper, and which reduce drag as the shark swims. Sharks also have no swim bladder, the gas-filled organ that many fish use to stay at a given depth; instead, they have a large oil-filled liver, and many species must keep swimming to avoid sinking."""
C = """Shark teeth are remarkable. Sharks do not have a single set of teeth but rows of them, which are constantly replaced. When a tooth is lost, one from the row behind moves forward, like a conveyor belt. Some sharks may grow and lose tens of thousands of teeth in a lifetime. The shape of the teeth shows how the shark feeds: sharp, narrow teeth for gripping slippery fish, broad, serrated teeth for cutting large prey, and flat teeth for crushing shellfish. The whale shark and the basking shark, the two largest, have tiny teeth and instead filter plankton from the water."""
D = """Sharks have an extraordinary set of senses. Their sense of smell is acute: some species can detect a drop of blood diluted in a swimming pool of water. They also have good vision in dim light. In addition, they have a unique sense organ, called the ampullae of Lorenzini, a network of tiny jelly-filled pores around the snout which can detect the weak electrical fields produced by the muscles of other animals. A shark can find a fish hidden in sand by its electricity alone. Along the sides of the body, a line of sensitive cells detects vibrations in the water, so that a shark can feel an injured fish from far away."""
E = """Reproduction in sharks is varied and slow. Some species lay eggs in tough cases, often called mermaid's purses, which are attached to seaweed or rocks. Others keep the eggs inside the body until they hatch and give birth to live young, and in some species, the embryo is nourished through a link like a placenta, as in mammals. Sharks grow slowly and mature late: some species do not breed until they are twenty or even thirty years old. They produce few young, and the great white shark may live for seventy years. Because of this, a shark population cannot recover quickly if too many are killed."""
F = """Today, sharks are in danger. An estimated one hundred million sharks are killed every year, mostly in fishing nets and on long lines, many as an unwanted by-catch. Others are caught for their fins, which are used in a soup in some countries; often the fins are cut off and the body is thrown back into the sea. About a third of shark and ray species are now considered threatened with extinction. Dr Jonas Eriksen, a marine biologist who studies sharks with underwater cameras, points out that this has consequences beyond the sharks themselves, because many are top predators that keep the numbers of other species in balance."""
G = """There are signs of hope. Many countries now ban the finning of sharks, and some have created sanctuaries where fishing for sharks is forbidden. In some places, divers who pay to see sharks bring more money to the local economy than fishermen who kill them. Dr Eriksen urges consumers to avoid shark products and to choose fish from sustainable sources. He also hopes that attitudes are changing. Young people, he says, are growing up with a different picture of sharks, not as monsters but as ancient and important animals, which have survived several mass extinctions and deserve a place in the future."""
P = passage('p100', 'Sharks: Ancient and Endangered', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Sharks have lived in the oceans for more than 400 million years.', 'T', 'A', 'more than four hundred million years'),
  ('There are over five hundred species of shark.', 'T', 'A', 'over five hundred species'),
  ('The whale shark can reach twelve metres.', 'T', 'A', 'twelve metres in length'),
  ('A shark\'s skeleton is made of bone.', 'F', 'B', 'cartilage'),
  ('Most sharks have a swim bladder.', 'F', 'B', 'no swim bladder'),
  ('Shark teeth are replaced constantly.', 'T', 'C', 'constantly replaced'),
  ('The ampullae of Lorenzini detect electrical fields.', 'T', 'D', 'weak electrical fields'),
  ('Some sharks lay eggs in cases.', 'T', 'E', 'mermaid\'s purses'),
  ('Sharks are found in the Aral Sea.', 'NG', 'A', 'in the oceans', 'The Aral Sea is not mentioned.'),
 ]),
 mcq([
  ('Why is cartilage useful to a shark?', ['It is lighter than bone.', 'It is harder than bone.', 'It is warmer.', 'It is cheaper.'], 0, 'B', 'lighter than bone'),
  ('What happens when a shark loses a tooth?', ['One from the row behind moves forward.', 'It never grows back.', 'The shark stops eating.', 'It grows a bone.'], 0, 'C', 'moves forward'),
  ('Why do sharks matter to the sea?', ['They keep other species in balance.', 'They clean the water.', 'They make waves.', 'They feed on plants.'], 0, 'F', 'in balance'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Skeleton', 'Made of [[1]]'], ['Skin', 'Covered with tooth-like [[2]]'], ['Whale shark and basking shark', 'Filter [[3]]'], ['Fins', 'Used in a [[4]]']],
  [(['cartilage'], 'B', 'cartilage'), (['scales'], 'B', 'tooth-like scales'), (['plankton'], 'C', 'plankton'), (['soup'], 'F', 'soup')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['A tooth is lost.', 'A tooth from the row [[1]] moves forward.', 'The new tooth is used for gripping, cutting or [[2]].', 'Sharks may lose tens of [[3]] of teeth in a lifetime.'],
  [(['behind'], 'C', 'row behind'), (['crushing'], 'C', 'crushing shellfish'), (['thousands'], 'C', 'tens of thousands')], 1),
 feat('Match each statement with the correct item, A to D.', ['Denticles', 'Mermaid\'s purses', 'Finning', 'Sanctuaries'], [
  ('They reduce drag as a shark swims.', 0, 'B', 'reduce drag'),
  ('They are tough egg cases.', 1, 'E', 'tough cases'),
  ('Many countries now ban it.', 2, 'G', 'ban the finning'),
  ('Fishing for sharks is forbidden there.', 3, 'G', 'fishing for sharks is forbidden'),
 ]),
 multi('Which TWO ways of detecting prey are mentioned in paragraph D?', ['Smell.', 'Electrical fields.', 'Hearing music.', 'Seeing colours.', 'Tasting water.'], [0, 1], [('D', 'sense of smell'), ('D', 'electrical fields')]),
 head(['Ancient and misunderstood', 'Built of cartilage', 'A conveyor belt of teeth', 'Extraordinary senses', 'Slow to breed', 'A threatened species', 'Signs of hope', 'The history of fishing', 'Whales in the sea'],
  [('A', 0, 'longer than trees have existed on land'), ('B', 1, 'skeleton made of cartilage'), ('C', 2, 'like a conveyor belt'), ('D', 3, 'extraordinary set of senses'), ('E', 4, 'varied and slow'), ('F', 5, 'sharks are in danger'), ('G', 6, 'signs of hope')]),
 info([
  ('a comparison with sandpaper', 'B', 'sandpaper'),
  ('a reference to a swimming pool', 'D', 'swimming pool'),
  ('a reference to the great white shark\'s lifespan', 'E', 'seventy years'),
  ('a reference to by-catch', 'F', 'by-catch'),
  ('a reference to mass extinctions', 'G', 'several mass extinctions'),
 ]),
 ends(['is rough like sandpaper.', 'detect electrical fields.', 'mature late.', 'are caught for their fins.', 'is made of bone.', 'are always dangerous.', 'live in rivers only.'], [
  ('Shark skin', 0, 'B', 'rough to the touch'),
  ('The ampullae of Lorenzini', 1, 'D', 'electrical fields'),
  ('Many sharks', 2, 'E', 'do not breed until'),
  ('Millions of sharks', 3, 'F', 'caught for their fins'),
 ]),
 sent(2, [
  ('A shark\'s skeleton is made of ___.', ['cartilage'], 'B', 'cartilage'),
  ('Sharks have no ___ bladder.', ['swim'], 'B', 'swim bladder'),
  ('The two largest sharks filter ___.', ['plankton'], 'C', 'plankton'),
  ('Dr Eriksen is a marine ___.', ['biologist'], 'F', 'marine biologist'),
 ]),
 short(3, [
  ('How long can a great white shark live?', ['seventy years'], 'E', 'seventy years'),
  ('How many sharks are killed each year?', ['one hundred million'], 'F', 'one hundred million'),
  ('What fraction of species are threatened?', ['a third'], 'F', 'a third'),
 ]),
])
