from lib import *
from svgs import *
A = """Prices tell a story about an economy, and the prices in the imaginary country of Calderia, recorded every month for ten years by the national statistics office, tell several stories at once. Some goods have become steadily more expensive, some have become cheaper, and some have moved up and down without any clear direction. Economists study such patterns in order to understand why prices change, and shoppers study them in order to decide when to buy. This passage looks at four goods in the office's records: tomatoes, petrol, bread and laptop computers. Each follows its own pattern, and the reasons for each are quite different."""
B = """The price of tomatoes goes up and down all the time. It is lowest in late summer, when the harvest is large and the shops are full of fruit grown in the open air, and highest in winter, when tomatoes must be grown in heated greenhouses or brought from abroad. Over the ten years there was no real upward or downward trend, only a regular rise and fall with the seasons, and occasional sudden jumps after bad weather destroyed crops. Shoppers who want to save money have learned to buy in bulk when prices are low and to preserve the fruit in jars for the colder months."""
C = """Petrol was cheap and stable for most of the period. For seven years its price hardly moved, and drivers grew used to filling their tanks without thinking about the cost. Then, in the eighth year, the price rose sharply, after a war in a distant oil-producing region cut supplies, and within eighteen months it had almost doubled. It has since crept up a little further. The effect on the economy was immediate: transport companies raised their charges, and the prices of many other goods followed, which shows how much modern life depends on the cost of fuel."""
D = """The price of bread followed another pattern. It rose quickly during the first four years, as the cost of wheat, flour and energy increased, and then it reached a level at which it stayed. The government, worried that poor families could not afford their daily bread, froze the price and paid bakers a subsidy to cover the difference. The policy has been popular, but it is expensive, costing the treasury about the same each year as the building of a hundred new schools. Some economists argue that the money would be better spent giving direct help to poor families, rather than keeping the price of one product artificially low."""
E = """Laptop computers have become cheaper, but the fall came suddenly, not gradually. For the first six years, their price stayed almost the same, because only two companies sold them in the country, and neither wanted to start a price war. Then a new factory opened in the south, and several foreign makers entered the market. Within a few months, the average price fell by nearly half, and it has stayed at the lower level ever since. Competition, in other words, can change a market far more quickly than any government order, which is a lesson that economists often repeat."""
F = """Dr Anita Rossi, a professor of economics, says that the four cases illustrate the main forces behind prices: the seasons, supply, government decisions and competition. When supply is limited, as with petrol after the war, prices rise; when many sellers compete, as with laptops, they fall. She warns, however, that people often misunderstand the pattern they see. A rise in the price of a single product, she says, is not inflation, which is a general rise in the cost of living, and a fall in one price does not always mean that people are better off, since the money saved may be lost somewhere else in the economy."""
G = """The statistics office has recently made its figures available to the public on a website, and thousands of people now use them. Teachers use the charts in lessons, journalists use them in articles, and ordinary families use them to plan their budgets. The office's director says that the aim is to make economics less mysterious: when citizens can see for themselves how prices move, he argues, they are less likely to be misled by rumours or by claims made in advertisements. Next year the website will add figures for wages, so that visitors can compare the cost of goods with the amount of money that people actually earn."""
P = passage('p63', 'The Shape of Prices', 'Economics', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the price trend of each product described in the passage?', [(graph('fluct'), 160, 120), (graph('sharp'), 160, 120), (graph('plateau'), 160, 120), (graph('drop'), 160, 120)], [
  ('tomatoes', 0, 'B', 'goes up and down all the time'),
  ('petrol', 1, 'C', 'the price rose sharply'),
  ('bread', 2, 'D', 'it reached a level at which it stayed'),
  ('laptops', 3, 'E', 'fell by nearly half'),
 ]),
 tfng([
  ('Calderia is an imaginary country.', 'T', 'A', 'imaginary country of Calderia'),
  ('The records cover ten years.', 'T', 'A', 'ten years'),
  ('Tomatoes are cheapest in winter.', 'F', 'B', 'lowest in late summer'),
  ('Tomato prices showed no real upward or downward trend.', 'T', 'B', 'no real upward or downward trend'),
  ('Petrol was cheap and stable for most of the period.', 'T', 'C', 'Petrol was cheap and stable for most of the period'),
  ('The price of petrol almost doubled within eighteen months.', 'T', 'C', 'within eighteen months it had almost doubled'),
  ('The government froze the price of bread.', 'T', 'D', 'froze the price'),
  ('The bread subsidy costs more than the army.', 'NG', 'D', 'costing the treasury', 'The army is not mentioned.'),
  ('Only two companies sold laptops at first.', 'T', 'E', 'only two companies sold them in the country'),
 ]),
 mcq([
  ('Why did the government freeze the price of bread?', ['Wheat was cheap.', 'Poor families could not afford it.', 'Bakers asked for it.', 'Exports fell.'], 1, 'D', 'worried that poor families could not afford their daily bread'),
  ('What caused the fall in laptop prices?', ['A tax cut.', 'A new factory and foreign makers.', 'A war.', 'Bad weather.'], 1, 'E', 'a new factory opened in the south'),
  ('According to Dr Rossi, what is inflation?', ['A fall in one price.', 'A general rise in the cost of living.', 'A seasonal change.', 'A government subsidy.'], 1, 'F', 'a general rise in the cost of living'),
 ]),
 feat('Match each statement with the correct product, A to D.', ['Tomatoes', 'Petrol', 'Bread', 'Laptops'], [
  ('Its price changes with the seasons.', 0, 'B', 'regular rise and fall with the seasons'),
  ('Its price rose after a war cut supplies.', 1, 'C', 'cut supplies'),
  ('Bakers receive a subsidy for it.', 2, 'D', 'paid bakers a subsidy'),
  ('Competition made its price fall.', 3, 'E', 'several foreign makers entered the market'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Product', 'Detail'],
  [['Tomatoes', 'Prices are lowest in late [[1]]'], ['Petrol', 'The price rose after a [[2]] cut supplies'], ['Bread', 'The government froze the [[3]]'], ['Laptops', 'A new [[4]] opened in the south']],
  [(['summer'], 'B', 'late summer'), (['war'], 'C', 'after a war in a distant oil-producing region'), (['price'], 'D', 'froze the price'), (['factory'], 'E', 'a new factory opened')], 1),
 multi('Which TWO users of the statistics office\'s figures are mentioned in paragraph G?', ['Teachers.', 'Journalists.', 'Police officers.', 'Farmers.', 'Sailors.'], [0, 1], [('G', 'Teachers use the charts in lessons'), ('G', 'journalists use them in articles')]),
 head(['Prices and their stories', 'Ups and downs with the seasons', 'A sudden and lasting rise', 'Rapid growth, then a fixed level', 'A fall caused by competition', 'The forces behind prices', 'Figures for everyone', 'The history of money', 'How to cook with tomatoes'],
  [('A', 0, 'tell several stories at once'), ('B', 1, 'regular rise and fall with the seasons'), ('C', 2, 'Then, in the eighth year, the price rose sharply'), ('D', 3, 'It rose quickly during the first four years'), ('E', 4, 'Competition, in other words'), ('F', 5, 'the main forces behind prices'), ('G', 6, 'made its figures available to the public on a website')]),
 info([
  ('a reference to greenhouses', 'B', 'heated greenhouses'),
  ('a reference to drivers not worrying about cost', 'C', 'without thinking about the cost'),
  ('a comparison with the cost of schools', 'D', 'a hundred new schools'),
  ('a mention of a price war', 'E', 'a price war'),
  ('a plan to publish figures about earnings', 'G', 'figures for wages'),
 ]),
 ends(['change with the seasons.', 'rose after supplies were cut.', 'receive money from the government.', 'has published its figures on a website.', 'sell computers only.', 'grow wheat abroad.', 'raise petrol prices every year.'], [
  ('Tomato prices', 0, 'B', 'regular rise and fall with the seasons'),
  ('The price of petrol', 1, 'C', 'cut supplies'),
  ('Bakers', 2, 'D', 'paid bakers a subsidy'),
  ('The statistics office', 3, 'G', 'available to the public on a website'),
 ]),
 sent(2, [
  ('The records were made by the national ___ office.', ['statistics'], 'A', 'statistics office'),
  ('In winter, tomatoes must be grown in heated ___.', ['greenhouses'], 'B', 'heated greenhouses'),
  ('Dr Rossi is a ___ of economics.', ['professor'], 'F', 'a professor of economics'),
  ('The website will add figures for ___ next year.', ['wages'], 'G', 'figures for wages'),
 ]),
 short(3, [
  ('How long did petrol prices stay stable?', ['seven years'], 'C', 'seven years'),
  ('Where did the new factory open?', ['the south', 'south'], 'E', 'in the south'),
  ('What is a general rise in the cost of living?', ['inflation'], 'F', 'inflation'),
 ]),
])
