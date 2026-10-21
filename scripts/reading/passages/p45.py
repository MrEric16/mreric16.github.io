from lib import *
from svgs import *
A = """How people spend their time says a great deal about their lives. Researchers who study this subject often ask volunteers to keep a diary of everything they do in a normal day, and they then show the results as a circle divided into slices, each one representing a share of the twenty-four hours. This passage describes four people and their daily routines. Their circles look quite different, even though each person has exactly the same amount of time. All four agreed to be described by their first names, and all four kept their diaries for a full month, so that the figures do not depend on a single unusual day."""
B = """Dilnoza is a student in her final year at school. She divides her day into three equal parts: one third for sleep, one third for lessons and homework, and one third for everything else, including meals, travelling, friends and rest. She says that this pattern is not accidental, because she planned it carefully at the beginning of the year, and it has helped her to remain calm during the busy weeks before her examinations."""
C = """Bahodir is a doctor in a city hospital. Half of his day is spent at work, and the other half is divided equally between sleep and everything else. When he is on night duty, the pattern changes, but over a month the average is close to this. He admits that there is little time left for hobbies, and that he sometimes sleeps for only five hours. He would like to work fewer hours, but there are not enough doctors in the hospital."""
D = """Madina runs a small farm outside the city. In the summer, she works from before sunrise until late in the evening, and about three quarters of her day goes to the farm, leaving only one quarter for sleep, meals and family. In winter, there is far less to do, and her circle looks completely different. She says that farming is not a job but a way of life, and that she accepts the long hours because she loves the work. Her children help at weekends and during the harvest, and she hopes that one of them will take over the farm when she is older."""
E = """Jasur is a retired teacher. His day has one large slice and four small, equal ones. The large slice, about sixty per cent of the day, is for sleep and rest, which he needs more than he used to, since he now gets tired more easily than he did when he was young and often takes a short nap after lunch. The small slices are for walking, reading, visiting neighbours and helping his grandchildren with their homework. He says that after a lifetime of rushing, he enjoys having time to do nothing in particular."""
F = """What do these circles show? According to Dr Karina Petrova, a researcher in time use, they show that the amount of time is the same for everybody, but that the choices are very different, and that these choices are shaped by age, work and the needs of family. She adds that people who are satisfied with their lives are not always those with the most free time, but those whose time is spent on activities that matter to them."""
G = """It can be useful to draw one's own circle. Many people are surprised to find how much time goes to activities that they did not choose, such as waiting, scrolling on a phone or travelling. Dr Petrova suggests keeping a diary for just one week and asking, at the end, which slices should be larger and which smaller. The exercise costs nothing, she says, and it often leads to small changes that make a surprising difference to a person's well-being."""
P = passage('p45', 'Four Daily Routines', 'Society', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which pie chart, A to D, shows the daily routine of each person described in the passage?', [(pie([34, 33, 33]), 160, 120), (pie([50, 25, 25]), 160, 120), (pie([75, 25]), 160, 120), (pie([60, 10, 10, 10, 10]), 160, 120)], [
  ('Dilnoza', 0, 'B', 'three equal parts'),
  ('Bahodir', 1, 'C', 'Half of his day is spent at work'),
  ('Madina in summer', 2, 'D', 'about three quarters of her day goes to the farm'),
  ('Jasur', 3, 'E', 'one large slice and four small, equal ones'),
 ]),
 tfng([
  ('Researchers ask volunteers to keep diaries of their day.', 'T', 'A', 'keep a diary of everything they do in a normal day'),
  ('Every person has a different amount of time.', 'F', 'A', 'exactly the same amount of time'),
  ('Dilnoza spends one third of her day sleeping.', 'T', 'B', 'one third for sleep'),
  ('Dilnoza\'s pattern was an accident.', 'F', 'B', 'she planned it carefully'),
  ('Bahodir sometimes sleeps for only five hours.', 'T', 'C', 'only five hours'),
  ('Bahodir works at a private clinic.', 'NG', 'C', 'a doctor in a city hospital', 'The passage says it is a city hospital, not whether it is public or private.'),
  ('Madina\'s winter routine is the same as her summer routine.', 'F', 'D', 'her circle looks completely different'),
  ('Jasur is bored in retirement.', 'F', 'E', 'he enjoys having time to do nothing in particular'),
  ('Dr Petrova says people with the most free time are the happiest.', 'F', 'F', 'not always those with the most free time'),
 ]),
 mcq([
  ('Why would Bahodir like to work fewer hours?', ['He dislikes medicine.', 'He has little time for hobbies.', 'He is retiring.', 'He has moved abroad.'], 1, 'C', 'there is little time left for hobbies'),
  ('What does Madina say about farming?', ['It is a hobby.', 'It is a way of life.', 'It is easy.', 'It is badly paid.'], 1, 'D', 'a way of life'),
  ('What does Dr Petrova suggest?', ['Sleeping less.', 'Keeping a diary for a week.', 'Working more.', 'Buying a new phone.'], 1, 'G', 'keeping a diary for just one week'),
 ]),
 multi('Which TWO activities does Jasur enjoy, according to paragraph E?', ['Walking.', 'Visiting neighbours.', 'Playing chess.', 'Travelling abroad.', 'Gardening.'], [0, 1], [('E', 'walking, reading, visiting neighbours'), ('E', 'walking, reading, visiting neighbours')]),
 head(['A way of showing time', 'A balanced plan for a student', 'The long hours of a doctor', 'A life ruled by the seasons', 'The slower pace of retirement', 'What the circles reveal', 'Drawing your own circle', 'The history of clocks', 'How to cook a meal'],
  [('A', 0, 'This passage describes four people'), ('B', 1, 'She divides her day into three equal parts'), ('C', 2, 'Half of his day is spent at work'), ('D', 3, 'In the summer, she works from before sunrise'), ('E', 4, 'a retired teacher'), ('F', 5, 'What do these circles show'), ('G', 6, 'It can be useful to draw one\'s own circle')]),
 info([
  ('a reference to a student\'s examinations', 'B', 'busy weeks before her examinations'),
  ('a reason why a doctor cannot work fewer hours', 'C', 'not enough doctors in the hospital'),
  ('a comparison of summer with winter', 'D', 'In winter, there is far less to do'),
  ('a list of small activities in retirement', 'E', 'walking, reading, visiting neighbours and helping his grandchildren'),
  ('a mention of activities that people did not choose', 'G', 'waiting, scrolling on a phone or travelling'),
 ]),
 sent(2, [
  ('Dilnoza is in her ___ year at school.', ['final'], 'B', 'her final year at school'),
  ('Bahodir is a doctor in a city ___.', ['hospital'], 'C', 'a city hospital'),
  ('Madina runs a small ___.', ['farm'], 'D', 'a small farm'),
  ('Dr Petrova is a researcher in ___ use.', ['time'], 'F', 'a researcher in time use'),
 ]),
 short(3, [
  ('What share of Jasur\'s day goes to sleep and rest?', ['sixty per cent', '60 per cent', '60%'], 'E', 'about sixty per cent of the day'),
  ('What does the circle represent?', ['twenty-four hours', '24 hours'], 'A', 'the twenty-four hours'),
  ('What does Dr Petrova say the exercise costs?', ['nothing'], 'G', 'costs nothing'),
 ]),
])
