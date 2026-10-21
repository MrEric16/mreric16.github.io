from lib import *
from svgs import *
A = """Humans spend about a third of their lives asleep, yet for most of history sleep was a mystery. Until the middle of the twentieth century, many scientists believed that the brain simply switched off at night, like a machine. Modern research has shown the opposite: the sleeping brain is active, and it performs tasks that are essential for health, from repairing the body to sorting the memories of the day. Without enough sleep, people become forgetful, irritable and more likely to catch infections, and in the long term they face a higher risk of serious illness. This passage explains how sleep works and why teenagers in particular need more of it than they usually get."""
B = """A night's sleep is not a single state, but a series of cycles of about ninety minutes each. In every cycle the sleeper passes through several stages. In light sleep, the heartbeat slows and the body temperature falls, and the sleeper can easily be woken. In deep sleep, which is most common in the first half of the night, the brain waves become slow and large, and it is very difficult to wake the sleeper; this is when the body repairs its tissues and strengthens its defences against disease. A typical adult goes through four or five cycles in a night, and being woken in the middle of deep sleep leaves a person confused and tired."""
C = """The last stage of each cycle is REM sleep, named after the rapid eye movements that can be seen beneath the closed eyelids. During REM sleep, the brain is almost as active as when awake, the breathing becomes faster and irregular, and most dreams occur. The muscles, however, are temporarily paralysed, which prevents the sleeper from acting out the dreams. REM periods are short at the start of the night, lasting about ten minutes, but they grow longer in later cycles, and the final one may last for nearly an hour. Scientists believe that REM sleep helps the brain to process emotions and to store memories."""
D = """The timing of sleep is controlled by an internal body clock, which follows a rhythm of roughly twenty-four hours. Light is the main signal that sets the clock. When darkness falls, a small gland in the brain releases a hormone called melatonin, which makes the body feel sleepy; in the morning, light stops its production and helps to wake a person up. The clock changes with age. During the teenage years, it shifts later by about two hours, so that many teenagers do not feel sleepy until after eleven at night and find it hard to wake early, which is a matter of biology and not of laziness."""
E = """The amount of sleep that people need depends on their age. Babies sleep for more than twelve hours a day, and young children for about ten. Experts recommend that teenagers sleep for between eight and ten hours a night, and that adults sleep for at least seven. In fact, a large proportion of teenagers sleep far less than this, because they have to get up early for school, spend their evenings on homework and social media, and then lie awake in front of screens. The result is a kind of permanent jet lag, in which students are tired in the morning lessons and cannot concentrate on what the teacher says."""
F = """Dr Isabel Moreno, a sleep researcher, has studied the effect of tiredness on students' results. She found that students who slept less than seven hours scored lower in memory tests than those who slept for nine, even when they had studied for the same length of time. She explains that learning is not complete until it has been stored during sleep, so that a student who stays up all night to revise may actually forget more than one who revises less and goes to bed at a sensible time. She also warns that the blue light from phones and tablets reduces the production of melatonin and delays sleep."""
G = """Fortunately, sleep can be improved by simple habits. Experts advise people to go to bed and wake up at the same time every day, including weekends, to keep the bedroom dark, quiet and cool, and to avoid screens for an hour before bed. Caffeine in coffee, tea and energy drinks should be avoided in the afternoon, because it stays in the body for many hours. Taking exercise in the daytime helps, but not just before bedtime. If a person cannot fall asleep within about twenty minutes, it is better to get up and read quietly in dim light than to lie awake and worry."""
P = passage('p77', 'The Science of Sleep', 'Health', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Humans spend about a third of their lives asleep.', 'T', 'A', 'about a third of their lives asleep'),
  ('Scientists once believed the brain switched off at night.', 'T', 'A', 'the brain simply switched off at night'),
  ('A night\'s sleep consists of cycles of about ninety minutes.', 'T', 'B', 'cycles of about ninety minutes each'),
  ('Deep sleep is most common in the second half of the night.', 'F', 'B', 'most common in the first half of the night'),
  ('Most dreams occur in REM sleep.', 'T', 'C', 'most dreams occur'),
  ('During REM sleep the muscles are fully active.', 'F', 'C', 'temporarily paralysed'),
  ('Melatonin is released when darkness falls.', 'T', 'D', 'When darkness falls'),
  ('Teenagers are recommended to sleep for eight to ten hours.', 'T', 'E', 'between eight and ten hours'),
  ('Dr Moreno has studied sleep in children under five.', 'NG', 'F', 'Dr Isabel Moreno', 'Young children are not discussed there.'),
 ]),
 mcq([
  ('Why is deep sleep important?', ['The body repairs its tissues.', 'Dreams occur.', 'Light is needed.', 'The eyes move.'], 0, 'B', 'the body repairs its tissues'),
  ('What happens to the body clock in the teenage years?', ['It stops.', 'It shifts later by about two hours.', 'It speeds up.', 'It shifts earlier.'], 1, 'D', 'shifts later by about two hours'),
  ('Why may a student who stays up all night forget more?', ['Learning is not complete until stored during sleep.', 'The books are boring.', 'The room is dark.', 'The teacher is tired.'], 0, 'F', 'learning is not complete until it has been stored during sleep'),
 ]),
 flow('Complete the flow chart. Write ONE WORD from the passage for each answer.',
  ['In light sleep the heartbeat [[1]].', 'In deep sleep the brain waves become slow and [[2]].', 'REM sleep is named after rapid eye [[3]].', 'During REM sleep the muscles are temporarily [[4]].'],
  [(['slows'], 'B', 'the heartbeat slows'), (['large'], 'B', 'slow and large'), (['movements'], 'C', 'rapid eye movements'), (['paralysed'], 'C', 'temporarily paralysed')], 1),
 table('Complete the table. Write ONE WORD from the passage for each answer.', ['Stage', 'Detail'],
  [['Light sleep', 'The sleeper can easily be [[1]]'], ['Deep sleep', 'The body repairs its [[2]]'], ['REM sleep', 'Most [[3]] occur'], ['Melatonin', 'A [[4]] released in the dark']],
  [(['woken'], 'B', 'easily be woken'), (['tissues'], 'B', 'repairs its tissues'), (['dreams'], 'C', 'most dreams occur'), (['hormone'], 'D', 'a hormone called melatonin')], 1),
 feat('Match each statement with the correct group of people, A to D.', ['Babies', 'Young children', 'Teenagers', 'Adults'], [
  ('They sleep for more than twelve hours a day.', 0, 'E', 'more than twelve hours a day'),
  ('Their body clock shifts later by about two hours.', 2, 'D', 'shifts later by about two hours'),
  ('They should sleep for at least seven hours.', 3, 'E', 'at least seven'),
  ('They are recommended to sleep for between eight and ten hours.', 2, 'E', 'between eight and ten hours'),
 ]),
 multi('Which TWO habits to improve sleep are mentioned in paragraph G?', ['Going to bed at the same time every day.', 'Avoiding screens for an hour before bed.', 'Drinking coffee in the evening.', 'Exercising just before bedtime.', 'Sleeping late at weekends.'], [0, 1], [('G', 'go to bed and wake up at the same time every day'), ('G', 'avoid screens for an hour before bed')]),
 head(['A brain that never switches off', 'Cycles of the night', 'The stage of dreams', 'The body\'s clock', 'How much is enough', 'Sleep and learning', 'Habits for better sleep', 'The history of the bed', 'Dreams of animals'],
  [('A', 0, 'the sleeping brain is active'), ('B', 1, 'a series of cycles of about ninety minutes each'), ('C', 2, 'most dreams occur'), ('D', 3, 'an internal body clock'), ('E', 4, 'The amount of sleep that people need depends on their age'), ('F', 5, 'learning is not complete until it has been stored during sleep'), ('G', 6, 'sleep can be improved by simple habits')]),
 info([
  ('a reference to feeling confused after waking', 'B', 'confused and tired'),
  ('a reference to paralysed muscles', 'C', 'temporarily paralysed'),
  ('a reference to a gland in the brain', 'D', 'a small gland in the brain'),
  ('a comparison with jet lag', 'E', 'permanent jet lag'),
  ('a warning about blue light', 'F', 'blue light from phones and tablets'),
 ]),
 ends(['is when the body repairs itself.', 'is when most dreams occur.', 'sets the body clock.', 'stays in the body for many hours.', 'prevents all dreams.', 'makes teenagers wake early.', 'is produced by the eyes.'], [
  ('Deep sleep', 0, 'B', 'the body repairs its tissues'),
  ('REM sleep', 1, 'C', 'most dreams occur'),
  ('Light', 2, 'D', 'Light is the main signal that sets the clock'),
  ('Caffeine', 3, 'G', 'stays in the body for many hours'),
 ]),
 sent(2, [
  ('A typical adult goes through four or five ___ in a night.', ['cycles'], 'B', 'four or five cycles'),
  ('REM stands for rapid eye ___.', ['movement', 'movements'], 'C', 'rapid eye movements'),
  ('Teenagers need between eight and ___ hours of sleep.', ['ten', '10'], 'E', 'eight and ten hours'),
  ('Dr Moreno is a sleep ___.', ['researcher'], 'F', 'sleep researcher'),
 ]),
 short(3, [
  ('Which hormone makes the body feel sleepy?', ['melatonin'], 'D', 'called melatonin'),
  ('How long might the final REM period last?', ['nearly an hour'], 'C', 'nearly an hour'),
  ('How long should you wait before getting up if you cannot sleep?', ['twenty minutes', 'about twenty minutes'], 'G', 'about twenty minutes'),
 ]),
])
