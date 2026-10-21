from lib import *
from svgs import *
A = """The air around the Earth is not the same all the way up. It forms a series of layers, each with its own temperature, pressure and chemical make-up, and together they make up the atmosphere. The layers are not separated by sharp lines; instead, one gradually merges into the next. Altogether, the atmosphere is roughly a hundred kilometres deep, which sounds a great distance but is about the same as the journey between two neighbouring cities. If the Earth were the size of an apple, the atmosphere would be thinner than the apple's skin."""
B = """The lowest layer is the troposphere, which extends from the ground to a height of between eight and sixteen kilometres, depending on the latitude and the season. It is the layer in which we live, and it contains about eighty per cent of the mass of the atmosphere and nearly all of its water vapour. For that reason, almost all weather, including clouds, rain and storms, takes place here. The temperature falls steadily as one climbs, by about six degrees for every thousand metres, which is why mountain tops are cold even in summer."""
C = """Above it lies the stratosphere, which reaches to about fifty kilometres. Here the pattern changes, and the temperature begins to rise with height. The reason is the ozone layer, a thin region rich in a form of oxygen called ozone. Ozone absorbs ultraviolet radiation from the Sun, and in doing so it warms the air around it. Without this natural shield, the radiation reaching the ground would damage plants and cause skin cancer in humans. Because the stratosphere is calm and has few clouds, passenger jets often fly in its lower part."""
D = """The mesosphere comes next, from about fifty to eighty-five kilometres above the ground. It is the coldest part of the atmosphere, with temperatures that can fall to ninety degrees below zero. Although the air here is far too thin to breathe, it is dense enough to stop most meteors, which burn up as they enter it and can be seen from the ground as shooting stars. Scientists find the layer hard to study, since it is too high for aircraft and balloons but too low for satellites, and so it has sometimes been called the ignorosphere."""
E = """Beyond the mesosphere lies the thermosphere, which stretches to roughly six hundred kilometres. The air here is extremely thin, but it absorbs powerful radiation from the Sun, so its temperature can exceed a thousand degrees Celsius. A person would not feel hot, however, because there are so few molecules to transfer the heat. The thermosphere is the home of the aurora, the glowing curtains of light seen near the poles, which appear when charged particles from the Sun strike the gases. The International Space Station orbits within this layer."""
F = """The last layer is the exosphere, which has no clear upper limit. Its gases are so thin that the molecules rarely collide, and some of the lightest, hydrogen and helium, escape slowly into space. Many satellites orbit in or near this layer. Beyond it, the atmosphere fades into the near-emptiness between the planets. Dr Anita Rao, an atmospheric physicist, explains that the border between the atmosphere and space is a matter of convention, and that the most widely used figure, one hundred kilometres, was chosen because it is a round number."""
G = """Human activity is changing the atmosphere in ways that scientists are only beginning to understand. In the 1980s, chemicals used in refrigerators and spray cans were found to be destroying ozone over the Antarctic, and an international agreement, signed in 1987, banned them. The ozone layer has since begun to recover. Carbon dioxide, on the other hand, continues to build up in the lowest layer, where it traps heat, and it also cools the upper layers, which are shrinking slowly as a result. The study of these changes is therefore important for the whole planet."""
S, PT, W, H = layers(5)
P = passage('p26', 'The Layers of the Atmosphere', 'Earth science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The atmosphere has sharp boundaries between its layers.', 'F', 'A', 'one gradually merges into the next'),
  ('The atmosphere is about a hundred kilometres deep.', 'T', 'A', 'roughly a hundred kilometres deep'),
  ('Most of the water vapour in the atmosphere is in the troposphere.', 'T', 'B', 'nearly all of its water vapour'),
  ('The temperature rises steadily as one climbs through the troposphere.', 'F', 'B', 'The temperature falls steadily as one climbs'),
  ('Ozone absorbs ultraviolet radiation.', 'T', 'C', 'absorbs ultraviolet radiation from the Sun'),
  ('The stratosphere has many storms.', 'F', 'C', 'calm and has few clouds'),
  ('Meteors burn up in the mesosphere.', 'T', 'D', 'burn up as they enter it'),
  ('Scientists have sent balloons to study the mesosphere in detail.', 'F', 'D', 'too high for aircraft and balloons'),
  ('The aurora has been photographed from the space station.', 'NG', 'E', 'The International Space Station orbits within this layer', 'Photographs are not mentioned.'),
 ]),
 mcq([
  ('Why does the stratosphere get warmer with height?', ['Because of the ozone layer.', 'Because of the clouds.', 'Because of volcanoes.', 'Because of satellites.'], 0, 'C', 'in doing so it warms the air around it'),
  ('Why would a person not feel hot in the thermosphere?', ['The air is too cold.', 'There are few molecules to pass on heat.', 'The Sun is too far away.', 'Astronauts wear suits.'], 1, 'E', 'so few molecules to transfer the heat'),
  ('Why is the border of space put at one hundred kilometres?', ['It is where the air stops.', 'It was measured by satellites.', 'It is a round number.', 'It is the top of the thermosphere.'], 2, 'F', 'because it is a round number'),
 ]),
 multi('Which TWO effects of the loss of the ozone layer are mentioned in paragraph C?', ['Damage to plants.', 'Skin cancer in humans.', 'Rising sea levels.', 'Stronger winds.', 'Heavier rain.'], [0, 1], [('C', 'damage plants'), ('C', 'skin cancer in humans')]),
 head(['A layered blanket of air', 'Where the weather happens', 'A shield against radiation', 'The coldest region', 'Heat and light shows', 'Where air meets space', 'People and the atmosphere', 'The invention of the jet engine', 'The size of the Earth'],
  [('A', 0, 'It forms a series of layers'), ('B', 1, 'almost all weather, including clouds, rain and storms'), ('C', 2, 'Ozone absorbs ultraviolet radiation'), ('D', 3, 'It is the coldest part of the atmosphere'), ('E', 4, 'The thermosphere is the home of the aurora'), ('F', 5, 'The last layer is the exosphere'), ('G', 6, 'Human activity is changing the atmosphere')]),
 info([
  ('a comparison with a piece of fruit', 'A', 'thinner than the apple\'s skin'),
  ('a rate of temperature fall with height', 'B', 'about six degrees for every thousand metres'),
  ('a mention of a nickname for a layer', 'D', 'the ignorosphere'),
  ('a place where the aurora is seen', 'E', 'near the poles'),
  ('a date of an international agreement', 'G', 'signed in 1987'),
 ]),
 ends(['contains most of the atmosphere\'s mass.', 'protects the Earth from ultraviolet radiation.', 'stops most meteors.', 'can exceed a thousand degrees Celsius.', 'has been banned by international law.', 'is the coldest layer of all.', 'is where satellites never travel.'], [
  ('The troposphere', 0, 'B', 'about eighty per cent of the mass of the atmosphere'),
  ('The ozone layer', 1, 'C', 'Ozone absorbs ultraviolet radiation from the Sun'),
  ('The mesosphere', 2, 'D', 'dense enough to stop most meteors'),
  ('The temperature of the thermosphere', 3, 'E', 'can exceed a thousand degrees Celsius'),
 ]),
 diag('Label the layers of the atmosphere, from the ground upwards. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['troposphere'], 'B', 'the troposphere'), (['stratosphere'], 'C', 'the stratosphere'), (['mesosphere'], 'D', 'The mesosphere'), (['thermosphere'], 'E', 'the thermosphere'), (['exosphere'], 'F', 'the exosphere')], 1),
 feat('Match each statement with the correct layer, A to D.', ['The troposphere', 'The stratosphere', 'The mesosphere', 'The thermosphere'], [
  ('Passenger jets often fly in its lower part.', 1, 'C', 'passenger jets often fly in its lower part'),
  ('It is the layer in which we live.', 0, 'B', 'It is the layer in which we live'),
  ('It is too high for aircraft but too low for satellites.', 2, 'D', 'too high for aircraft and balloons but too low for satellites'),
  ('The International Space Station orbits within it.', 3, 'E', 'The International Space Station orbits within this layer'),
 ]),
 sent(2, [
  ('The troposphere reaches a height of between eight and ___ kilometres.', ['sixteen', '16'], 'B', 'between eight and sixteen kilometres'),
  ('The ozone layer is rich in a form of ___.', ['oxygen'], 'C', 'a form of oxygen'),
  ('Shooting stars are ___ burning up in the mesosphere.', ['meteors'], 'D', 'stop most meteors'),
  ('An international agreement to protect ozone was signed in ___.', ['1987'], 'G', 'signed in 1987'),
 ]),
 short(3, [
  ('What are the lightest gases that escape into space?', ['hydrogen and helium', 'hydrogen', 'helium'], 'F', 'hydrogen and helium'),
  ('What is Dr Rao\'s profession?', ['atmospheric physicist', 'an atmospheric physicist'], 'F', 'an atmospheric physicist'),
  ('Where was ozone found to be destroyed?', ['over the antarctic', 'antarctic'], 'G', 'over the Antarctic'),
 ]),
])
