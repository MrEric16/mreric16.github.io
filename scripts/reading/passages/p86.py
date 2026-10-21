from lib import *
from svgs import *
A = """People have used the wind for thousands of years, to sail ships and to grind grain. Today the same force is used to make electricity. A wind turbine turns the energy of moving air into power for homes, factories and schools, without burning any fuel or producing any smoke. Wind is one of the fastest-growing sources of energy in the world, and in some countries, such as Denmark, it already supplies about half of the electricity. This passage explains how a turbine works, where they are built and what problems the technology still has to solve."""
B = """A modern turbine looks like a tall white tower with three long blades. When the wind blows, the blades, which are shaped like the wings of an aeroplane, are pushed round, turning a shaft inside a housing at the top of the tower, called the nacelle. The shaft is connected to a gearbox, which increases the slow turning of the blades, about fifteen revolutions a minute, to the much faster turning, over a thousand revolutions a minute, that a generator needs. The generator produces electricity, which passes through a transformer and then travels along cables to the grid. Sensors measure the direction of the wind, and motors turn the whole nacelle to face it."""
C = """Size matters. The power in the wind rises very rapidly with its speed: if the wind speed doubles, the power increases eight times. Taller towers reach higher, where the wind is stronger and steadier, and longer blades sweep a larger area. A typical turbine today may stand a hundred metres high, with blades fifty metres long, and a single machine can supply electricity to well over a thousand homes. The largest sea-based turbines are even bigger, taller than a fifty-storey building, with blades that can be as long as a football pitch."""
D = """The best places for wind farms are those where the wind is strong and regular: coasts, open plains, mountain passes and the sea. Offshore wind farms have an advantage, as the wind at sea is stronger and more constant than that on land, and there are fewer people to disturb. But building at sea is more expensive, since the turbines must be fixed to the sea bed or float on platforms, and the repairs require boats. On land, wind farms are cheaper but may meet opposition from local residents, who object to the noise or to the appearance of tall machines on the horizon."""
E = """The most serious problem is that the wind does not blow all the time. On a calm day, a wind farm produces almost nothing, and on a stormy day, turbines must be stopped to prevent damage. The electricity grid has to be balanced from minute to minute, since supply must match demand, so other sources are needed to fill the gaps. Engineers are working on solutions: batteries to store extra power, networks that connect distant regions so that a calm place can borrow from a windy one, and better forecasts of the weather. Another solution is to use surplus electricity to make hydrogen, which can be stored and burnt later."""
F = """Wind farms also affect wildlife. Birds and bats sometimes collide with the blades, although the number killed is much smaller than the number killed by cats, buildings or cars. Careful planning can reduce the risk: turbines are kept away from migration routes and nesting sites, and some are stopped for a short time when radar shows that a flock is approaching. Noise is another complaint, though a modern turbine at a distance of three hundred metres is no louder than a quiet conversation. Dr Fiona Maxwell, an environmental scientist, concludes that the harm caused by wind power is small when compared with the damage caused by coal and oil."""
G = """Many governments plan to expand wind power rapidly. Countries with large open spaces, including several in Central Asia, are building wind farms on plains and deserts where winds blow strongly for most of the year. Turbines are becoming more efficient and cheaper, and the cost of electricity from a good wind farm is now lower than that of a new coal or gas power station in many regions. Dr Maxwell believes that wind will supply a quarter of the world's electricity within a generation, provided that the grids and storage keep pace. She adds that the greatest change must be in attitudes, since people must accept that producing energy is a visible activity, which cannot be hidden."""
S, PT, W, H = chain(4)
P = passage('p86', 'Power from the Wind', 'Technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('People have used the wind for thousands of years.', 'T', 'A', 'thousands of years'),
  ('Denmark gets about half of its electricity from wind.', 'T', 'A', 'about half of the electricity'),
  ('Wind turbines burn fuel.', 'F', 'A', 'without burning any fuel'),
  ('A modern turbine has three blades.', 'T', 'B', 'three long blades'),
  ('The nacelle is at the top of the tower.', 'T', 'B', 'at the top of the tower, called the nacelle'),
  ('If the wind speed doubles, the power doubles.', 'F', 'C', 'the power increases eight times'),
  ('The wind at sea is more constant than on land.', 'T', 'D', 'stronger and more constant'),
  ('A wind farm produces a lot of power on calm days.', 'F', 'E', 'produces almost nothing'),
  ('Wind farms are cheaper than nuclear power stations.', 'NG', 'G', 'lower than that of a new coal or gas power station', 'Nuclear power is not mentioned.'),
 ]),
 mcq([
  ('Why is a gearbox needed?', ['To increase the speed for the generator.', 'To stop the blades.', 'To measure the wind.', 'To store power.'], 0, 'B', 'increases the slow turning of the blades'),
  ('Why are offshore wind farms more expensive?', ['Turbines are fixed to the sea bed and repairs need boats.', 'Wind is weaker.', 'Blades are smaller.', 'There are more people.'], 0, 'D', 'fixed to the sea bed or float on platforms'),
  ('What does Dr Maxwell conclude about the harm of wind power?', ['It is small compared with coal and oil.', 'It is huge.', 'It is increasing.', 'It is unknown.'], 0, 'F', 'small when compared with the damage caused by coal and oil'),
 ]),
 diag('Label the parts of a wind turbine in the order that the energy passes through them. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['blades'], 'B', 'the blades'), (['gearbox'], 'B', 'connected to a gearbox'), (['generator'], 'B', 'The generator produces electricity'), (['transformer'], 'B', 'passes through a transformer')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Feature', 'Detail'],
  [['Blades', 'Turn about fifteen [[1]] a minute'], ['Doubling the wind speed', 'Power increases [[2]] times'], ['Offshore turbines', 'Fixed to the sea [[3]] or float'], ['Surplus electricity', 'Used to make [[4]]']],
  [(['revolutions'], 'B', 'fifteen revolutions a minute'), (['eight'], 'C', 'increases eight times'), (['bed'], 'D', 'sea bed'), (['hydrogen'], 'E', 'make hydrogen')], 1),
 feat('Match each statement with the correct item, A to D.', ['Offshore wind farms', 'Onshore wind farms', 'Batteries', 'Radar'], [
  ('The wind is stronger and more constant there.', 0, 'D', 'stronger and more constant'),
  ('They may meet opposition from local residents.', 1, 'D', 'opposition from local residents'),
  ('They store extra power.', 2, 'E', 'store extra power'),
  ('It shows when a flock of birds is approaching.', 3, 'F', 'a flock is approaching'),
 ]),
 multi('Which TWO solutions to the problem of calm days are mentioned in paragraph E?', ['Batteries to store extra power.', 'Networks connecting distant regions.', 'Larger blades.', 'Stopping all turbines.', 'Burning coal.'], [0, 1], [('E', 'batteries to store extra power'), ('E', 'networks that connect distant regions')]),
 head(['An old force in a new job', 'How a turbine works', 'Big machines, big power', 'Choosing the site', 'When the wind drops', 'Birds, bats and noise', 'A growing future', 'The history of sailing', 'Windmills in art'],
  [('A', 0, 'Today the same force is used to make electricity'), ('B', 1, 'The shaft is connected to a gearbox'), ('C', 2, 'Size matters'), ('D', 3, 'The best places for wind farms'), ('E', 4, 'the wind does not blow all the time'), ('F', 5, 'Birds and bats sometimes collide with the blades'), ('G', 6, 'plan to expand wind power rapidly')]),
 info([
  ('a reference to a gearbox', 'B', 'gearbox'),
  ('a comparison with a tall building', 'C', 'fifty-storey building'),
  ('a reference to floating platforms', 'D', 'float on platforms'),
  ('a reference to hydrogen', 'E', 'make hydrogen'),
  ('a reference to radar', 'F', 'radar shows that a flock is approaching'),
 ]),
 ends(['are shaped like aeroplane wings.', 'reach stronger winds.', 'are more expensive to build.', 'believes wind will supply a quarter of electricity.', 'burn coal.', 'are never noisy.', 'stop birds migrating.'], [
  ('The blades', 0, 'B', 'wings of an aeroplane'),
  ('Taller towers', 1, 'C', 'where the wind is stronger and steadier'),
  ('Offshore farms', 2, 'D', 'more expensive'),
  ('Dr Maxwell', 3, 'G', 'a quarter of the world\'s electricity'),
 ]),
 sent(2, [
  ('The housing at the top of the tower is called the ___.', ['nacelle'], 'B', 'called the nacelle'),
  ('At sea, the wind is stronger and more ___ than on land.', ['constant'], 'D', 'more constant'),
  ('Dr Maxwell is an environmental ___.', ['scientist'], 'F', 'environmental scientist'),
  ('Wind will supply a quarter of the world\'s electricity within a ___.', ['generation'], 'G', 'within a generation'),
 ]),
 short(3, [
  ('How many homes can one turbine supply?', ['over a thousand'], 'C', 'over a thousand homes'),
  ('What do sensors measure?', ['direction'], 'B', 'direction of the wind'),
  ('At what distance is noise compared with a quiet conversation?', ['three hundred metres'], 'F', 'three hundred metres'),
 ]),
])
