from lib import *
from svgs import *
A = """Cities, like people, have different life stories. Some grow quickly and keep growing, others shrink, and a few rise and fall in a pattern that surprises even the experts who study them. To illustrate the main patterns, this passage looks at four imaginary cities, each based on a real type of place, and at the economic reasons behind the changes in their populations over a period of fifty years. Planners use such studies to decide where to build schools, roads and hospitals, and mistakes can be very expensive."""
B = """Marden began as a small market town beside a river. In the 1970s, a technology company opened its headquarters there, and other firms followed. Young graduates moved in to take the new jobs, and their children were born in the city. Since then the population has risen every single year, and it now stands at more than a million. The growth brings problems of its own, however: house prices have tripled, and many of the original residents can no longer afford to live in the neighbourhoods where they were born."""
C = """Olvia is a mining town in the mountains. For a century it prospered, but when the last coal mine closed in 1985, the main employer disappeared and families began to leave. The population has fallen steadily ever since, and several schools have been merged. The council has tried to attract tourists to the old mine buildings, but the effect so far has been small, and many of the young people who remain say that they plan to move away as soon as they finish their studies."""
D = """The history of Kessing was quite different. A car factory opened there in 1960 and the population rose rapidly, reaching a peak in 1990. Then the factory moved its production abroad, and thousands of workers lost their jobs. The population fell almost as quickly as it had risen, and it is now not much larger than it was before the factory arrived. Researchers who study such places say that cities depending on one industry are especially at risk, because a single decision in a distant boardroom can change the lives of a whole community."""
E = """Tarn followed a fourth path. It was a quiet port city whose population fell in the 1970s when the old shipping trade declined. For two decades, nothing seemed to help. Then the city turned its empty warehouses into studios, cafes and small workshops, and artists and designers began to arrive. By the early 2000s the decline had turned into recovery, and the population has now returned to about the level at which it began. Tarn is often given as an example of a city that reinvented itself."""
F = """Why do these patterns matter? According to Dr Isabel Fontaine, an urban economist, the shape of a city's population curve tells a story about its economy. Steady growth suggests a variety of jobs, a sharp rise and fall suggests dependence on a single industry, and slow decline points to a lack of opportunities for the young. She warns, though, that the pattern can change quickly, and that planners who simply extend an existing trend into the future are often proved wrong by events that nobody predicted."""
G = """What can other cities learn from these four? First, a varied economy is safer than a single large employer. Second, a city must provide homes that ordinary people can afford, or it risks losing the workers it needs. Third, empty buildings are a resource as well as a problem, as Tarn showed. Finally, planners should treat predictions with care. The future of a city, like that of its people, depends on choices that have not yet been made, and on the willingness of its citizens to adapt when the world around them changes."""
P = passage('p27', 'Four Cities, Four Stories', 'Economics', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which graph, A to D, shows the population of each city described in the passage?', [(graph('rise'), 160, 120), (graph('fall'), 160, 120), (graph('peak'), 160, 120), (graph('dip'), 160, 120)], [
  ('Marden', 0, 'B', 'the population has risen every single year'),
  ('Olvia', 1, 'C', 'The population has fallen steadily ever since'),
  ('Kessing', 2, 'D', 'reaching a peak in 1990'),
  ('Tarn', 3, 'E', 'the decline had turned into recovery'),
 ]),
 tfng([
  ('The four cities in the passage are real.', 'F', 'A', 'four imaginary cities'),
  ('Planners use population studies to decide where to build schools.', 'T', 'A', 'where to build schools, roads and hospitals'),
  ('A technology company opened its headquarters in Marden in the 1970s.', 'T', 'B', 'In the 1970s, a technology company opened its headquarters there'),
  ('House prices in Marden have doubled.', 'F', 'B', 'house prices have tripled'),
  ('Olvia\'s last coal mine closed in 1985.', 'T', 'C', 'the last coal mine closed in 1985'),
  ('Tourism has solved the problems of Olvia.', 'F', 'C', 'the effect so far has been small'),
  ('The car factory in Kessing was owned by a foreign company.', 'NG', 'D', 'the factory moved its production abroad', 'Ownership of the factory is not mentioned.'),
  ('Tarn\'s decline was caused by the end of the shipping trade.', 'T', 'E', 'when the old shipping trade declined'),
  ('Dr Fontaine believes that trends can always be safely extended.', 'F', 'F', 'are often proved wrong by events that nobody predicted'),
 ]),
 mcq([
  ('Why can many original residents of Marden no longer live in their neighbourhoods?', ['The firms moved away.', 'Housing is too expensive.', 'The river flooded.', 'The schools closed.'], 1, 'B', 'can no longer afford to live'),
  ('What is especially risky for a city, according to researchers?', ['Depending on one industry.', 'Having a port.', 'Attracting graduates.', 'Having old buildings.'], 0, 'D', 'cities depending on one industry are especially at risk'),
  ('How did Tarn recover?', ['By building a new factory.', 'By reusing empty warehouses.', 'By closing its port.', 'By lowering taxes.'], 1, 'E', 'turned its empty warehouses into studios'),
 ]),
 multi('Which TWO effects of growth in Marden are mentioned in paragraph B?', ['Young graduates moved in.', 'House prices rose.', 'Schools were closed.', 'The river became polluted.', 'The airport was enlarged.'], [0, 1], [('B', 'Young graduates moved in'), ('B', 'house prices have tripled')]),
 head(['The purpose of the study', 'A city that keeps growing', 'A town that lost its main employer', 'A rapid rise and fall', 'A city that reinvented itself', 'What the curves reveal', 'Advice for the future', 'The best way to build a bridge', 'A history of mining'],
  [('A', 0, 'this passage looks at four imaginary cities'), ('B', 1, 'Marden began as a small market town'), ('C', 2, 'Olvia is a mining town'), ('D', 3, 'The history of Kessing was quite different'), ('E', 4, 'Tarn followed a fourth path'), ('F', 5, 'tells a story about its economy'), ('G', 6, 'What can other cities learn from these four')]),
 info([
  ('a reference to a population figure above a million', 'B', 'more than a million'),
  ('a mention of schools being merged', 'C', 'several schools have been merged'),
  ('a year in which a population peaked', 'D', 'reaching a peak in 1990'),
  ('a list of new uses for empty buildings', 'E', 'studios, cafes and small workshops'),
  ('a suggestion that homes should be affordable', 'G', 'homes that ordinary people can afford'),
 ]),
 ends(['a city with a varied economy.', 'a decline in opportunities for the young.', 'planners who extend trends.', 'a factory that moved abroad.', 'a university in the mountains.', 'a river that changed course.', 'a decision by the council of Tarn.'], [
  ('Steady growth suggests', 0, 'F', 'Steady growth suggests a variety of jobs'),
  ('Slow decline points to', 1, 'F', 'slow decline points to a lack of opportunities for the young'),
  ('Dr Fontaine warns about', 2, 'F', 'planners who simply extend an existing trend'),
  ('Kessing lost thousands of jobs because of', 3, 'D', 'the factory moved its production abroad'),
 ]),
 sent(2, [
  ('Marden began as a small ___ town.', ['market'], 'B', 'a small market town'),
  ('Olvia is a ___ town in the mountains.', ['mining'], 'C', 'a mining town'),
  ('Kessing\'s car factory opened in ___.', ['1960'], 'D', 'opened there in 1960'),
  ('Tarn is often given as an example of a city that ___ itself.', ['reinvented'], 'E', 'reinvented itself'),
 ]),
 short(3, [
  ('What is Dr Fontaine\'s profession?', ['urban economist', 'an urban economist'], 'F', 'an urban economist'),
  ('What is safer than a single large employer?', ['a varied economy', 'varied economy'], 'G', 'a varied economy is safer'),
  ('What did the council of Olvia try to attract?', ['tourists'], 'C', 'attract tourists'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Marden grew because of a technology company, while Olvia lost its main [[1]] when the mine closed. Kessing relied on one [[2]] and suffered when it moved abroad. Tarn recovered by turning empty [[3]] into places for artists, and planners should treat [[4]] with care.',
  [(['employer'], 'C', 'the main employer disappeared'), (['factory'], 'D', 'A car factory'), (['warehouses'], 'E', 'empty warehouses'), (['predictions'], 'G', 'treat predictions with care')], 1,
  bank=['employer', 'factory', 'warehouses', 'predictions', 'schools', 'rivers', 'taxes', 'tourists']),
])
