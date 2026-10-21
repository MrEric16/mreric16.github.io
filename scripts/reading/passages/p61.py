from lib import *
from svgs import *
A = """A roof is more than a lid on a building. It keeps out rain, snow and sun, it holds in heat, and it often gives a building its character, so that an experienced traveller can usually tell from the shape of the roofs alone which part of the world a photograph was taken in. The shape depends mainly on three things: the climate, the materials that are available locally, and the traditions of the people who build. Over thousands of years, builders in different regions have found different solutions to the same problem, and the result is an astonishing variety of roofs, from the flat to the spired."""
B = """Flat roofs are common in dry regions, such as parts of North Africa and the Middle East, where rain is rare and heavy. A flat roof is simple and cheap to build, using beams of wood covered with layers of clay or earth, and it has an extra advantage: it is a useful space. Families dry fruit and washing there, sleep on it on hot nights, and meet their neighbours on the rooftops. In very hot places, the thick roof also keeps the rooms cool during the day. The weakness of a flat roof is that it copes badly with heavy rain, which can collect on the surface and leak through."""
C = """Where rain and snow are common, builders prefer the pitched roof, which slopes steeply from a central ridge. Water runs off it quickly and snow slides down before it becomes too heavy. In northern Europe, houses often have roofs steeper than forty-five degrees for this reason. The space under the slope, called the attic, can be used for storage or as a bedroom. Pitched roofs are covered with tiles, slates, wooden shingles or straw, according to what is available nearby; in some villages, thatch made from reeds can last for sixty years if it is carefully maintained by a skilled craftsman."""
D = """The dome, a roof shaped like half a ball, spans a wide space without columns in the middle. The Romans learned to build large domes with concrete, and the dome of the Pantheon in Rome, completed nearly nineteen centuries ago, is still the largest unreinforced concrete dome in the world. Builders in the Islamic world and later in Renaissance Europe developed the dome further, using it for mosques, churches and public buildings. A dome has a strong shape, because the weight is spread evenly around its curve, and it also has a pleasing echo and a sense of grandeur which many architects admire. However, it is difficult and expensive to construct."""
E = """The spire is a tall, narrow roof that rises to a point. Spires appeared on churches in medieval Europe, where they pointed towards heaven and could be seen from a great distance, so that travellers could find their way to a town. Some of them are enormous: the spire of Ulm Minster in Germany is the tallest church spire in the world, at more than one hundred and sixty metres. Building such a tower required skilled stone masons and many years of work, and some projects took centuries to finish. In modern cities, glass skyscrapers sometimes borrow the same pointed form in order to catch the attention of people in the street."""
F = """In recent years, many cities have begun to plant their roofs. A green roof is covered with soil and plants, and it provides several benefits. It absorbs rainwater, reducing the danger of flooding, it keeps the building cooler in summer and warmer in winter, and it offers a home for insects and birds. Dr Lucia Moretti, an architect, says that a green roof can last twice as long as an ordinary one because the plants protect the surface from sun and frost. The main disadvantage is the weight, since wet soil is heavy, so the building must be designed to support it from the start, which raises the initial cost."""
G = """Another modern idea is the solar roof, which turns a surface that was once simply a shelter into a small power station. Panels made of silicon change sunlight into electricity, and a typical family house needs only about twenty panels to produce as much power as it uses in a year in a sunny climate. Some manufacturers now make solar tiles that look like ordinary slates, so that owners need not spoil the appearance of an old house. The cost of panels has fallen sharply in the last decade, and in many regions installing them now pays for itself within about eight years."""
P = passage('p61', 'Roofs of the World', 'Architecture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which roof, A to D, is described in each statement?', [(roof('flat'), 160, 120), (roof('pitched'), 160, 120), (roof('dome'), 160, 120), (roof('spire'), 160, 120)], [
  ('a roof common in dry regions', 0, 'B', 'Flat roofs are common in dry regions'),
  ('a roof that sheds snow easily', 1, 'C', 'snow slides down before it becomes too heavy'),
  ('a roof that spans a wide space without columns', 2, 'D', 'spans a wide space without columns in the middle'),
  ('a roof found on medieval churches', 3, 'E', 'Spires appeared on churches in medieval Europe'),
 ]),
 tfng([
  ('The shape of a roof depends partly on the climate.', 'T', 'A', 'the climate'),
  ('Flat roofs are often built of wood and clay.', 'T', 'B', 'beams of wood covered with layers of clay or earth'),
  ('Flat roofs cope well with heavy rain.', 'F', 'B', 'copes badly with heavy rain'),
  ('Houses in northern Europe often have steep roofs.', 'T', 'C', 'roofs steeper than forty-five degrees'),
  ('Thatch can last for sixty years.', 'T', 'C', 'can last for sixty years'),
  ('The Pantheon has the largest unreinforced concrete dome in the world.', 'T', 'D', 'largest unreinforced concrete dome in the world'),
  ('Domes are cheap to construct.', 'F', 'D', 'difficult and expensive to construct'),
  ('Ulm Minster took over a hundred years to build.', 'NG', 'E', 'Ulm Minster in Germany', 'Its building time is not given.'),
  ('A green roof adds weight to a building.', 'T', 'F', 'wet soil is heavy'),
 ]),
 mcq([
  ('Why is a flat roof useful in dry regions?', ['It is also a useful space.', 'It is very tall.', 'It never leaks.', 'It is made of glass.'], 0, 'B', 'it is a useful space'),
  ('Why is the dome a strong shape?', ['It is made of stone.', 'The weight is spread evenly around the curve.', 'It is small.', 'It has columns.'], 1, 'D', 'the weight is spread evenly around its curve'),
  ('What do some manufacturers make for old houses?', ['Solar tiles that look like slates.', 'Glass domes.', 'Thatch panels.', 'Flat roofs.'], 0, 'G', 'solar tiles that look like ordinary slates'),
 ]),
 feat('Match each feature with the correct roof, A to D.', ['Flat roof', 'Pitched roof', 'Dome', 'Spire'], [
  ('Families dry fruit on it.', 0, 'B', 'Families dry fruit and washing there'),
  ('The space beneath it is called the attic.', 1, 'C', 'called the attic'),
  ('The Romans built large ones with concrete.', 2, 'D', 'The Romans learned to build large domes with concrete'),
  ('It helped travellers find their way to a town.', 3, 'E', 'travellers could find their way to a town'),
 ]),
 multi('Which TWO benefits of green roofs are mentioned in paragraph F?', ['They absorb rainwater.', 'They offer a home for insects and birds.', 'They produce electricity.', 'They are cheap to install.', 'They need no water.'], [0, 1], [('F', 'It absorbs rainwater'), ('F', 'a home for insects and birds')]),
 head(['More than a cover', 'Roofs for dry lands', 'Roofs for rain and snow', 'Curved coverings for wide spaces', 'Reaching for the sky', 'Gardens above our heads', 'Power from the sun', 'The history of tiles', 'How to repair a roof'],
  [('A', 0, 'A roof is more than a lid on a building'), ('B', 1, 'Flat roofs are common in dry regions'), ('C', 2, 'Where rain and snow are common'), ('D', 3, 'spans a wide space without columns'), ('E', 4, 'a tall, narrow roof that rises to a point'), ('F', 5, 'many cities have begun to plant their roofs'), ('G', 6, 'turns a surface that was once simply a shelter into a small power station')]),
 info([
  ('a reference to people sleeping on a roof', 'B', 'sleep on it on hot nights'),
  ('a list of materials used to cover roofs', 'C', 'tiles, slates, wooden shingles or straw'),
  ('a record for the height of a church spire', 'E', 'tallest church spire in the world'),
  ('a claim about how long a green roof lasts', 'F', 'twice as long as an ordinary one'),
  ('a reference to the time panels take to pay for themselves', 'G', 'pays for itself within about eight years'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Roof', 'Detail'],
  [['Flat', 'Common in [[1]] regions'], ['Pitched', 'Slopes from a central [[2]]'], ['Dome', 'Shaped like half a [[3]]'], ['Solar', 'A typical house needs about twenty [[4]]']],
  [(['dry'], 'B', 'common in dry regions'), (['ridge'], 'C', 'central ridge'), (['ball'], 'D', 'half a ball'), (['panels'], 'G', 'twenty panels')], 1),
 sent(2, [
  ('Pitched roofs often use tiles, slates, shingles or ___.', ['straw'], 'C', 'shingles or straw'),
  ('The Pantheon has the largest unreinforced ___ dome in the world.', ['concrete'], 'D', 'unreinforced concrete dome'),
  ('The spire of Ulm Minster is in ___.', ['germany'], 'E', 'in Germany'),
  ('Dr Moretti is an ___.', ['architect'], 'F', 'an architect'),
 ]),
 short(3, [
  ('What is thatch made from?', ['reeds'], 'C', 'made from reeds'),
  ('What shape is a dome?', ['half a ball'], 'D', 'half a ball'),
  ('What are solar panels made of?', ['silicon'], 'G', 'made of silicon'),
 ]),
])
