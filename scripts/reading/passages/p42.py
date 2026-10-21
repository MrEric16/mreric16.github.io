from lib import *
from svgs import *
A = """Every country must decide how to produce the energy that it needs, and the choices that it makes tend to change over time. This passage describes the history of energy in the imaginary country of Calderia, from 1970 to the present. It deals with four sources: solar power, coal, oil and natural gas. Each source followed its own path, and together they show how technology, price and politics shape the way that a nation lights its cities and runs its factories. Calderia is a medium-sized country of about twenty million people, with long winters in the north and a hot, dry climate in the south, so its energy needs vary a great deal from region to region and from season to season."""
B = """Solar power has the most dramatic story. For years it contributed almost nothing, because panels were costly and poorly made. After 2005 the price of a panel began to fall, and a government scheme paid homeowners for the electricity they fed into the grid. Production has risen every year since, and solar now provides more than a fifth of Calderia's electricity. Engineers expect the figure to keep climbing for the foreseeable future."""
C = """Coal, by contrast, has fallen steadily. In 1970 it produced almost two-thirds of the nation's power, but its share has dropped decade after decade as mines were closed and power stations were switched to cleaner fuels. The last large coal station is due to shut within five years. The decline has hurt the mining towns of the north, where thousands of workers have lost their jobs and where unemployment remains high."""
D = """Oil followed a pattern with a peak. After the discovery of large deposits near the coast in the 1970s, production climbed quickly and reached its highest level in 1995. Then the wells began to run dry, and output fell year after year. Although the country once exported oil, it is now a net importer, and its economy is therefore more sensitive to changes in world prices than it was in the past. Economists in the capital warn that this makes it difficult to plan the national budget, since the price of imported oil can change by thirty per cent in a single year."""
E = """Natural gas has behaved differently again. Its use rose rapidly in the 1980s and 1990s, when pipes were laid to bring it to homes and factories, and then it levelled off. Since the year 2000 the amount has hardly changed. Gas is cleaner than coal, but the country's reserves are limited, and the government has chosen not to expand it further, since it prefers to invest in renewable energy."""
F = """What lies behind the differences? Dr Farid Haddad, an energy economist, identifies three main factors. The first is the cost of the technology: solar panels became cheaper, while new coal stations became more expensive to build and operate. The second is government policy, which has favoured clean energy in the last twenty years. The third is geology, since oil and gas depend on reserves that are limited by nature. He adds that none of these factors is permanent, and that forecasts must be revised often."""
G = """Looking ahead, Calderia's planners hope to cut the nation's carbon emissions by half within twenty years. This will require not only more solar panels but also better ways of storing electricity, so that the sun's energy can be used at night and on cloudy days. Large batteries are already being installed beside the biggest solar farms, and a pilot project is testing the use of surplus power to produce hydrogen. Success is not certain, but few experts doubt that the direction of travel is clear."""
P = passage('p42', 'Energy in Calderia', 'Environment', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the history of each energy source described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('plateau'), 160, 120)], [
  ('solar power', 0, 'B', 'Production has risen every year since'),
  ('coal', 1, 'C', 'has fallen steadily'),
  ('oil', 2, 'D', 'reached its highest level in 1995'),
  ('natural gas', 3, 'E', 'then it levelled off'),
 ]),
 tfng([
  ('Calderia is a real country.', 'F', 'A', 'the imaginary country of Calderia'),
  ('The passage deals with four energy sources.', 'T', 'A', 'It deals with four sources'),
  ('Calderia has more wind farms than solar farms.', 'NG', 'G', 'more solar panels but also better ways of storing electricity', 'Wind power is not discussed in the passage.'),
  ('Solar panels were cheap in the early years.', 'F', 'B', 'panels were costly and poorly made'),
  ('Solar power now provides more than a fifth of the electricity.', 'T', 'B', 'more than a fifth of Calderia\'s electricity'),
  ('Coal produced about two-thirds of power in 1970.', 'T', 'C', 'almost two-thirds of the nation\'s power'),
  ('Unemployment in the northern mining towns is low.', 'F', 'C', 'unemployment remains high'),
  ('Oil production peaked in 1995.', 'T', 'D', 'highest level in 1995'),
  ('Calderia is now a net exporter of oil.', 'F', 'D', 'it is now a net importer'),
  ('Natural gas will be expanded in the coming years.', 'F', 'E', 'the government has chosen not to expand it further'),
 ]),
 mcq([
  ('Why did the price of solar panels matter?', ['It decided where they were built.', 'Falling prices helped solar to grow.', 'It affected coal prices.', 'It lowered taxes.'], 1, 'B', 'the price of a panel began to fall'),
  ('What hurt the mining towns?', ['The closing of coal mines.', 'Oil prices.', 'Solar farms.', 'Gas pipes.'], 0, 'C', 'as mines were closed'),
  ('What does Dr Haddad say about his three factors?', ['They are permanent.', 'None is permanent.', 'Only policy matters.', 'They explain gas only.'], 1, 'F', 'none of these factors is permanent'),
 ]),
 multi('Which TWO factors behind the differences are named by Dr Haddad?', ['The cost of the technology.', 'Government policy.', 'The weather.', 'The size of the population.', 'The price of food.'], [0, 1], [('F', 'The first is the cost of the technology'), ('F', 'The second is government policy')]),
 head(['Introduction to the question', 'A rapid rise', 'A long decline', 'A rise, a peak and a fall', 'A rise followed by stability', 'Why the sources differ', 'Targets and technology for the future', 'The history of the wheel', 'How batteries are made'],
  [('A', 0, 'This passage describes the history of energy'), ('B', 1, 'Solar power has the most dramatic story'), ('C', 2, 'Coal, by contrast, has fallen steadily'), ('D', 3, 'Oil followed a pattern with a peak'), ('E', 4, 'Natural gas has behaved differently again'), ('F', 5, 'What lies behind the differences'), ('G', 6, 'Looking ahead, Calderia\'s planners')]),
 info([
  ('a mention of a government scheme to pay homeowners', 'B', 'paid homeowners for the electricity they fed into the grid'),
  ('a reference to the closing of the last large coal station', 'C', 'due to shut within five years'),
  ('a reference to a changed export position', 'D', 'a net importer'),
  ('a comparison of gas with coal', 'E', 'Gas is cleaner than coal'),
  ('a mention of an experiment with hydrogen', 'G', 'to produce hydrogen'),
 ]),
 ends(['has fallen steadily since 1970.', 'was paid for by a government scheme.', 'reached its highest level in 1995.', 'hardly changed after 2000.', 'is the cheapest fuel of all.', 'was banned in 1970.', 'comes only from the north.'], [
  ('The share of coal', 0, 'C', 'Coal, by contrast, has fallen steadily'),
  ('Electricity from household panels', 1, 'B', 'paid homeowners for the electricity they fed into the grid'),
  ('Oil production', 2, 'D', 'reached its highest level in 1995'),
  ('The use of natural gas', 3, 'E', 'Since the year 2000 the amount has hardly changed'),
 ]),
 sent(2, [
  ('Solar panels were once costly and poorly ___.', ['made'], 'B', 'costly and poorly made'),
  ('Coal stations were switched to cleaner ___.', ['fuels'], 'C', 'switched to cleaner fuels'),
  ('Oil wells began to run ___.', ['dry'], 'D', 'began to run dry'),
  ('Large ___ are being installed beside solar farms.', ['batteries'], 'G', 'Large batteries'),
 ]),
 short(3, [
  ('What is Dr Haddad\'s speciality?', ['energy economist', 'an energy economist'], 'F', 'an energy economist'),
  ('How much do planners want to cut emissions?', ['by half', 'half'], 'G', 'by half'),
  ('Where were the large oil deposits found?', ['near the coast', 'coast'], 'D', 'near the coast'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Solar power rose after the price of panels began to [[1]], while coal has [[2]] steadily as mines closed. Oil reached a [[3]] in 1995, and gas [[4]] off after 2000.',
  [(['fall'], 'B', 'began to fall'), (['fallen'], 'C', 'has fallen steadily'), (['peak'], 'D', 'a peak'), (['levelled'], 'E', 'levelled off')], 1,
  bank=['fall', 'fallen', 'peak', 'levelled', 'rose', 'gas', 'water', 'exports']),
])
