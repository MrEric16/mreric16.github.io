from lib import *
A = """Ask a group of students how they revise and most will give the same answer: they read their notes again, and they highlight the important parts. These habits feel productive, and they are popular because they are easy. Yet psychologists who have compared study methods for decades rank rereading and highlighting among the least effective ways to learn. The methods that work best tend to be less comfortable, and for that reason fewer students choose them."""
B = """The first of these is retrieval practice, which simply means testing yourself on material instead of looking at it again. In a well-known experiment, Dr Katherine Doyle asked two groups of students to study a short science text. One group read it four times. The other read it once and then wrote down everything they could remember. A week later, the second group recalled about half as much again as the first, even though they had spent less time with the text. Strangely, the students who had reread the text felt more confident that they knew it."""
C = """The second method is spacing, which means spreading study over several days instead of cramming it into one long session. Memory fades quickly at first and then more slowly, and each time a person recalls something just as it starts to slip away, the memory becomes stronger and lasts longer. Three study sessions of an hour, on different days, will produce better results than a single three-hour session the night before a test, although the cramming student may feel well prepared at the time."""
D = """The third method is called interleaving. Most textbooks present one type of problem at a time, so that students practise a skill twenty times in a row before moving on. Professor Marcus Webb compared this with a mixed approach, in which different kinds of mathematics problem were shuffled together. During the practice sessions, the students who practised one type at a time made fewer mistakes. A week later, however, in a test, the students who had practised a mixture solved roughly twice as many problems correctly. Webb explains that mixing forces the learner to decide which method a problem needs, and that deciding is exactly what an examination demands."""
E = """Why do students avoid techniques that work? Psychologists point to what they call the illusion of fluency. When material is familiar, because we have just read it or because we have just practised the same skill, it feels easy, and we mistake that feeling for learning. Effortful methods are slower and produce more errors, and so they feel like failures. Researchers describe the extra effort as a 'desirable difficulty': a challenge that makes learning harder in the short term but better in the long term."""
F = """Teachers can help by building these methods into lessons. Short, frequent quizzes, which count for little or nothing towards a final grade, give students regular practice at retrieval. Homework that returns to topics from earlier in the term supplies spacing, and a worksheet that mixes several kinds of question supplies interleaving. Some teachers worry that frequent testing will make their students anxious, but studies suggest that low-stakes quizzes actually reduce anxiety, because students become used to being tested."""
G = """For students working alone, the advice is simple. Close the book and write down what you remember before you check your notes. Make flashcards, and go through them again after a day, a few days and a week. Return to old topics instead of leaving them behind, and mix different kinds of exercise in a single session. None of this will feel as pleasant as reading a neat page of highlighted notes, but, as the research shows, it is the discomfort that does the work."""
P = passage('p13', 'Learning How to Learn', 'Education', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Most students revise by rereading and highlighting their notes.', 'T', 'A', 'most will give the same answer: they read their notes again, and they highlight'),
  ('Psychologists rank rereading as one of the most effective study methods.', 'F', 'A', 'among the least effective ways to learn'),
  ('Retrieval practice means looking at material again.', 'F', 'B', 'testing yourself on material instead of looking at it again'),
  ('In Dr Doyle\'s experiment, one group read the text four times.', 'T', 'B', 'One group read it four times'),
  ('The students who reread the text felt more confident than the others.', 'T', 'B', 'felt more confident that they knew it'),
  ('Dr Doyle\'s experiment involved more than two hundred students.', 'NG', 'B', 'asked two groups of students to study a short science text', 'The number of students is not given.'),
  ('Three one-hour sessions on different days work better than one three-hour session.', 'T', 'C', 'Three study sessions of an hour, on different days, will produce better results'),
  ('Memory fades more slowly at first and then more quickly.', 'F', 'C', 'Memory fades quickly at first and then more slowly'),
  ('In Webb\'s practice sessions, students who practised one type of problem made fewer mistakes.', 'T', 'D', 'made fewer mistakes'),
  ('Webb\'s students were tested on the same day as the practice.', 'F', 'D', 'A week later, however, in a test'),
  ('Low-stakes quizzes make students more anxious.', 'F', 'F', 'low-stakes quizzes actually reduce anxiety'),
 ]),
 feat('Match each statement with the correct researcher, A or B. You may use either letter more than once.', ['Dr Katherine Doyle', 'Professor Marcus Webb'], [
  ('Students who tested themselves remembered more after a week.', 0, 'B', 'recalled about half as much again as the first'),
  ('Mixed practice led to about twice as many correct answers on a test.', 1, 'D', 'solved roughly twice as many problems correctly'),
  ('Students who reread a text were more confident than those who tested themselves.', 0, 'B', 'felt more confident that they knew it'),
  ('Mixing problem types forces learners to decide which method is needed.', 1, 'D', 'mixing forces the learner to decide which method a problem needs'),
  ('Students wrote down all they could remember.', 0, 'B', 'wrote down everything they could remember'),
 ], cls=True),
 mcq([
  ('Why do many students prefer rereading and highlighting?', ['It is more effective.', 'It is easy.', 'It is recommended by teachers.', 'It takes less time.'], 1, 'A', 'they are popular because they are easy'),
  ('What does the writer say about the cramming student?', ['He remembers more in the long term.', 'He may feel well prepared.', 'He needs three hours of sleep.', 'He avoids retrieval practice.'], 1, 'C', 'the cramming student may feel well prepared at the time'),
  ('What is meant by a "desirable difficulty"?', ['an exercise that is too hard to complete', 'a challenge that improves long-term learning', 'a problem teachers should avoid', 'a method that feels easy'], 1, 'E', 'makes learning harder in the short term but better in the long term'),
 ]),
 head(['Popular methods that do not work well', 'Testing yourself', 'Spreading study over time', 'Mixing the types of problem', 'Why the feeling of ease is misleading', 'What teachers can do', 'Advice for students working alone', 'The history of school examinations'],
  [('A', 0, 'among the least effective ways to learn'), ('B', 1, 'The first of these is retrieval practice'), ('C', 2, 'The second method is spacing'), ('D', 3, 'The third method is called interleaving'), ('E', 4, 'Why do students avoid techniques that work?'), ('F', 5, 'Teachers can help by building these methods into lessons')]),
 info([
  ('a reason why familiar material seems easy', 'E', 'When material is familiar'),
  ('a suggestion for using flashcards at intervals', 'G', 'go through them again after a day, a few days and a week'),
  ('a concern that some teachers have', 'F', 'Some teachers worry that frequent testing will make their students anxious'),
  ('a comparison between three sessions and a single long session', 'C', 'Three study sessions of an hour'),
  ('a description of what one group of students did after reading', 'B', 'wrote down everything they could remember'),
  ('a statement that these methods may feel unpleasant', 'G', 'None of this will feel as pleasant as reading a neat page'),
 ]),
 sent(2, [
  ('Doyle asked students to study a short ___ text.', ['science'], 'B', 'a short science text'),
  ('Spacing means spreading study over several ___.', ['days'], 'C', 'spreading study over several days'),
  ('Webb mixed different kinds of ___ problem together.', ['mathematics', 'maths', 'math'], 'D', 'different kinds of mathematics problem'),
  ('The illusion of ___ makes familiar material feel easy.', ['fluency'], 'E', 'the illusion of fluency'),
  ('Homework that returns to earlier topics supplies ___.', ['spacing'], 'F', 'supplies spacing'),
  ('Students should write down what they remember before checking their ___.', ['notes'], 'G', 'before you check your notes'),
 ]),
 short(3, [
  ('How many times did one group read the text in Doyle\'s experiment?', ['four', '4', 'four times', '4 times'], 'B', 'read it four times'),
  ('When did students in Webb\'s study take their test?', ['a week later', 'one week later'], 'D', 'A week later, however, in a test'),
  ('What do low-stakes quizzes count for towards a final grade?', ['little or nothing'], 'F', 'count for little or nothing'),
  ('Which topics should students return to instead of leaving them behind?', ['old topics', 'old'], 'G', 'Return to old topics'),
 ]),
 table('Complete the table. Write ONE WORD ONLY from the passage for each answer.', ['Technique', 'What it involves'],
  [['Retrieval practice', 'Testing [[1]] on the material'], ['Spacing', 'Spreading study over several [[2]]'], ['Interleaving', 'Different types of problem are [[3]] together'], ['Quizzes', 'Give students regular practice at [[4]]']],
  [(['yourself'], 'B', 'testing yourself'), (['days'], 'C', 'over several days'), (['shuffled'], 'D', 'shuffled together'), (['retrieval'], 'F', 'regular practice at retrieval')], 1),
 summ('Complete the summary. Write ONE WORD ONLY from the passage for each answer.',
  'Students prefer rereading because it feels [[1]], but effective methods are less comfortable. When material is familiar, we mistake that feeling for [[2]]. Researchers call the extra effort a desirable [[3]], because it makes learning better in the long term.',
  [(['easy'], 'E', 'it feels easy'), (['learning'], 'E', 'mistake that feeling for learning'), (['difficulty'], 'E', 'desirable difficulty')], 1),
])
