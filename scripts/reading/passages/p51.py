from lib import *
from svgs import *
A = """The deepest hole that humans have ever drilled, on the Kola Peninsula in Russia, is just over twelve kilometres deep. That sounds impressive, but it is less than two-tenths of one per cent of the distance to the centre of the Earth, which is about 6,370 kilometres. Scientists cannot therefore examine the interior directly, and they have learned about it mostly from the waves produced by earthquakes, which travel through the planet and change speed and direction when they meet different materials. From this evidence they have concluded that the Earth is made of four main layers."""
B = """The outermost layer is the crust, a thin shell of rock on which we live. Beneath the oceans it is only about seven kilometres thick, and beneath the continents it averages about thirty-five kilometres, though it can reach seventy kilometres under high mountains. If the Earth were an apple, the crust would be no thicker than the skin. It is broken into huge slabs, called tectonic plates, which move very slowly, at about the speed at which fingernails grow, and this movement is the cause of earthquakes and volcanoes."""
C = """Beneath the crust lies the mantle, which is by far the thickest layer. It extends to a depth of about 2,900 kilometres and makes up about eighty-four per cent of the Earth's volume. The mantle is made of hot, dense rock. It is not liquid, but over millions of years it flows very slowly, like extremely thick toffee, carrying heat from the interior towards the surface. The temperature rises from about 1,000 degrees Celsius at the top to more than 3,500 degrees at the bottom."""
D = """Below the mantle is the outer core, a layer of liquid metal about 2,200 kilometres thick, made mainly of iron with some nickel. Its temperature is between 4,000 and 5,000 degrees Celsius. The liquid moves in great swirling currents, and because the metal conducts electricity, these movements create the Earth's magnetic field. This field extends far into space and protects the planet from harmful particles from the Sun. Without it, the atmosphere might have been stripped away long ago."""
E = """At the centre is the inner core, a ball of solid iron and nickel about 1,220 kilometres in radius, which is roughly three-quarters the size of the Moon. It is as hot as the surface of the Sun, about 5,500 degrees Celsius, but it stays solid because the pressure there, more than three million times that of the atmosphere at sea level, prevents the metal from melting. The inner core is growing very slowly as the Earth cools, by about a millimetre a year."""
F = """How do we know all this? When an earthquake occurs, it sends out two kinds of waves. P-waves, which are like sound, can pass through both solids and liquids, but S-waves, which shake the rock from side to side, cannot cross a liquid. In 1906, the Irish geologist Richard Oldham noticed that S-waves did not arrive on the far side of the Earth, and he concluded that part of the interior must be liquid. Three decades later, the Danish scientist Inge Lehmann used the paths of P-waves to show that inside the liquid core there is a smaller solid one."""
G = """Understanding the interior is more than a matter of curiosity. The mantle's slow movement explains why continents drift, why mountains rise and why some regions suffer earthquakes and others do not. The core's magnetic field has reversed direction many times in the planet's history, and it is now weakening in some regions, which worries engineers who depend on satellites. Dr Yusuf Demir, a geophysicist, says that every new measurement of the deep Earth is likely to bring surprises, because the planet is far more active than it appears from the surface."""
S, PT, W, H = layers(4)
P = passage('p51', 'Journey to the Centre of the Earth', 'Earth science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Kola hole reaches the Earth\'s outer core.', 'NG', 'A', 'is just over twelve kilometres deep', 'Only its depth is given; it is far above the core.'),
  ('The deepest hole ever drilled is over twelve kilometres deep.', 'T', 'A', 'just over twelve kilometres deep'),
  ('Scientists have learned about the interior mostly from earthquake waves.', 'T', 'A', 'mostly from the waves produced by earthquakes'),
  ('The crust is thicker beneath the oceans than beneath the continents.', 'F', 'B', 'beneath the continents it averages about thirty-five kilometres'),
  ('Tectonic plates move about as fast as fingernails grow.', 'T', 'B', 'at about the speed at which fingernails grow'),
  ('The mantle is liquid.', 'F', 'C', 'It is not liquid'),
  ('The mantle makes up most of the Earth\'s volume.', 'T', 'C', 'about eighty-four per cent of the Earth\'s volume'),
  ('The outer core is made mainly of iron.', 'T', 'D', 'made mainly of iron with some nickel'),
  ('The inner core is liquid.', 'F', 'E', 'a ball of solid iron and nickel'),
  ('Inge Lehmann was a Swedish scientist.', 'F', 'F', 'the Danish scientist Inge Lehmann'),
 ]),
 mcq([
  ('Why does the inner core stay solid?', ['It is cold.', 'The pressure is enormous.', 'It is made of rock.', 'It is far from the Sun.'], 1, 'E', 'the pressure there'),
  ('What creates the Earth\'s magnetic field?', ['The movement of liquid metal.', 'Plate movement.', 'The Moon.', 'Volcanoes.'], 0, 'D', 'these movements create the Earth\'s magnetic field'),
  ('What did Oldham conclude?', ['The core is solid.', 'Part of the interior is liquid.', 'The crust is thick.', 'The mantle is cold.'], 1, 'F', 'part of the interior must be liquid'),
 ]),
 multi('Which TWO things does the magnetic field do or show, according to the passage?', ['It protects the planet from harmful particles.', 'It has reversed direction many times.', 'It heats the mantle.', 'It makes the Moon orbit.', 'It causes earthquakes.'], [0, 1], [('D', 'protects the planet from harmful particles from the Sun'), ('G', 'has reversed direction many times')]),
 head(['The limits of drilling', 'A thin and broken shell', 'A slowly flowing layer', 'A liquid metal layer', 'A hot, solid centre', 'How scientists found out', 'Why the interior matters', 'The history of the volcano', 'How to drill a well'],
  [('A', 0, 'Scientists cannot therefore examine the interior directly'), ('B', 1, 'The outermost layer is the crust'), ('C', 2, 'Beneath the crust lies the mantle'), ('D', 3, 'Below the mantle is the outer core'), ('E', 4, 'At the centre is the inner core'), ('F', 5, 'How do we know all this'), ('G', 6, 'Understanding the interior is more than a matter of curiosity')]),
 info([
  ('a comparison of the crust with fruit', 'B', 'no thicker than the skin'),
  ('a comparison of the mantle\'s movement with a food', 'C', 'like extremely thick toffee'),
  ('a comparison of the inner core\'s temperature with the Sun', 'E', 'as hot as the surface of the Sun'),
  ('a description of the way S-waves move', 'F', 'shake the rock from side to side'),
  ('a mention of satellites', 'G', 'engineers who depend on satellites'),
 ]),
 ends(['is the thinnest layer.', 'is the thickest layer.', 'is made of liquid metal.', 'is a solid ball of iron and nickel.', 'is the hottest layer in the mantle.', 'was drilled on the Kola Peninsula.', 'is found only under oceans.'], [
  ('The crust', 0, 'B', 'a thin shell of rock'),
  ('The mantle', 1, 'C', 'by far the thickest layer'),
  ('The outer core', 2, 'D', 'a layer of liquid metal'),
  ('The inner core', 3, 'E', 'a ball of solid iron and nickel'),
 ]),
 diag('Label the layers of the Earth, from the outside to the centre. Write ONE OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['crust'], 'B', 'the crust'), (['mantle'], 'C', 'the mantle'), (['outer core'], 'D', 'the outer core'), (['inner core'], 'E', 'the inner core')], 2),
 sent(2, [
  ('The centre of the Earth is about ___ kilometres away.', ['6,370', '6370'], 'A', 'about 6,370 kilometres'),
  ('The crust is broken into tectonic ___.', ['plates'], 'B', 'tectonic plates'),
  ('The mantle flows like thick ___.', ['toffee'], 'C', 'thick toffee'),
  ('Dr Demir is a ___.', ['geophysicist'], 'G', 'a geophysicist'),
 ]),
 short(3, [
  ('How thick is the crust beneath the oceans?', ['seven kilometres', 'about seven kilometres'], 'B', 'about seven kilometres thick'),
  ('Which waves cannot cross a liquid?', ['s-waves'], 'F', 'S-waves, which shake the rock'),
  ('How fast is the inner core growing?', ['a millimetre', 'millimetre'], 'E', 'by about a millimetre a year'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Scientists study the interior through [[1]] waves. The Earth has a thin crust, a thick mantle, a liquid outer core and a solid inner [[2]]. The movement of the liquid metal creates the magnetic [[3]], which protects the planet from harmful [[4]].',
  [(['earthquake'], 'A', 'waves produced by earthquakes'.replace('waves produced by earthquakes','earthquakes')), (['core'], 'E', 'inner core'), (['field'], 'D', 'magnetic field'), (['particles'], 'D', 'harmful particles')], 1,
  bank=['earthquake', 'core', 'field', 'particles', 'ocean', 'storm', 'water', 'oxygen']),
])
