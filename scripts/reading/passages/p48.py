from lib import *
from svgs import *
A = """Every minute, about a million plastic bottles are bought around the world, and most of them are used once and then thrown away. Yet a plastic bottle can be given a second life. The plastic most commonly used for drinks bottles is called PET, short for polyethylene terephthalate, and it is one of the easiest plastics to recycle. The process that turns an old bottle into a new product has five main stages, which are carried out in special factories that now operate in most large countries. A modern plant can handle more than ten thousand tonnes of bottles in a year, and some of the largest are located close to the cities that supply their raw material, which reduces the cost and the pollution of transport."""
B = """The process begins with collection. In many cities, households put empty bottles into special bins, which are emptied by the council, while in some countries shops take back bottles and pay a small deposit to the customer. Such deposit schemes work well: in Germany, about ninety-eight per cent of bottles that carry a deposit are returned. Collected bottles are pressed into large blocks called bales, so that they can be transported cheaply to the recycling factory."""
C = """At the factory, the bales are broken open and the bottles pass through sorting. Machines with infrared sensors identify the type of plastic by the way it reflects light, and jets of air blow the wrong types onto a different belt. Workers standing beside the belt remove anything that the machines have missed, such as metal, glass and bottles of the wrong colour. Clear plastic is worth more than coloured plastic, so the bottles are separated by colour as well as by type."""
D = """The next stage is shredding. The sorted bottles are fed into a machine with sharp rotating blades, which cuts them into small pieces called flakes, each about the size of a fingernail. Shredding makes the plastic easier to clean and to melt, and it also reduces the amount of space that the material takes up. The noise in the shredding hall is so great that workers must wear ear protection, and the machines are cooled with water to stop the blades overheating."""
E = """Washing follows. The flakes are placed in tanks of hot water and detergent, which remove labels, glue and the remains of drinks. The flakes are then stirred in a second tank in which the PET sinks while the lids, which are made of a different plastic, float to the top and can be skimmed off. This simple method of separating materials by density is very efficient. The clean flakes are then dried with hot air before being sent to the last stage."""
F = """The final stage is melting. The dry flakes are heated to about 250 degrees Celsius and pushed through a fine filter to remove any remaining impurities. The liquid plastic is then cut into small pellets, which are sold to manufacturers. Some of the pellets are used to make new bottles, but many are spun into fibre for clothes, such as fleece jackets, or for carpets and bags. A fleece jacket may contain the plastic of a few dozen recycled bottles."""
G = """Recycling is helpful, but it is not a complete solution. Only a small share of all the plastic ever produced has been recycled, and the quality of the material gets worse each time, so that bottles cannot be recycled for ever. Dr Hiroshi Tanabe, a materials scientist, says that the best answer is to use less plastic in the first place, for example by choosing refillable bottles, and to treat recycling as a second line of defence instead of the first."""
S, PT, W, H = chain(5)
P = passage('p48', 'A Second Life for Plastic Bottles', 'Environment', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('PET is a plastic used for drinks bottles.', 'T', 'A', 'most commonly used for drinks bottles'),
  ('PET is very difficult to recycle.', 'F', 'A', 'one of the easiest plastics to recycle'),
  ('The recycling process has five stages.', 'T', 'A', 'five main stages'),
  ('In Germany most bottles with a deposit are returned.', 'T', 'B', 'about ninety-eight per cent'),
  ('Bales are blocks of pressed bottles.', 'T', 'B', 'pressed into large blocks called bales'),
  ('Machines identify plastic by the way it reflects light.', 'T', 'C', 'by the way it reflects light'),
  ('Coloured plastic is worth more than clear plastic.', 'F', 'C', 'Clear plastic is worth more than coloured plastic'),
  ('The flakes are the size of a coin.', 'NG', 'D', 'each about the size of a fingernail', 'A fingernail is mentioned, but no comparison with a coin.'),
  ('Lids float in the washing tank.', 'T', 'E', 'the lids, which are made of a different plastic, float'),
 ]),
 mcq([
  ('Why are bottles separated by colour?', ['Colour affects the smell.', 'Clear plastic is worth more.', 'Coloured plastic melts faster.', 'Machines cannot see clear plastic.'], 1, 'C', 'Clear plastic is worth more than coloured plastic'),
  ('Why is shredding done?', ['To make the plastic cleaner and easier to melt.', 'To remove metal.', 'To add colour.', 'To print labels.'], 0, 'D', 'easier to clean and to melt'),
  ('What does Dr Tanabe say is the best answer?', ['Using less plastic.', 'Burning plastic.', 'Burying plastic.', 'Recycling more often.'], 0, 'G', 'use less plastic in the first place'),
 ]),
 multi('Which TWO things does a deposit scheme involve, according to paragraph B?', ['Shops take back bottles.', 'Customers receive a small payment.', 'Bottles are burned.', 'Bottles are shipped abroad.', 'Customers pay extra tax.'], [0, 1], [('B', 'shops take back bottles'), ('B', 'pay a small deposit to the customer')]),
 head(['A bottle\'s second chance', 'Gathering the bottles', 'Finding the right plastic', 'Cutting into small pieces', 'Cleaning the pieces', 'Making new products', 'The limits of recycling', 'The history of glass', 'The cost of oil'],
  [('A', 0, 'a plastic bottle can be given a second life'), ('B', 1, 'The process begins with collection'), ('C', 2, 'the bottles pass through sorting'), ('D', 3, 'The next stage is shredding'), ('E', 4, 'Washing follows'), ('F', 5, 'The final stage is melting'), ('G', 6, 'Recycling is helpful, but it is not a complete solution')]),
 info([
  ('a figure for the number of bottles bought every minute', 'A', 'about a million plastic bottles'),
  ('a reference to a use for compressed bottles', 'B', 'transported cheaply to the recycling factory'),
  ('a reference to the use of air', 'C', 'jets of air'),
  ('a reference to protection for workers\' ears', 'D', 'ear protection'),
  ('an example of a product made from fibre', 'F', 'fleece jackets'),
 ]),
 ends(['are collected in special bins.', 'identify plastic by the way it reflects light.', 'cut the bottles into flakes.', 'float to the top of the tank.', 'is the largest plastic in the world.', 'are made of glass.', 'melt at room temperature.'], [
  ('Households put bottles', 0, 'B', 'put empty bottles into special bins'),
  ('Infrared sensors', 1, 'C', 'identify the type of plastic by the way it reflects light'),
  ('Rotating blades', 2, 'D', 'cuts them into small pieces called flakes'),
  ('Lids', 3, 'E', 'float to the top'),
 ]),
 diag('Label the stages of recycling a plastic bottle. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['collection'], 'B', 'The process begins with collection'), (['sorting'], 'C', 'pass through sorting'), (['shredding'], 'D', 'The next stage is shredding'), (['washing'], 'E', 'Washing follows'), (['melting'], 'F', 'The final stage is melting')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Bottles are pressed into [[1]] and taken to the factory.', 'Machines with [[2]] sensors identify the type of plastic.', 'Blades cut the bottles into [[3]].', 'The dry flakes are [[4]] and made into pellets.'],
  [(['bales'], 'B', 'called bales'), (['infrared'], 'C', 'infrared sensors'), (['flakes'], 'D', 'called flakes'), (['heated', 'melted'], 'F', 'heated to about 250 degrees')], 1),
 sent(2, [
  ('PET is short for polyethylene ___.', ['terephthalate'], 'A', 'polyethylene terephthalate'),
  ('Workers remove metal and ___ from the belt.', ['glass'], 'C', 'metal, glass'),
  ('The flakes are dried with hot ___.', ['air'], 'E', 'dried with hot air'),
  ('Dr Tanabe is a materials ___.', ['scientist'], 'G', 'a materials scientist'),
 ]),
 short(3, [
  ('At what temperature are the flakes heated?', ['250 degrees', '250 degrees celsius', 'about 250 degrees'], 'F', 'about 250 degrees Celsius'),
  ('What is the liquid plastic cut into?', ['pellets', 'small pellets'], 'F', 'cut into small pellets'),
  ('What does Dr Tanabe recommend, for example?', ['refillable bottles'], 'G', 'refillable bottles'),
 ]),
])
