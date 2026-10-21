from lib import *
A = """There are about seven thousand languages in the world, but they are very unevenly shared. Twenty-three of them are spoken by more than half of the world's population, while thousands of others have fewer than ten thousand speakers each. Many have never been written down. According to one often-quoted estimate, a language falls silent somewhere in the world about once every two weeks, and linguists believe that around forty per cent of those still spoken are at risk of disappearing."""
B = """Languages rarely die because they are forbidden. More often they fade because speaking them stops being useful. When villagers move to cities for work, their children grow up surrounded by the dominant language, and parents who want their children to succeed at school and in the job market may decide to use it at home. The process typically takes three generations: grandparents speak the old language, their children are bilingual, and the grandchildren understand only a few words. Once children stop learning a language, its future is almost certainly short."""
C = """Why does this matter? Each language carries a store of knowledge that has built up over centuries. Dr Amara Okonjo, who has recorded the speech of elders in a forest region, found that they could name and describe the medical uses of plants for which science has no names. When the last speakers die, such knowledge goes with them. A language is also a marker of identity, and many communities that have lost theirs describe a sense of having lost the thread connecting them with their ancestors."""
D = """The first response of most linguists is documentation. They record conversations, transcribe and translate them, and compile dictionaries and grammars so that something permanent remains. Okonjo admits, though, that a recording is a kind of fossil. It preserves the sounds and the words, but a language that is no longer spoken in daily life cannot adapt to new subjects, and archives do not create speakers."""
E = """Reviving a language is far harder, but it has been done. In New Zealand, the 1980s saw the founding of Māori 'language nests', pre-schools in which elders speak only Māori to very young children. The idea spread, and within a generation the number of young people able to speak the language had risen. The most famous revival of all is Hebrew, which for centuries was used mainly in religious texts and became an everyday language again in the nineteenth and twentieth centuries. Few cases can be compared with it, however, since Hebrew had a long written tradition, and later the backing of a state."""
F = """Not everyone is comfortable with the language-saving movement. Professor Lena Hartmann argues that speakers have the right to choose, and that outsiders who romanticise small languages may in effect be urging poor communities to stay poor. Revival programmes, she says, succeed only when the community itself wants them. Her point deserves to be taken seriously, but it assumes that the choice is made freely, and in many places the pressure to abandon a language comes from economic necessity, and from a school system that treats it as a handicap."""
G = """Technology cuts both ways. The internet has strengthened the position of a few dominant languages, yet it also gives small communities cheap ways to teach and publish. Keyboards now exist for scripts that were once impossible to type, learning apps are available for languages with only a few hundred speakers, and researchers have found that speech-recognition software can be trained with only a few hours of recorded speech. Whether these tools will arrive in time for the most endangered languages is another matter."""
P = passage('p10', 'When a Language Falls Silent', 'Linguistics', 3, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('Twenty-three languages are spoken by more than half of the world\'s population.', 'T', 'A', 'Twenty-three of them are spoken by more than half of the world\'s population'),
  ('Most of the world\'s languages have been written down.', 'F', 'A', 'Many have never been written down'),
  ('The estimate that a language disappears every two weeks is accepted by every linguist.', 'NG', 'A', 'According to one often-quoted estimate', 'It is described as often quoted, but the passage does not say who accepts it.'),
  ('Languages usually die because governments forbid them.', 'F', 'B', 'Languages rarely die because they are forbidden'),
  ('Language loss typically takes three generations.', 'T', 'B', 'The process typically takes three generations'),
  ('Dr Okonjo recorded elders in a forest region.', 'T', 'C', 'who has recorded the speech of elders in a forest region'),
  ('Dr Okonjo compared the languages of forty communities.', 'NG', 'C', 'who has recorded the speech of elders in a forest region', 'The number of communities is not given.'),
  ('A recording of a language can make it adapt to new subjects.', 'F', 'D', 'a language that is no longer spoken in daily life cannot adapt to new subjects'),
  ('Māori language nests were set up in the 1980s.', 'T', 'E', 'the 1980s saw the founding of Māori \'language nests\''),
  ('Hebrew had official support after its revival began.', 'T', 'E', 'later the backing of a state'),
  ('Speech-recognition software needs hundreds of hours of recordings.', 'F', 'G', 'trained with only a few hours of recorded speech'),
 ]),
 tfng([
  ('Professor Hartmann\'s argument should be taken seriously.', 'Y', 'F', 'Her point deserves to be taken seriously'),
  ('The pressure to abandon a language is always freely chosen.', 'N', 'F', 'it assumes that the choice is made freely, and in many places the pressure'),
  ('Documentation alone is enough to keep a language alive.', 'N', 'D', 'archives do not create speakers'),
  ('Every endangered language will be saved by new technology.', 'NG', 'G', 'Whether these tools will arrive in time for the most endangered languages is another matter', 'The writer is uncertain and gives no prediction either way.'),
  ('The loss of a language also means the loss of knowledge.', 'Y', 'C', 'When the last speakers die, such knowledge goes with them'),
  ('Revival programmes should be imposed on communities.', 'N', 'F', 'succeed only when the community itself wants them'),
 ], yn=True),
 feat('Match each statement with the correct source, A to C. You may use any letter more than once.', ['Dr Amara Okonjo', 'Professor Lena Hartmann', 'The Māori language nests'], [
  ('Speakers have the right to choose which language to use.', 1, 'F', 'speakers have the right to choose'),
  ('Plants have been named and described by elders in a forest region.', 0, 'C', 'name and describe the medical uses of plants'),
  ('Elders speak only Māori to very young children.', 2, 'E', 'elders speak only Māori to very young children'),
  ('A recording is a kind of fossil.', 0, 'D', 'a recording is a kind of fossil'),
  ('Outsiders may be urging poor communities to stay poor.', 1, 'F', 'urging poor communities to stay poor'),
  ('The number of young speakers rose within a generation.', 2, 'E', 'within a generation the number of young people able to speak the language had risen'),
 ], cls=True),
 head(['The scale of the problem', 'How languages fade away', 'What is lost with a language', 'The limits of recording', 'Success stories and exceptions', 'An argument about choice', 'New tools for small languages', 'Why governments ban languages', 'How children learn to read'],
  [('A', 0, 'There are about seven thousand languages in the world'), ('B', 1, 'Languages rarely die because they are forbidden'), ('C', 2, 'Each language carries a store of knowledge'), ('D', 3, 'a recording is a kind of fossil'), ('E', 4, 'Reviving a language is far harder, but it has been done'), ('F', 5, 'speakers have the right to choose'), ('G', 6, 'Technology cuts both ways')]),
 info([
  ('a figure showing how unevenly languages are spread', 'A', 'Twenty-three of them are spoken by more than half'),
  ('a description of the stages by which a language is lost', 'B', 'grandparents speak the old language'),
  ('a comparison between a language and a sense of identity', 'C', 'A language is also a marker of identity'),
  ('a reason why Hebrew is hard to compare with other cases', 'E', 'Hebrew had a long written tradition'),
  ('a criticism of a school system', 'F', 'a school system that treats it as a handicap'),
  ('an example of a tool for typing', 'G', 'Keyboards now exist for scripts that were once impossible to type'),
 ]),
 sent(3, [
  ('Thousands of languages have fewer than ___ speakers each.', ['ten thousand', '10,000', '10000'], 'A', 'fewer than ten thousand speakers each'),
  ('Parents may use the dominant language at home to help children succeed at ___.', ['school'], 'B', 'succeed at school'),
  ('Okonjo found that elders could describe the ___ uses of plants.', ['medical'], 'C', 'the medical uses of plants'),
  ('Linguists compile dictionaries and ___ to leave something permanent.', ['grammars'], 'D', 'dictionaries and grammars'),
  ('Hebrew was used mainly in ___ texts for centuries.', ['religious'], 'E', 'mainly in religious texts'),
  ('Learning apps exist for languages with only a few hundred ___.', ['speakers'], 'G', 'only a few hundred speakers'),
 ]),
 short(3, [
  ('Which country founded the Māori language nests?', ['new zealand'], 'E', 'In New Zealand'),
  ('What proportion of spoken languages are said to be at risk?', ['forty per cent', '40 per cent', '40%'], 'A', 'around forty per cent'),
  ('What does a school system sometimes treat a minority language as?', ['a handicap', 'handicap'], 'F', 'treats it as a handicap'),
  ('What does Okonjo call a recording of a language?', ['a fossil', 'fossil'], 'D', 'a recording is a kind of fossil'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Villagers move to [[1]] for work.', 'Their children grow up surrounded by the [[2]] language.', 'The children become [[3]] and use both languages.', 'The grandchildren understand only a few [[4]] of the old language.'],
  [(['cities'], 'B', 'move to cities for work'), (['dominant'], 'B', 'the dominant language'), (['bilingual'], 'B', 'their children are bilingual'), (['words'], 'B', 'only a few words')], 2),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'Linguists try to [[1]] endangered languages by recording speakers, but Dr Okonjo calls a recording a [[2]]. Reviving a language is more difficult. In New Zealand, Māori language [[3]] were founded, and later the number of young speakers had [[4]]. Hebrew is an unusual case because it had a long written [[5]].',
  [(['document'], 'D', 'The first response of most linguists is documentation'.replace('documentation', 'documentation')), (['fossil'], 'D', 'a kind of fossil'), (['nests'], 'E', 'language nests'), (['risen'], 'E', 'had risen'), (['tradition'], 'E', 'long written tradition')], 1,
  bank=['document', 'fossil', 'nests', 'risen', 'tradition', 'fallen', 'schools', 'weapon', 'ignore']),
])
