from lib import *
from svgs import *
A = """Food is the body's fuel, but it cannot be used until it has been broken down into tiny molecules that can pass into the blood. This task is carried out by the digestive system, a long tube, about nine metres in length, that runs from the mouth to the anus, together with several organs that help it. The whole journey takes between one and three days, and every stage has its own task, from the cutting of food by the teeth to the final absorption of water."""
B = """Digestion begins in the mouth. The teeth cut and grind food into small pieces, and the tongue mixes it with saliva, a liquid made by glands beneath the tongue and in the cheeks. Saliva contains an enzyme that starts to break down starch, which is why a piece of bread tastes slightly sweet if it is chewed for a long time. When the food has been formed into a soft ball, it is swallowed, and the next stage of the journey begins."""
C = """The swallowed food enters the oesophagus, a muscular tube about twenty-five centimetres long that leads from the throat to the stomach. The walls of the tube contract in waves, a process called peristalsis, which pushes the food downwards. The waves are so powerful that a person can swallow while standing on his or her head, and astronauts can eat in space. A flap of tissue closes the windpipe during swallowing, to prevent food from entering the lungs."""
D = """The stomach is a stretchable bag that normally holds about one litre of food, although it can expand to hold much more. Its walls produce hydrochloric acid, which kills most of the bacteria swallowed with food, and enzymes that break down protein. The muscles of the stomach churn the food for about two to four hours until it becomes a thick liquid. The stomach protects itself from its own acid with a layer of mucus, and if this layer fails, the result may be an ulcer."""
E = """The semi-liquid food then moves to the small intestine, which is about six metres long. This is where most digestion is completed and almost all nutrients enter the blood. The liver supplies bile, which breaks fat into small drops, and the pancreas supplies enzymes that digest protein, fat and starch. The inner surface of the intestine is covered with millions of tiny finger-like projections called villi, which greatly increase its area and allow absorption to be fast and efficient."""
F = """What cannot be digested, such as fibre, passes into the large intestine, which is shorter, at about one and a half metres, but wider. Its main job is to absorb water and some minerals, so that the waste becomes solid. Trillions of bacteria live here, and many of them are helpful: they make certain vitamins and help to break down fibre. The remains are stored in the rectum until they are passed out of the body. A diet rich in fibre keeps this process working smoothly."""
G = """Digestive problems are among the most common reasons for visiting a doctor. Dr Paolo Ricci, a gastroenterologist, advises people to eat slowly, to chew well, to drink plenty of water and to include fruit, vegetables and whole grains in their meals. He also warns that antibiotics, which kill harmful bacteria, may also harm the helpful ones in the intestines, and that they should therefore be taken only when a doctor prescribes them. Good digestion, he says, is the foundation of good health. Patients who ignore persistent pain, bleeding or sudden weight loss, he adds, should see a doctor without delay, since early treatment of most digestive diseases is simple and successful."""
S, PT, W, H = chain(5)
P = passage('p58', 'How We Digest Food', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The digestive tube is about nine metres long.', 'T', 'A', 'about nine metres in length'),
  ('Food takes only a few minutes to pass through the body.', 'F', 'A', 'between one and three days'),
  ('Saliva starts to break down starch.', 'T', 'B', 'starts to break down starch'),
  ('The oesophagus leads from the mouth to the intestine.', 'F', 'C', 'from the throat to the stomach'),
  ('Peristalsis pushes food downwards.', 'T', 'C', 'pushes the food downwards'),
  ('Stomach acid kills most bacteria swallowed with food.', 'T', 'D', 'kills most of the bacteria swallowed with food'),
  ('Most nutrients enter the blood in the small intestine.', 'T', 'E', 'almost all nutrients enter the blood'),
  ('The large intestine is longer than the small intestine.', 'F', 'F', 'shorter, at about one and a half metres'),
  ('Antibiotics cure all digestive problems.', 'NG', 'G', 'antibiotics, which kill harmful bacteria', 'This claim is not made.'),
 ]),
 mcq([
  ('Why does bread taste sweet if chewed for a long time?', ['Sugar is added.', 'Saliva breaks down starch.', 'The teeth release sugar.', 'The tongue makes sugar.'], 1, 'B', 'an enzyme that starts to break down starch'),
  ('What protects the stomach from its own acid?', ['A layer of mucus.', 'Saliva.', 'Bile.', 'Fibre.'], 0, 'D', 'a layer of mucus'),
  ('What is the main job of the large intestine?', ['To digest fat.', 'To absorb water.', 'To make bile.', 'To store food.'], 1, 'F', 'to absorb water and some minerals'),
 ]),
 multi('Which TWO substances supplied to the small intestine are mentioned in paragraph E?', ['Bile.', 'Enzymes.', 'Acid.', 'Saliva.', 'Mucus.'], [0, 1], [('E', 'The liver supplies bile'), ('E', 'the pancreas supplies enzymes')]),
 head(['A tube with many tasks', 'The first stage', 'A muscular passage', 'A bag of acid', 'The main place for absorption', 'Water, waste and bacteria', 'Advice for good digestion', 'The history of medicine', 'The structure of the heart'],
  [('A', 0, 'a long tube, about nine metres in length'), ('B', 1, 'Digestion begins in the mouth'), ('C', 2, 'The swallowed food enters the oesophagus'), ('D', 3, 'The stomach is a stretchable bag'), ('E', 4, 'where most digestion is completed'), ('F', 5, 'What cannot be digested'), ('G', 6, 'advises people to eat slowly')]),
 info([
  ('a reference to a liquid made by glands', 'B', 'saliva, a liquid made by glands'),
  ('a mention of astronauts', 'C', 'astronauts can eat in space'),
  ('a reference to an ulcer', 'D', 'the result may be an ulcer'),
  ('a description of finger-like projections', 'E', 'tiny finger-like projections called villi'),
  ('a mention of helpful bacteria', 'F', 'many of them are helpful'),
 ]),
 ends(['cut and grind food.', 'push food by waves of contraction.', 'kills bacteria.', 'breaks fat into small drops.', 'absorbs most of the water.', 'is made in the mouth only.', 'is found in the lungs.'], [
  ('The teeth', 0, 'B', 'cut and grind food into small pieces'),
  ('The walls of the oesophagus', 1, 'C', 'contract in waves'),
  ('Hydrochloric acid', 2, 'D', 'kills most of the bacteria swallowed with food'),
  ('Bile', 3, 'E', 'breaks fat into small drops'),
 ]),
 diag('Label the parts of the digestive system, in order. Write ONE OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['mouth'], 'B', 'in the mouth'), (['oesophagus'], 'C', 'the oesophagus'), (['stomach'], 'D', 'The stomach'), (['small intestine'], 'E', 'the small intestine'), (['large intestine'], 'F', 'the large intestine')], 2),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Teeth cut food and the tongue mixes it with [[1]].', 'Waves of [[2]] push the food down the oesophagus.', 'The stomach churns the food into a thick [[3]].', 'In the small intestine, nutrients enter the [[4]].'],
  [(['saliva'], 'B', 'mixes it with saliva'), (['peristalsis'], 'C', 'peristalsis'), (['liquid'], 'D', 'a thick liquid'), (['blood'], 'E', 'enter the blood')], 1),
 sent(2, [
  ('The oesophagus is about twenty-five ___ long.', ['centimetres'], 'C', 'twenty-five centimetres long'),
  ('The stomach normally holds about one ___.', ['litre'], 'D', 'about one litre'),
  ('The small intestine is covered with ___.', ['villi'], 'E', 'called villi'),
  ('Dr Ricci is a ___.', ['gastroenterologist'], 'G', 'a gastroenterologist'),
 ]),
 short(3, [
  ('What do bacteria in the large intestine make?', ['vitamins', 'certain vitamins'], 'F', 'make certain vitamins'),
  ('What is the longest the food journey takes?', ['three days'], 'A', 'one and three days'),
  ('What diet keeps the process working smoothly?', ['rich in fibre', 'fibre'], 'F', 'A diet rich in fibre'),
 ]),
])
