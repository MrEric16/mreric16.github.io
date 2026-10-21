from lib import *
A = """In everyday speech, people are often described as introverts or extroverts. The terms were popularised by the Swiss psychiatrist Carl Jung in the 1920s, who used them to describe where a person gets energy: extroverts feel energised by company and activity, while introverts feel energised by time alone and by reflection. The distinction has since become one of the most widely used ideas in psychology, but it is also one of the most misunderstood, and the popular picture of the two types is often a caricature. Understanding what the words really mean can help both individuals and organisations to make better decisions about work, study and friendship."""
B = """The first misunderstanding is that introverts are shy. Shyness is a fear of social judgement, while introversion is a preference for less stimulation. An introvert may be perfectly confident when speaking to a large audience, and then need a quiet hour to recover. A shy extrovert, on the other hand, may long for company but be too anxious to seek it. The two qualities often occur together, but they are separate, and mixing them up can lead to unhelpful advice."""
C = """Research suggests that personality is better described as a spectrum than as two types. Most people lie somewhere in the middle and are sometimes called ambiverts, behaving as introverts in some situations and extroverts in others. Surveys in several countries find that the great majority of people score in the middle range, and that very high or very low scores are uncommon. Nevertheless, the labels remain useful, since they describe real differences in preference, even if they are not sharp dividing lines."""
D = """Where do these differences come from? Studies of twins suggest that about half of the variation in extroversion is inherited. Some researchers believe that introverts have brains that react more strongly to stimulation, so that busy places tire them faster. Others emphasise upbringing and culture. In some cultures, outgoing behaviour is admired and encouraged, while in others, quiet reflection is valued more. Whatever the cause, it is clear that personality cannot be entirely changed, though people can learn to act differently when necessary."""
E = """Schools and workplaces often favour extroverts. Classroom teaching rewards pupils who speak up, and many offices are open-plan, with noise and constant interruptions. The writer Susan Cain argued in a popular book that this wastes the talents of the quieter half of the population, who may be better at listening, at concentrating for long periods, and at thinking before acting. Critics reply that the evidence for such differences is weaker than she suggests and that some of her claims go further than the research allows."""
F = """Employers have tried different solutions. Some companies offer quiet rooms where staff can work without interruption, while others allow long periods of working from home. Team leaders are encouraged to let people prepare before meetings, instead of asking for instant opinions. Dr Rosa Almeida, an organisational psychologist, says that the best teams include both types and that the key to success is for the leader to recognise how each member works best, instead of requiring all to behave in the same way."""
G = """At an individual level, understanding one's own preferences can be valuable. An introvert who knows that crowded events are tiring can plan time to recover afterwards, while an extrovert who finds long periods alone difficult can arrange to meet friends. The aim is not to change one's personality but to build a life that suits it. As Dr Almeida puts it, 'neither type is better; each is a different way of being at one\'s best.' It is a reminder that people differ in ways that are worth respecting."""
P = passage('p44', 'Introverts and Extroverts', 'Psychology', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Carl Jung was a Swiss psychiatrist.', 'T', 'A', 'the Swiss psychiatrist Carl Jung'),
  ('Extroverts feel energised by time alone.', 'F', 'A', 'extroverts feel energised by company and activity'),
  ('Shyness and introversion are the same thing.', 'F', 'B', 'The two qualities often occur together, but they are separate'),
  ('An introvert may be confident in front of a large audience.', 'T', 'B', 'perfectly confident when speaking to a large audience'),
  ('Most people score at the extremes of the scale.', 'F', 'C', 'the great majority of people score in the middle range'),
  ('About half of the variation in extroversion is inherited.', 'T', 'D', 'about half of the variation in extroversion is inherited'),
  ('Personality can be entirely changed.', 'F', 'D', 'personality cannot be entirely changed'),
  ('Susan Cain\'s claims have been fully confirmed by research.', 'F', 'E', 'the evidence for such differences is weaker than she suggests'),
  ('Open-plan offices were invented to help introverts.', 'NG', 'E', 'many offices are open-plan', 'The reason for open-plan design is not given.'),
 ]),
 mcq([
  ('What does the writer say about shyness?', ['It is a preference for quiet.', 'It is a fear of social judgement.', 'It is a form of extroversion.', 'It is rare.'], 1, 'B', 'Shyness is a fear of social judgement'),
  ('What is an ambivert?', ['A very shy person.', 'A person in the middle of the range.', 'A person who dislikes work.', 'A strong extrovert.'], 1, 'C', 'Most people lie somewhere in the middle and are sometimes called ambiverts'),
  ('What does Dr Almeida advise leaders to do?', ['Hire only extroverts.', 'Recognise how each member works best.', 'Ban quiet rooms.', 'Hold more meetings.'], 1, 'F', 'recognise how each member works best'),
 ]),
 feat('Match each statement with the correct person, A to C.', ['Carl Jung', 'Susan Cain', 'Dr Rosa Almeida'], [
  ('Used the terms to describe where a person gets energy.', 0, 'A', 'to describe where a person gets energy'),
  ('Argued that quiet people\'s talents are wasted.', 1, 'E', 'this wastes the talents of the quieter half of the population'),
  ('Believes the best teams include both types.', 2, 'F', 'the best teams include both types'),
  ('Said that neither type is better.', 2, 'G', 'neither type is better'),
 ]),
 multi('Which TWO strengths of introverts are suggested in paragraph E?', ['Listening well.', 'Concentrating for long periods.', 'Speaking in public.', 'Leading large teams.', 'Making friends quickly.'], [0, 1], [('E', 'better at listening'), ('E', 'concentrating for long periods')]),
 head(['Origins of two terms', 'A common confusion', 'A scale rather than two boxes', 'Nature, nurture and culture', 'Who benefits from modern institutions', 'What organisations can do', 'Living in line with one\'s preferences', 'The history of psychology', 'The best jobs for introverts'],
  [('A', 0, 'popularised by the Swiss psychiatrist Carl Jung'), ('B', 1, 'The first misunderstanding is that introverts are shy'), ('C', 2, 'personality is better described as a spectrum'), ('D', 3, 'Where do these differences come from'), ('E', 4, 'Schools and workplaces often favour extroverts'), ('F', 5, 'Employers have tried different solutions'), ('G', 6, 'understanding one\'s own preferences can be valuable')]),
 info([
  ('a reference to a decade in which terms became popular', 'A', 'in the 1920s'),
  ('a description of a person who wants company but is anxious', 'B', 'A shy extrovert'),
  ('a mention of studies of twins', 'D', 'Studies of twins'),
  ('a mention of rooms for staff to work quietly', 'F', 'quiet rooms'),
  ('a suggestion about planning recovery time', 'G', 'plan time to recover afterwards'),
 ]),
 ends(['feel energised by company.', 'is a fear of social judgement.', 'is better described as a spectrum.', 'is partly inherited.', 'was invented by Susan Cain.', 'cannot be measured at all.', 'is the same in every culture.'], [
  ('Extroverts', 0, 'A', 'extroverts feel energised by company and activity'),
  ('Shyness', 1, 'B', 'Shyness is a fear of social judgement'),
  ('Personality', 2, 'C', 'better described as a spectrum than as two types'),
  ('Extroversion', 3, 'D', 'about half of the variation in extroversion is inherited'),
 ]),
 sent(2, [
  ('Jung popularised the terms in the ___.', ['1920s'], 'A', 'in the 1920s'),
  ('People in the middle of the range are sometimes called ___.', ['ambiverts'], 'C', 'called ambiverts'),
  ('In some cultures, quiet ___ is valued more.', ['reflection'], 'D', 'quiet reflection'),
  ('Dr Almeida is an organisational ___.', ['psychologist'], 'F', 'an organisational psychologist'),
 ]),
 short(3, [
  ('What do twin studies suggest?', ['about half', 'half'], 'D', 'about half of the variation in extroversion is inherited'),
  ('Who wrote a popular book arguing for the quiet half?', ['susan cain'], 'E', 'The writer Susan Cain'),
  ('What can team leaders let people do before meetings?', ['prepare'], 'F', 'let people prepare before meetings'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Jung used the terms to describe where a person gets [[1]]. Introversion is not the same as [[2]], and most people lie in the [[3]] of the range. Some offices offer quiet [[4]] to help people who need less stimulation.',
  [(['energy'], 'A', 'where a person gets energy'), (['shyness'], 'B', 'Shyness'), (['middle'], 'C', 'in the middle range'), (['rooms'], 'F', 'quiet rooms')], 1,
  bank=['energy', 'shyness', 'middle', 'rooms', 'money', 'edges', 'books', 'noise']),
])
