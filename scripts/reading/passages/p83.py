from lib import *
from svgs import *
A = """A photograph is so familiar today that it is hard to imagine a world without cameras. Every day, people take billions of pictures with their phones, and the images record meals, holidays, friendships and news events. Yet two hundred years ago, the only way to record a scene was to draw or paint it, and portraits were a luxury of the wealthy. The invention of photography, which took place over about sixty years in the nineteenth century, changed the way people see themselves and the world. This passage follows the main stages of the story, from the first blurred image to the camera in the pocket."""
B = """The story begins with a very old idea. Thousands of years ago, people noticed that when light passes through a small hole into a dark room, an upside-down picture of the scene outside appears on the opposite wall. The device is called a camera obscura, which is Latin for dark room. Artists used it from the Renaissance onward to help them draw accurate pictures, and by the seventeenth century it had shrunk to a portable box with a lens. But nobody could keep the image: it disappeared as soon as the light was removed. The problem was not how to make a picture of light, but how to fix it."""
C = """The problem was solved by a French inventor, Nicéphore Niépce. Around 1826 he coated a pewter plate with a light-sensitive substance, placed it in a camera obscura at a window of his house, and left it for many hours. The sunlight slowly hardened the coating where it fell, and after washing away the unhardened parts, he obtained the oldest surviving photograph, a hazy view of rooftops and a courtyard. The exposure took at least eight hours, so that the sun appears to shine on both sides of the buildings. The picture is blurred, but it proved that nature could draw its own picture."""
D = """Niépce's partner, Louis Daguerre, improved the process. He found that a silver-coated copper plate, exposed to iodine fumes, was far more sensitive to light, and that the hidden image could be brought out by mercury vapour. The new process, announced in 1839 and called the daguerreotype, needed exposures of only a few minutes. The pictures were sharp and beautiful, and they caused a sensation; the French government bought the invention and gave it to the world. Within a year, studios appeared in the cities of Europe and America. However, each daguerreotype was a unique object, which could not be copied."""
E = """At the same time in England, William Henry Fox Talbot developed a different method. He made a paper negative, in which light and dark were reversed, and from it he could print any number of positive copies. The pictures were less sharp than daguerreotypes, but the idea of the negative became the basis of photography for the next hundred and fifty years. Over the following decades, other advances made photography quicker and cheaper: glass plates replaced paper, exposures were reduced to a fraction of a second, and portraits, once a luxury, became affordable for ordinary families."""
F = """The final step to mass photography was taken by an American, George Eastman. In 1888 he launched the Kodak camera, a simple box with a roll of film for a hundred pictures. His slogan was You press the button, we do the rest: when the film was full, the owner sent the whole camera to the company, which developed the pictures and returned the camera with new film. For the first time, anyone could be a photographer without learning chemistry. Photography became a hobby, and families began to keep albums of snapshots. Later, colour film, small cameras and instant prints made the art still more popular."""
G = """The next revolution came from electronics. In 1975, an engineer at Kodak, Steven Sasson, built the first digital camera. It weighed almost four kilograms, took twenty-three seconds to record a single black-and-white picture, and stored it on a cassette tape. Compared with today's cameras, it was primitive, but it showed that an image could be turned into numbers. Digital sensors became better and cheaper, and in the early 2000s they were included in mobile phones. Dr Camille Laurent, a historian of photography, says that the change has been so complete that the main question today is no longer how to take a picture, but which of the billions of pictures deserves to be remembered."""
S, PT, W, H = chain(5)
P = passage('p83', 'How Photography Began', 'History of technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('People take billions of pictures every day.', 'T', 'A', 'billions of pictures'),
  ('Portraits were a luxury of the wealthy two hundred years ago.', 'T', 'A', 'a luxury of the wealthy'),
  ('A camera obscura can fix an image permanently.', 'F', 'B', 'nobody could keep the image'),
  ('A camera obscura produces an upside-down picture.', 'T', 'B', 'upside-down picture'),
  ('Niépce\'s exposure took at least eight hours.', 'T', 'C', 'at least eight hours'),
  ('Daguerre used mercury vapour to bring out the image.', 'T', 'D', 'mercury vapour'),
  ('Daguerreotypes could be copied easily.', 'F', 'D', 'a unique object'),
  ('Talbot worked in England.', 'T', 'E', 'in England'),
  ('George Eastman was born in Rochester.', 'NG', 'F', 'an American, George Eastman', 'His birthplace is not given.'),
 ]),
 mcq([
  ('What did the French government do with the daguerreotype?', ['Destroyed it.', 'Bought it and gave it to the world.', 'Sold it abroad.', 'Banned it.'], 1, 'D', 'bought the invention and gave it to the world'),
  ('Why was Talbot\'s negative important?', ['It was sharper.', 'It allowed any number of copies.', 'It was in colour.', 'It was cheaper than glass.'], 1, 'E', 'print any number of positive copies'),
  ('What did the owner of a Kodak do when the film was full?', ['Sent the camera to the company.', 'Bought new film.', 'Developed it at home.', 'Threw it away.'], 0, 'F', 'sent the whole camera to the company'),
 ]),
 diag('Label the key steps in the history of photography, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['photograph'], 'C', 'oldest surviving photograph'), (['daguerreotype'], 'D', 'called the daguerreotype'), (['negative'], 'E', 'paper negative'), (['kodak'], 'F', 'Kodak camera'), (['digital'], 'G', 'first digital camera')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Light passes through a small hole into a dark [[1]].', 'Niépce hardens the image on a [[2]] plate.', 'Daguerre brings out the image with [[3]] vapour.', 'Talbot prints positive copies from a paper [[4]].'],
  [(['room'], 'B', 'dark room'), (['pewter'], 'C', 'pewter plate'), (['mercury'], 'D', 'mercury vapour'), (['negative'], 'E', 'paper negative')], 1),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Date', 'Event'],
  [['1826', 'Niépce exposed a plate for at least [[1]] hours'], ['1839', 'The [[2]] process was announced'], ['1888', 'Eastman launched the [[3]] camera'], ['1975', 'The first digital camera took [[4]] seconds to record a picture']],
  [(['eight'], 'C', 'at least eight hours'), (['daguerreotype'], 'D', 'called the daguerreotype'), (['kodak'], 'F', 'Kodak camera'), (['twenty-three'], 'G', 'twenty-three seconds')], 2),
 feat('Match each statement with the correct person, A to D.', ['Niépce', 'Daguerre', 'Talbot', 'Eastman'], [
  ('He made the oldest surviving photograph.', 0, 'C', 'oldest surviving photograph'),
  ('His process used a silver-coated copper plate.', 1, 'D', 'silver-coated copper plate'),
  ('He made a paper negative.', 2, 'E', 'paper negative'),
  ('His slogan was You press the button, we do the rest.', 3, 'F', 'You press the button, we do the rest'),
 ]),
 multi('Which TWO improvements made photography quicker and cheaper, according to paragraph E?', ['Glass plates replaced paper.', 'Exposures were reduced to a fraction of a second.', 'Cameras became larger.', 'Colour was added.', 'Flash was invented.'], [0, 1], [('E', 'glass plates replaced paper'), ('E', 'a fraction of a second')]),
 head(['A world full of pictures', 'An old idea with a problem', 'The first lasting image', 'A sharp new process', 'Copies from a negative', 'A camera for everybody', 'Pictures made of numbers', 'The history of painting', 'Famous photographers'],
  [('A', 0, 'hard to imagine a world without cameras'), ('B', 1, 'how to fix it'), ('C', 2, 'the oldest surviving photograph'), ('D', 3, 'The pictures were sharp and beautiful'), ('E', 4, 'print any number of positive copies'), ('F', 5, 'anyone could be a photographer'), ('G', 6, 'an image could be turned into numbers')]),
 info([
  ('a reference to Latin', 'B', 'Latin for dark room'),
  ('a reference to a hazy view of rooftops', 'C', 'hazy view of rooftops'),
  ('a reference to iodine fumes', 'D', 'iodine fumes'),
  ('a reference to families keeping albums', 'F', 'albums of snapshots'),
  ('a reference to a cassette tape', 'G', 'cassette tape'),
 ]),
 ends(['was used by artists.', 'coated a pewter plate.', 'were unique objects.', 'recorded images on tape.', 'took colour pictures.', 'was made of wood.', 'was invented in 1999.'], [
  ('The camera obscura', 0, 'B', 'Artists used it'),
  ('Niépce', 1, 'C', 'coated a pewter plate'),
  ('Daguerreotypes', 2, 'D', 'unique object'),
  ('Sasson\'s camera', 3, 'G', 'cassette tape'),
 ]),
 sent(2, [
  ('Camera obscura is Latin for dark ___.', ['room'], 'B', 'dark room'),
  ('The oldest surviving photograph shows rooftops and a ___.', ['courtyard'], 'C', 'courtyard'),
  ('Eastman launched the ___ camera in 1888.', ['kodak'], 'F', 'Kodak camera'),
  ('Dr Laurent is a historian of ___.', ['photography'], 'G', 'historian of photography'),
 ]),
 short(3, [
  ('What did Talbot make?', ['a paper negative', 'paper negative'], 'E', 'paper negative'),
  ('How many pictures did the first Kodak hold?', ['a hundred'], 'F', 'a hundred pictures'),
  ('How heavy was the first digital camera?', ['four kilograms', 'almost four kilograms'], 'G', 'almost four kilograms'),
 ]),
])
