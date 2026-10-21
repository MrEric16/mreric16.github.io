from lib import *
from svgs import *
A = """In the Fergana Valley of eastern Uzbekistan lies the town of Rishtan, which has been famous for its pottery for many centuries. Potters here have made plates, bowls, jugs and water vessels from the local clay, and their work is recognised by its deep blue and turquoise colours and its patterns of flowers, leaves and stars. Skills have passed from father to son for generations, and many families in the town still run a workshop at home. This passage describes how a Rishtan plate is made and why the tradition has survived, in a modern world of factory-made dishes."""
B = """Good pottery begins with good clay. Rishtan potters have traditionally used clay from the local area, which is red and fine-grained and is considered particularly suitable for ceramics. The clay is dug out of the ground, left to dry in the sun, then crushed and soaked in water. Stones and roots are removed, and the clay is kneaded by hand or foot, until it is smooth and free of air bubbles. If a bubble remains, the object may crack or even burst in the kiln, so this stage must be done with care. Only then is the clay ready to be shaped."""
C = """The potter shapes the clay on a wheel. Traditional wheels were turned by foot, while many workshops today use an electric motor. The potter places a ball of clay at the centre, wets his hands and presses gently, so that the clay rises and opens into the shape of a bowl, a plate or a jug. A skilled potter can make a plate in a few minutes, each one almost identical to the last. The shaped pieces are then dried slowly in the shade for several days, because quick drying in strong sun could cause cracks."""
D = """After drying, the piece is fired in a kiln for the first time. This firing, at a temperature of about nine hundred degrees, turns the soft clay into hard, porous ceramic. Next comes the decoration, which is the part that makes Rishtan work so special. The piece is covered with a white slip, a thin layer of liquid clay, and the artist paints the pattern with a fine brush, using natural mineral pigments. The traditional blue is made from cobalt, which gives the intense colour that people call Rishtan blue. Each artist has a favourite pattern, but many designs are shared, such as the pomegranate and the cotton flower."""
E = """The most distinctive part of Rishtan pottery is the glaze, called ishkor. It is made from the ashes of desert plants, which are mixed with quartz and other minerals. Ishkor is a transparent glaze which, when fired, gives the surface a glass-like shine and makes the colours underneath appear deeper. The recipe was long a closely guarded family secret, and some masters say that the exact mixture varies according to the plants used and the season in which they were burned. The painted pieces are covered with the glaze and fired a second time, and this is when the final colours appear."""
F = """For a time, the future of the craft looked uncertain. In the twentieth century, factories began to produce cheap dishes in large numbers, and many young people left the villages to look for other work. A number of workshops closed. Ibrohim Kamolov, a master potter, recalls that the revival came when people at home and abroad began to appreciate handmade objects once more. Tourists who visited the Fergana Valley bought plates and bowls as souvenirs, and the demand encouraged young people to learn the skills of their grandfathers. Today, there are several dozen workshops in the town, some of which are training apprentices."""
G = """The craft is also being adapted to modern needs. Besides traditional plates and jugs, some potters now make tiles for buildings, lamps and cups for coffee. Others experiment with new colours and shapes while keeping the old methods. Some workshops are open to visitors, who can watch the potters at work and even try the wheel for themselves. Master Kamolov says that the greatest danger is not competition from factories but loss of knowledge, and that the best way to protect a craft is to use its products every day. A plate that is hung on a wall, he says, is only half alive, but a plate on which bread is served is alive."""
P = passage('p88', 'The Potters of Rishtan', 'Culture and crafts', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Rishtan is in the Fergana Valley.', 'T', 'A', 'Fergana Valley'),
  ('Skills pass from father to son.', 'T', 'A', 'father to son'),
  ('Rishtan clay is white.', 'F', 'B', 'red and fine-grained'),
  ('Air bubbles in the clay can make an object burst in the kiln.', 'T', 'B', 'burst in the kiln'),
  ('Pieces are dried quickly in strong sun.', 'F', 'C', 'dried slowly in the shade'),
  ('The first firing is at about nine hundred degrees.', 'T', 'D', 'about nine hundred degrees'),
  ('Rishtan blue is made from cobalt.', 'T', 'D', 'made from cobalt'),
  ('Ishkor is made from the ashes of desert plants.', 'T', 'E', 'ashes of desert plants'),
  ('Ibrohim Kamolov has trained more than fifty apprentices.', 'NG', 'F', 'a master potter', 'The number of apprentices is not given.'),
 ]),
 mcq([
  ('What makes air bubbles in the clay a danger?', ['The object may crack or burst.', 'The colour fades.', 'The clay smells.', 'The wheel stops.'], 0, 'B', 'crack or even burst in the kiln'),
  ('What caused the craft\'s revival?', ['People began to appreciate handmade objects.', 'New factories.', 'Government laws.', 'A new type of clay.'], 0, 'F', 'appreciate handmade objects once more'),
  ('What does Master Kamolov say is the greatest danger?', ['Loss of knowledge.', 'Factories.', 'Poor clay.', 'High prices.'], 0, 'G', 'loss of knowledge'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Clay is dug out and dried in the [[1]].', 'It is crushed and soaked in [[2]].', 'It is shaped on a [[3]].', 'The piece is painted with a fine [[4]].'],
  [(['sun'], 'B', 'dry in the sun'), (['water'], 'B', 'soaked in water'), (['wheel'], 'C', 'on a wheel'), (['brush'], 'D', 'fine brush')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Preparing clay', 'Kneaded until free of air [[1]]'], ['Drying', 'Several [[2]] in the shade'], ['Decoration', 'Natural mineral [[3]]'], ['Glaze', 'Called [[4]]']],
  [(['bubbles'], 'B', 'air bubbles'), (['days'], 'C', 'several days'), (['pigments'], 'D', 'mineral pigments'), (['ishkor'], 'E', 'called ishkor')], 1),
 feat('Match each statement with the correct item, A to D.', ['The wheel', 'Cobalt', 'Ishkor', 'Tourists'], [
  ('It shapes the clay into a bowl or jug.', 0, 'C', 'shape of a bowl, a plate or a jug'),
  ('It gives the intense blue colour.', 1, 'D', 'intense colour'),
  ('It gives a glass-like shine.', 2, 'E', 'glass-like shine'),
  ('They bought plates and bowls as souvenirs.', 3, 'F', 'as souvenirs'),
 ]),
 multi('Which TWO designs are mentioned in paragraph D?', ['The pomegranate.', 'The cotton flower.', 'The dragon.', 'The horse.', 'The sun.'], [0, 1], [('D', 'the pomegranate'), ('D', 'the cotton flower')]),
 head(['A town of potters', 'Preparing the clay', 'On the wheel', 'Fire and colour', 'The secret glaze', 'A craft in danger and its revival', 'Looking forward', 'A history of glass', 'Famous museums'],
  [('A', 0, 'famous for its pottery'), ('B', 1, 'Good pottery begins with good clay'), ('C', 2, 'shapes the clay on a wheel'), ('D', 3, 'fired in a kiln for the first time'), ('E', 4, 'closely guarded family secret'), ('F', 5, 'the future of the craft looked uncertain'), ('G', 6, 'adapted to modern needs')]),
 info([
  ('a reference to a family secret', 'E', 'family secret'),
  ('a reference to roots being removed', 'B', 'Stones and roots are removed'),
  ('a reference to an electric motor', 'C', 'electric motor'),
  ('a reference to a white slip', 'D', 'white slip'),
  ('a reference to visitors trying the wheel', 'G', 'try the wheel'),
 ]),
 ends(['is red and fine-grained.', 'is made from desert plant ashes.', 'bought plates as souvenirs.', 'serve bread on a plate.', 'is blue.', 'is made of glass.', 'ends in Tashkent.'], [
  ('The local clay', 0, 'B', 'red and fine-grained'),
  ('Ishkor', 1, 'E', 'ashes of desert plants'),
  ('Tourists', 2, 'F', 'bought plates and bowls'),
  ('Master Kamolov', 3, 'G', 'on which bread is served'),
 ]),
 sent(2, [
  ('The thin layer of liquid clay is called a ___.', ['slip'], 'D', 'a white slip'),
  ('Rishtan blue is made from ___.', ['cobalt'], 'D', 'made from cobalt'),
  ('The plate is fired a ___ time after glazing.', ['second'], 'E', 'a second time'),
  ('Kamolov is a master ___.', ['potter'], 'F', 'master potter'),
 ]),
 short(3, [
  ('At what temperature is the first firing?', ['nine hundred'], 'D', 'nine hundred degrees'),
  ('What is ishkor mixed with?', ['quartz'], 'E', 'quartz and other minerals'),
  ('What do some potters now make?', ['tiles', 'lamps'], 'G', 'tiles for buildings, lamps'),
 ]),
])
