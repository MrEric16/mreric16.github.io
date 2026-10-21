from lib import *
A = """Every day, in most parts of the world, the sea rises and falls twice. The force behind this movement is the gravity of the Moon and, to a lesser extent, the Sun, and it is so regular that tide tables can be printed years in advance. Engineers have long been tempted by the idea of capturing that energy because, unlike wind or sunshine, the tides never fail to arrive. The difficulty has always been the price."""
B = """The oldest method is the tidal barrage, a long wall built across the mouth of an estuary. The world's first large tidal power station, on the Rance estuary in France, opened in 1966 and is still in operation. A barrage works in a series of stages. At high tide, sluice gates in the wall are opened and seawater flows into a basin behind it. The gates are then closed, trapping the water as the tide falls outside. When the difference in water level is great enough, the trapped water is released through turbines built into the barrage. The moving water spins the turbine blades, which drive a generator, and the electricity it produces is fed into the national grid."""
C = """Barrages can generate large amounts of power, but they have serious drawbacks. A wall across an estuary changes the way water, mud and sand move through it, and can damage the feeding grounds of wading birds. Fish may be injured by the turbines or blocked from reaching their spawning rivers. The construction costs are also enormous, and many projects have been cancelled before a single stone was laid. A station that opened at Sihwa Lake in South Korea in 2011 avoided some of these problems because it was built into a seawall that already existed, which kept costs down and prevented new damage."""
D = """A second approach is the tidal lagoon, a curved wall built out from the shore in shallow water. Because it encloses an area of open sea rather than blocking a river, it interferes less with the natural flow of water. Supporters say lagoons could also be used to protect coastlines from flooding. Critics reply that electricity from the first lagoon proposed in Britain would have cost more than electricity from a new nuclear plant, and in 2018 the government declined to support it."""
E = """The newest and most promising technology is the tidal stream turbine, which resembles an underwater wind turbine. Fixed to the seabed in channels where the current is strong, its blades turn as the water flows past, in both directions. Since water is roughly 800 times denser than air, a blade can be much shorter than the blade of a wind turbine and still produce the same power. A group of these machines off the north coast of Scotland has been supplying electricity since 2016."""
F = """Developers face challenges, though. Seawater corrodes metal, and storms can damage equipment that is difficult to reach for repairs. Installing a turbine in a fast channel requires specialised vessels, which can work only during the short periods when the water is almost still. Early prototypes failed because their blades were damaged by floating debris, and the companies that built them lost their investors' money. Each failure made funding harder to obtain."""
G = """Even so, many experts believe tidal power will find a place in the energy mix. Its great advantage is that it is predictable: a grid operator knows exactly when output will rise and fall and can plan around it, whereas the output of wind power has to be forecast. Costs are expected to fall as more turbines are built, as happened with solar panels and wind farms. Nobody expects the tides to supply more than a modest share of any country's electricity, but as a steady partner to other renewable sources they may prove very valuable."""
SVG = ('<rect class="w" x="10" y="70" width="210" height="170"/><rect class="w" x="300" y="70" width="210" height="170"/>'
 '<rect class="s" x="0" y="240" width="520" height="20"/><rect class="s" x="220" y="40" width="80" height="200"/>'
 '<rect class="f" x="222" y="150" width="76" height="40"/><circle class="c" cx="260" cy="170" r="16"/><path class="l" d="M244 170h32M260 154v32"/>'
 '<rect class="c" x="225" y="80" width="12" height="50"/><rect class="f" x="245" y="12" width="30" height="26"/><path class="l" d="M260 38V154"/>'
 '<path class="l" d="M275 25H317M225 105L163 110M244 170L163 200M300 60L372 52"/><text x="75" y="175">Sea</text>')
P = passage('p02', 'Harnessing the Tides', 'Energy', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The Moon is the only cause of the tides.', 'F', 'A', 'the gravity of the Moon and, to a lesser extent, the Sun'),
  ('Tide tables can be produced years in advance.', 'T', 'A', 'tide tables can be printed years in advance'),
  ('The power station on the Rance estuary has been closed down.', 'F', 'B', 'is still in operation'),
  ('Large numbers of fish have been killed by barrage turbines.', 'NG', 'C', 'Fish may be injured by the turbines', 'The passage says fish may be injured, but gives no figures for deaths.'),
  ('The Sihwa Lake station was built into an existing structure.', 'T', 'C', 'it was built into a seawall that already existed'),
  ('Tidal lagoons block the flow of rivers.', 'F', 'D', 'rather than blocking a river'),
  ('The British government supported the first proposed lagoon in 2018.', 'F', 'D', 'in 2018 the government declined to support it'),
  ('Tidal stream turbines can only generate power when the tide is rising.', 'F', 'E', 'its blades turn as the water flows past, in both directions'),
  ('Tidal stream turbines have been supplying electricity off Scotland since 2016.', 'T', 'E', 'has been supplying electricity since 2016'),
  ('Solar panels became cheaper more quickly than wind farms did.', 'NG', 'G', 'as happened with solar panels and wind farms', 'The two are mentioned together; no comparison of speed is made.'),
 ]),
 mcq([
  ('According to paragraph A, what has always been the main difficulty with tidal power?', ['It is not reliable.', 'It is expensive.', 'It needs unusual coastlines.', 'It is opposed by fishermen.'], 1, 'A', 'The difficulty has always been the price.'),
  ('Why can a tidal stream turbine blade be shorter than a wind turbine blade?', ['It spins in both directions.', 'It is made from lighter metal.', 'Water is much denser than air.', 'It is fixed to the seabed.'], 2, 'E', 'Since water is roughly 800 times denser than air'),
  ('Early tidal prototypes failed mainly because', ['their blades were damaged by floating debris.', 'they could not be anchored to the seabed.', 'storms washed them away from the channel.', 'specialised vessels were not available.'], 0, 'F', 'Early prototypes failed because their blades were damaged by floating debris'),
 ]),
 multi('Which TWO problems for wildlife are linked with barrages in paragraph C?', ['Wading birds may lose their feeding grounds.', 'Fish may be unable to reach their spawning rivers.', 'Warmer water may kill plants in the estuary.', 'The noise of turbines may frighten whales.', 'Coastal erosion may destroy nesting sites.'], [0, 1], [('C', 'damage the feeding grounds of wading birds'), ('C', 'blocked from reaching their spawning rivers')]),
 head(['How a barrage produces electricity', 'Damage to wildlife and heavy costs', 'A gentler alternative that still costs too much', 'Turbines that work like underwater windmills', 'Technical and financial setbacks', 'A modest but reliable role', 'A rapid fall in the cost of tidal power', 'The first power station in Asia'],
  [('B', 0, 'A barrage works in a series of stages'), ('C', 1, 'Barrages can generate large amounts of power, but they have serious drawbacks'), ('D', 2, 'A second approach is the tidal lagoon'), ('E', 3, 'The newest and most promising technology is the tidal stream turbine'), ('F', 4, 'Developers face challenges'), ('G', 5, 'many experts believe tidal power will find a place in the energy mix')]),
 info([
  ('the astronomical cause of the tides', 'A', 'the gravity of the Moon'),
  ('an example of a project that saved money by using an existing structure', 'C', 'built into a seawall that already existed, which kept costs down'),
  ('a suggestion that a structure could protect the coast', 'D', 'protect coastlines from flooding'),
  ('a comparison between the density of water and air', 'E', 'roughly 800 times denser than air'),
  ('a reason why equipment can be hard to repair', 'F', 'storms can damage equipment that is difficult to reach for repairs'),
  ('a reason why a grid operator can plan around tidal output', 'G', 'a grid operator knows exactly when output will rise and fall'),
 ]),
 ends(['is built into a wall that already existed.', 'encloses an area of open sea.', 'is fixed to the seabed in a fast channel.', 'was dropped after the government refused support.', 'can be damaged by floating debris.', 'traps water behind a wall across an estuary.', 'produces output that can be forecast exactly.', 'needs no maintenance at all.'],
  [('A tidal barrage', 5, 'B', 'a long wall built across the mouth of an estuary'), ('The Sihwa Lake station', 0, 'C', 'built into a seawall that already existed'), ('A tidal lagoon', 1, 'D', 'encloses an area of open sea'), ('A tidal stream turbine', 2, 'E', 'Fixed to the seabed in channels where the current is strong'), ('The first lagoon proposed in Britain', 3, 'D', 'in 2018 the government declined to support it'), ('Tidal power as a whole', 6, 'G', 'a grid operator knows exactly when output will rise and fall')]),
 sent(2, [
  ('Tide tables can be printed ___ in advance.', ['years'], 'A', 'printed years in advance'),
  ('At high tide, ___ in the wall are opened.', ['sluice gates'], 'B', 'sluice gates in the wall are opened'),
  ('The Rance power station opened in ___.', ['1966'], 'B', 'opened in 1966'),
  ('Lagoons could also help to protect coastlines from ___.', ['flooding'], 'D', 'protect coastlines from flooding'),
  ('Seawater ___ metal, which causes problems for turbines.', ['corrodes'], 'F', 'Seawater corrodes metal'),
  ('Turbines can be installed only when the water is almost ___.', ['still'], 'F', 'when the water is almost still'),
 ]),
 short(3, [
  ('In which country is the Sihwa Lake power station?', ['south korea', 'korea'], 'C', 'Sihwa Lake in South Korea'),
  ('What is needed to install a turbine in a fast channel?', ['specialised vessels', 'vessels'], 'F', 'requires specialised vessels'),
  ('What damaged the blades of early prototypes?', ['floating debris', 'debris'], 'F', 'damaged by floating debris'),
  ('Which kind of power station was said to produce cheaper electricity than the first British lagoon?', ['new nuclear plant', 'nuclear plant', 'nuclear'], 'D', 'a new nuclear plant'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['At high tide, [[1]] in the barrage open and seawater flows into the basin.', 'The gates close and the water is trapped as the [[2]] falls outside.', 'When the difference in water level is great enough, the water is released through [[3]].', 'The moving water spins the blades, which drive a [[4]].', 'The electricity is fed into the national [[5]].'],
  [(['sluice gates', 'gates'], 'B', 'sluice gates in the wall are opened'), (['tide'], 'B', 'as the tide falls outside'), (['turbines'], 'B', 'released through turbines'), (['generator'], 'B', 'drive a generator'), (['grid'], 'B', 'national grid')], 2),
 diag('Label the diagram of a tidal barrage. Write NO MORE THAN TWO WORDS from the passage for each answer.', 520, 260, SVG, [[330, 25], [150, 110], [150, 200], [400, 130], [385, 50]],
  [(['generator'], 'B', 'drive a generator'), (['sluice gate', 'sluice gates'], 'B', 'sluice gates in the wall are opened'), (['turbine', 'turbines'], 'B', 'released through turbines built into the barrage'), (['basin'], 'B', 'flows into a basin behind it'), (['barrage'], 'B', 'a long wall built across the mouth of an estuary'.replace('a long wall built across the mouth of an estuary', 'tidal barrage'))], 2),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Tidal stream turbines look like underwater [[1]] turbines and are fixed to the [[2]]. Because water is much [[3]] than air, their blades can be shorter. However, seawater [[4]] metal, and early [[5]] were damaged by debris. The main advantage of tidal power is that it is [[6]].',
  [(['wind'], 'E', 'resembles an underwater wind turbine'), (['seabed'], 'E', 'Fixed to the seabed'), (['denser'], 'E', 'roughly 800 times denser than air'), (['corrodes'], 'F', 'Seawater corrodes metal'), (['prototypes'], 'F', 'Early prototypes failed'), (['predictable'], 'G', 'it is predictable')], 1,
  bank=['wind', 'seabed', 'denser', 'corrodes', 'prototypes', 'predictable', 'cheaper', 'lighter', 'expensive']),
])
