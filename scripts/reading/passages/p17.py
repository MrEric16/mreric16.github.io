from lib import *
A = """Every bridge must deal with two forces. Compression squeezes a material together, and tension pulls it apart. Engineers choose the shape of a bridge according to how it shares these forces between its parts. Over the centuries, four main designs have emerged, each suited to a different distance, and each solving the problem in its own way. The choice is never only technical: the width of the river, the nature of the ground and the budget all play a part."""
B = """The simplest design is the beam bridge, which is a horizontal beam resting on supports at each end. A fallen tree across a stream is the earliest example. When a load crosses the beam, the top of the beam is squeezed and the bottom is stretched, so beams are strong only over short distances. The longest rarely exceed 250 metres, and to cross a wide river they need many piers, which can be expensive to build and may block the flow of water."""
C = """The arch turns the downward weight of the bridge into compression, which stone handles very well. The Romans built arches that are still standing after two thousand years. The curved shape pushes outwards at its base, so an arch needs strong abutments, heavy blocks of stone or concrete at each end, to stop it from spreading. Arches are rarely used for spans longer than about 500 metres, but in the right valley, with solid rock on both sides, they are hard to beat for both beauty and strength."""
D = """The suspension bridge hangs the road from huge cables that are draped over tall towers and anchored firmly at both ends. The cables carry the load in tension, and steel wire, which is strong when pulled, is the ideal material. The Akashi Kaikyo Bridge in Japan has a central span of 1,991 metres. Suspension bridges can move in the wind, however. In 1940, the Tacoma Narrows Bridge in the United States twisted itself apart in a wind of only sixty-four kilometres per hour, and since then designers have tested models in wind tunnels."""
E = """The cable-stayed bridge looks similar but works differently. Its cables run straight from the towers to the road, in a pattern like the strings of a harp or the spokes of a fan, and there is no need for the enormous anchorages at the ends. This design is cheaper and faster to build over medium distances of between 200 and 1,000 metres, and it has become popular since the 1980s. The Russky Bridge in Vladivostok, with a span of 1,104 metres, is the longest of its kind in the world."""
F = """Building a bridge is only the beginning. Steel rusts, concrete cracks, and the number of vehicles often grows far beyond what the designers expected. Many countries now fit sensors to their bridges to measure movement and strain. According to the engineer Dr Hana Petrova, the data from sensors can warn of problems years before they can be seen by the eye, and a repair done early may cost one tenth of a repair done late. Even so, repairs are often delayed, because a bridge that still stands seems to be in no danger."""
G = """Engineers are also trying new materials. Fibre-reinforced plastics, which are lighter than steel and do not rust, are already used for footbridges. Researchers have developed a self-healing concrete that contains bacteria; when a crack lets in water, the bacteria wake up and produce limestone that seals the gap. Designers may soon be able to build a bridge that repairs itself, and so lasts far longer than the hundred years that most bridges are expected to survive."""
BEAM = '<path class="l" d="M0 100H160"/><rect class="f" x="30" y="58" width="8" height="42"/><rect class="f" x="76" y="58" width="8" height="42"/><rect class="f" x="122" y="58" width="8" height="42"/><rect class="s" x="10" y="50" width="140" height="8"/>'
ARCH = '<path class="l" d="M0 108H160"/><path class="s" style="fill:none;stroke-width:5" d="M22 100A58 58 0 0 1 138 100"/><path class="l" d="M10 100H150"/><rect class="f" x="10" y="98" width="16" height="10"/><rect class="f" x="134" y="98" width="16" height="10"/>'
SUSP = '<path class="l" d="M0 108H160"/><rect class="f" x="40" y="22" width="6" height="86"/><rect class="f" x="114" y="22" width="6" height="86"/><path class="l" d="M5 82H155"/><path class="l" style="fill:none" d="M0 62Q20 62 43 24Q80 76 117 24Q140 62 160 62"/><path class="l" d="M60 62V82M80 70V82M100 62V82"/>'
CABLE = '<path class="l" d="M0 108H160"/><rect class="f" x="77" y="18" width="6" height="90"/><path class="l" d="M5 82H155"/><path class="l" d="M80 24L20 82M80 34L40 82M80 44L60 82M80 24L140 82M80 34L120 82M80 44L100 82"/>'
P = passage('p17', 'Bridges That Last', 'Engineering', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Compression pulls a material apart.', 'F', 'A', 'tension pulls it apart'),
  ('The width of the river affects the choice of design.', 'T', 'A', 'the width of the river, the nature of the ground and the budget all play a part'),
  ('The earliest beam bridge was made of stone.', 'F', 'B', 'A fallen tree across a stream is the earliest example'),
  ('Piers can block the flow of water.', 'T', 'B', 'may block the flow of water'),
  ('Roman arch bridges have all been destroyed.', 'F', 'C', 'still standing after two thousand years'),
  ('Steel wire is strong when it is pulled.', 'T', 'D', 'steel wire, which is strong when pulled'),
  ('The Tacoma Narrows Bridge was built in 1940.', 'NG', 'D', 'In 1940, the Tacoma Narrows Bridge', 'The year given is that of its collapse, not its construction.'),
  ('Cable-stayed bridges need huge anchorages at both ends.', 'F', 'E', 'no need for the enormous anchorages at the ends'),
  ('Dr Petrova works for the government.', 'NG', 'F', 'the engineer Dr Hana Petrova', 'Her employer is not mentioned.'),
 ]),
 mcq([
  ('What is the main weakness of a beam bridge?', ['It cannot carry heavy loads at all.', 'It is strong only over short distances.', 'It is unattractive.', 'It cannot be built of steel.'], 1, 'B', 'beams are strong only over short distances'),
  ('Why do arches need abutments?', ['To make them look larger.', 'To carry the cables.', 'To stop the arch spreading outwards.', 'To protect them from wind.'], 2, 'C', 'to stop it from spreading'),
  ('Why are repairs often delayed?', ['They cost too much.', 'A standing bridge seems safe.', 'Sensors give poor data.', 'Engineers refuse to do them.'], 1, 'F', 'a bridge that still stands seems to be in no danger'),
 ]),
 pic('Which picture, A to D, shows each type of bridge described in the passage?', [(BEAM, 160, 120), (ARCH, 160, 120), (SUSP, 160, 120), (CABLE, 160, 120)], [
  ('a horizontal beam resting on supports', 0, 'B', 'a horizontal beam resting on supports at each end'),
  ('a curved shape that pushes outwards at its base', 1, 'C', 'The curved shape pushes outwards at its base'),
  ('cables draped over towers and anchored at both ends', 2, 'D', 'draped over tall towers and anchored firmly at both ends'),
  ('cables running straight from the tower to the road in a fan', 3, 'E', 'cables run straight from the towers to the road'),
 ]),
 head(['Two forces and four designs', 'The simplest and shortest', 'Weight turned into squeezing', 'Hanging a road from cables', 'A cheaper alternative for medium spans', 'Why maintenance matters', 'Materials of the future', 'The history of the Roman Empire', 'A bridge that fell down'],
  [('A', 0, 'Every bridge must deal with two forces'), ('B', 1, 'The simplest design is the beam bridge'), ('C', 2, 'The arch turns the downward weight'), ('D', 3, 'hangs the road from huge cables'), ('E', 4, 'cheaper and faster to build over medium distances'), ('F', 5, 'Building a bridge is only the beginning'), ('G', 6, 'Engineers are also trying new materials')]),
 info([
  ('the name of a very long bridge in Japan', 'D', 'The Akashi Kaikyo Bridge in Japan'),
  ('a reason why models are tested in wind tunnels', 'D', 'twisted itself apart'),
  ('a comparison of cable patterns with musical or mechanical objects', 'E', 'the strings of a harp or the spokes of a fan'),
  ('the saving that comes from early repairs', 'F', 'one tenth of a repair done late'),
  ('a description of how a material mends itself', 'G', 'produce limestone that seals the gap'),
 ]),
 sent(2, [
  ('A beam bridge over a wide river needs many ___.', ['piers'], 'B', 'they need many piers'),
  ('An arch is rarely used for a span longer than about ___ metres.', ['500', 'five hundred'], 'C', 'about 500 metres'),
  ('The Tacoma Narrows Bridge was tested in wind tunnels after it ___ itself apart.', ['twisted'], 'D', 'twisted itself apart'),
  ('Cable-stayed bridges have become popular since the ___.', ['1980s'], 'E', 'since the 1980s'),
 ]),
 short(3, [
  ('What do designers fit to bridges to measure movement and strain?', ['sensors'], 'F', 'fit sensors to their bridges'),
  ('What do the bacteria in self-healing concrete produce?', ['limestone'], 'G', 'produce limestone'),
  ('How many years are most bridges expected to survive?', ['a hundred', 'hundred', '100', 'one hundred'], 'G', 'the hundred years that most bridges are expected to survive'),
 ]),
 multi('Which TWO materials are mentioned as being used in bridge building in the passage?', ['Stone.', 'Steel wire.', 'Glass.', 'Wood panels.', 'Aluminium.'], [0, 1], [('D', 'steel wire'), ('C', 'stone handles very well')]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'A beam bridge is only suitable for [[1]] distances. An arch relies on [[2]], while a suspension bridge carries its load in [[3]]. A cable-stayed bridge needs no huge [[4]] and is cheaper over medium spans.',
  [(['short'], 'B', 'strong only over short distances'), (['compression'], 'C', 'into compression'), (['tension'], 'D', 'in tension'), (['anchorages'], 'E', 'enormous anchorages')], 1,
  bank=['short', 'compression', 'tension', 'anchorages', 'long', 'towers', 'piers', 'weight']),
])
