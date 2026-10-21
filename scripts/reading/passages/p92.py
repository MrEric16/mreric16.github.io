from lib import *
from svgs import *
A = """Glass is so common that we hardly notice it. We drink from it, look through it, and live and work behind it. Yet few materials have a stranger or more useful nature. Glass is hard but brittle, transparent but made largely of ordinary sand, and it can be shaped into anything from a window to a telescope lens to a fibre thinner than a hair. It is made by melting a few simple ingredients, which are cheap and plentiful. This passage traces the history of glass, explains how it is made and describes some of the ways in which it is changing our world."""
B = """Nobody knows exactly who first made glass. Natural glass has existed for millions of years: obsidian, a black glass, is formed when volcanic lava cools quickly, and prehistoric people used it to make sharp knives and arrowheads. Man-made glass appeared in Mesopotamia and Egypt more than four thousand years ago, at first as coloured beads and small vessels. Making glass was difficult, since it required very high temperatures, and the objects were expensive. They were prized by rulers and were often buried with them."""
C = """A great step forward came in the first century BC, when craftsmen in the Roman world discovered glassblowing. The glassblower gathers a blob of molten glass on the end of a hollow iron pipe and blows into it, so that the glass swells like a balloon. Objects could be made quickly, in many shapes, and glass became cheap enough for ordinary households. The Romans produced bottles, cups, jars and even window panes. Later, the glassmakers of Venice became famous for fine, clear glass, and in the thirteenth century the authorities moved the furnaces to the island of Murano, partly to protect the secrets of the trade."""
D = """Modern glass is made from three main ingredients. The first is silica, in the form of pure sand, which makes up about seventy per cent of the mixture. The second is soda ash, which lowers the melting point of the sand, and the third is limestone, which makes the glass stronger and prevents it from dissolving in water. The ingredients are mixed and heated in a furnace to about fifteen hundred degrees until they melt. Recycled glass, called cullet, is added, saving energy. The molten glass is then shaped by blowing, pressing or floating, according to the product."""
E = """Most window glass is now made by the float process, invented in Britain in the 1950s. Molten glass flows continuously from the furnace on to a bath of liquid tin, a metal that is heavier than glass and does not mix with it. The glass spreads out and floats on the surface, producing a perfectly flat sheet with smooth surfaces on both sides. It is then slowly cooled and cut into large panes. The method produces glass of high quality at low cost, and it replaced older techniques in which sheets had to be ground and polished by hand."""
F = """Different properties can be given to glass by changing the mixture or treating it. Adding boron produces a glass which can resist sudden changes in temperature, and this is why laboratory flasks and some oven dishes are made from it. Tempered glass, which is heated and rapidly cooled, is up to five times stronger than ordinary glass, and when it breaks, it crumbles into small harmless pieces; it is used in car windows. Laminated glass has a thin plastic layer between two sheets and does not fall apart when broken, so it is used in windscreens. Metal oxides colour the glass: cobalt gives blue, and copper gives green or red."""
G = """Glass has shaped the history of science. The lens made it possible to build the microscope and the telescope, with which people discovered cells and distant planets. Today, glass fibres carry most of the world's internet traffic, as pulses of light travelling through strands thinner than a hair. Dr Hannah Brandt, a materials scientist, says that glass is also an environmental success story, since it can be recycled endlessly without losing quality. She is working on windows that darken in sunlight and on glass that generates electricity. As she puts it, the oldest man-made material still has a great deal to teach us."""
P = passage('p92', 'The Story of Glass', 'Science and technology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Glass is made largely from sand.', 'T', 'A', 'made largely of ordinary sand'),
  ('Obsidian is formed when lava cools quickly.', 'T', 'B', 'cools quickly'),
  ('Man-made glass first appeared in Rome.', 'F', 'B', 'Mesopotamia and Egypt'),
  ('Glassblowing was discovered in the first century BC.', 'T', 'C', 'first century BC'),
  ('The glassmakers of Venice were moved to Murano.', 'T', 'C', 'island of Murano'),
  ('Silica makes up about seventy per cent of the mixture.', 'T', 'D', 'about seventy per cent'),
  ('Limestone lowers the melting point.', 'F', 'D', 'soda ash, which lowers the melting point'),
  ('The float process was invented in the 1950s.', 'T', 'E', 'in the 1950s'),
  ('Murano glass is the most expensive in the world.', 'NG', 'C', 'island of Murano', 'Its price is not mentioned.'),
 ]),
 mcq([
  ('Why was early glass expensive?', ['It needed very high temperatures.', 'Sand was rare.', 'There were no craftsmen.', 'It was taxed.'], 0, 'B', 'very high temperatures'),
  ('Why is liquid tin used in the float process?', ['It is heavier than glass and does not mix with it.', 'It is cheap.', 'It is clear.', 'It is cold.'], 0, 'E', 'heavier than glass and does not mix with it'),
  ('What is true of laminated glass?', ['It does not fall apart when broken.', 'It is coloured.', 'It is boron glass.', 'It melts easily.'], 0, 'F', 'does not fall apart when broken'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Pure sand, soda ash and [[1]] are mixed.', 'The mixture is heated in a [[2]].', 'Molten glass flows on to a bath of liquid [[3]].', 'The sheet is slowly cooled and [[4]] into panes.'],
  [(['limestone'], 'D', 'limestone'), (['furnace'], 'D', 'furnace'), (['tin'], 'E', 'liquid tin'), (['cut'], 'E', 'cut into large panes')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Type of glass', 'Property'],
  [['Boron glass', 'Resists sudden changes in [[1]]'], ['Tempered glass', 'Up to five times [[2]]'], ['Laminated glass', 'Used in [[3]]'], ['Cobalt', 'Gives [[4]] colour']],
  [(['temperature'], 'F', 'temperature'), (['stronger'], 'F', 'stronger'), (['windscreens'], 'F', 'windscreens'), (['blue'], 'F', 'blue')], 1),
 feat('Match each statement with the correct item, A to D.', ['Obsidian', 'Glassblowing', 'Cullet', 'Glass fibres'], [
  ('It was used by prehistoric people for knives.', 0, 'B', 'sharp knives and arrowheads'),
  ('It made glass cheap enough for ordinary households.', 1, 'C', 'cheap enough for ordinary households'),
  ('It is recycled glass added to the mixture.', 2, 'D', 'Recycled glass, called cullet'),
  ('They carry most of the world\'s internet traffic.', 3, 'G', 'internet traffic'),
 ]),
 multi('Which TWO scientific instruments made with lenses are mentioned in paragraph G?', ['The microscope.', 'The telescope.', 'The thermometer.', 'The barometer.', 'The radio.'], [0, 1], [('G', 'microscope'), ('G', 'telescope')]),
 head(['An ordinary yet strange material', 'Ancient beginnings', 'Blowing a bubble', 'The recipe', 'A river of glass on tin', 'Glass with special powers', 'A material for the future', 'The history of mirrors', 'Famous museums'],
  [('A', 0, 'stranger or more useful nature'), ('B', 1, 'more than four thousand years ago'), ('C', 2, 'blows into it'), ('D', 3, 'three main ingredients'), ('E', 4, 'floats on the surface'), ('F', 5, 'Different properties can be given to glass'), ('G', 6, 'a great deal to teach us')]),
 info([
  ('a reference to arrowheads', 'B', 'arrowheads'),
  ('a reference to protecting trade secrets', 'C', 'secrets of the trade'),
  ('a reference to the melting temperature', 'D', 'fifteen hundred degrees'),
  ('a reference to a perfectly flat sheet', 'E', 'perfectly flat sheet'),
  ('a reference to glass that generates electricity', 'G', 'generates electricity'),
 ]),
 ends(['was buried with rulers.', 'was moved to Murano.', 'is added to save energy.', 'is used in car windows.', 'is made from wood.', 'floats on water.', 'was invented by Romans.'], [
  ('Early glass objects', 0, 'B', 'buried with them'),
  ('The Venetian furnaces', 1, 'C', 'moved the furnaces to the island of Murano'),
  ('Cullet', 2, 'D', 'saving energy'),
  ('Tempered glass', 3, 'F', 'car windows'),
 ]),
 sent(2, [
  ('Obsidian is a black ___.', ['glass'], 'B', 'a black glass'),
  ('The glassblower uses a hollow iron ___.', ['pipe'], 'C', 'hollow iron pipe'),
  ('Soda ash lowers the ___ point of sand.', ['melting'], 'D', 'melting point'),
  ('Dr Brandt is a materials ___.', ['scientist'], 'G', 'materials scientist'),
 ]),
 short(3, [
  ('What is the main ingredient of glass?', ['silica', 'sand'], 'D', 'silica'),
  ('Where was the float process invented?', ['britain'], 'E', 'in Britain'),
  ('What gives glass a green or red colour?', ['copper'], 'F', 'copper gives green or red'),
 ]),
])
