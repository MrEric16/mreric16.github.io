from lib import *
from svgs import *
A = """The human heart is a muscle about the size of a clenched fist, and it never rests. In an average lifetime it beats more than two and a half billion times, pumping blood through about ninety-six thousand kilometres of blood vessels, a distance greater than twice the circumference of the Earth. It sits slightly to the left of the middle of the chest, behind the breastbone, and weighs about three hundred grams. Although it is small, it is the most hardworking organ in the body, and if it stops for more than a few minutes, the brain is damaged."""
B = """The heart has four chambers. The two upper chambers, called atria, receive blood, and the two lower chambers, called ventricles, push it out. A wall of muscle, the septum, divides the heart into a right and a left side, so that the blood which has been to the lungs and the blood returning from the body never mix. Valves between the chambers open and close like one-way doors, and the familiar sound of a heartbeat, lub-dub, is the noise made when they snap shut."""
C = """The journey of the blood begins when it returns from the body, short of oxygen, and enters the right atrium. It passes through a valve into the right ventricle, which pumps it to the lungs. In the lungs, the blood loses carbon dioxide and takes in fresh oxygen. This part of the circuit is short and needs only a gentle push, so the muscle of the right ventricle is relatively thin. The oxygen-rich blood then flows back to the heart along four vessels called the pulmonary veins."""
D = """These vessels deliver the blood to the left atrium, from which it passes through a second valve into the left ventricle. This is the strongest chamber of all, with a wall about three times as thick as that of the right ventricle, since it must send blood to every part of the body, from the brain to the toes. The blood leaves through the aorta, the largest artery, which is as wide as a garden hose. From the aorta, smaller arteries branch again and again until they reach every organ."""
E = """A heartbeat is controlled by a tiny group of cells called the pacemaker, in the wall of the right atrium. It sends out a small electrical signal about seventy times each minute at rest, and the signal spreads across the muscle, making it contract in a precise order. During exercise, the brain tells the pacemaker to work faster, and the heart rate can rise to more than two hundred beats a minute in a young athlete. Some people are born with a pacemaker that does not work properly, and doctors can then fit a small battery-powered device."""
F = """The heart itself needs a supply of blood, and it receives it through the coronary arteries, which run over its surface. If one of these arteries is blocked, by fat for example, part of the heart muscle is starved of oxygen, and the person suffers a heart attack. Heart disease is the most common cause of death in the world. Doctors recognise several risk factors: smoking, high blood pressure, lack of exercise and a diet rich in fat. Dr Karim Yusupov, a cardiologist, says that about half of all heart attacks could be prevented by changes in the way people live."""
G = """Advances in treatment have saved millions of lives. Surgeons can now open a blocked artery with a tiny balloon, replace a damaged valve and even give a patient a new heart from a donor. In some cases, a mechanical pump can keep a person alive for months while he or she waits for a transplant. Researchers are also working on growing heart tissue in the laboratory from a patient's own cells. Nevertheless, the best advice has not changed in decades: do not smoke, eat sensibly, and take regular exercise."""
S, PT, W, H = cycle(5)
P = passage('p38', 'The Human Heart', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The heart is about the size of a clenched fist.', 'T', 'A', 'about the size of a clenched fist'),
  ('The heart sits exactly in the middle of the chest.', 'F', 'A', 'slightly to the left of the middle of the chest'),
  ('The heart has four chambers.', 'T', 'B', 'The heart has four chambers'),
  ('Blood from the body and blood from the lungs mix in the heart.', 'F', 'B', 'never mix'),
  ('The sound of a heartbeat is made by the valves closing.', 'T', 'B', 'the noise made when they snap shut'),
  ('The right ventricle has a thicker wall than the left.', 'F', 'D', 'about three times as thick as that of the right ventricle'),
  ('The aorta is the largest artery.', 'T', 'D', 'the largest artery'),
  ('The pacemaker is in the wall of the left ventricle.', 'F', 'E', 'in the wall of the right atrium'),
  ('Heart disease is more common in men than in women.', 'NG', 'F', 'Heart disease is the most common cause of death in the world', 'The passage makes no comparison between men and women.'),
 ]),
 mcq([
  ('Why is the wall of the right ventricle thin?', ['It is old.', 'It pumps blood a short distance.', 'It is not used.', 'It holds less blood.'], 1, 'C', 'short and needs only a gentle push'),
  ('What happens in a heart attack?', ['The pacemaker fails.', 'Part of the muscle lacks oxygen.', 'The valves open.', 'The aorta bursts.'], 1, 'F', 'part of the heart muscle is starved of oxygen'),
  ('What does Dr Yusupov say?', ['Heart attacks cannot be prevented.', 'About half could be prevented.', 'Only old people suffer them.', 'Surgery is always needed.'], 1, 'F', 'about half of all heart attacks could be prevented'),
 ]),
 multi('Which TWO risk factors for heart disease are mentioned in paragraph F?', ['Smoking.', 'High blood pressure.', 'Drinking tea.', 'Living in cities.', 'Working at night.'], [0, 1], [('F', 'smoking, high blood pressure'), ('F', 'smoking, high blood pressure')]),
 head(['An organ that never rests', 'Chambers and valves', 'From the body to the lungs', 'From the lungs to the body', 'Controlling the beat', 'Disease and prevention', 'Modern medicine', 'The history of the stethoscope', 'How the lungs work'],
  [('A', 0, 'it never rests'), ('B', 1, 'The heart has four chambers'), ('C', 2, 'The journey of the blood begins'), ('D', 3, 'These vessels deliver the blood to the left atrium'), ('E', 4, 'A heartbeat is controlled by a tiny group of cells'), ('F', 5, 'The heart itself needs a supply of blood'), ('G', 6, 'Advances in treatment have saved millions of lives')]),
 info([
  ('a comparison with the circumference of the Earth', 'A', 'twice the circumference of the Earth'),
  ('a description of the function of valves', 'B', 'open and close like one-way doors'),
  ('a comparison of the aorta with a household object', 'D', 'as wide as a garden hose'),
  ('a mention of a battery-powered device', 'E', 'a small battery-powered device'),
  ('a mention of a tiny balloon used in treatment', 'G', 'with a tiny balloon'),
 ]),
 ends(['receive blood.', 'push blood out.', 'sends the blood to the lungs.', 'is controlled by the pacemaker.', 'is found in the lungs.', 'is made of bone.', 'was invented in the twentieth century.'], [
  ('The atria', 0, 'B', 'The two upper chambers, called atria, receive blood'),
  ('The ventricles', 1, 'B', 'the two lower chambers, called ventricles, push it out'),
  ('The right ventricle', 2, 'C', 'which pumps it to the lungs'),
  ('The rate of the heartbeat', 3, 'E', 'A heartbeat is controlled by a tiny group of cells'),
 ]),
 diag('Label the path of the blood, in order, starting at the top. Write ONE OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['right atrium'], 'C', 'the right atrium'), (['right ventricle'], 'C', 'the right ventricle'), (['lungs'], 'C', 'to the lungs'), (['left atrium'], 'D', 'the left atrium'), (['left ventricle'], 'D', 'the left ventricle')], 2),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Blood short of oxygen enters the [[1]].', 'The right ventricle pumps it to the [[2]].', 'The blood returns along the pulmonary [[3]].', 'The left ventricle sends it out through the [[4]].'],
  [(['right atrium'], 'C', 'enters the right atrium'), (['lungs'], 'C', 'pumps it to the lungs'), (['veins'], 'C', 'pulmonary veins'), (['aorta'], 'D', 'through the aorta')], 2),
 sent(2, [
  ('The heart weighs about three hundred ___.', ['grams'], 'A', 'about three hundred grams'),
  ('The wall dividing the heart is called the ___.', ['septum'], 'B', 'the septum'),
  ('The coronary arteries run over the heart\'s ___.', ['surface'], 'F', 'run over its surface'),
  ('Researchers are growing heart ___ in the laboratory.', ['tissue'], 'G', 'growing heart tissue'),
 ]),
 short(3, [
  ('What is the sound of a heartbeat?', ['lub-dub'], 'B', 'lub-dub'),
  ('Which vessel is the largest artery?', ['the aorta', 'aorta'], 'D', 'the aorta, the largest artery'),
  ('What is Dr Yusupov\'s speciality?', ['cardiologist', 'a cardiologist'], 'F', 'a cardiologist'),
 ]),
])
