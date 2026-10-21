from lib import *
A = """For most of human history, sleep was regarded as a simple pause in life, a period of rest during which the body and brain did nothing of importance. Over the past fifty years that belief has been overturned. Brain scans show that the sleeping brain is highly active, and that different stages of sleep seem to carry out different tasks. Scientists now consider sleep to be as essential to health as food and water. Yet surveys in many countries suggest that busy adults treat it as the first thing to give up when life becomes crowded, and the consequences of that habit are only now being understood."""
B = """A night of sleep is not a uniform block. It is made up of cycles lasting about ninety minutes, each containing a period of light sleep, a period of deep sleep and a period of rapid eye movement, or REM, sleep, during which most vivid dreaming occurs. Early in the night deep sleep dominates; towards morning, REM periods grow longer. This pattern explains why people who wake after only five or six hours miss out on a disproportionate amount of REM sleep."""
C = """The link between sleep and memory has produced some of the most striking research. Dr Anna Voss asked two groups of students to learn a list of word pairs in the evening. One group slept normally; the other stayed awake all night. After two further nights of recovery sleep, both groups were tested, and the students who had slept on the first night remembered about a third more of the pairs. Voss concludes that sleep soon after learning helps to fix new information in the memory, and that a later night of rest cannot fully repair the loss."""
D = """Teenagers have attracted particular attention. During adolescence the body clock shifts, so that many young people do not feel sleepy until after eleven at night and find it hard to wake before eight in the morning. Professor Kenji Mori studied schools in three districts that moved the start of lessons from eight o'clock to half past nine. Attendance rose, and students reported feeling more alert, although their examination results improved only slightly. Mori admits that the improvement in grades might have been larger if students had not simply gone to bed later."""
E = """Napping is more controversial. Dr Leila Haddad found that a short nap of twenty minutes improved the performance of office workers on afternoon tasks, whereas naps longer than forty minutes left many of them feeling groggy. She advises that anyone who naps should set an alarm, because waking from deep sleep produces a heavy feeling that can last for half an hour. Some employers have therefore begun to provide quiet rooms, although others worry that staff will take advantage. Haddad answers that a rested worker who spends twenty minutes asleep at lunchtime is likely to be more productive than a tired one who spends the same time looking at a screen."""
F = """Modern technology is often blamed for poor sleep. Professor Tom Garrick showed that bright screens in the hour before bed delay the release of melatonin, a hormone that signals to the body that it is time to sleep. However, he points out that many people stay awake because of what they are doing on a device, such as reading stressful messages, and not because of the light. In his view, advice to buy special glasses or filters has been oversold; a better strategy is to put the phone away."""
G = """Taken together, these findings suggest some simple advice. Adults need between seven and nine hours; going to bed and rising at the same time each day helps; and the bedroom should be dark, quiet and cool. It would be foolish to treat sleep as a luxury to be traded for extra work, since people who do so tend, in the long run, to achieve less, not more. A tired employee makes more mistakes, forgets instructions and finds it harder to deal calmly with colleagues, so the hours saved are quickly lost again in repairing errors."""
P = passage('p03', 'The Science of Sleep', 'Psychology', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Each sleep cycle lasts about ninety minutes.', 'T', 'B', 'cycles lasting about ninety minutes'),
  ('Periods of deep sleep become longer towards morning.', 'F', 'B', 'towards morning, REM periods grow longer'),
  ('In Voss\'s study, the students who stayed awake all night were tested the next morning.', 'F', 'C', 'After two further nights of recovery sleep, both groups were tested'),
  ('Voss tested more than a hundred students.', 'NG', 'C', 'Dr Anna Voss asked two groups of students', 'The number of students is never given.'),
  ('The schools in Mori\'s study began lessons at half past nine.', 'T', 'D', 'moved the start of lessons from eight o\'clock to half past nine'),
  ('Examination results rose sharply in Mori\'s study.', 'F', 'D', 'their examination results improved only slightly'),
  ('Naps longer than forty minutes left many workers feeling groggy.', 'T', 'E', 'naps longer than forty minutes left many of them feeling groggy'),
  ('Garrick\'s experiment involved teenagers.', 'NG', 'F', 'Professor Tom Garrick showed that bright screens', 'The passage does not say who took part in Garrick\'s work.'),
  ('Bright screens before bed delay the release of melatonin.', 'T', 'F', 'bright screens in the hour before bed delay the release of melatonin'),
 ]),
 tfng([
  ('People who sacrifice sleep for extra work are likely to achieve less in the long run.', 'Y', 'G', 'tend, in the long run, to achieve less, not more'),
  ('Employers are right to provide quiet rooms for napping.', 'NG', 'E', 'Some employers have therefore begun to provide quiet rooms', 'The writer reports both views and gives no opinion of his own.'),
  ('Sleep should be regarded as a luxury.', 'N', 'G', 'It would be foolish to treat sleep as a luxury'),
  ('Early scientists were correct that nothing important happens during sleep.', 'N', 'A', 'Over the past fifty years that belief has been overturned'),
  ('Research on sleep and memory has produced some remarkable findings.', 'Y', 'C', 'some of the most striking research'),
  ('Most adults today sleep too little.', 'NG', 'G', 'Adults need between seven and nine hours', 'The passage says how much adults need, not how much they get.'),
  ('Going to bed at regular times is useful.', 'Y', 'G', 'going to bed and rising at the same time each day helps'),
  ('A warm bedroom is recommended.', 'N', 'G', 'dark, quiet and cool'),
 ], yn=True),
 feat('Match each statement with the correct researcher, A to D.', ['Dr Anna Voss', 'Professor Kenji Mori', 'Dr Leila Haddad', 'Professor Tom Garrick'], [
  ('Staying awake after learning led to poorer recall even after recovery sleep.', 0, 'C', 'a later night of rest cannot fully repair the loss'),
  ('Moving the start of the school day increased attendance.', 1, 'D', 'Attendance rose'),
  ('Anyone who takes a nap should set an alarm.', 2, 'E', 'anyone who naps should set an alarm'),
  ('What a person does on a device may matter more than the light it gives off.', 3, 'F', 'not because of the light'),
  ('The improvement in grades could have been larger.', 1, 'D', 'the improvement in grades might have been larger'),
  ('A twenty-minute nap improved afternoon performance.', 2, 'E', 'a short nap of twenty minutes improved the performance of office workers'),
  ('Special glasses and filters have been oversold.', 3, 'F', 'has been oversold'),
 ]),
 mcq([
  ('Why do people who sleep for only five or six hours miss out on REM sleep?', ['REM periods are longer later in the night.', 'Deep sleep replaces REM sleep.', 'Dreams wake them too early.', 'Their cycles are shorter than ninety minutes.'], 0, 'B', 'towards morning, REM periods grow longer'),
  ('Why do many teenagers find it hard to wake before eight?', ['They have too much homework.', 'Their body clock shifts during adolescence.', 'They sleep in cycles of two hours.', 'They use screens late at night.'], 1, 'D', 'During adolescence the body clock shifts'),
  ('According to Dr Haddad, what causes the heavy feeling after a long nap?', ['an alarm clock', 'working at night', 'waking from deep sleep', 'a lack of REM sleep'], 2, 'E', 'waking from deep sleep produces a heavy feeling'),
 ]),
 head(['The structure of a night\'s sleep', 'Evidence that sleep strengthens memory', 'Starting school later', 'The benefits and risks of short naps', 'Do screens really keep us awake?', 'Practical advice from the findings', 'How animals sleep in the wild', 'Why dreams are forgotten'],
  [('B', 0, 'A night of sleep is not a uniform block'), ('C', 1, 'The link between sleep and memory'), ('D', 2, 'moved the start of lessons from eight o\'clock to half past nine'), ('E', 3, 'Napping is more controversial'), ('F', 4, 'Modern technology is often blamed for poor sleep'), ('G', 5, 'these findings suggest some simple advice')]),
 info([
  ('a description of how the pattern of sleep changes through the night', 'B', 'Early in the night deep sleep dominates'),
  ('a comparison between two groups of students', 'C', 'One group slept normally; the other stayed awake all night'),
  ('a reason why teenagers go to bed late', 'D', 'do not feel sleepy until after eleven at night'),
  ('a concern felt by some employers', 'E', 'others worry that staff will take advantage'),
  ('an explanation of the role of a hormone', 'F', 'a hormone that signals to the body that it is time to sleep'),
  ('a description of the ideal bedroom', 'G', 'dark, quiet and cool'),
 ]),
 sent(3, [
  ('Sleep cycles last around ___ minutes.', ['ninety', '90'], 'B', 'cycles lasting about ninety minutes'),
  ('Most vivid dreaming occurs during ___ sleep.', ['rem'], 'B', 'rapid eye movement, or REM, sleep, during which most vivid dreaming occurs'),
  ('Voss\'s students learned a list of ___ in the evening.', ['word pairs'], 'C', 'a list of word pairs'),
  ('Mori\'s schools moved the start of lessons to ___.', ['half past nine', '9.30', '9:30'], 'D', 'to half past nine'),
  ('A nap longer than ___ minutes often left workers groggy.', ['forty', '40'], 'E', 'naps longer than forty minutes'),
  ('Garrick thinks the value of special glasses has been ___.', ['oversold'], 'F', 'has been oversold'),
 ]),
 short(3, [
  ('Which hormone does screen light delay?', ['melatonin'], 'F', 'delay the release of melatonin'),
  ('How many hours of sleep do adults need?', ['seven and nine', '7 and 9', 'seven to nine', '7 to 9'], 'G', 'between seven and nine hours'),
  ('What should anyone who naps set?', ['an alarm', 'alarm'], 'E', 'should set an alarm'),
  ('What have some employers begun to provide?', ['quiet rooms'], 'E', 'provide quiet rooms'),
 ]),
 summ('Complete the summary. Write ONE WORD ONLY from the passage for each answer.',
  'Dr Voss asked two groups of students to learn [[1]] pairs. One group slept normally and the other stayed [[2]] all night. After two nights of recovery sleep, those who had slept on the first night remembered about a [[3]] more. Voss concludes that a later night of rest cannot fully [[4]] the loss.',
  [(['word'], 'C', 'a list of word pairs'), (['awake'], 'C', 'stayed awake all night'), (['third'], 'C', 'about a third more'), (['repair'], 'C', 'cannot fully repair the loss')], 1),
 table('Complete the table. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Researcher', 'Topic', 'Finding'],
  [['Voss', 'Sleep and [[1]]', 'Sleep soon after learning helps to fix new information'], ['Mori', 'Later school start times', 'Attendance rose; grades improved only slightly'], ['Haddad', 'A short [[2]] for office workers', 'Twenty minutes improved afternoon performance'], ['Garrick', 'Bright [[3]] before bed', 'The release of [[4]] is delayed']],
  [(['memory'], 'C', 'The link between sleep and memory'), (['nap', 'naps'], 'E', 'a short nap'), (['screens'], 'F', 'bright screens'), (['melatonin'], 'F', 'delay the release of melatonin')], 2),
])
