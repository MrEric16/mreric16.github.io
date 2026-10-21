from lib import *
from svgs import *
A = """Coffee is one of the most widely traded products in the world, and billions of cups are drunk every day. According to a popular legend, its effect was first noticed in Ethiopia by a goatherd named Kaldi, who saw that his goats became lively after eating the red berries of a certain bush. Whatever the truth of the tale, coffee drinking was well established in the Arab world by the fifteenth century, and the port of Mocha in Yemen gave its name to a famous type of coffee, which is still sold under that name today."""
B = """Coffee grows on evergreen bushes, mostly in a belt around the equator, at heights between six hundred and two thousand metres. The two main species are Arabica, which has a fine flavour and makes up about sixty per cent of the world's coffee, and Robusta, which is stronger, more bitter and easier to grow. A bush begins to bear fruit after about three years. The fruits, called cherries, turn from green to bright red when they are ripe, and a single bush produces enough cherries for about half a kilogram of roasted coffee each year."""
C = """On many farms the harvest is carried out by hand, since the cherries on a bush ripen at different times and must be picked one by one. A good worker can pick between one hundred and two hundred kilograms of cherries in a day. On large, flat plantations, as in Brazil, machines shake the bushes and collect everything at once, which is faster but lowers quality because unripe cherries are included. The choice of method depends on the shape of the land and on the price that the farmer expects to receive."""
D = """After picking, the seeds, which are called beans, must be removed from the fruit. This stage is known as processing, and there are two main methods. In the dry method, the cherries are spread out in the sun for several weeks and turned regularly, and then the dried skin is broken off. In the wet method, the fruit is washed away with water in a machine, and the beans are left to ferment for a day before they are dried. The wet method produces a cleaner and brighter flavour but uses large amounts of water, which can pollute rivers if it is not treated."""
E = """Roasting turns the pale green beans brown and creates the flavour. During roasting, which takes between ten and twenty minutes, the beans reach a temperature of more than two hundred degrees Celsius, and they pop with a sound like popcorn and double in size. A light roast keeps more of the original taste of the bean, while a dark roast has a strong, smoky flavour. Once the beans are roasted they begin to lose their freshness, so many coffee lovers buy whole beans and grind them just before making a drink."""
F = """The final stage is brewing, in which hot water takes the flavour out of ground coffee. There are many methods. An espresso machine forces hot water through finely ground coffee at high pressure, and makes a small, strong cup; filter coffee is made by letting the water drip slowly through a paper filter; and in Turkey and parts of Central Asia, coffee is boiled with the grounds in a small pot with a long handle. The grounds sink to the bottom of the cup, and the drinker must leave the last mouthful."""
G = """Behind the pleasure of a cup of coffee lie serious problems. Most farmers are poor, and receive only a small share of the price that the customer pays in a cafe. Climate change is making some areas too warm for Arabica, and scientists warn that a large part of the land now used for it may become unsuitable within decades. Some companies have therefore begun to pay farmers higher prices for coffee grown in ways that protect the forest, a practice known as fair trade, though critics say that its benefits are limited."""
S, PT, W, H = chain(4)
P = passage('p35', 'From Bean to Cup', 'Food and culture', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The legend says coffee was discovered in Ethiopia.', 'T', 'A', 'first noticed in Ethiopia'),
  ('Mocha takes its name from a type of coffee.', 'F', 'A', 'the port of Mocha in Yemen gave its name to a famous type of coffee'),
  ('Arabica makes up about sixty per cent of the world\'s coffee.', 'T', 'B', 'about sixty per cent of the world\'s coffee'),
  ('Robusta is harder to grow than Arabica.', 'F', 'B', 'easier to grow'),
  ('Cherries turn red when they are ripe.', 'T', 'B', 'bright red when they are ripe'),
  ('Machine harvesting improves the quality of coffee.', 'F', 'C', 'lowers quality'),
  ('The wet method uses a great deal of water.', 'T', 'D', 'uses large amounts of water'),
  ('A dark roast tastes more like the original bean.', 'F', 'E', 'A light roast keeps more of the original taste'),
  ('Espresso is the most popular way of making coffee.', 'NG', 'F', 'An espresso machine forces hot water through finely ground coffee', 'Popularity is not compared.'),
 ]),
 mcq([
  ('Why must cherries often be picked by hand?', ['Machines are expensive.', 'They ripen at different times.', 'They are very small.', 'Workers prefer it.'], 1, 'C', 'ripen at different times'),
  ('Why do many coffee lovers grind beans just before use?', ['Whole beans are cheaper.', 'Roasted beans lose freshness.', 'Grinding is quick.', 'It reduces the smoke.'], 1, 'E', 'they begin to lose their freshness'),
  ('What does fair trade aim to do?', ['Reduce the price of coffee.', 'Pay farmers more for forest-friendly coffee.', 'Ban Robusta.', 'Stop climate change.'], 1, 'G', 'pay farmers higher prices for coffee grown in ways that protect the forest'),
 ]),
 multi('Which TWO methods of making coffee are described in paragraph F?', ['Using an espresso machine.', 'Dripping through a paper filter.', 'Boiling in a large pan.', 'Soaking in cold water.', 'Heating in a microwave.'], [0, 1], [('F', 'An espresso machine forces hot water'), ('F', 'letting the water drip slowly through a paper filter')]),
 head(['A legend and a trade', 'Where and how coffee grows', 'Picking the fruit', 'Separating the seeds', 'Creating the flavour', 'Making the drink', 'The cost of coffee to farmers and nature', 'The history of tea', 'How to open a cafe'],
  [('A', 0, 'According to a popular legend'), ('B', 1, 'Coffee grows on evergreen bushes'), ('C', 2, 'the harvest is carried out by hand'), ('D', 3, 'the seeds, which are called beans, must be removed from the fruit'), ('E', 4, 'Roasting turns the pale green beans brown'), ('F', 5, 'The final stage is brewing'), ('G', 6, 'Behind the pleasure of a cup of coffee lie serious problems')]),
 info([
  ('a reference to a person who noticed animals behaving oddly', 'A', 'a goatherd named Kaldi'),
  ('a reference to the height at which coffee grows', 'B', 'between six hundred and two thousand metres'),
  ('a reference to a country that uses machines to harvest', 'C', 'as in Brazil'),
  ('a comparison of the sound of beans with a snack', 'E', 'a sound like popcorn'),
  ('a place where coffee is boiled with the grounds', 'F', 'in Turkey and parts of Central Asia'),
 ]),
 ends(['are picked by hand one by one.', 'is left to ferment for a day.', 'turns the beans brown.', 'sink to the bottom of the cup.', 'is grown only in Brazil.', 'is made from tea.', 'was invented in Turkey.'], [
  ('Ripe cherries', 0, 'C', 'must be picked one by one'),
  ('In the wet method, the fruit', 1, 'D', 'the beans are left to ferment for a day'),
  ('Roasting', 2, 'E', 'Roasting turns the pale green beans brown'),
  ('In Turkish coffee, the grounds', 3, 'F', 'The grounds sink to the bottom of the cup'),
 ]),
 diag('Label the stages in the journey of coffee. Write ONE WORD from the passage for each answer.', W, H, S, PT,
  [(['picking'], 'D', 'After picking'), (['processing'], 'D', 'known as processing'), (['roasting'], 'E', 'Roasting turns'), (['brewing'], 'F', 'The final stage is brewing')], 1),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Ripe cherries are picked from the [[1]].', 'The seeds, called beans, are removed from the [[2]].', 'The beans are roasted until they turn [[3]].', 'Hot water takes the [[4]] out of the ground coffee.'],
  [(['bush', 'bushes'], 'C', 'the cherries on a bush'), (['fruit'], 'D', 'removed from the fruit'), (['brown'], 'E', 'turns the pale green beans brown'), (['flavour'], 'F', 'takes the flavour out')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Method', 'Detail'],
  [['Dry method', 'Cherries are spread out in the [[1]]'], ['Wet method', 'Beans are left to [[2]] for a day'], ['Light roast', 'Keeps the [[3]] taste of the bean'], ['Fair trade', 'Farmers receive higher [[4]]']],
  [(['sun'], 'D', 'spread out in the sun'), (['ferment'], 'D', 'left to ferment'), (['original'], 'E', 'the original taste'), (['prices'], 'G', 'higher prices')], 1),
 sent(2, [
  ('Mocha is a port in ___.', ['yemen'], 'A', 'Mocha in Yemen'),
  ('A coffee bush begins to bear fruit after about three ___.', ['years'], 'B', 'after about three years'),
  ('During roasting the beans double in ___.', ['size'], 'E', 'double in size'),
  ('Climate change is making some areas too ___ for Arabica.', ['warm'], 'G', 'too warm for Arabica'),
 ]),
 short(4, [
  ('A good worker can pick up to how many kilograms of cherries in a day?', ['two hundred', '200'], 'C', 'between one hundred and two hundred kilograms'),
  ('What can the wet method pollute?', ['rivers'], 'D', 'pollute rivers'),
  ('How long does roasting take?', ['ten and twenty minutes', 'twenty minutes'], 'E', 'between ten and twenty minutes'),
 ]),
])
