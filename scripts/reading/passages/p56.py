from lib import *
A = """When winter comes, many animals face a crisis: the cold makes life uncomfortable, and food becomes hard to find. Some animals, such as swallows, solve the problem by migrating to a warmer region. Others stay and endure the cold by entering a state called hibernation, in which the body slows down so dramatically that it can survive for months on the fat stored during the summer. Hibernation is not simply a long sleep but a different state of life, with its own rules, its own dangers and its own surprising benefits."""
B = """During hibernation, an animal's body temperature, heart rate and breathing all fall. A ground squirrel's temperature may drop from about 37 degrees Celsius to just above freezing, and its heart rate from 200 beats a minute to as few as five. Its breathing may stop for several minutes at a time. These changes reduce the amount of energy that the animal uses to a few per cent of the normal figure, so that a small store of fat is enough to last the whole winter."""
C = """Not all hibernators behave in the same way. Some, like ground squirrels and bats, enter a deep state, and wake only every few weeks. Others, notably bears, enter a lighter state sometimes called torpor, in which the temperature falls by only five or six degrees. Female bears give birth in the middle of this period, in the den, without eating, drinking or passing waste, and they continue to feed their cubs on milk until spring. Scientists find this ability so remarkable that they study it for medical clues."""
D = """Preparing for hibernation takes months. In autumn, animals eat far more than usual, sometimes doubling their body weight, and they store the extra energy as fat. Some, such as chipmunks, also hide stores of food in their burrows and eat from them during their brief periods of waking. The animals must also choose a safe place. A good den or burrow has a steady temperature, protects from predators and stays dry; a poor choice can mean death, since a sleeper cannot escape from danger."""
E = """Why do hibernators wake up periodically if the state saves energy? The question puzzles scientists, because each awakening uses a great deal of energy, in total most of the energy that the animal spends during the winter. Some researchers believe that the animals need to sleep normally from time to time, since the brain still requires its ordinary rest. Others suggest that waking allows the body to repair damage or to remove waste. The truth is probably a combination of these explanations."""
F = """Hibernation is also a subject of medical research. Hibernating animals do not lose bone or muscle in the way that humans do after months in bed, and bears seem to avoid blood clots and kidney damage. Dr Elena Voss, a physiologist, hopes that understanding these mechanisms may one day help patients who must lie still for long periods, and perhaps even astronauts on long space journeys. Some researchers dream of putting humans into a state like hibernation, but that remains far from reality."""
G = """Climate change is complicating the lives of hibernators. In warmer winters, animals may wake early and find no food, or they may emerge to find that the plants on which they depend have not yet grown. Bats are also threatened by a disease called white-nose syndrome, caused by a fungus that grows on hibernating animals and makes them wake more often and use up their fat. Millions of bats have died in North America since the disease was first noticed in 2006, and scientists are searching for a cure."""
P = passage('p56', 'The Secrets of Hibernation', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Swallows survive the winter by hibernating.', 'F', 'A', 'solve the problem by migrating to a warmer region'),
  ('Hibernating animals live on fat stored in the summer.', 'T', 'A', 'the fat stored during the summer'),
  ('A ground squirrel\'s temperature can fall to just above freezing.', 'T', 'B', 'just above freezing'),
  ('A ground squirrel\'s heart rate can fall to five beats a minute.', 'T', 'B', 'as few as five'),
  ('Bats enter a lighter state than bears.', 'F', 'C', 'Some, like ground squirrels and bats, enter a deep state'),
  ('Female bears feed their cubs during hibernation.', 'T', 'C', 'they continue to feed their cubs on milk'),
  ('Chipmunks eat stored food during brief periods of waking.', 'T', 'D', 'eat from them during their brief periods of waking'),
  ('Bears in the wild live longer than ground squirrels.', 'NG', 'C', 'Others, notably bears, enter a lighter state', 'Lifespan is not discussed.'),
  ('White-nose syndrome was first noticed in 2006.', 'T', 'G', 'first noticed in 2006'),
 ]),
 mcq([
  ('Why does hibernation save so much energy?', ['The animal eats more.', 'The body slows dramatically.', 'The den is warm.', 'The animal wakes often.'], 1, 'B', 'reduce the amount of energy that the animal uses'),
  ('Why is the choice of den important?', ['A sleeper cannot escape danger.', 'Dens are rare.', 'The cubs need it.', 'It is used for storing food only.'], 0, 'D', 'a sleeper cannot escape from danger'),
  ('What is puzzling about waking periods?', ['They are too long.', 'They use a lot of energy.', 'They occur in summer.', 'They are caused by noise.'], 1, 'E', 'each awakening uses a great deal of energy'),
 ]),
 feat('Match each statement with the correct animal, A to C.', ['Ground squirrels', 'Bears', 'Chipmunks'], [
  ('They hide food in their burrows.', 2, 'D', 'hide stores of food in their burrows'),
  ('Their temperature falls only five or six degrees.', 1, 'C', 'falls by only five or six degrees'),
  ('Their heart rate can fall to five beats a minute.', 0, 'B', 'as few as five'),
  ('The females give birth during hibernation.', 1, 'C', 'Female bears give birth in the middle of this period'),
 ]),
 multi('Which TWO medical benefits of hibernation are mentioned in paragraph F?', ['Hibernators do not lose bone or muscle.', 'Bears seem to avoid blood clots.', 'Hibernators never catch infections.', 'Hibernators live for centuries.', 'Hibernators need no water.'], [0, 1], [('F', 'do not lose bone or muscle'), ('F', 'bears seem to avoid blood clots and kidney damage')]),
 head(['A way to survive the winter', 'The slowing of the body', 'Different degrees of sleep', 'Fat, food and shelter', 'The puzzle of waking', 'Lessons for medicine', 'Modern threats', 'The migration of birds', 'The life of a bat'],
  [('A', 0, 'entering a state called hibernation'), ('B', 1, 'body temperature, heart rate and breathing all fall'), ('C', 2, 'Not all hibernators behave in the same way'), ('D', 3, 'Preparing for hibernation takes months'), ('E', 4, 'Why do hibernators wake up periodically'), ('F', 5, 'Hibernation is also a subject of medical research'), ('G', 6, 'Climate change is complicating the lives of hibernators')]),
 info([
  ('a reference to a bird that migrates', 'A', 'swallows'),
  ('a figure for normal heart rate in a squirrel', 'B', '200 beats a minute'),
  ('a mention of a lighter state of hibernation', 'C', 'torpor'),
  ('a reference to doubling body weight', 'D', 'doubling their body weight'),
  ('a mention of space travellers', 'F', 'astronauts on long space journeys'),
 ]),
 ends(['stores fat during the summer.', 'wakes only every few weeks.', 'gives birth in the den.', 'make animals wake more often.', 'is a long sleep without any change.', 'is found only in Africa.', 'cures kidney disease.'], [
  ('A hibernating animal', 0, 'A', 'survive for months on the fat stored during the summer'),
  ('A deep hibernator', 1, 'C', 'wake only every few weeks'),
  ('A female bear', 2, 'C', 'Female bears give birth in the middle of this period, in the den'),
  ('The fungus of white-nose syndrome', 3, 'G', 'makes them wake more often and use up their fat'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['In autumn, animals eat far more and store the extra energy as [[1]].', 'They choose a safe [[2]] that stays dry.', 'Body temperature, heart rate and [[3]] all fall.', 'The animal wakes up again in [[4]].'],
  [(['fat'], 'D', 'store the extra energy as fat'), (['den', 'burrow'], 'D', 'A good den or burrow'), (['breathing'], 'B', 'breathing all fall'), (['spring'], 'C', 'until spring')], 1),
 sent(2, [
  ('Hibernation is a different ___ of life.', ['state'], 'A', 'a different state of life'),
  ('A ground squirrel\'s heart rate falls from 200 beats a minute to as few as ___.', ['five'], 'B', 'as few as five'),
  ('The lighter state of a bear is sometimes called ___.', ['torpor'], 'C', 'called torpor'),
  ('Dr Voss is a ___.', ['physiologist'], 'F', 'a physiologist'),
 ]),
 short(3, [
  ('Which animals wake only every few weeks?', ['ground squirrels', 'bats'], 'C', 'ground squirrels and bats'),
  ('What do bats suffer from?', ['white-nose syndrome'], 'G', 'white-nose syndrome'),
  ('Where have millions of bats died?', ['north america'], 'G', 'in North America'),
 ]),
])
