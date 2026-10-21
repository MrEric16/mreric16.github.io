from lib import *
from svgs import *
A = """Every building uses energy, but the amount and the purpose differ greatly between types of building. The imaginary country of Altonia carried out a national survey last year to find out where its energy goes, with the aim of deciding where savings would be easiest. Inspectors visited thousands of homes, offices, factories and hospitals and measured how much power each used for heating, lighting, machinery and other purposes. The results were published as a set of charts, and they surprised many officials, who had expected the factories to be the main concern. This passage describes the findings and what they mean for the country's plans to cut its energy bills."""
B = """In homes, the picture is simple. About half of all the energy used goes on heating rooms and water, because winters in Altonia are long and cold. Lighting and cooking each take a smaller share, and the remainder is used by televisions, computers and other equipment that people plug in. The survey found that houses built before 1980 use nearly twice as much heat as modern ones, because their walls and roofs are thin and their windows let the warmth escape. Inspectors also found that a surprising number of families leave heating on when they are out all day, which wastes money without making anyone more comfortable at home."""
C = """Offices are different. Energy there is shared almost equally among four uses: heating, lighting, computers and air-conditioning. Because the shares are so even, there is no single obvious saving, and managers must work on all four fronts at once. Many offices leave lights and computers running overnight, and the survey estimates that switching them off would cut the average bill by about a tenth. Some firms have installed sensors that turn off the lights in empty rooms, and others allow staff to work from home on certain days, which reduces the need to heat and light the building at all."""
D = """Factories were expected to be the largest users, and in total they are, but the survey revealed something unexpected. In a typical factory, more than two thirds of the energy goes into running machinery, while heating, lighting and offices share the rest. This means that the biggest savings can be made by replacing old machines with efficient ones, a change which pays for itself in a few years. Engineers also discovered that many machines were left running while idle, simply because switching them on and off was thought to be troublesome. Modern equipment can slow down automatically when there is no work to do, and several factories report savings of up to a fifth."""
E = """Hospitals have unusual needs. They must be warm, brightly lit and ready to work at every hour of the day and night, and so heating and medical equipment each use just under half of the energy, with a small remainder going to lighting and kitchens. Savings are difficult, because patients' safety must never be put at risk. Dr Marta Kowalczyk, an energy engineer who led the hospital part of the survey, found that the most promising approach was to recover the heat produced by machines such as scanners and refrigerators and to use it to warm the wards, which cut one hospital's gas bill by about a quarter."""
F = """The government has used the findings to draw up a plan with three parts. First, it will give grants to families who add insulation to older homes. Second, it will require large offices to install sensors and timers within five years. Third, it will offer cheap loans to factories that replace old machines. Officials estimate that together these measures could reduce the country's total energy use by eight per cent within a decade. Critics reply that the target is modest, but supporters say that a realistic goal is better than a bold one that cannot be reached, and that further steps can follow once these have succeeded."""
G = """Experts believe that people's behaviour will matter as much as new equipment. Studies in other countries suggest that households which receive a monthly report comparing their energy use with that of their neighbours reduce their consumption by about two per cent, with no cost at all. Altonia plans to test the idea in three towns next winter. Meanwhile, the survey itself will be repeated every five years, so that officials can check whether the savings are real. If the results are encouraging, the government hopes to extend the programme to schools and shops, which were not included in the first survey for lack of money."""
P = passage('p62', 'Where the Energy Goes', 'Environment', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which pie chart, A to D, shows the use of energy in each type of building described in the passage?', [(pie([50, 20, 15, 15]), 160, 120), (pie([25, 25, 25, 25]), 160, 120), (pie([70, 10, 10, 10]), 160, 120), (pie([45, 45, 10]), 160, 120)], [
  ('homes', 0, 'B', 'About half of all the energy used goes on heating'),
  ('offices', 1, 'C', 'shared almost equally among four uses'),
  ('factories', 2, 'D', 'more than two thirds of the energy goes into running machinery'),
  ('hospitals', 3, 'E', 'heating and medical equipment each use just under half of the energy'),
 ]),
 tfng([
  ('Altonia is an imaginary country.', 'T', 'A', 'The imaginary country of Altonia'),
  ('The survey was carried out last year.', 'T', 'A', 'last year'),
  ('Officials had expected factories to be the main concern.', 'T', 'A', 'expected the factories to be the main concern'),
  ('Winters in Altonia are short and mild.', 'F', 'B', 'long and cold'),
  ('Houses built before 1980 use nearly twice as much heat as modern ones.', 'T', 'B', 'nearly twice as much heat as modern ones'),
  ('Switching off lights and computers overnight would cut the average office bill by about a tenth.', 'T', 'C', 'cut the average bill by about a tenth'),
  ('Many factory machines were left running while idle.', 'T', 'D', 'many machines were left running while idle'),
  ('Hospitals use more energy in total than factories.', 'NG', 'E', 'Hospitals have unusual needs', 'Total use is not compared.'),
  ('The government will require large offices to install sensors.', 'T', 'F', 'require large offices to install sensors and timers within five years'),
 ]),
 mcq([
  ('Why is there no single obvious saving in offices?', ['Offices are small.', 'The shares of energy are so even.', 'Workers dislike change.', 'Machines are old.'], 1, 'C', 'Because the shares are so even'),
  ('What did Dr Kowalczyk find most promising?', ['Closing wards.', 'Recovering heat from machines.', 'Using less light.', 'Cheaper gas.'], 1, 'E', 'recover the heat produced by machines'),
  ('What do supporters of the plan say?', ['It is too bold.', 'A realistic goal is better than a bold one.', 'It costs nothing.', 'It should be cancelled.'], 1, 'F', 'a realistic goal is better than a bold one'),
 ]),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Building', 'Main use'],
  [['Homes', 'Heating rooms and [[1]]'], ['Offices', 'Heating, lighting, computers and [[2]]'], ['Factories', 'Running [[3]]'], ['Hospitals', 'Heating and medical [[4]]']],
  [(['water'], 'B', 'heating rooms and water'), (['air-conditioning'], 'C', 'air-conditioning'), (['machinery'], 'D', 'running machinery'), (['equipment'], 'E', 'medical equipment')], 2),
 multi('Which TWO measures in the government plan are mentioned in paragraph F?', ['Grants for insulation in older homes.', 'Sensors and timers in large offices.', 'Free cars for families.', 'New power stations.', 'Taxes on families.'], [0, 1], [('F', 'give grants to families who add insulation to older homes'), ('F', 'require large offices to install sensors and timers')]),
 head(['A national survey', 'Warmth at home', 'Even shares in the office', 'The importance of machines', 'Special demands of medical buildings', 'A three-part plan', 'Changing habits', 'The history of electricity', 'Cheap ways to travel'],
  [('A', 0, 'carried out a national survey'), ('B', 1, 'About half of all the energy used goes on heating'), ('C', 2, 'shared almost equally among four uses'), ('D', 3, 'more than two thirds of the energy goes into running machinery'), ('E', 4, 'Hospitals have unusual needs'), ('F', 5, 'a plan with three parts'), ('G', 6, 'people\'s behaviour will matter as much as new equipment')]),
 info([
  ('a reference to windows letting heat escape', 'B', 'windows let the warmth escape'),
  ('a mention of sensors for empty rooms', 'C', 'turn off the lights in empty rooms'),
  ('a claim about savings of up to a fifth', 'D', 'savings of up to a fifth'),
  ('a reference to scanners and refrigerators', 'E', 'scanners and refrigerators'),
  ('a plan to test an idea in several towns', 'G', 'three towns next winter'),
 ]),
 sent(2, [
  ('The survey was carried out in the imaginary country of ___.', ['altonia'], 'A', 'Altonia'),
  ('In homes, lighting and ___ each take a smaller share.', ['cooking'], 'B', 'Lighting and cooking'),
  ('Dr Kowalczyk is an energy ___.', ['engineer'], 'E', 'energy engineer'),
  ('The survey will be repeated every ___ years.', ['five', '5'], 'G', 'every five years'),
 ]),
 short(3, [
  ('By how much could total energy use fall within a decade?', ['eight per cent'], 'F', 'eight per cent'),
  ('What will cheap loans help factories replace?', ['old machines'], 'F', 'replace old machines'),
  ('Which buildings were left out of the first survey?', ['schools and shops'], 'G', 'schools and shops'),
 ]),
])
