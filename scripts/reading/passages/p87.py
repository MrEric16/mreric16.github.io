from lib import *
from svgs import *
A = """Every autumn, billions of birds leave their summer homes and fly to warmer places, and every spring they return. This journey is called migration, and it is one of the great spectacles of nature. Some birds travel only a few hundred kilometres, from a mountain valley to the plains below. Others cross whole continents and oceans. The Arctic tern, for example, breeds near the North Pole and spends the northern winter near the South Pole, a round trip of some seventy thousand kilometres. Scientists have studied migration for centuries, yet they are still discovering how small animals with brains the size of a nut find their way across the planet."""
B = """The main reason for migration is food. In summer, the northern lands are rich in insects, seeds and fruit, and the long days give birds more time to feed their young. In winter, the insects disappear, the ground freezes, and food becomes scarce. Birds that stayed would starve, so they move to places where food is still plentiful. The journey is dangerous, however, and many birds die on the way from storms, hunger or exhaustion. Evolution has favoured migration because, for many species, the benefits of the rich summer feeding grounds outweigh the risks of the long flight."""
C = """To prepare, birds eat large amounts of food and store the energy as fat. A small warbler may almost double its weight in a few weeks. Fat is an excellent fuel, as it contains more than twice as much energy as the same weight of sugar. Some species change their bodies for the journey: they shrink their digestive organs, which are heavy, and enlarge their flight muscles. The bar-tailed godwit holds the record for the longest non-stop flight of any bird, flying about eleven thousand kilometres from Alaska to New Zealand in about eight days without eating, drinking or resting."""
D = """How do birds know when to leave? The main signal is the length of the day. As days shorten in autumn, changes in the amount of light trigger hormones which make the birds restless and hungry. Even birds kept in cages show this restlessness at the usual time, pointing their bodies in the direction of the migration. Weather also plays a part, and birds often wait for a favourable wind before taking off. Many birds travel in flocks, which helps them to save energy: geese fly in a V-shape, where each bird gets a little lift from the air disturbed by the one in front."""
E = """Finding the way is even more remarkable. Birds seem to use several compasses at once. They read the position of the sun by day and the pattern of the stars at night. They can sense the Earth's magnetic field, which acts as a natural compass, and some researchers believe that special molecules in their eyes allow them to see it. Birds also learn landmarks, such as rivers, coastlines and mountain ranges, and some may use smell. Young birds that are migrating for the first time often follow instinct alone, and they may find a winter home which they have never seen."""
F = """Today migration faces new threats. Cities with bright lights confuse night migrants, and thousands of birds die each year in collisions with buildings. Wetlands, where birds rest and feed during the journey, are being drained for farms and housing. Climate change is also altering the seasons: in some places, spring now arrives earlier, so that insects hatch before the birds get there to eat them. Dr Elena Marsh, an ornithologist who tracks small birds with tiny electronic tags, reports that some species have already changed their routes and timing to adapt. Others are in decline because they cannot change fast enough."""
G = """Many countries are cooperating to protect the birds. Because migrants pass through many nations, no single country can protect them alone, and international agreements now protect important resting sites. Some cities switch off their lights on peak migration nights, with good results. In Central Asia, a region on several major flyways, conservationists are working with local people to protect lakes and reed beds. Dr Marsh believes that the cost of such protection is small compared with the gain, and that anybody can help, for instance by making windows more visible to birds or by reporting their sightings to scientific projects."""
P = passage('p87', 'The Great Bird Migration', 'Biology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Billions of birds migrate each year.', 'T', 'A', 'billions of birds'),
  ('The Arctic tern spends the northern winter near the South Pole.', 'T', 'A', 'near the South Pole'),
  ('All birds migrate more than a thousand kilometres.', 'F', 'A', 'only a few hundred kilometres'),
  ('Food becomes scarce in winter in northern lands.', 'T', 'B', 'food becomes scarce'),
  ('Fat contains less energy than sugar.', 'F', 'C', 'more than twice as much energy'),
  ('The bar-tailed godwit flies from Alaska to New Zealand.', 'T', 'C', 'from Alaska to New Zealand'),
  ('Day length is the main signal to leave.', 'T', 'D', 'length of the day'),
  ('Geese fly in a V-shape to save energy.', 'T', 'D', 'V-shape'),
  ('Small birds migrate faster than large birds.', 'NG', 'C', 'A small warbler', 'Relative speeds are not given.'),
 ]),
 mcq([
  ('What is the main reason for migration?', ['Food.', 'Fashion.', 'Noise.', 'Fear.'], 0, 'B', 'The main reason for migration is food'),
  ('How do birds prepare for the journey?', ['They store energy as fat.', 'They grow larger wings.', 'They stop eating.', 'They sleep for weeks.'], 0, 'C', 'store the energy as fat'),
  ('What is happening because of climate change?', ['Insects hatch before the birds arrive.', 'Birds stop flying.', 'Lakes grow larger.', 'Winters get longer.'], 0, 'F', 'insects hatch before the birds get there'),
 ]),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Topic', 'Detail'],
  [['Arctic tern', 'Round trip of about seventy thousand [[1]]'], ['Godwit', 'Flies without eating, drinking or [[2]]'], ['Geese', 'Fly in a [[3]]-shape'], ['City lights', 'Confuse night [[4]]']],
  [(['kilometres'], 'A', 'seventy thousand kilometres'), (['resting'], 'C', 'resting'), (['v'], 'D', 'V-shape'), (['migrants'], 'F', 'night migrants')], 1),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['Days shorten in [[1]].', 'Light changes trigger [[2]].', 'Birds become restless and [[3]].', 'They wait for a favourable [[4]] before taking off.'],
  [(['autumn'], 'D', 'shorten in autumn'), (['hormones'], 'D', 'trigger hormones'), (['hungry'], 'D', 'restless and hungry'), (['wind'], 'D', 'favourable wind')], 1),
 feat('Match each statement with the correct item, A to D.', ['Arctic tern', 'Bar-tailed godwit', 'Geese', 'Dr Marsh'], [
  ('It breeds near the North Pole.', 0, 'A', 'breeds near the North Pole'),
  ('It holds the record for the longest non-stop flight.', 1, 'C', 'longest non-stop flight'),
  ('They get a little lift from the bird in front.', 2, 'D', 'lift from the air disturbed'),
  ('She tracks small birds with electronic tags.', 3, 'F', 'electronic tags'),
 ]),
 multi('Which TWO ways of finding the way are mentioned in paragraph E?', ['Reading the position of the sun.', 'Sensing the magnetic field.', 'Following ships.', 'Listening to the sea.', 'Using maps.'], [0, 1], [('E', 'position of the sun'), ('E', 'magnetic field')]),
 head(['A journey across the world', 'Why birds leave', 'Fuel for the flight', 'The signal to go', 'Compasses in the sky', 'New dangers', 'Working together', 'The history of aviation', 'Birds in myths'],
  [('A', 0, 'cross whole continents and oceans'), ('B', 1, 'The main reason for migration is food'), ('C', 2, 'store the energy as fat'), ('D', 3, 'The main signal is the length of the day'), ('E', 4, 'use several compasses at once'), ('F', 5, 'Today migration faces new threats'), ('G', 6, 'Many countries are cooperating')]),
 info([
  ('a reference to the size of a bird\'s brain', 'A', 'size of a nut'),
  ('a reference to shrinking digestive organs', 'C', 'shrink their digestive organs'),
  ('a reference to birds in cages', 'D', 'kept in cages'),
  ('a reference to landmarks', 'E', 'rivers, coastlines and mountain ranges'),
  ('a reference to switching off lights', 'G', 'switch off their lights'),
 ]),
 ends(['are drained for farms.', 'confuse night migrants.', 'trigger hormones.', 'are working with local people.', 'sing at night.', 'never rest.', 'have no wings.'], [
  ('Wetlands', 0, 'F', 'drained for farms and housing'),
  ('Bright lights', 1, 'F', 'confuse night migrants'),
  ('Changes in light', 2, 'D', 'trigger hormones'),
  ('Conservationists in Central Asia', 3, 'G', 'working with local people'),
 ]),
 sent(2, [
  ('Birds store energy as ___.', ['fat'], 'C', 'as fat'),
  ('Geese fly in a ___-shape.', ['v'], 'D', 'V-shape'),
  ('Dr Marsh is an ___.', ['ornithologist'], 'F', 'an ornithologist'),
  ('Wetlands are places where birds rest and ___.', ['feed'], 'F', 'rest and feed'),
 ]),
 short(3, [
  ('How long does the godwit flight last?', ['eight days', 'about eight days'], 'C', 'about eight days'),
  ('What do night migrants use to navigate?', ['stars', 'the stars'], 'E', 'pattern of the stars'),
  ('What can help windows?', ['more visible'], 'G', 'more visible to birds'),
 ]),
])
