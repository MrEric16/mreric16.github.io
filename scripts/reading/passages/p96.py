from lib import *
from svgs import *
A = """Mars, the fourth planet from the Sun, has fascinated people for centuries. It is visible to the naked eye as a reddish point of light, and its colour led the ancient Romans to name it after their god of war. When telescopes became powerful enough, astronomers saw dark and light patches on its surface and some thought they saw canals, built by an intelligent civilisation. We now know that this was an illusion. Yet Mars remains the most Earth-like of the other planets, and the one where scientists most hope to find evidence of life, past or present. This passage describes what spacecraft have taught us about the red planet."""
B = """Mars is about half the diameter of Earth, and its gravity is only about thirty-eight per cent of ours, so a person weighing seventy kilograms on Earth would weigh around twenty-six there. A day on Mars lasts 24 hours and 37 minutes, very close to ours, and the planet has seasons because its axis is tilted at a similar angle. But a year on Mars is almost twice as long as on Earth, at 687 Earth days. The planet has two tiny moons, Phobos and Deimos, which are probably captured asteroids and are shaped like potatoes."""
C = """The red colour comes from iron in the soil, which has rusted, as iron does on Earth. The surface is a cold desert of dust, rock and sand. The average temperature is around minus sixty degrees Celsius, though at the equator on a summer day it may reach twenty degrees. The air is very thin, with a pressure less than one per cent of Earth's, and it consists mostly of carbon dioxide. Strong winds can raise dust storms which sometimes cover the whole planet for weeks. A human being on the surface without a spacesuit would not survive."""
D = """Mars has spectacular landscapes. Olympus Mons, a volcano, is the tallest known mountain in the solar system, about twenty-two kilometres high, nearly three times the height of Mount Everest. Valles Marineris is a system of canyons which stretches for about four thousand kilometres, roughly the width of the United States. There are also polar caps of ice, mostly frozen water with a layer of frozen carbon dioxide on top, which grow and shrink with the seasons. Many of these features were formed long ago, because Mars today has little volcanic or tectonic activity."""
E = """The greatest question is whether Mars had water. Photographs from orbit show channels and dry riverbeds, and the rovers have found minerals which form only in the presence of liquid water. Scientists now think that about three or four billion years ago Mars was warmer and wetter, with rivers, lakes and perhaps an ocean. Then the planet lost most of its atmosphere, perhaps because it has a much weaker magnetic field than Earth's, and the water froze or escaped into space. Today, frozen water lies under the surface and at the poles, and liquid water may exist deep underground."""
F = """Since the 1960s, dozens of spacecraft have been sent to Mars, and about half of them have failed. The first successes were orbiters that photographed the planet. In 1976 two American Viking landers touched down and tested the soil for signs of life, with unclear results. In 1997, a small rover named Sojourner explored the surface, and since then bigger rovers have followed, including Curiosity in 2012 and Perseverance in 2021. Perseverance carried a small helicopter, Ingenuity, which made the first powered flight on another planet, in April 2021, and is collecting rock samples which may one day be returned to Earth."""
G = """The question now is whether humans should go there. Dr Samuel Okafor, a planetary scientist, points out that the journey would take around seven months in each direction, and that astronauts would be exposed to dangerous radiation, because Mars has no magnetic shield. They would need to produce their own water, food, oxygen and fuel on the planet. Several space agencies and companies hope to land people on Mars within the next few decades. Dr Okafor believes that robots can do much of the science more cheaply, but that a human geologist, who can make decisions on the spot, would be worth a hundred rovers."""
P = passage('p96', 'Exploring Mars', 'Astronomy', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Mars is the fourth planet from the Sun.', 'T', 'A', 'fourth planet from the Sun'),
  ('The Romans named Mars after their god of war.', 'T', 'A', 'god of war'),
  ('The canals on Mars were built by a civilisation.', 'F', 'A', 'this was an illusion'),
  ('A day on Mars is about the same length as a day on Earth.', 'T', 'B', 'very close to ours'),
  ('A Martian year is shorter than an Earth year.', 'F', 'B', 'almost twice as long'),
  ('The red colour comes from rusted iron.', 'T', 'C', 'iron in the soil'),
  ('Olympus Mons is about twenty-two kilometres high.', 'T', 'D', 'about twenty-two kilometres high'),
  ('Curiosity landed on Mars in 2012.', 'T', 'F', 'Curiosity in 2012'),
  ('Mars has more than two moons.', 'F', 'B', 'two tiny moons'),
  ('Perseverance has found signs of life.', 'NG', 'F', 'collecting rock samples', 'No such finding is reported.'),
 ]),
 mcq([
  ('Why is the air on Mars unsuitable for people?', ['It is thin and mostly carbon dioxide.', 'It is too hot.', 'It is too humid.', 'It is full of oxygen.'], 0, 'C', 'mostly of carbon dioxide'),
  ('Why did Mars lose its water, perhaps?', ['Its magnetic field is weak.', 'It is too small.', 'It is too far.', 'It has no sun.'], 0, 'E', 'weaker magnetic field'),
  ('What did Ingenuity do?', ['Made the first powered flight on another planet.', 'Collected samples.', 'Found water.', 'Photographed Phobos.'], 0, 'F', 'first powered flight on another planet'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Gravity', 'About thirty-eight per cent of [[1]]'], ['Year', '687 Earth [[2]]'], ['Atmosphere', 'Mostly carbon [[3]]'], ['Valles Marineris', 'A system of [[4]]']],
  [(['ours'], 'B', 'of ours'), (['days'], 'B', '687 Earth days'), (['dioxide'], 'C', 'carbon dioxide'), (['canyons'], 'D', 'canyons')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Mars was once warm and [[1]].', 'It lost most of its [[2]].', 'The water froze or escaped into [[3]].', 'Frozen water now lies under the [[4]].'],
  [(['wetter'], 'E', 'warmer and wetter'), (['atmosphere'], 'E', 'atmosphere'), (['space'], 'E', 'into space'), (['surface'], 'E', 'under the surface')], 1),
 feat('Match each statement with the correct item, A to D.', ['Phobos and Deimos', 'Olympus Mons', 'Viking', 'Perseverance'], [
  ('They are shaped like potatoes.', 0, 'B', 'shaped like potatoes'),
  ('It is the tallest known mountain in the solar system.', 1, 'D', 'tallest known mountain'),
  ('Landers tested the soil for signs of life.', 2, 'F', 'signs of life'),
  ('It carried a small helicopter.', 3, 'F', 'small helicopter'),
 ]),
 multi('Which TWO dangers for astronauts are mentioned in paragraph G?', ['A long journey.', 'Radiation.', 'Giant animals.', 'Floods.', 'Earthquakes.'], [0, 1], [('G', 'seven months'), ('G', 'dangerous radiation')]),
 head(['The red planet', 'Size, days and moons', 'A cold desert', 'Mountains and canyons', 'The mystery of the water', 'Robots on the surface', 'Should people go?', 'The history of war', 'Life on Venus'],
  [('A', 0, 'Mars, the fourth planet from the Sun'), ('B', 1, 'Phobos and Deimos'), ('C', 2, 'cold desert of dust, rock and sand'), ('D', 3, 'spectacular landscapes'), ('E', 4, 'whether Mars had water'), ('F', 5, 'dozens of spacecraft'), ('G', 6, 'whether humans should go there')]),
 info([
  ('a reference to canals', 'A', 'canals'),
  ('a comparison with Mount Everest', 'D', 'Mount Everest'),
  ('a reference to dust storms', 'C', 'dust storms'),
  ('a reference to polar ice caps', 'D', 'polar caps of ice'),
  ('a reference to a geologist', 'G', 'human geologist'),
 ]),
 ends(['is red because of iron.', 'is the tallest mountain.', 'tested the soil.', 'would take seven months.', 'is a gas giant.', 'has an ocean today.', 'has no gravity.'], [
  ('The soil', 0, 'C', 'iron in the soil'),
  ('Olympus Mons', 1, 'D', 'tallest known mountain'),
  ('The Viking landers', 2, 'F', 'tested the soil'),
  ('The journey', 3, 'G', 'seven months'),
 ]),
 sent(2, [
  ('Mars is named after the Roman god of ___.', ['war'], 'A', 'god of war'),
  ('A Martian day lasts 24 hours and ___ minutes.', ['37'], 'B', '37 minutes'),
  ('The average temperature is about minus ___ degrees.', ['sixty', '60'], 'C', 'minus sixty degrees'),
  ('Dr Okafor is a planetary ___.', ['scientist'], 'G', 'planetary scientist'),
 ]),
 short(3, [
  ('How long is a year on Mars?', ['687 earth days', '687 days'], 'B', '687 Earth days'),
  ('How long is Valles Marineris?', ['four thousand kilometres'], 'D', 'four thousand kilometres'),
  ('What was the first rover called?', ['sojourner'], 'F', 'Sojourner'),
 ]),
])
