from lib import *
A = """More than thirteen hundred volcanoes on land are considered potentially active, and about fifty of them erupt in an average year. Most lie along the edges of tectonic plates, especially around the Pacific Ocean in a belt known as the Ring of Fire. Where one plate is forced beneath another, rock melts deep in the Earth and rises as magma. Others, such as those of Hawaii, sit over hot spots, where a plume of heat rises from deep in the mantle through the middle of a plate."""
B = """A typical volcano consists of a magma chamber, a few kilometres below the surface, from which a conduit leads upwards to a vent. When the pressure in the chamber becomes greater than the strength of the rock above it, magma is forced up the conduit. Once it reaches the surface it is called lava. Over many eruptions, layers of lava and ash build a cone around the vent, and the crater at the top marks the place from which material has been thrown out."""
C = """Not all eruptions are alike, and the thickness of the magma decides how violent they are. Runny magma, as in Hawaii, lets gas escape easily, so the lava flows quietly for long distances. Thick, sticky magma traps gas, and the pressure builds until the volcano explodes. The 1980 eruption of Mount St Helens in the United States removed the top four hundred metres of the mountain in a few seconds. The 1815 eruption of Tambora in Indonesia was larger still, and the ash it threw into the atmosphere cooled the planet so much that 1816 became known in Europe as the year without a summer."""
D = """Despite the danger, about eight hundred million people live within one hundred kilometres of an active volcano. One reason is that volcanic soil is rich in minerals, and farmers on its slopes can grow several crops a year. Volcanic regions also supply geothermal energy: in Iceland, a large share of the country's electricity comes from this source, and hot water from the ground heats most homes. Tourists add to the income of these places, which makes it even harder to ask the people who live there to leave."""
E = """Predicting eruptions is difficult, but scientists have learned to read the warning signs. Before an eruption, rising magma causes many small earthquakes, and the ground may swell by several centimetres. Instruments also measure the gas that escapes from the vent, and a sudden increase in sulphur dioxide often means that magma is close to the surface. Satellites can detect the swelling from space. In 1991, such warnings allowed scientists to persuade tens of thousands of people to leave the area around Mount Pinatubo in the Philippines days before it erupted, and thousands of lives were saved."""
F = """However, forecasts are never certain. Some volcanoes show signs for months and then fall quiet, while others give almost no warning at all. Evacuating a city that is then not threatened is expensive, and it may cause people to ignore the next order. Dr Mateo Ruiz, a volcanologist, argues that the best protection is not prediction but preparation: clear evacuation routes, regular drills and honest communication with the public. 'A good plan', he says, 'works even when the forecast is wrong.'"""
G = """Scientists also study a rarer danger, the supervolcano. Such a volcano can produce an eruption a thousand times larger than that of Mount St Helens. The last one, at Lake Toba in Indonesia, took place about 74,000 years ago, and some researchers think that it reduced the human population to a few thousand. Most experts regard another eruption of that size in the near future as extremely unlikely, but they say it would be a global disaster with effects lasting for years."""
SVG = ('<path class="l" d="M20 190H400"/><path class="s" d="M60 190L195 60H225L360 190Z"/><rect class="f" x="203" y="66" width="14" height="170"/>'
 '<ellipse class="c" cx="210" cy="248" rx="62" ry="22"/><path class="l" d="M127 125L90 120M227 60L300 42M217 140H330M272 248H335"/>')
P = passage('p16', 'Living with Volcanoes', 'Geology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('About fifty volcanoes erupt in an average year.', 'T', 'A', 'about fifty of them erupt in an average year'),
  ('All volcanoes lie along the edges of tectonic plates.', 'F', 'A', 'sit over hot spots, where a plume of heat rises from deep in the mantle through the middle of a plate'),
  ('Magma is called lava once it reaches the surface.', 'T', 'B', 'Once it reaches the surface it is called lava'),
  ('Runny magma usually produces the most violent eruptions.', 'F', 'C', 'lets gas escape easily, so the lava flows quietly'),
  ('Mount St Helens erupted in 1980.', 'T', 'C', 'The 1980 eruption of Mount St Helens'),
  ('Tambora caused more deaths than Mount St Helens.', 'NG', 'C', 'was larger still', 'The eruption was larger, but deaths are not compared.'),
  ('Most homes in Iceland are heated by hot water from the ground.', 'T', 'D', 'hot water from the ground heats most homes'),
  ('Satellites cannot detect any changes in the ground.', 'F', 'E', 'Satellites can detect the swelling from space'),
  ('The Pinatubo evacuation was ordered by the government of the Philippines.', 'NG', 'E', 'scientists to persuade tens of thousands of people to leave', 'Scientists persuaded people; the passage does not say who gave the order.'),
 ]),
 mcq([
  ('What does the thickness of magma determine?', ['the colour of the lava', 'the height of the cone', 'how violent the eruption is', 'where the volcano forms'], 2, 'C', 'the thickness of the magma decides how violent they are'),
  ('Why do people live near active volcanoes?', ['The government pays them to stay.', 'The soil is fertile.', 'Eruptions are easy to predict.', 'There are no other places to live.'], 1, 'D', 'volcanic soil is rich in minerals'),
  ('What is the main idea of Dr Ruiz\'s argument?', ['Forecasts will soon be perfect.', 'Cities should never be evacuated.', 'Preparation matters more than prediction.', 'Volcanologists need better satellites.'], 2, 'F', 'the best protection is not prediction but preparation'),
 ]),
 multi('Which TWO warning signs of an eruption are mentioned in paragraph E?', ['Many small earthquakes.', 'Swelling of the ground.', 'A change in the colour of the sea.', 'A fall in the temperature of the vent.', 'The disappearance of local animals.'], [0, 1], [('E', 'many small earthquakes'), ('E', 'the ground may swell')]),
 head(['Where volcanoes occur', 'The parts of a volcano', 'Mild and violent eruptions', 'Reasons to live in danger', 'Reading the signs', 'Why plans matter more than forecasts', 'A rare and terrible threat', 'The first scientist to study lava', 'How to survive an eruption at home'],
  [('A', 0, 'Most lie along the edges of tectonic plates'), ('B', 1, 'A typical volcano consists of a magma chamber'), ('C', 2, 'Not all eruptions are alike'), ('D', 3, 'Despite the danger'), ('E', 4, 'scientists have learned to read the warning signs'), ('F', 5, 'forecasts are never certain'), ('G', 6, 'Scientists also study a rarer danger')]),
 info([
  ('a name for a belt of volcanoes', 'A', 'a belt known as the Ring of Fire'),
  ('a reason for a cold year in Europe', 'C', 'cooled the planet so much'),
  ('a source of energy from the ground', 'D', 'geothermal energy'),
  ('a gas whose increase is a warning sign', 'E', 'a sudden increase in sulphur dioxide'),
  ('an example of an eruption that may have reduced the human population', 'G', 'reduced the human population to a few thousand'),
 ]),
 ends(['along the edges of tectonic plates.', 'traps gas until the volcano explodes.', 'cooled the planet.', 'lets farmers grow several crops a year.', 'is found only in Hawaii.', 'is used to make building materials.', 'tells scientists the exact date of an eruption.'], [
  ('Most volcanoes lie', 0, 'A', 'Most lie along the edges of tectonic plates'),
  ('Thick, sticky magma', 1, 'C', 'Thick, sticky magma traps gas, and the pressure builds until the volcano explodes'),
  ('The ash from Tambora', 2, 'C', 'cooled the planet so much'),
  ('Volcanic soil', 3, 'D', 'grow several crops a year'),
 ]),
 sent(2, [
  ('Volcanoes in Hawaii sit over ___.', ['hot spots', 'hot spot'], 'A', 'sit over hot spots'),
  ('The Mount Pinatubo area is in the ___.', ['philippines', 'the philippines'], 'E', 'Mount Pinatubo in the Philippines'),
  ('Dr Ruiz is a ___.', ['volcanologist'], 'F', 'a volcanologist'),
  ('The last supervolcano eruption was at Lake ___.', ['toba'], 'G', 'Lake Toba'),
 ]),
 short(3, [
  ('How far from an active volcano do about eight hundred million people live?', ['one hundred kilometres', '100 kilometres', '100 km'], 'D', 'within one hundred kilometres of an active volcano'),
  ('What does Dr Ruiz say a good plan works even when wrong?', ['the forecast'], 'F', 'works even when the forecast is wrong'),
  ('What kind of volcano can produce an eruption a thousand times larger than Mount St Helens?', ['a supervolcano', 'supervolcano'], 'G', 'the supervolcano'),
 ]),
 diag('Label the diagram of a volcano. Write NO MORE THAN TWO WORDS from the passage for each answer.', 420, 280, SVG, [[80, 118], [310, 40], [340, 140], [345, 248]],
  [(['cone'], 'B', 'layers of lava and ash build a cone'), (['crater'], 'B', 'the crater at the top'), (['conduit'], 'B', 'a conduit leads upwards'), (['magma chamber'], 'B', 'a magma chamber')], 2),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Volcanoes form where plates meet or over hot [[1]]. Thick magma traps [[2]] and causes explosions. People stay nearby because the [[3]] is fertile, and scientists watch for [[4]] and swelling ground to give warning.',
  [(['spots'], 'A', 'hot spots'), (['gas'], 'C', 'traps gas'), (['soil'], 'D', 'volcanic soil'), (['earthquakes'], 'E', 'many small earthquakes')], 1,
  bank=['spots', 'gas', 'soil', 'earthquakes', 'rivers', 'water', 'storms', 'crops']),
])
