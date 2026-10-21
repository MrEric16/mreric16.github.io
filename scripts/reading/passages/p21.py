from lib import *
A = """Not long ago, a job meant a contract with one employer, a regular salary and a pension at the end. Today, millions of people earn money in a different way: by taking short pieces of work, called gigs, through digital platforms. They drive passengers, deliver meals, translate documents or design logos, and they are paid for each task rather than by the hour or the month. This arrangement is known as the gig economy, and by some estimates it already involves more than a hundred million workers around the world."""
B = """Supporters point first to freedom. A gig worker chooses when to work, and can stop at any time to study, to look after a child or to rest. For people who find it hard to get a regular job, such as students, migrants or those with disabilities, a platform may be the only opening. Customers benefit too, as services that once required a telephone call and a long wait can now be ordered in seconds, often at lower prices. For many young people, a few hours of gig work is also a first step towards a career."""
C = """Critics, however, argue that the freedom is smaller than it appears. Most platforms set the price of each task, and workers who refuse too many offers may find that they receive fewer in the future. Because gig workers are usually classed as self-employed, they do not receive paid holidays, sick pay or a pension, and they must pay for their own vehicles, phones and insurance. A study of delivery riders in one European city found that, after these costs were deducted, many earned less than the legal minimum wage."""
D = """The legal position is still unclear. In 2021, the UK Supreme Court ruled that drivers working for a large taxi app were 'workers', not self-employed, and were therefore entitled to a minimum wage and paid leave. Courts in other countries have reached different conclusions, and some governments have written new laws instead. Professor Samir Haddad, an economist, believes that a third category, between employee and self-employed, would be fairer than forcing every worker into one of the two existing boxes."""
E = """Algorithms add a further complication. A platform's software decides which worker receives a task, rates workers on the basis of customer reviews and, in some cases, removes workers from the platform without a human being involved. Workers often complain that they cannot find out why a decision was taken, and have no one to whom they can appeal. Some countries are therefore considering laws that would give workers the right to an explanation, and the right to take their ratings with them if they move to another platform."""
F = """It would be wrong, though, to see the gig economy only as a problem. Surveys in several countries suggest that many workers value the flexibility and would not exchange it for a fixed timetable. The difficulty is that flexibility and security are hard to combine. Some platforms have begun to offer insurance or a guaranteed minimum for hours worked, but critics say that such schemes cover only a small share of workers, and that they are often withdrawn when the platform faces competition."""
G = """Whatever the outcome of these debates, the pattern of work is likely to keep changing. Automation may replace some tasks, while creating others that nobody has yet imagined. The most useful response, many economists argue, is not to resist the change but to ensure that the protections once linked to a single job, such as health care and pensions, are attached to the worker instead. How quickly governments will agree to do so remains to be seen."""
P = passage('p21', 'Work in the Gig Economy', 'Economics', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Gig workers are usually paid by the hour.', 'F', 'A', 'paid for each task rather than by the hour or the month'),
  ('Some estimates put the number of gig workers above a hundred million.', 'T', 'A', 'more than a hundred million workers'),
  ('Platforms may be the only opening for some people who cannot find regular jobs.', 'T', 'B', 'a platform may be the only opening'),
  ('Gig work is mainly done by people over forty.', 'NG', 'B', 'such as students, migrants or those with disabilities', 'No age data is given.'),
  ('Workers who refuse many offers may receive fewer later.', 'T', 'C', 'workers who refuse too many offers may find that they receive fewer in the future'),
  ('Gig workers are usually entitled to paid holidays.', 'F', 'C', 'they do not receive paid holidays, sick pay or a pension'),
  ('The UK Supreme Court ruled in 2021 that the drivers were self-employed.', 'F', 'D', 'not self-employed'),
  ('Professor Haddad wants every worker to become an employee.', 'F', 'D', 'a third category, between employee and self-employed'),
  ('Some governments are considering a right to an explanation of algorithm decisions.', 'T', 'E', 'the right to an explanation'),
 ]),
 mcq([
  ('What do supporters of the gig economy value most?', ['Higher pay.', 'Freedom to choose when to work.', 'A guaranteed pension.', 'A single employer.'], 1, 'B', 'A gig worker chooses when to work'),
  ('Why might riders earn less than the minimum wage?', ['They work too few hours.', 'They pay their own costs.', 'Customers pay late.', 'The law has changed.'], 1, 'C', 'after these costs were deducted'),
  ('What is said about schemes offering insurance?', ['They are used by most workers.', 'They are forbidden by law.', 'They cover only a few workers.', 'They are very expensive.'], 2, 'F', 'cover only a small share of workers'),
 ]),
 feat('Match each opinion with the correct person or group, A to C.', ['Supporters of gig work', 'Critics of gig work', 'Professor Haddad'], [
  ('Workers should not be forced into one of two categories.', 2, 'D', 'forcing every worker into one of the two existing boxes'),
  ('Customers benefit from lower prices.', 0, 'B', 'often at lower prices'),
  ('Many riders earn less than the minimum wage.', 1, 'C', 'many earned less than the legal minimum wage'),
  ('Workers who refuse tasks may be punished.', 1, 'C', 'workers who refuse too many offers may find that they receive fewer'),
 ], cls=True),
 head(['A new way to earn a living', 'Freedom and convenience', 'Hidden costs of independence', 'Who counts as an employee?', 'Decisions made by software', 'Balancing flexibility and security', 'Preparing for further change', 'The history of the pension', 'A day in the life of a taxi driver'],
  [('A', 0, 'Today, millions of people earn money in a different way'), ('B', 1, 'Supporters point first to freedom'), ('C', 2, 'Critics, however, argue'), ('D', 3, 'The legal position is still unclear'), ('E', 4, 'Algorithms add a further complication'), ('F', 5, 'The difficulty is that flexibility and security are hard to combine'), ('G', 6, 'the pattern of work is likely to keep changing')]),
 info([
  ('examples of tasks done through platforms', 'A', 'translate documents or design logos'),
  ('a reference to services that are ordered quickly', 'B', 'ordered in seconds'),
  ('a mention of equipment that workers must buy', 'C', 'their own vehicles, phones and insurance'),
  ('a criticism that workers cannot discover the reason for decisions', 'E', 'cannot find out why a decision was taken'),
  ('a reference to jobs that nobody has yet imagined', 'G', 'others that nobody has yet imagined'),
 ]),
 ends(['are paid for each task.', 'set the price of each task.', 'were ruled to be workers by a court.', 'could replace some tasks.', 'are rarely used outside Europe.', 'cannot be reviewed by customers.', 'were invented by the government.'], [
  ('Gig workers', 0, 'A', 'paid for each task rather than by the hour'),
  ('Most platforms', 1, 'C', 'Most platforms set the price of each task'),
  ('Taxi drivers in the 2021 case', 2, 'D', 'were \'workers\', not self-employed'),
  ('Automation', 3, 'G', 'Automation may replace some tasks'),
 ]),
 multi('Which TWO benefits of the gig economy for customers are mentioned in paragraph B?', ['Services can be ordered quickly.', 'Prices are often lower.', 'Quality is always higher.', 'Workers are better trained.', 'Services are free.'], [0, 1], [('B', 'ordered in seconds'), ('B', 'often at lower prices')]),
 sent(2, [
  ('Gig workers do not receive paid holidays, sick pay or a ___.', ['pension'], 'C', 'sick pay or a pension'),
  ('The UK Supreme Court ruled in ___.', ['2021'], 'D', 'In 2021'),
  ('A platform\'s software rates workers on the basis of customer ___.', ['reviews'], 'E', 'customer reviews'),
  ('Many workers would not exchange flexibility for a fixed ___.', ['timetable'], 'F', 'a fixed timetable'),
 ]),
 short(3, [
  ('What kind of workers did the study of delivery riders examine?', ['delivery riders', 'riders'], 'C', 'A study of delivery riders'),
  ('What is Professor Haddad\'s profession?', ['economist', 'an economist'], 'D', 'an economist'),
  ('What might workers take with them to another platform?', ['their ratings', 'ratings'], 'E', 'take their ratings with them'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Gig workers are usually classed as [[1]], so they lose benefits such as sick pay. Some courts have decided that certain drivers are [[2]] with rights. Algorithms [[3]] workers by customer reviews, and some countries want workers to have the right to an [[4]].',
  [(['self-employed'], 'C', 'classed as self-employed'), (['workers'], 'D', 'were \'workers\''), (['rate', 'rates'], 'E', 'rates workers'), (['explanation'], 'E', 'right to an explanation')], 1,
  bank=['self-employed', 'workers', 'rate', 'explanation', 'employers', 'ignore', 'apology', 'salary']),
])
