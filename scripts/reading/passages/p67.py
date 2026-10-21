from lib import *
from svgs import *
A = """The atmosphere is the blanket of gases that surrounds the Earth and makes life possible. It supplies the oxygen that animals breathe, the carbon dioxide that plants need, and the water that falls as rain. It also protects the planet from the worst of the sun's radiation and from most of the small rocks that fall from space, which burn up as shooting stars. Air has no clear upper edge, but fades gradually into space, and scientists divide it into five layers according to changes in temperature. This passage describes the layers in order, starting at the ground and ending at the edge of space."""
B = """The lowest layer is the troposphere, which extends from the ground to a height of between eight and fifteen kilometres, depending on the place and the season. It is the thinnest layer but contains about three quarters of the mass of the air, and almost all of the water vapour, which is why all weather occurs here. Temperature falls with height, by roughly six degrees for every thousand metres, so the top of the troposphere is bitterly cold, at about minus fifty degrees. Aeroplanes fly near the top of this layer, where the air is thin and smooth, and where they can travel faster using less fuel."""
C = """Above it lies the stratosphere, which reaches to about fifty kilometres. Here the temperature rises with height, because the layer contains the ozone layer, a thin region of gas that absorbs harmful ultraviolet radiation from the sun and turns it into heat. Without the ozone, life on land would be impossible. The air in the stratosphere is calm and dry, with no storms, and the clouds are rare. Weather balloons can rise into it, and so do a few very high aircraft, but ordinary passengers never see it. In the 1980s, scientists discovered a hole in the ozone layer above Antarctica, which led the world's governments to ban the chemicals responsible."""
D = """The mesosphere extends from about fifty to eighty-five kilometres above the ground. It is the coldest layer, with temperatures as low as minus ninety degrees, and the air is so thin that it is almost impossible to measure from the ground. Most meteors burn up here, as the friction of the air heats them, which is why we see shooting stars in the night sky. Because the mesosphere is too high for balloons and too low for satellites, it remains the least understood layer, and scientists must study it using rockets, which spend only a few minutes passing through it."""
E = """Next comes the thermosphere, which reaches to about six hundred kilometres. The temperature here may exceed a thousand degrees, but a person would not feel hot, because the air is so thin that there are too few particles to transfer the heat. The thermosphere contains the electric particles that produce the aurora, the green and red lights seen near the poles. It is also the home of the International Space Station, which orbits at about four hundred kilometres, and of many satellites. The layer expands and contracts as the sun's activity changes, and this affects the paths of satellites, which must be adjusted regularly."""
F = """The outermost layer is the exosphere, where the atmosphere fades into space. Here the gas is so thin that the particles rarely collide, and light atoms such as hydrogen and helium can escape from the Earth altogether. There is no sharp upper limit, but the exosphere is thought to extend to about ten thousand kilometres. Dr Ingrid Solberg, an atmospheric physicist, says that it is the most remote part of the planet, yet it is the first to meet the stream of particles which the sun throws out, and so it provides valuable warning of storms in space that can damage satellites and electrical networks."""
G = """Understanding the layers is not simply a matter of curiosity. Weather forecasts depend on the troposphere, radio communications depend on the electric particles above, and our safety on the ozone layer. Dr Solberg points out that human activity has altered the lowest layers, by adding gases that trap heat, but also the highest ones, since thousands of satellites and pieces of space rubbish now orbit the planet. She urges nations to cooperate in keeping the environment clean, from the ground to the edge of space, since the atmosphere, unlike a country, has no borders. A single volcanic eruption or industrial accident can send pollution thousands of kilometres from its source, and for this reason the problem can only be solved by agreement between many countries."""
S, PT, W, H = layers(5)
P = passage('p67', 'The Layers of the Atmosphere', 'Earth science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The atmosphere has a clear upper edge.', 'F', 'A', 'no clear upper edge'),
  ('Scientists divide the atmosphere into five layers.', 'T', 'A', 'into five layers'),
  ('Most weather occurs in the troposphere.', 'T', 'B', 'all weather occurs here'),
  ('Temperature rises with height in the troposphere.', 'F', 'B', 'Temperature falls with height'),
  ('The ozone layer absorbs ultraviolet radiation.', 'T', 'C', 'absorbs harmful ultraviolet radiation from the sun'),
  ('The mesosphere is the coldest layer.', 'T', 'D', 'It is the coldest layer'),
  ('A person would feel hot in the thermosphere.', 'F', 'E', 'a person would not feel hot'),
  ('The International Space Station orbits in the thermosphere.', 'T', 'E', 'the home of the International Space Station'),
  ('Dr Solberg has visited the exosphere.', 'NG', 'F', 'Dr Ingrid Solberg', 'Her own travel is not mentioned.'),
 ]),
 mcq([
  ('Why do most meteors burn up in the mesosphere?', ['Friction with the air heats them.', 'The ozone melts them.', 'Rockets hit them.', 'Water vapour cools them.'], 0, 'D', 'the friction of the air heats them'),
  ('Why is the mesosphere the least understood layer?', ['It is too small.', 'It is too high for balloons and too low for satellites.', 'It has no air.', 'It is too hot.'], 1, 'D', 'too high for balloons and too low for satellites'),
  ('What does the exosphere give warning of?', ['Rain.', 'Earthquakes.', 'Storms in space.', 'Floods.'], 2, 'F', 'warning of storms in space'),
 ]),
 multi('Which TWO things does the atmosphere supply, according to paragraph A?', ['Oxygen for animals.', 'Carbon dioxide for plants.', 'Heat from the Earth\'s core.', 'Salt for the oceans.', 'Gold from space.'], [0, 1], [('A', 'the oxygen that animals breathe'), ('A', 'the carbon dioxide that plants need')]),
 head(['Why we need air', 'The home of the weather', 'A shield against the sun', 'The coldest region', 'Lights, stations and satellites', 'Where air meets space', 'Why the layers matter', 'The history of flight', 'How to make a balloon'],
  [('A', 0, 'makes life possible'), ('B', 1, 'all weather occurs here'), ('C', 2, 'absorbs harmful ultraviolet radiation'), ('D', 3, 'It is the coldest layer'), ('E', 4, 'the home of the International Space Station'), ('F', 5, 'where the atmosphere fades into space'), ('G', 6, 'Understanding the layers is not simply a matter of curiosity')]),
 info([
  ('a reference to aeroplanes', 'B', 'Aeroplanes fly near the top'),
  ('a reference to a hole in the ozone layer', 'C', 'a hole in the ozone layer above Antarctica'),
  ('a reference to the use of rockets', 'D', 'using rockets'),
  ('a reference to satellite paths needing adjustment', 'E', 'must be adjusted regularly'),
  ('a reference to danger from space weather', 'F', 'storms in space'),
 ]),
 ends(['burn up in the mesosphere.', 'turns radiation into heat.', 'is produced by electric particles.', 'can escape from the exosphere.', 'fall as rain.', 'are found only in the troposphere.', 'cannot be seen from the ground.'], [
  ('Most meteors', 0, 'D', 'Most meteors burn up here'),
  ('The ozone layer', 1, 'C', 'turns it into heat'),
  ('The aurora', 2, 'E', 'electric particles that produce the aurora'),
  ('Light atoms such as helium', 3, 'F', 'can escape from the Earth altogether'),
 ]),
 diag('Label the layers of the atmosphere, from the highest to the lowest. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['exosphere'], 'F', 'is the exosphere'), (['thermosphere'], 'E', 'Next comes the thermosphere'), (['mesosphere'], 'D', 'The mesosphere extends'), (['stratosphere'], 'C', 'lies the stratosphere'), (['troposphere'], 'B', 'is the troposphere')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Layer', 'Detail'],
  [['Troposphere', 'Contains almost all the water [[1]]'], ['Stratosphere', 'Contains the [[2]] layer'], ['Mesosphere', 'Temperatures as low as minus [[3]] degrees'], ['Thermosphere', 'Electric particles produce the [[4]]']],
  [(['vapour'], 'B', 'water vapour'), (['ozone'], 'C', 'the ozone layer'), (['ninety'], 'D', 'minus ninety degrees'), (['aurora'], 'E', 'produce the aurora')], 1),
 sent(2, [
  ('The troposphere contains about ___ quarters of the mass of the air.', ['three'], 'B', 'three quarters'),
  ('The stratosphere reaches to about ___ kilometres.', ['fifty', '50'], 'C', 'about fifty kilometres'),
  ('The International Space Station orbits at about four hundred ___.', ['kilometres'], 'E', 'four hundred kilometres'),
  ('Dr Solberg is an atmospheric ___.', ['physicist'], 'F', 'atmospheric physicist'),
 ]),
 short(3, [
  ('What does ozone absorb?', ['ultraviolet radiation'], 'C', 'ultraviolet radiation'),
  ('What lights are seen near the poles?', ['the aurora', 'aurora'], 'E', 'the aurora'),
  ('What has no borders?', ['atmosphere', 'the atmosphere'], 'G', 'the atmosphere, unlike a country, has no borders'),
 ]),
])
