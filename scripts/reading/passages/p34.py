from lib import *
A = """Few subjects raise stronger feelings than the effect of robots on employment. Some people fear that machines will take every job within a generation, while others believe that technology has always created more work than it has destroyed. Both sides can point to history. In the early nineteenth century, English textile workers known as Luddites smashed the new looms that threatened their livelihoods, yet within a few decades there were more jobs in the textile industry than ever before, although they were different jobs, in different places, for different workers."""
B = """What is different now, according to the economist Dr Peter Lindgren, is the range of tasks that machines can perform. The machines of the industrial revolution replaced muscle. Modern software and robots can also recognise speech, read medical scans and write simple reports, tasks that were once thought to need a human mind. A widely quoted study from Oxford University in 2013 estimated that almost half of the jobs in the United States could be automated within twenty years, although many experts regard that figure as too high."""
C = """A more careful approach is to look at tasks rather than whole jobs. Very few occupations consist entirely of routine activities that a machine could do; most contain a mixture of routine tasks and tasks that need judgement, creativity or care for other people. On this analysis, estimates suggest that only about one job in ten is at high risk of being automated, though roughly one in three is likely to change significantly. A bank clerk may spend less time counting money, but more time advising customers."""
D = """The kind of work most at risk is the routine, repetitive kind: assembling parts, sorting parcels, processing forms. Those who do such work are often the least well paid and the least able to retrain. Jobs that are hardest to automate include those that need dexterity in unpredictable surroundings, such as plumbing or nursing, and those that depend on emotions, such as teaching and therapy. Ironically, some highly paid professional work, such as analysing legal documents, may be easier for a machine than cleaning an office."""
E = """Governments and companies are therefore considering how to help workers through the change. Some propose a universal basic income, a regular payment to every citizen whether or not they work. Supporters say it would provide security and make it easier for people to retrain; opponents say it would be very expensive and might discourage work. Others prefer to invest in education, so that workers can move to new kinds of jobs. Experiments have been carried out in Finland and in several other countries, but their results are still being debated."""
F = """There is a further argument that the benefits of automation depend on how they are shared. If machines make firms richer but leave workers poorer, the effect on society could be harmful, however efficient the factories may be. Professor Aiko Matsuda points out that the shorter working week, introduced in many countries in the twentieth century, was the result of political choices as well as of new machines. In her view, the question is not what technology will do to us, but what we choose to do with it."""
G = """In the end, nobody can be sure what the working world will look like in thirty years. Past predictions about technology have often been wrong, in both directions: flying cars have not arrived, but few people in 1990 foresaw how much of their lives would be spent with a telephone that has the power of a computer. The sensible response is perhaps to prepare in several ways at once: to teach flexible skills, to support those who lose their jobs, and to keep watching the evidence, instead of relying on fear or on hope."""
P = passage('p34', 'Robots and the Future of Work', 'Economics', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The writer says that history supports only one side of the debate.', 'F', 'A', 'Both sides can point to history'),
  ('The Luddites destroyed machines.', 'T', 'A', 'smashed the new looms'),
  ('The textile industry employed fewer people after the Luddites.', 'F', 'A', 'more jobs in the textile industry than ever before'),
  ('The machines of the industrial revolution replaced human muscle.', 'T', 'B', 'replaced muscle'),
  ('Most experts accept the Oxford estimate without question.', 'F', 'B', 'many experts regard that figure as too high'),
  ('About one job in ten is at high risk, according to some estimates.', 'T', 'C', 'about one job in ten is at high risk'),
  ('Nursing is easy to automate.', 'F', 'D', 'hardest to automate include those that need dexterity in unpredictable surroundings, such as plumbing or nursing'),
  ('A universal basic income has been tried in Finland.', 'T', 'E', 'Experiments have been carried out in Finland'),
  ('Dr Lindgren believes that robots will replace all teachers.', 'NG', 'D', 'those that depend on emotions, such as teaching and therapy', 'Dr Lindgren is not connected with this claim.'),
 ]),
 mcq([
  ('What is new about modern machines, according to Dr Lindgren?', ['They are cheaper.', 'They can do a wider range of tasks.', 'They are slower.', 'They need no electricity.'], 1, 'B', 'the range of tasks that machines can perform'),
  ('Why is analysing legal documents mentioned?', ['It is poorly paid.', 'It may be easier to automate than cleaning.', 'It is a new profession.', 'It is dangerous.'], 1, 'D', 'may be easier for a machine than cleaning an office'),
  ('What is Professor Matsuda\'s main point?', ['Machines are harmless.', 'Technology decides everything.', 'People\'s choices determine the effects of technology.', 'The working week should be longer.'], 2, 'F', 'what we choose to do with it'),
 ]),
 multi('Which TWO arguments against a universal basic income are given in paragraph E?', ['It would be very expensive.', 'It might discourage work.', 'It would increase prices.', 'It is against the law.', 'Nobody has tried it.'], [0, 1], [('E', 'it would be very expensive'), ('E', 'might discourage work')]),
 head(['An old argument', 'Why this time may be different', 'Tasks, not jobs', 'Who is most at risk', 'Ways to help workers', 'A question of sharing the gains', 'Preparing for uncertainty', 'The history of the telephone', 'The best career for a robot'],
  [('A', 0, 'Both sides can point to history'), ('B', 1, 'the range of tasks that machines can perform'), ('C', 2, 'look at tasks rather than whole jobs'), ('D', 3, 'The kind of work most at risk'), ('E', 4, 'how to help workers through the change'), ('F', 5, 'the benefits of automation depend on how they are shared'), ('G', 6, 'nobody can be sure what the working world will look like')]),
 info([
  ('a reference to people who broke machines', 'A', 'English textile workers known as Luddites'),
  ('examples of tasks software can now perform', 'B', 'recognise speech, read medical scans'),
  ('an example of a changing job in a bank', 'C', 'A bank clerk'),
  ('a mention of the shorter working week', 'F', 'the shorter working week'),
  ('a reference to a prediction that did not come true', 'G', 'flying cars have not arrived'),
 ]),
 ends(['might be much higher than experts now believe.', 'is at high risk of automation.', 'are hardest to automate.', 'would be a payment to every citizen.', 'is the same in every country.', 'has already been abolished.', 'was invented by Luddites.'], [
  ('The Oxford estimate of the risk to jobs', 0, 'B', 'many experts regard that figure as too high'),
  ('Routine, repetitive work', 1, 'D', 'The kind of work most at risk is the routine, repetitive kind'),
  ('Jobs that need dexterity in unpredictable surroundings', 2, 'D', 'hardest to automate'),
  ('A universal basic income', 3, 'E', 'a regular payment to every citizen'),
 ]),
 sent(2, [
  ('The Oxford study was published in ___.', ['2013'], 'B', 'from Oxford University in 2013'),
  ('Most jobs contain a mixture of routine tasks and tasks needing judgement, creativity or ___ for others.', ['care'], 'C', 'care for other people'),
  ('Workers doing routine tasks are often the least able to ___.', ['retrain'], 'D', 'least able to retrain'),
  ('Professor Matsuda says the shorter working week resulted from political ___.', ['choices'], 'F', 'political choices'),
 ]),
 short(3, [
  ('What is Dr Lindgren\'s profession?', ['economist', 'an economist'], 'B', 'the economist Dr Peter Lindgren'),
  ('Which country is mentioned for basic income experiments?', ['finland'], 'E', 'in Finland'),
  ('What should be taught, according to the writer?', ['flexible skills'], 'G', 'to teach flexible skills'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Both optimists and pessimists find support in [[1]]. Modern machines can perform a wider range of [[2]], but analysis suggests that most jobs will [[3]] rather than disappear. Governments are therefore considering a basic income and investment in [[4]].',
  [(['history'], 'A', 'point to history'), (['tasks'], 'B', 'range of tasks'), (['change'], 'C', 'likely to change significantly'), (['education'], 'E', 'invest in education')], 1,
  bank=['history', 'tasks', 'change', 'education', 'prices', 'wages', 'war', 'taxes']),
])
