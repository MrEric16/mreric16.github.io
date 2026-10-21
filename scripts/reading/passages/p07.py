from lib import *
A = """Octopuses belong to the cephalopods, a group that includes squid and cuttlefish. Their ancestors separated from the line that led to humans more than half a billion years ago, so whatever intelligence they possess evolved entirely independently of ours. An octopus has roughly five hundred million nerve cells, a number comparable with that of a dog, but the way they are arranged is very different: about two thirds of them lie not in the brain but in the arms."""
B = """This arrangement gives each arm a surprising degree of independence. A severed arm will still react to touch and can even grasp food. The suckers contain sensors that detect chemicals, so an octopus can taste what it touches. The brain does not appear to control every movement in detail; instead it sends general instructions, such as reaching towards a rock, and the arm works out the details for itself. Engineers who design flexible robots are studying this system closely."""
C = """In the laboratory, octopuses have shown a talent for solving problems. Dr Sofia Marchetti's team at a marine research centre placed a crab inside a sealed screw-top jar and found that most of the octopuses learned to open it within a few attempts. Once they had learned, they could do so in minutes. Others learned to escape from tanks by squeezing through gaps scarcely wider than their eyes, and aquarium staff report that some individuals squirt jets of water at lamps until they go out."""
D = """Evidence from the wild is even more striking. Researchers in Indonesia filmed veined octopuses collecting discarded coconut shells, carrying them across the seabed and later assembling them into a shelter. Because an octopus carrying shells can only shuffle slowly, and so is at greater risk from predators, the behaviour seems to involve planning for a future need. Many scientists regard it as one of the clearest examples of tool use in an invertebrate."""
E = """Camouflage is another remarkable ability. The skin contains thousands of cells called chromatophores, which expand and contract to change colour and pattern in less than a second, and muscles beneath the skin can raise bumps to imitate rock or coral. Yet most octopuses appear to be colour-blind, because their eyes contain only one type of light-sensitive cell. How they match the colours around them is not fully understood. Some researchers suspect that the skin itself can detect light, although this has not been proved."""
F = """Octopuses live short lives and mostly live alone. Most species survive for only one or two years, and a mother usually dies soon after her eggs hatch, so young octopuses have no parents from whom to learn. Everything they know must be discovered for themselves. Professor Alan Whitcombe urges caution about describing this as intelligence. A behaviour that looks clever, he says, may be instinct or the result of simple trial and error, and there is no agreed test for comparing minds that are so unlike our own. We tend, he argues, to judge animals by how closely they resemble humans, which is a poor standard. His warning is a fair one, but it cuts both ways: it is just as unwise to deny intelligence where it may exist."""
G = """The debate has practical consequences. In 2022 Britain passed a law that recognises octopuses and other cephalopods as sentient beings, meaning that they are capable of feeling pain and distress, and it set up a committee to advise the government on their welfare. Meanwhile, companies in several countries are exploring ways to farm octopuses for food. Whatever label we choose, the safest course is surely to give these animals the benefit of the doubt."""
P = passage('p07', 'Thinking with Eight Arms', 'Biology', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Octopus intelligence developed separately from human intelligence.', 'T', 'A', 'evolved entirely independently of ours'),
  ('An octopus has far more nerve cells than a dog.', 'F', 'A', 'a number comparable with that of a dog'),
  ('Most of an octopus\'s nerve cells are found in its arms.', 'T', 'A', 'about two thirds of them lie not in the brain but in the arms'),
  ('A severed octopus arm is unable to grasp food.', 'F', 'B', 'can even grasp food'),
  ('Dr Marchetti\'s octopuses opened the jar on their first attempt.', 'F', 'C', 'learned to open it within a few attempts'),
  ('Dr Marchetti\'s team used more than one species of octopus.', 'NG', 'C', 'Dr Sofia Marchetti\'s team at a marine research centre', 'The passage does not say which species were tested.'),
  ('The veined octopuses in Indonesia were filmed by researchers.', 'T', 'D', 'Researchers in Indonesia filmed veined octopuses'),
  ('Most octopuses can see colours clearly.', 'F', 'E', 'most octopuses appear to be colour-blind'),
  ('It has been proved that octopus skin can detect light.', 'F', 'E', 'although this has not been proved'),
  ('Octopus mothers usually die soon after their eggs hatch.', 'T', 'F', 'a mother usually dies soon after her eggs hatch'),
  ('Companies have already begun to sell farmed octopus in Britain.', 'NG', 'G', 'companies in several countries are exploring ways to farm octopuses for food', 'The passage says companies are exploring farming but not where the product is sold.'),
 ]),
 tfng([
  ('Octopus arms are simply controlled in every detail by the brain.', 'N', 'B', 'The brain does not appear to control every movement in detail'),
  ('Professor Whitcombe\'s warning about the word intelligence is reasonable.', 'Y', 'F', 'His warning is a fair one'),
  ('It would be equally wrong to refuse to call octopuses intelligent if they are.', 'Y', 'F', 'it is just as unwise to deny intelligence where it may exist'),
  ('Octopuses should be farmed on a large scale.', 'NG', 'G', 'Whatever label we choose, the safest course is surely to give these animals the benefit of the doubt', 'The writer does not say whether farming should be expanded.'),
  ('Judging animals by how much they resemble humans is a good method.', 'N', 'F', 'which is a poor standard'),
  ('The law passed in 2022 was unnecessary.', 'NG', 'G', 'In 2022 Britain passed a law that recognises octopuses', 'The writer reports the law but gives no opinion on it.'),
  ('Octopus behaviour in the wild is more impressive than in the laboratory.', 'Y', 'D', 'Evidence from the wild is even more striking'),
 ], yn=True),
 feat('Match each statement with the correct source, A to C. You may use any letter more than once.', ['Dr Sofia Marchetti\'s team', 'Professor Alan Whitcombe', 'Researchers in Indonesia'], [
  ('Octopuses learned to open a sealed jar.', 0, 'C', 'learned to open it within a few attempts'),
  ('Octopus behaviour that seems clever may be a simple instinct.', 1, 'F', 'may be instinct or the result of simple trial and error'),
  ('Octopuses carried coconut shells across the seabed.', 2, 'D', 'carrying them across the seabed'),
  ('Humans judge animals by how like us they are.', 1, 'F', 'judge animals by how closely they resemble humans'),
  ('Octopuses assembled shells to make a shelter.', 2, 'D', 'assembling them into a shelter'),
  ('Once a skill was learned, it took only minutes to use.', 0, 'C', 'Once they had learned, they could do so in minutes'),
 ], cls=True),
 ends(['can react to touch even when separated from the body.', 'contain sensors that detect chemicals.', 'change colour in less than a second.', 'carry out the details of a movement without detailed instructions.', 'survive for only one or two years.', 'are the main way the animals find a mate.', 'protect their eggs after they hatch.', 'evolved from the ancestors of humans.'],
  [('A severed arm', 0, 'B', 'A severed arm will still react to touch'), ('The suckers of an octopus', 1, 'B', 'The suckers contain sensors that detect chemicals'), ('The arms of an octopus', 3, 'B', 'the arm works out the details for itself'), ('The chromatophores in the skin', 2, 'E', 'expand and contract to change colour and pattern in less than a second'), ('Most species of octopus', 4, 'F', 'Most species survive for only one or two years')]),
 mcq([
  ('What does the writer say about the nerve cells of an octopus?', ['They are arranged very differently from a dog\'s.', 'They are mostly found in the eyes.', 'They are fewer than those of a dog.', 'They are identical to human nerve cells.'], 0, 'A', 'the way they are arranged is very different'),
  ('Why does the writer mention the shells carried by veined octopuses?', ['to show that they are slow when carrying them', 'to suggest that they plan ahead', 'to explain how they hide from prey', 'to show that they work in groups'], 1, 'D', 'the behaviour seems to involve planning for a future need'),
  ('What does the writer say about Professor Whitcombe\'s warning?', ['It is mistaken in every respect.', 'It applies only to octopuses.', 'It has not been supported by tests.', 'It should be applied in both directions.'], 3, 'F', 'it cuts both ways'),
 ]),
 head(['A nervous system with an unusual layout', 'Arms that think for themselves', 'Success with puzzles', 'Planning in the wild', 'Changing colour without seeing it', 'Why caution is needed', 'The effect on the law and on farming', 'How octopuses care for their young'],
  [('B', 1, 'This arrangement gives each arm a surprising degree of independence'), ('C', 2, 'octopuses have shown a talent for solving problems'), ('D', 3, 'Evidence from the wild is even more striking'), ('E', 4, 'Camouflage is another remarkable ability'), ('F', 5, 'Professor Alan Whitcombe urges caution'), ('G', 6, 'The debate has practical consequences')]),
 info([
  ('a reference to a use that engineers might make of octopus research', 'B', 'Engineers who design flexible robots are studying this system closely'),
  ('an example of an escape from a tank', 'C', 'squeezing through gaps scarcely wider than their eyes'),
  ('a reason why the behaviour of carrying shells is risky', 'D', 'at greater risk from predators'),
  ('a theory about how octopuses detect light', 'E', 'the skin itself can detect light'),
  ('an explanation of why young octopuses learn alone', 'F', 'young octopuses have no parents from whom to learn'),
  ('a description of a legal change', 'G', 'passed a law that recognises octopuses'),
 ]),
 sent(2, [
  ('Octopuses belong to a group called the ___.', ['cephalopods'], 'A', 'belong to the cephalopods'),
  ('The suckers of an octopus contain sensors that detect ___.', ['chemicals'], 'B', 'sensors that detect chemicals'),
  ('In Marchetti\'s experiment, a ___ was placed inside a sealed jar.', ['crab'], 'C', 'placed a crab inside a sealed screw-top jar'),
  ('The skin cells that change colour are called ___.', ['chromatophores'], 'E', 'cells called chromatophores'),
  ('Octopus eyes contain only one type of ___ cell.', ['light-sensitive', 'light sensitive'], 'E', 'only one type of light-sensitive cell'),
  ('In 2022 a committee was set up to advise the government on octopus ___.', ['welfare'], 'G', 'advise the government on their welfare'),
 ]),
 short(3, [
  ('How many years do most octopus species live?', ['one or two', '1 or 2'], 'F', 'one or two years'),
  ('What can muscles beneath the skin raise to imitate rock or coral?', ['bumps'], 'E', 'raise bumps to imitate rock or coral'),
  ('What do some aquarium octopuses squirt water at?', ['lamps'], 'C', 'squirt jets of water at lamps'),
  ('What did the veined octopuses assemble from the shells?', ['a shelter', 'shelter'], 'D', 'assembling them into a shelter'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'About two thirds of an octopus\'s nerve cells lie in its [[1]]. The brain sends only [[2]] instructions, and each arm works out the details for itself. In the laboratory, octopuses learned to open a [[3]] jar to reach food, and in the wild they have been seen carrying [[4]] shells to make a shelter. Professor Whitcombe warns that some behaviour may be [[5]] and not intelligence.',
  [(['arms'], 'A', 'but in the arms'), (['general'], 'B', 'it sends general instructions'), (['screw-top'], 'C', 'a sealed screw-top jar'), (['coconut'], 'D', 'discarded coconut shells'), (['instinct'], 'F', 'may be instinct')], 1,
  bank=['arms', 'general', 'screw-top', 'coconut', 'instinct', 'detailed', 'glass', 'oyster', 'training']),
])
