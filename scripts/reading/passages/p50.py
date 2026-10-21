from lib import *
from svgs import *
A = """Vision is the most important of our senses, since about a quarter of the human brain is involved in processing what we see. The eye works rather like a camera: it collects light from the world, focuses it into a sharp image, and turns that image into electrical signals that the brain can read. The whole process is so fast and smooth that we are normally unaware of it, and only when something goes wrong do we notice how much we depend on it. This passage follows the path of a ray of light from an object into the brain, stage by stage."""
B = """Light first meets the cornea, the clear, curved window at the front of the eye. The cornea does most of the work of focusing, bending the light rays inwards so that they converge. It has no blood vessels, which would block the view, and it receives oxygen directly from the air and from the tears that cover its surface. It is also very sensitive to touch, which is why a speck of dust on the eye is so painful."""
C = """Behind the cornea is the pupil, the round black opening in the centre of the coloured part of the eye, which is called the iris. The iris is a ring of muscle that controls the size of the pupil. In bright light the pupil becomes small to protect the eye, and in the dark it widens to admit as much light as possible. The change takes only a fraction of a second, although it takes longer to adapt fully to darkness, which is why a cinema seems black at first."""
D = """Next the light passes through the lens, a flexible, transparent disc that adjusts the focus. When we look at a distant object, the lens becomes thin, and when we look at something close, such as a book, it becomes thick and round. This ability to change shape is called accommodation. With age the lens becomes stiffer, so that after about forty-five most people find it hard to read small print and need glasses."""
E = """The focused light then falls on the retina, a thin layer of tissue lining the back of the eye. It contains about 120 million rod cells, which respond to dim light but not to colour, and about six million cone cells, which respond to colour but need brighter light. The image on the retina is upside down, but the brain corrects this automatically. A small area called the macula contains the highest number of cone cells and gives the sharpest vision, which we use for reading."""
F = """The retina turns light into electrical signals, and these travel along the optic nerve, a bundle of about a million fibres, to the brain. At the back of the head, the visual cortex puts together the signals from both eyes to produce a single three-dimensional picture. There is a small spot where the nerve leaves the eye, which contains no sensing cells, so that everyone has a blind spot in each eye, but the brain fills in the gap so cleverly that we never notice it."""
G = """Many problems with vision can now be corrected. Glasses and contact lenses make up for a cornea or lens that is the wrong shape, and laser surgery can reshape the cornea permanently. Cataracts, in which the lens becomes cloudy, can be removed and replaced by a clear plastic lens in an operation that takes about fifteen minutes. Dr Sofia Marin, an eye surgeon, says that regular examinations are important, since some diseases, such as glaucoma, cause damage long before the patient notices any change."""
S, PT, W, H = chain(5)
P = passage('p50', 'How We See', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('About a quarter of the brain is involved in processing vision.', 'T', 'A', 'about a quarter of the human brain'),
  ('The cornea contains many blood vessels.', 'F', 'B', 'It has no blood vessels'),
  ('The cornea does most of the focusing.', 'T', 'B', 'does most of the work of focusing'),
  ('The iris is the opening in the middle of the eye.', 'F', 'C', 'The iris is a ring of muscle'),
  ('The pupil widens in the dark.', 'T', 'C', 'in the dark it widens'),
  ('The lens becomes thin to see distant objects.', 'T', 'D', 'the lens becomes thin'),
  ('Rod cells respond to colour.', 'F', 'E', 'rod cells, which respond to dim light but not to colour'),
  ('The image on the retina is the right way up.', 'F', 'E', 'The image on the retina is upside down'),
  ('Blind spots are more common in older people.', 'NG', 'F', 'everyone has a blind spot in each eye', 'The passage says everyone has one; age is not mentioned.'),
 ]),
 mcq([
  ('Why does a cinema seem black at first?', ['The screen is off.', 'The eye takes time to adapt to darkness.', 'The pupil is small.', 'The lens is thick.'], 1, 'C', 'it takes longer to adapt fully to darkness'),
  ('Why do people over forty-five often need glasses for reading?', ['The cornea becomes cloudy.', 'The lens becomes stiffer.', 'The retina shrinks.', 'The pupil closes.'], 1, 'D', 'the lens becomes stiffer'),
  ('Why are regular eye examinations important?', ['Glasses wear out.', 'Some diseases cause damage before symptoms appear.', 'Laser surgery is dangerous.', 'Eyes change colour.'], 1, 'G', 'cause damage long before the patient notices any change'),
 ]),
 multi('Which TWO problems that can be corrected are mentioned in paragraph G?', ['A cornea or lens of the wrong shape.', 'Cataracts.', 'Colour blindness.', 'A blind spot.', 'Sleepiness.'], [0, 1], [('G', 'a cornea or lens that is the wrong shape'), ('G', 'Cataracts, in which the lens becomes cloudy')]),
 head(['An eye like a camera', 'The clear window', 'The adjustable opening', 'The flexible focusing disc', 'The light-sensing layer', 'Sending the message to the brain', 'Correcting vision problems', 'The history of glasses', 'The colours of the rainbow'],
  [('A', 0, 'The eye works rather like a camera'), ('B', 1, 'Light first meets the cornea'), ('C', 2, 'Behind the cornea is the pupil'), ('D', 3, 'Next the light passes through the lens'), ('E', 4, 'The focused light then falls on the retina'), ('F', 5, 'these travel along the optic nerve'), ('G', 6, 'Many problems with vision can now be corrected')]),
 info([
  ('a reference to a cause of pain when something enters the eye', 'B', 'a speck of dust on the eye is so painful'),
  ('a figure for the number of cone cells', 'E', 'about six million cone cells'),
  ('a description of the structure of the optic nerve', 'F', 'a bundle of about a million fibres'),
  ('the name of the part that produces a three-dimensional picture', 'F', 'the visual cortex'),
  ('the time taken by an operation', 'G', 'about fifteen minutes'),
 ]),
 ends(['bends the light rays inwards.', 'controls the size of the pupil.', 'adjusts the focus.', 'contains rod and cone cells.', 'is a kind of glasses.', 'is found only in children.', 'was invented in the twentieth century.'], [
  ('The cornea', 0, 'B', 'bending the light rays inwards'),
  ('The iris', 1, 'C', 'controls the size of the pupil'),
  ('The lens', 2, 'D', 'adjusts the focus'),
  ('The retina', 3, 'E', 'about 120 million rod cells'),
 ]),
 diag('Label the path of light through the eye, in order. Write ONE OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['cornea'], 'B', 'the cornea'), (['pupil'], 'C', 'the pupil'), (['lens'], 'D', 'the lens'), (['retina'], 'E', 'the retina'), (['optic nerve'], 'F', 'the optic nerve')], 2),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Light is bent inwards by the [[1]].', 'The iris controls the size of the [[2]].', 'The lens becomes [[3]] when we look at something close.', 'Signals travel along the optic [[4]] to the brain.'],
  [(['cornea'], 'B', 'the cornea'), (['pupil'], 'C', 'size of the pupil'), (['thick'], 'D', 'it becomes thick and round'), (['nerve'], 'F', 'the optic nerve')], 1),
 sent(2, [
  ('The change in the shape of the lens is called ___.', ['accommodation'], 'D', 'called accommodation'),
  ('The retina contains rod cells and ___ cells.', ['cone'], 'E', 'cone cells'),
  ('The macula gives the sharpest vision, which we use for ___.', ['reading'], 'E', 'which we use for reading'),
  ('Dr Marin is an eye ___.', ['surgeon'], 'G', 'an eye surgeon'),
 ]),
 short(3, [
  ('What is the coloured part of the eye called?', ['the iris', 'iris'], 'C', 'which is called the iris'),
  ('How many rod cells does the retina contain?', ['120 million', 'about 120 million'], 'E', 'about 120 million rod cells'),
  ('What are cataracts?', ['cloudy'], 'G', 'the lens becomes cloudy'),
 ]),
])
