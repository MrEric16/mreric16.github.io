from lib import *
from svgs import *
A = """In most cities, the water that comes out of a tap began its journey weeks earlier as rain or melted snow. It runs into rivers, lakes and underground stores, and from there it is taken to a treatment plant, where it is made safe to drink. The process takes only a few hours, but it involves several carefully controlled stages, and an error at any stage could make thousands of people ill. For this reason, the quality of drinking water is tested far more often than that of almost any other product that people buy, sometimes as often as every hour."""
B = """The first stage is the intake, where water is drawn from a river or reservoir through large pipes. At the entrance, a metal screen removes leaves, fish, plastic bottles and other large objects that would damage the machinery. Some plants also use a pre-treatment tank, where the water rests for a time so that the heaviest sand and stones sink to the bottom. Engineers monitor the flow constantly, because after heavy rain the water can contain ten times more mud than usual, and the plant must adjust its settings quickly to cope with the change."""
C = """Next comes coagulation. A chemical, usually a compound of aluminium or iron, is added to the water and mixed quickly. The tiny particles of clay and dirt that make the water cloudy carry a small electric charge, which keeps them apart, but the chemical cancels the charge, and the particles stick together to form larger lumps called flocs. The water then flows slowly into a settling tank, where the flocs, now heavy enough, sink to the bottom as sludge. This can remove up to ninety per cent of the dirt, and the sludge is later pumped away and dried."""
D = """The water that remains still contains very small particles, so it is passed through a filter. A typical filter is a deep bed of sand and gravel, with a layer of crushed coal on top. As the water trickles down through it, the particles are trapped between the grains. Every day or two, the filter is washed by pushing clean water upwards through it, which carries the dirt away. Some modern plants use membranes instead of sand; a membrane has holes so small that even bacteria cannot pass through, although it is more expensive to run."""
E = """Even clear water may contain bacteria and viruses, so the next step is disinfection. Most plants add a small amount of chlorine, which kills germs and continues to protect the water as it travels through the pipes. Others use ultraviolet light or ozone gas, which work faster and leave no taste, but give no protection once the water has left the plant. Chlorine does have disadvantages: some people dislike its smell, and in rare cases it can combine with natural substances to form harmful compounds, so the amount used must be carefully controlled."""
F = """The treated water is finally stored in large covered tanks, often built on hills so that gravity can push it through the pipes to homes and factories. Pumps provide the extra pressure that is needed for tall buildings. A city's pipe network may be many thousands of kilometres long, and in old cities some pipes are more than a century old, so leaks are a serious problem. In some places, as much as a third of the treated water is lost before it reaches the customer, which wastes both money and energy."""
G = """Engineers are now looking for ways to make the whole system more efficient. Sensors placed in the pipes can detect a leak within minutes and show where it is, so that crews can repair it before a road collapses. Some cities reuse water from their sewage plants, after treating it so that it is cleaner than the river water it replaces. Dr Hamid Karimi, a water engineer, says that the supply of clean water is one of the great challenges of this century, and that wasting it will soon be seen as a luxury that nobody can afford."""
S, PT, W, H = chain(5)
P = passage('p25', 'How Water Reaches Your Tap', 'Engineering', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Drinking water is tested very often.', 'T', 'A', 'tested far more often than that of almost any other product'),
  ('The treatment process takes several weeks.', 'F', 'A', 'takes only a few hours'),
  ('A metal screen removes large objects at the intake.', 'T', 'B', 'a metal screen removes leaves, fish, plastic bottles'),
  ('After heavy rain, river water contains less mud than usual.', 'F', 'B', 'ten times more mud than usual'),
  ('The chemical added in coagulation makes particles stick together.', 'T', 'C', 'the particles stick together to form larger lumps called flocs'),
  ('Sludge is thrown back into the river.', 'NG', 'C', 'the sludge is later pumped away and dried', 'The passage does not say where the dried sludge goes.'),
  ('A filter is cleaned by pushing clean water upwards.', 'T', 'D', 'pushing clean water upwards through it'),
  ('Ultraviolet light protects water inside the pipes.', 'F', 'E', 'give no protection once the water has left the plant'),
  ('Some pipes in old cities are more than a hundred years old.', 'T', 'F', 'more than a century old'),
 ]),
 mcq([
  ('Why is a metal screen used at the intake?', ['To make the water clean.', 'To protect the machinery.', 'To cool the water.', 'To add chlorine.'], 1, 'B', 'that would damage the machinery'),
  ('What is the advantage of membranes?', ['They are cheaper than sand.', 'They stop even bacteria.', 'They never need cleaning.', 'They add chlorine.'], 1, 'D', 'even bacteria cannot pass through'),
  ('Why are storage tanks often built on hills?', ['To save land.', 'To let gravity push the water.', 'To keep the water cold.', 'To avoid floods.'], 1, 'F', 'so that gravity can push it through the pipes'),
 ]),
 multi('Which TWO objects are mentioned as being removed by the screen in paragraph B?', ['Leaves.', 'Plastic bottles.', 'Aluminium.', 'Clay.', 'Chlorine.'], [0, 1], [('B', 'leaves, fish, plastic bottles'), ('B', 'plastic bottles')]),
 head(['Why water must be treated', 'Taking the water in', 'Making dirt stick together', 'Trapping small particles', 'Killing germs', 'From plant to customer', 'Smarter ways of saving water', 'The history of the water wheel', 'How rain forms'],
  [('A', 0, 'it is made safe to drink'), ('B', 1, 'The first stage is the intake'), ('C', 2, 'Next comes coagulation'), ('D', 3, 'so it is passed through a filter'), ('E', 4, 'the next step is disinfection'), ('F', 5, 'The treated water is finally stored'), ('G', 6, 'Engineers are now looking for ways to make the whole system more efficient')]),
 info([
  ('a figure for how often water is tested', 'A', 'sometimes as often as every hour'),
  ('a description of what makes water cloudy', 'C', 'clay and dirt that make the water cloudy'),
  ('a comparison of two materials in a filter bed', 'D', 'a deep bed of sand and gravel, with a layer of crushed coal'),
  ('a disadvantage of a chemical', 'E', 'some people dislike its smell'),
  ('a figure for water lost from pipes', 'F', 'as much as a third of the treated water'),
 ]),
 ends(['kills germs and protects the water in the pipes.', 'can remove up to ninety per cent of the dirt.', 'is used instead of sand in some plants.', 'help engineers find leaks within minutes.', 'is added at the intake to cool the water.', 'is used only in very small towns.', 'is a kind of metal pipe.'], [
  ('Chlorine', 0, 'E', 'kills germs and continues to protect the water'),
  ('Coagulation and settling', 1, 'C', 'This can remove up to ninety per cent of the dirt'),
  ('A membrane', 2, 'D', 'Some modern plants use membranes instead of sand'),
  ('Sensors in the pipes', 3, 'G', 'can detect a leak within minutes'),
 ]),
 diag('Label the stages of the water treatment plant. Write ONE WORD OR TWO WORDS from the passage for each answer.', W, H, S, PT,
  [(['intake'], 'B', 'The first stage is the intake'), (['coagulation'], 'C', 'Next comes coagulation'), (['filter'], 'D', 'passed through a filter'), (['disinfection'], 'E', 'the next step is disinfection'), (['tanks'], 'F', 'large covered tanks')], 2),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Water is drawn from a [[1]] through large pipes.', 'A chemical makes particles form [[2]], which sink as sludge.', 'The water is passed through a bed of sand and [[3]].', 'A small amount of [[4]] is added to kill germs.'],
  [(['river', 'reservoir'], 'B', 'a river or reservoir'), (['flocs'], 'C', 'larger lumps called flocs'), (['gravel'], 'D', 'sand and gravel'), (['chlorine'], 'E', 'a small amount of chlorine')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Stage', 'Detail'],
  [['Intake', 'A metal [[1]] removes large objects'], ['Coagulation', 'A compound of [[2]] or iron is added'], ['Filtration', 'The filter is washed with clean [[3]]'], ['Storage', 'Tanks are built on [[4]]']],
  [(['screen'], 'B', 'a metal screen'), (['aluminium'], 'C', 'aluminium or iron'), (['water'], 'D', 'pushing clean water upwards'), (['hills'], 'F', 'often built on hills')], 1),
 sent(2, [
  ('After heavy rain the water can contain ten times more ___ than usual.', ['mud'], 'B', 'ten times more mud'),
  ('Flocs sink to the bottom of the settling tank as ___.', ['sludge'], 'C', 'sink to the bottom as sludge'),
  ('Ozone gas leaves no ___.', ['taste'], 'E', 'leave no taste'),
  ('Pumps give the extra ___ needed for tall buildings.', ['pressure'], 'F', 'extra pressure'),
 ]),
 short(3, [
  ('Water from which kind of plant do some cities reuse?', ['sewage plants'], 'G', 'reuse water from their sewage plants'),
  ('Who is Dr Karimi?', ['a water engineer', 'water engineer'], 'G', 'a water engineer'),
  ('How often is a filter washed?', ['day or two'], 'D', 'Every day or two'),
 ]),
])
