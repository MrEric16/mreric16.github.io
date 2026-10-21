from lib import *
A = """Most people regard forgetting as a failure of the brain, and they are probably wrong. In the 1880s the German psychologist Hermann Ebbinghaus tested himself by learning lists of nonsense syllables such as ZOF and WID, and he found that his memory of them fell sharply within an hour and continued to decline more slowly over the following days. This 'forgetting curve' has been confirmed many times. Yet a growing number of scientists argue that forgetting is not a flaw but a feature of a healthy mind."""
B = """Their reasoning is practical. Every day the brain receives far more information than it could ever use, and keeping all of it would make the important details hard to find. A person who remembered everything would struggle to think clearly. The best-known case is that of a Russian journalist, known only as S., who was studied by the psychologist Alexander Luria in the 1920s. S. could recall long tables of numbers after many years, but he found it difficult to understand a simple story, because each word brought a flood of images with it."""
C = """Psychologists distinguish between several kinds of forgetting. In the first, the memory was never properly stored, which usually happens when attention was elsewhere. A person who cannot say which way the head on a coin faces has probably seen coins thousands of times without really noticing. In the second, the memory is stored but fades through lack of use. In the third, the memory is still there, but other memories interfere with it. Anyone who has moved house and then tried to remember the old telephone number will recognise this."""
D = """Retrieval, the act of bringing a memory back, is itself a form of learning. In a well-known experiment at Washington University, students who studied a text once and then tried to recall it from memory performed better a week later than students who read the text several times. Yet most students prefer re-reading, because it feels easier and creates a sense of familiarity. Professor Rachel Dunmore, who has reviewed the evidence, calls this 'the most expensive mistake in education', since it persuades people to spend hours on a method that produces little."""
E = """Sleep plays a central role in deciding what is kept. During deep sleep the brain replays the events of the day, and connections that are important are strengthened while weaker ones are allowed to fade. People who sleep after learning remember more than those who stay awake for the same period, although the benefit varies from one individual to another. Researchers are cautious about claims that listening to recordings while asleep can teach a language, because the evidence for it remains weak."""
F = """Technology is changing what we choose to remember. When people expect to find a fact later on a search engine, they remember where to find it rather than the fact itself, an effect nicknamed 'the Google effect'. Some commentators fear that this will weaken the mind. Others point out that people have always relied on tools, from written lists to notebooks, and that using the tools frees attention for harder tasks. The evidence so far does not settle the argument, and larger studies are needed."""
G = """For those who wish to remember more, researchers offer a few simple suggestions. Spread study over several days instead of one long session, since a gap forces the brain to work harder at retrieval. Test yourself regularly. Explain ideas aloud in your own words, because this quickly shows what you have not understood. Sleep properly. None of these methods is new, and none is easy. But all are supported by decades of research, which is more than can be said for most of the products that claim to improve memory."""
P = passage('p18', 'Why We Forget', 'Psychology', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The writer believes that forgetting is usually a sign of a damaged brain.', 'N', 'A', 'Most people regard forgetting as a failure of the brain, and they are probably wrong'),
  ('Ebbinghaus found that his memory fell most quickly in the first hour.', 'Y', 'A', 'fell sharply within an hour and continued to decline more slowly'),
  ('The writer thinks that a person who remembered everything would think more clearly.', 'N', 'B', 'A person who remembered everything would struggle to think clearly'),
  ('The writer believes that S. understood stories easily.', 'N', 'B', 'he found it difficult to understand a simple story'),
  ('The writer says that re-reading is the most effective way to study.', 'N', 'D', 'Yet most students prefer re-reading', 'Re-reading is described as what students prefer, in contrast to recall, which worked better.'),
  ('The writer is sure that learning during sleep is impossible.', 'N', 'E', 'the evidence for it remains weak', 'The writer says the evidence is weak, not that it is impossible.'),
  ('The writer thinks more research on the Google effect is needed.', 'Y', 'F', 'larger studies are needed'),
  ('The writer believes that most students sleep too little.', 'NG', 'E', 'People who sleep after learning remember more', 'The passage never says how much students sleep.'),
  ('The writer thinks that many memory products have little scientific support.', 'Y', 'G', 'more than can be said for most of the products that claim to improve memory'),
 ], yn=True),
 mcq([
  ('Why did S. find stories difficult?', ['He forgot the numbers.', 'Each word brought a flood of images.', 'He could not read.', 'He slept badly.'], 1, 'B', 'each word brought a flood of images with it'),
  ('What does the writer suggest the coin example shows?', ['People rarely handle coins.', 'Memories fade with age.', 'Some things are never properly stored.', 'Coins are hard to describe.'], 2, 'C', 'without really noticing'),
  ('What is the writer\'s attitude to the Google effect?', ['Alarmed.', 'Scornful.', 'Cautiously open-minded.', 'Enthusiastic.'], 2, 'F', 'The evidence so far does not settle the argument'),
 ]),
 feat('Match each statement with the correct person, A to C.', ['Hermann Ebbinghaus', 'Alexander Luria', 'Rachel Dunmore'], [
  ('tested his own memory with meaningless syllables', 0, 'A', 'tested himself by learning lists of nonsense syllables'),
  ('studied a man with an extraordinary memory', 1, 'B', 'who was studied by the psychologist Alexander Luria'),
  ('has reviewed the evidence on re-reading', 2, 'D', 'who has reviewed the evidence'),
  ('described a pattern of forgetting that has been confirmed many times', 0, 'A', 'This \'forgetting curve\' has been confirmed many times'),
  ('criticised a common habit as costly', 2, 'D', 'the most expensive mistake in education'),
 ], cls=True),
 head(['A new view of forgetting', 'Too much memory, too little understanding', 'Three ways a memory is lost', 'Recall beats re-reading', 'The brain at night', 'Tools and the mind', 'Practical advice', 'The invention of the notebook', 'Why students fail exams'],
  [('A', 0, 'a growing number of scientists argue that forgetting'), ('B', 1, 'A person who remembered everything would struggle'), ('C', 2, 'Psychologists distinguish between several kinds of forgetting'), ('D', 3, 'students who studied a text once and then tried to recall it'), ('E', 4, 'During deep sleep the brain replays the events of the day'), ('F', 5, 'Technology is changing what we choose to remember'), ('G', 6, 'researchers offer a few simple suggestions')]),
 ends(['have been confirmed by many later studies.', 'was never stored properly in the first place.', 'can be improved by testing yourself.', 'is strengthened while weaker connections fade.', 'depends only on how much a person sleeps.', 'is easy to achieve with a new product.', 'was invented in the twentieth century.'], [
  ('Ebbinghaus\'s results', 0, 'A', 'has been confirmed many times'),
  ('A memory that is not noticed', 1, 'C', 'the memory was never properly stored'),
  ('Memory of a text', 2, 'D', 'tried to recall it from memory performed better'),
  ('An important connection in the brain', 3, 'E', 'connections that are important are strengthened'),
 ]),
 multi('Which TWO study methods are recommended in paragraph G?', ['Studying over several days.', 'Testing yourself.', 'Reading each page several times.', 'Studying late at night.', 'Listening to recordings.'], [0, 1], [('G', 'Spread study over several days'), ('G', 'Test yourself regularly')]),
 sent(2, [
  ('Ebbinghaus learned lists of ___ syllables.', ['nonsense'], 'A', 'nonsense syllables'),
  ('S. was studied in the ___.', ['1920s'], 'B', 'in the 1920s'),
  ('An experiment on recall took place at ___ University.', ['washington'], 'D', 'Washington University'),
  ('Using tools frees ___ for harder tasks.', ['attention'], 'F', 'frees attention for harder tasks'),
 ]),
 short(3, [
  ('What did S. work as?', ['a journalist', 'journalist'], 'B', 'a Russian journalist'),
  ('What is the third kind of forgetting caused by?', ['interference', 'other memories'], 'C', 'other memories interfere with it'),
  ('What is the effect nicknamed?', ['the google effect', 'google effect'], 'F', 'the Google effect'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Some scientists believe that forgetting is a [[1]] of a healthy mind rather than a flaw. Trying to [[2]] a text helps more than reading it again, and [[3]] helps the brain to keep important connections. Study that is [[4]] over several days works best.',
  [(['feature'], 'A', 'a feature of a healthy mind'), (['recall'], 'D', 'tried to recall it'), (['sleep'], 'E', 'Sleep plays a central role'), (['spread'], 'G', 'Spread study over several days')], 1,
  bank=['feature', 'recall', 'sleep', 'spread', 'harmful', 'copy', 'noise', 'shorter']),
])
