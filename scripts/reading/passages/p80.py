from lib import *
from svgs import *
A = """A glacier is a huge mass of ice that moves slowly downhill under its own weight. Glaciers cover about ten per cent of the Earth's land, mainly in Antarctica and Greenland, but they also exist on high mountains in every continent, including the Tien Shan and Pamir ranges of Central Asia. Together they hold about two thirds of all the fresh water on the planet. Glaciers may seem still, but they flow, like very thick honey, and the fastest travel several metres a day. This passage explains how glaciers form, how they shape the land and why the changes now taking place in them matter to millions of people."""
B = """A glacier begins as snow. In places where more snow falls in winter than melts in summer, the snow accumulates year after year. The weight of the upper layers presses on the lower ones, squeezing out the air and turning the loose flakes first into a granular material called firn and then into solid ice. This process may take from a few decades in a wet climate to thousands of years in a dry one. The ice of the deepest glaciers is very old: cores drilled in Antarctica contain ice that fell as snow more than eight hundred thousand years ago, and the bubbles of air trapped in it are samples of the ancient atmosphere."""
C = """Under pressure, ice behaves like a very slow liquid. The glacier flows downhill, sliding on a thin film of meltwater at its base and bending slowly within. The upper part is brittle, and as the ice moves over bumps in the valley floor, it cracks into deep splits called crevasses, which can be dangerous to climbers, especially when they are hidden by a thin bridge of snow. The upper end of the glacier, where snow accumulates, is called the accumulation zone; the lower end, where the ice melts, is the ablation zone. If the two are in balance, the glacier keeps its size, but if melting exceeds snowfall, it shrinks."""
D = """Glaciers are powerful sculptors. As they move, they carry rocks that grind the valley floor and walls, so that a river valley with a V-shaped section is changed into a broad U-shaped one. They pluck boulders from the mountain and drop them far away, in long ridges called moraines. When a glacier reaches the sea, the glacial valley fills with water to form a fjord, such as those of Norway and New Zealand. Many of the world's lakes, including the Great Lakes of North America, were formed by glaciers. Even the soil of some of the richest farmland is made of fine dust ground by ice."""
E = """Glaciers are also natural reservoirs. They store water as ice in winter and release it as meltwater in the summer, when rivers need it most. In Central Asia, the rivers that feed the cities and fields, such as the Amu Darya and the Syr Darya, receive a significant part of their summer flow from the glaciers of the Pamir and Tien Shan mountains. Hundreds of millions of people around the world depend on glacier water for drinking, farming and electricity. Because of this, the health of a glacier is a matter of life and death for entire regions."""
F = """Unfortunately, most of the world's glaciers are shrinking. As the climate warms, they melt faster in summer than they grow in winter. Measurements show that mountain glaciers have lost mass every year for decades, and in some areas the retreat is so rapid that small glaciers may vanish within a lifetime. In the beginning, the extra meltwater increases the flow of rivers, which seems to be a benefit; but once the ice has gone, the rivers will dry up in summer. Scientists call this tipping point peak water, and in some mountain regions it has already been passed."""
G = """Dr Nurlan Bekov, a glaciologist who has worked in the Tien Shan for twenty years, climbs to the glaciers every summer to measure their thickness with a radar and to place stakes in the ice that show how much it melts. He says that a glacier is a record of climate, written in ice, and that the evidence is clear. He argues that countries must plan now for the time when the glaciers are gone, by building water storage, using water more carefully and, above all, reducing the emissions that cause the warming. The decisions made today, he says, will determine how much ice remains for the next generation."""
S, PT, W, H = chain(4)
P = passage('p80', 'Rivers of Ice', 'Earth science', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Glaciers cover about ten per cent of the Earth\'s land.', 'T', 'A', 'about ten per cent of the Earth\'s land'),
  ('Glaciers exist only in the polar regions.', 'F', 'A', 'high mountains in every continent'),
  ('Glaciers hold about two thirds of the fresh water on Earth.', 'T', 'A', 'two thirds of all the fresh water'),
  ('The fastest glaciers travel several metres a day.', 'T', 'A', 'several metres a day'),
  ('Firn is a granular material.', 'T', 'B', 'granular material called firn'),
  ('Ice cores from Antarctica contain very old ice.', 'T', 'B', 'more than eight hundred thousand years ago'),
  ('Crevasses are always easy to see.', 'F', 'C', 'hidden by a thin bridge of snow'),
  ('Glaciers can turn V-shaped valleys into U-shaped ones.', 'T', 'D', 'broad U-shaped one'),
  ('Tourism in Norway depends on fjords.', 'NG', 'D', 'a fjord, such as those of Norway', 'Tourism is not mentioned.'),
 ]),
 mcq([
  ('What turns the lower layers of snow into ice?', ['The weight of the upper layers.', 'The wind.', 'The rain.', 'The sun.'], 0, 'B', 'The weight of the upper layers presses on the lower ones'),
  ('Why does the retreat of a glacier seem a benefit at first?', ['Extra meltwater increases river flow.', 'It makes valleys larger.', 'It cools the air.', 'It creates lakes.'], 0, 'F', 'the extra meltwater increases the flow of rivers'),
  ('What does Dr Bekov say a glacier is?', ['A record of climate written in ice.', 'A river of water.', 'A mountain of rock.', 'A lake.'], 0, 'G', 'a record of climate, written in ice'),
 ]),
 diag('Label the stages in the life of a glacier, in order. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['snow'], 'B', 'A glacier begins as snow'), (['firn'], 'B', 'called firn'), (['ice'], 'B', 'solid ice'), (['crevasses'], 'C', 'called crevasses')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Accumulation zone', 'Where [[1]] collects'], ['Ablation zone', 'Where the ice [[2]]'], ['Moraine', 'Rocks dropped in long [[3]]'], ['Fjord', 'A glacial valley filled with [[4]]']],
  [(['snow'], 'C', 'where snow accumulates'), (['melts'], 'C', 'where the ice melts'), (['ridges'], 'D', 'long ridges called moraines'), (['water'], 'D', 'fills with water')], 1),
 feat('Match each statement with the correct feature, A to D.', ['Crevasses', 'Moraines', 'Fjords', 'Meltwater'], [
  ('They can be dangerous to climbers.', 0, 'C', 'dangerous to climbers'),
  ('They are long ridges of dropped rocks.', 1, 'D', 'long ridges called moraines'),
  ('They are found in Norway and New Zealand.', 2, 'D', 'Norway and New Zealand'),
  ('It is released in summer when rivers need it.', 3, 'E', 'when rivers need it most'),
 ]),
 multi('Which TWO uses of glacier water are mentioned in paragraph E?', ['Drinking.', 'Farming.', 'Fishing.', 'Mining.', 'Shipping.'], [0, 1], [('E', 'drinking'), ('E', 'farming')]),
 head(['Rivers of ice', 'From snow to ice', 'A slow flow', 'Sculptors of the land', 'Reservoirs in the mountains', 'A shrinking supply', 'A scientist\'s plea', 'The history of skiing', 'Polar bears'],
  [('A', 0, 'a huge mass of ice that moves slowly downhill'), ('B', 1, 'turning the loose flakes first into a granular material'), ('C', 2, 'Under pressure, ice behaves like a very slow liquid'), ('D', 3, 'Glaciers are powerful sculptors'), ('E', 4, 'Glaciers are also natural reservoirs'), ('F', 5, 'most of the world\'s glaciers are shrinking'), ('G', 6, 'plan now for the time when the glaciers are gone')]),
 info([
  ('a comparison with honey', 'A', 'very thick honey'),
  ('a reference to the ancient atmosphere', 'B', 'ancient atmosphere'),
  ('a reference to a hidden hazard', 'C', 'thin bridge of snow'),
  ('a reference to lakes in North America', 'D', 'Great Lakes of North America'),
  ('a term for a tipping point', 'F', 'peak water'),
 ]),
 ends(['is pressed into ice by the weight above it.', 'form as the ice moves over bumps.', 'store water as ice in winter.', 'measures glacier thickness with a radar.', 'are found only in Antarctica.', 'melt in winter.', 'create deserts.'], [
  ('Snow', 0, 'B', 'The weight of the upper layers presses on the lower ones'),
  ('Crevasses', 1, 'C', 'moves over bumps'),
  ('Glaciers', 2, 'E', 'store water as ice in winter'),
  ('Dr Bekov', 3, 'G', 'measure their thickness with a radar'),
 ]),
 sent(2, [
  ('A glacier moves slowly downhill under its own ___.', ['weight'], 'A', 'own weight'),
  ('The lower end of a glacier is the ___ zone.', ['ablation'], 'C', 'ablation zone'),
  ('The Amu Darya and the Syr Darya receive part of their summer flow from ___.', ['glaciers'], 'E', 'from the glaciers'),
  ('Dr Bekov is a ___.', ['glaciologist'], 'G', 'a glaciologist'),
 ]),
 short(3, [
  ('What are ridges of dropped rocks called?', ['moraines'], 'D', 'called moraines'),
  ('How long has Dr Bekov worked in the Tien Shan?', ['twenty years'], 'G', 'twenty years'),
  ('What is the tipping point called?', ['peak water'], 'F', 'peak water'),
 ]),
])
