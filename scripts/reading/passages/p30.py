from lib import *
A = """For most of history, dreams were thought to carry messages from gods, spirits or the dead. The ancient Egyptians recorded dreams on papyrus, and the Greeks built temples where the sick slept in the hope of receiving a cure from a dream. It was only in the twentieth century that dreaming became a subject of laboratory research, after scientists discovered a stage of sleep in which the eyes move rapidly beneath the lids and the brain is almost as active as when awake."""
B = """This stage, known as REM sleep, was identified in 1953 at the University of Chicago. Subjects woken during REM sleep reported vivid dreams about four times out of five, while those woken at other times rarely did. We now know that the typical adult has four or five REM periods each night, and that the longest, towards morning, can last nearly an hour. During REM the body is almost paralysed, which prevents us from acting out our dreams, although in some people this mechanism fails."""
C = """Why we dream remains unknown, and several theories compete. Freud argued that dreams express hidden wishes that the mind has pushed out of everyday thought, but his ideas have little support from modern experiments. A second theory, known as activation-synthesis, proposes that dreams are the brain's attempt to make sense of random electrical signals produced during sleep. Critics point out that dreams are often far more organised and emotional than random signals would produce, and that the theory does not explain why the same themes recur."""
D = """A third theory, which has attracted much attention, says that dreaming helps memory. During sleep, the brain replays the events of the day and decides which to keep, and dreams may be the conscious side of that process. In one experiment, volunteers who dreamed about a maze they had been learning performed much better when tested later than those who did not. Not everyone accepts the explanation, and some researchers argue that dreams are a by-product, like the noise of a machine, with no function of their own."""
E = """A fourth theory suggests that dreams are a kind of rehearsal for threats. The Finnish researcher Antti Revonsuo has proposed that our ancestors who dreamed about danger became better at facing it, and that natural selection therefore favoured dreaming. The theory fits the fact that dreams so often contain fear, chase and failure, even in the lives of people who are safe and comfortable. On the other hand, many dreams are quite ordinary, and some contain pleasant or silly events that have no obvious survival value."""
F = """Some people can control their dreams. In a lucid dream, the sleeper knows that he or she is dreaming and may be able to change what happens. Researchers have shown that lucid dreamers can send signals to the laboratory by moving their eyes in a pre-arranged pattern, which proves that they are aware during the dream. Some athletes and musicians practise their skills in lucid dreams, and early results suggest that this may help real performance, although the research is limited and the numbers of people tested are small."""
G = """Whatever their purpose, dreams remain a source of fascination. Writers, scientists and artists have credited dreams with ideas: the chemist Kekulé said that the shape of the benzene ring came to him in a dream, and Mary Shelley said that the idea for Frankenstein came to her in one. Most researchers today are cautious about claims that a particular dream has a fixed meaning. As Professor Hannah Lindqvist puts it, 'a dream is not a message to be decoded but an experience to be understood.'"""
P = passage('p30', 'Why Do We Dream?', 'Psychology', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The ancient Greeks built temples for people who hoped to be cured by dreams.', 'T', 'A', 'built temples where the sick slept'),
  ('Dreaming was studied in laboratories in the nineteenth century.', 'F', 'A', 'only in the twentieth century'),
  ('REM sleep was identified in Chicago.', 'T', 'B', 'at the University of Chicago'),
  ('People woken outside REM sleep usually report vivid dreams.', 'F', 'B', 'those woken at other times rarely did'),
  ('Freud\'s ideas about dreams are strongly supported by modern experiments.', 'F', 'C', 'little support from modern experiments'),
  ('Activation-synthesis theory explains why dream themes recur.', 'F', 'C', 'does not explain why the same themes recur'),
  ('Volunteers who dreamed about a maze later did better in a test.', 'T', 'D', 'performed much better when tested later'),
  ('Revonsuo is a Swedish researcher.', 'F', 'E', 'The Finnish researcher'),
  ('Many lucid dreamers are professional athletes.', 'NG', 'F', 'Some athletes and musicians practise their skills in lucid dreams', 'The proportion of lucid dreamers who are athletes is not given.'),
 ]),
 mcq([
  ('What happens to the body during REM sleep?', ['It becomes very active.', 'It is almost paralysed.', 'It wakes briefly.', 'It becomes cold.'], 1, 'B', 'almost paralysed'),
  ('What is the main criticism of activation-synthesis theory?', ['It is too old.', 'Dreams are too organised for random signals.', 'It ignores sleep.', 'It cannot be tested.'], 1, 'C', 'far more organised and emotional than random signals would produce'),
  ('What does the threat-rehearsal theory fit?', ['The fear found in many dreams.', 'The length of REM periods.', 'The rarity of lucid dreams.', 'The use of eye movements.'], 0, 'E', 'dreams so often contain fear, chase and failure'),
 ]),
 feat('Match each idea with the correct theory, A to C.', ['Dreams are the brain\'s response to random signals', 'Dreams help to store memories', 'Dreams prepare us for danger'], [
  ('Dreams may be the conscious side of a process of choosing what to keep.', 1, 'D', 'dreams may be the conscious side of that process'),
  ('Natural selection favoured those who dreamed about danger.', 2, 'E', 'natural selection therefore favoured dreaming'),
  ('Dreams are an attempt to make sense of electrical signals.', 0, 'C', 'to make sense of random electrical signals'),
  ('Volunteers who dreamed about a maze performed better.', 1, 'D', 'volunteers who dreamed about a maze'),
 ]),
 head(['Ancient beliefs and modern science', 'The discovery of a sleep stage', 'Two older ideas under attack', 'A role for memory', 'A training ground for survival', 'Taking control of dreams', 'The value of dreams and the dangers of interpretation', 'The history of the Egyptian papyrus', 'How to sleep well'],
  [('A', 0, 'For most of history, dreams were thought to carry messages'), ('B', 1, 'This stage, known as REM sleep'), ('C', 2, 'Why we dream remains unknown'), ('D', 3, 'says that dreaming helps memory'), ('E', 4, 'a kind of rehearsal for threats'), ('F', 5, 'Some people can control their dreams'), ('G', 6, 'Whatever their purpose, dreams remain a source of fascination')]),
 info([
  ('a reference to a famous psychologist', 'C', 'Freud'),
  ('a reference to a machine', 'D', 'like the noise of a machine'),
  ('a mention of a method of communicating from within a dream', 'F', 'moving their eyes in a pre-arranged pattern'),
  ('a mention of a scientist who credited a dream', 'G', 'the chemist Kekulé'),
  ('a figure for the number of REM periods in a night', 'B', 'four or five REM periods each night'),
 ]),
 multi('Which TWO reasons are given in paragraph E for doubting the threat-rehearsal theory?', ['Many dreams are quite ordinary.', 'Some dreams contain pleasant or silly events.', 'Animals do not dream.', 'Dreams last only a few seconds.', 'People forget most of their dreams.'], [0, 1], [('E', 'many dreams are quite ordinary'), ('E', 'pleasant or silly events')]),
 ends(['can last nearly an hour.', 'were thought to carry messages from gods.', 'can signal by moving their eyes.', 'is said to have inspired Frankenstein.', 'was discovered by the Egyptians.', 'is the same for everyone.', 'was proved in 1953.'], [
  ('The longest REM period', 0, 'B', 'can last nearly an hour'),
  ('For most of history, dreams', 1, 'A', 'thought to carry messages from gods, spirits or the dead'),
  ('A lucid dreamer', 2, 'F', 'send signals to the laboratory by moving their eyes'),
  ('A dream', 3, 'G', 'the idea for Frankenstein came to her in one'),
 ]),
 sent(2, [
  ('In REM sleep the eyes move ___ beneath the lids.', ['rapidly'], 'A', 'move rapidly beneath the lids'),
  ('Subjects woken during REM reported vivid dreams about four times out of ___.', ['five'], 'B', 'four times out of five'),
  ('Some researchers say dreams are a ___ with no function.', ['by-product', 'byproduct'], 'D', 'a by-product'),
  ('Kekulé said that the shape of the benzene ring came to him in a ___.', ['dream'], 'G', 'came to him in a dream'),
 ]),
 short(3, [
  ('Where did the Egyptians record dreams?', ['on papyrus', 'papyrus'], 'A', 'on papyrus'),
  ('What is a dream, according to Professor Lindqvist?', ['an experience'], 'G', 'an experience to be understood'),
  ('What kind of dream lets the sleeper know he or she is dreaming?', ['lucid', 'a lucid dream'], 'F', 'In a lucid dream'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Dreaming was first studied in laboratories after scientists found [[1]] sleep. One theory says that dreams help [[2]], while another says that they are a rehearsal for [[3]]. Some people can control their dreams, which are called [[4]] dreams.',
  [(['REM'], 'B', 'known as REM sleep'), (['memory'], 'D', 'dreaming helps memory'), (['threats'], 'E', 'rehearsal for threats'), (['lucid'], 'F', 'lucid dream')], 1,
  bank=['REM', 'memory', 'threats', 'lucid', 'light', 'music', 'food', 'quiet']),
])
