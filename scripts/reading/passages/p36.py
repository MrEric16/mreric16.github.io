from lib import *
A = """The Moon is the Earth's only natural satellite and the fifth largest in the solar system. It orbits our planet at an average distance of about 384,000 kilometres, which is roughly thirty times the width of the Earth. Light from the Moon takes just over one second to reach us. The Moon is about a quarter of the Earth's diameter, which makes it unusually large compared with its planet, and it plays an important part in life on Earth, from the tides in the sea to the calendars that people have used for thousands of years."""
B = """Most scientists believe that the Moon was formed about 4.5 billion years ago, soon after the Earth itself. According to the giant impact theory, a body about the size of Mars crashed into the young Earth, and the debris thrown into orbit gathered together to form the Moon. The theory explains why the Moon's rocks are so similar to those of the Earth's outer layers, and why it has a small core. Other ideas, such as the capture of a passing body, do not fit these facts as well."""
C = """The surface of the Moon is covered with craters, which were made by meteorites striking it over billions of years. Since the Moon has no air or weather to wear them down, the craters survive, and some are more than two hundred kilometres wide. The dark areas that can be seen with the naked eye are called maria, a Latin word meaning seas, although they contain no water: they are huge plains of cooled lava. Everything is covered with a layer of fine grey dust, which clung to the astronauts' suits and smelled, they reported, like gunpowder."""
D = """The Moon does not produce light of its own; it shines because it reflects sunlight. As it orbits the Earth, about once every 29.5 days, we see different amounts of its lit side, which are called phases. At new moon, the lit side faces away from us and the Moon is almost invisible. Over the following two weeks it grows from a thin crescent to a full circle, and then it shrinks again. The pattern is so regular that many calendars, including the Islamic one, are based on it."""
E = """The Moon's gravity pulls on the oceans, causing the tides. Water on the side of the Earth that faces the Moon is pulled towards it, and a second bulge forms on the opposite side, so that most coasts have two high tides and two low tides each day. The Sun also affects the tides, and when the Sun, Moon and Earth are in line, the highest tides of all, called spring tides, occur. The Moon's pull is also slowing down the Earth's rotation, making each day longer by about two milliseconds each century."""
F = """Humans have long wished to go to the Moon. The first spacecraft to reach it, the Soviet Luna 2, crashed there in 1959. In 1969, the American astronaut Neil Armstrong became the first person to walk on its surface, and eleven others followed during the next three years. They brought back almost four hundred kilograms of rock, which scientists are still studying. No human has visited since 1972, partly because of the high cost, though several countries are now preparing new missions."""
G = """Interest in the Moon is now growing again. Space agencies hope to build a permanent base near the Moon's south pole, where craters that never see sunlight may contain frozen water. Water could provide drinking supplies and, when split into hydrogen and oxygen, fuel for rockets. Dr Alicia Navarro, a planetary scientist, believes that a lunar base would be a useful test for longer journeys, though she warns that the dust, the radiation and the cost will be difficult challenges."""
P = passage('p36', 'The Moon', 'Astronomy', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Moon is the largest satellite in the solar system.', 'F', 'A', 'the fifth largest'),
  ('Light from the Moon takes just over a second to reach the Earth.', 'T', 'A', 'just over one second to reach us'),
  ('The Moon was formed soon after the Earth.', 'T', 'B', 'soon after the Earth itself'),
  ('The giant impact theory explains the similarity of rocks.', 'T', 'B', 'why the Moon\'s rocks are so similar'),
  ('Weather has worn away the Moon\'s craters.', 'F', 'C', 'no air or weather to wear them down'),
  ('The maria contain water.', 'F', 'C', 'they contain no water'),
  ('At new moon the lit side faces the Earth.', 'F', 'D', 'the lit side faces away from us'),
  ('Eleven astronauts followed Armstrong onto the surface.', 'T', 'F', 'eleven others followed'),
  ('Neil Armstrong later became a politician.', 'NG', 'F', 'became the first person to walk on its surface', 'His later career is not mentioned.'),
 ]),
 mcq([
  ('What makes the Moon unusual among satellites?', ['It is very small.', 'It is large compared with its planet.', 'It has an atmosphere.', 'It has rings.'], 1, 'A', 'unusually large compared with its planet'),
  ('Why does the Moon shine?', ['It produces light.', 'It reflects sunlight.', 'It is on fire.', 'It is covered with ice.'], 1, 'D', 'it shines because it reflects sunlight'),
  ('Why might craters near the south pole be useful?', ['They are the largest.', 'They may contain frozen water.', 'They are warm.', 'They are flat.'], 1, 'G', 'may contain frozen water'),
 ]),
 feat('Match each statement with the correct term, A to D.', ['The giant impact theory', 'Maria', 'Phases', 'Spring tides'], [
  ('The highest tides of all occur.', 3, 'E', 'the highest tides of all, called spring tides'),
  ('Dark plains of cooled lava.', 1, 'C', 'huge plains of cooled lava'),
  ('A body the size of Mars struck the young Earth.', 0, 'B', 'a body about the size of Mars crashed into the young Earth'),
  ('The different amounts of the lit side that we see.', 2, 'D', 'different amounts of its lit side, which are called phases'),
 ]),
 multi('Which TWO effects of the Moon on Earth are mentioned in the passage?', ['The tides.', 'The slowing of the Earth\'s rotation.', 'Earthquakes.', 'Volcanic eruptions.', 'The seasons.'], [0, 1], [('E', 'causing the tides'), ('E', 'slowing down the Earth\'s rotation')]),
 head(['The Moon in numbers', 'How the Moon began', 'A landscape of craters and dust', 'Changing shapes in the sky', 'The Moon and the sea', 'Visitors from Earth', 'A base for the future', 'The Sun\'s surface', 'A history of calendars'],
  [('A', 0, 'orbits our planet at an average distance'), ('B', 1, 'According to the giant impact theory'), ('C', 2, 'The surface of the Moon is covered with craters'), ('D', 3, 'we see different amounts of its lit side'), ('E', 4, 'The Moon\'s gravity pulls on the oceans'), ('F', 5, 'The first spacecraft to reach it'), ('G', 6, 'Space agencies hope to build a permanent base')]),
 info([
  ('a comparison between the size of the Moon and the Earth', 'A', 'about a quarter of the Earth\'s diameter'),
  ('a description of the smell of dust', 'C', 'like gunpowder'),
  ('the length of the cycle of phases', 'D', 'about once every 29.5 days'),
  ('a figure for how much longer days are becoming', 'E', 'two milliseconds each century'),
  ('a reason why humans have not visited since 1972', 'F', 'partly because of the high cost'),
 ]),
 ends(['is called a phase.', 'are called maria.', 'brought back almost four hundred kilograms of rock.', 'crashed on the Moon in 1959.', 'is visible only at night.', 'is made of ice.', 'was built in 1972.'], [
  ('Each amount of the lit side seen from Earth', 0, 'D', 'different amounts of its lit side, which are called phases'),
  ('The dark areas seen with the naked eye', 1, 'C', 'The dark areas that can be seen with the naked eye are called maria'),
  ('The astronauts', 2, 'F', 'almost four hundred kilograms of rock'),
  ('Luna 2', 3, 'F', 'crashed there in 1959'),
 ]),
 sent(2, [
  ('The Moon is about ___ thousand kilometres from the Earth.', ['384'], 'A', 'about 384,000 kilometres'),
  ('The Moon formed about 4.5 ___ years ago.', ['billion'], 'B', '4.5 billion years ago'),
  ('Meteorites made the ___ on the Moon.', ['craters'], 'C', 'covered with craters'),
  ('Dr Navarro is a planetary ___.', ['scientist'], 'G', 'a planetary scientist'),
 ]),
 short(3, [
  ('What does the Latin word maria mean?', ['seas'], 'C', 'meaning seas'),
  ('Which calendar is based on the Moon\'s pattern?', ['islamic', 'the islamic one'], 'D', 'the Islamic one'),
  ('When did the last human visit the Moon?', ['1972'], 'F', 'since 1972'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'The Moon probably formed when a body hit the young Earth, and its surface is covered with [[1]]. It shines because it [[2]] sunlight, and its gravity causes the [[3]]. Space agencies want a base near the south [[4]].',
  [(['craters'], 'C', 'covered with craters'), (['reflects'], 'D', 'it reflects sunlight'), (['tides'], 'E', 'causing the tides'), (['pole'], 'G', 'south pole')], 1,
  bank=['craters', 'reflects', 'tides', 'pole', 'rivers', 'storms', 'atmosphere', 'oceans']),
])
