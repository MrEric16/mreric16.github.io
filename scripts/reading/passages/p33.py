from lib import *
A = """In the early hours of Sunday 2 September 1666, a fire broke out in a bakery in Pudding Lane, in the City of London. The baker, Thomas Farriner, and his family escaped through an upstairs window, but sparks from the oven had already set light to a pile of firewood. At first nobody thought the fire was serious. Fires were common in the crowded city, and most were put out within hours. This one, however, was to burn for four days and become the greatest disaster in the history of the city."""
B = """Several things allowed the fire to spread so quickly. The houses in the old city were built of wood and covered with tar, and their upper floors leaned so close across the narrow streets that neighbours could almost shake hands from their windows. It had also been a hot, dry summer, and a strong wind from the east carried burning pieces of wood from roof to roof. The warehouses beside the river were full of oil, tallow and coal, which fed the flames and produced a heat that could be felt a mile away."""
C = """The authorities were slow to act. The usual way of stopping a fire was to pull down the houses in its path, to create a gap that the flames could not cross, but the Lord Mayor hesitated to give the order, since the owners would have to be paid. By the time King Charles II took charge, much of the city was already burning. The king and his brother, the Duke of York, worked beside ordinary people, passing buckets of water and giving out money to the men who fought the flames."""
D = """The most famous account of the fire was written by Samuel Pepys, a government official, in his diary. He watched from a boat on the river and described the sky as red as a furnace. He also acted to protect his possessions: he buried his wine and a valuable Parmesan cheese in a pit in his garden. His diary is valuable to historians because it records what an ordinary person saw and felt, not only what the kings and ministers did, and it gives a vivid picture of the fear in the crowded streets."""
E = """By Wednesday, the wind had dropped, and the fire was brought under control, helped by the blowing up of houses with gunpowder to make wide gaps. When it was over, about thirteen thousand houses and eighty-seven churches had been destroyed, including the old St Paul's Cathedral. Roughly seventy thousand of the city's eighty thousand inhabitants had lost their homes. Remarkably, only a handful of deaths were officially recorded, although historians suspect that the poor, whose deaths were not noted, may have died in larger numbers."""
F = """The rebuilding of London took more than ten years. Plans for a completely new city with wide straight streets were drawn up by the architect Christopher Wren, but they were abandoned because landowners wished to rebuild on their old plots. New laws, however, required that houses be made of brick or stone, and that streets be made wider. Wren designed fifty-one new churches and a new St Paul's, whose great dome is still the most familiar part of the London skyline."""
G = """The fire also left a lasting mark on the way people think about safety. The first fire insurance companies were founded soon afterwards, and they employed their own fire fighters, who would only help buildings that carried the company's badge. A tall column, the Monument, was built near Pudding Lane in the 1670s to remember the disaster. It is 202 feet high, which is exactly the distance from its base to the place where the bakery once stood, and visitors can still climb its 311 steps."""
P = passage('p33', 'The Great Fire of London', 'History', 1, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 tfng([
  ('The fire began in a bakery.', 'T', 'A', 'a fire broke out in a bakery in Pudding Lane'),
  ('The baker\'s family died in the fire.', 'F', 'A', 'escaped through an upstairs window'),
  ('The baker was arrested after the fire.', 'NG', 'A', 'The baker, Thomas Farriner, and his family escaped through an upstairs window', 'The passage does not say what happened to the baker afterwards.'),
  ('The fire burned for four days.', 'T', 'A', 'burn for four days'),
  ('The houses were built of stone.', 'F', 'B', 'built of wood and covered with tar'),
  ('The summer of 1666 was wet.', 'F', 'B', 'a hot, dry summer'),
  ('The Lord Mayor gave the order to pull down houses at once.', 'F', 'C', 'hesitated to give the order'),
  ('Pepys watched the fire from a boat.', 'T', 'D', 'He watched from a boat on the river'),
  ('The fire destroyed about thirteen thousand houses.', 'T', 'E', 'about thirteen thousand houses'),
  ('Wren\'s plan for a new city was carried out.', 'F', 'F', 'they were abandoned'),
 ]),
 mcq([
  ('Why did the fire spread so fast?', ['The city had no river.', 'Houses were made of wood and a strong wind blew.', 'There were no people in the city.', 'It was winter.'], 1, 'B', 'a strong wind from the east carried burning pieces of wood'),
  ('Why is Pepys\'s diary valuable?', ['It lists the dead.', 'It shows what an ordinary person saw and felt.', 'It was written by the king.', 'It contains plans.'], 1, 'D', 'what an ordinary person saw and felt'),
  ('What did new laws require?', ['Houses of brick or stone.', 'Houses without roofs.', 'Fire fighters in every street.', 'A new river.'], 0, 'F', 'houses be made of brick or stone'),
 ]),
 multi('Which TWO things did Pepys bury in his garden, according to paragraph D?', ['Wine.', 'A Parmesan cheese.', 'Gold coins.', 'His diary.', 'A silver cup.'], [0, 1], [('D', 'his wine and a valuable Parmesan cheese'), ('D', 'his wine and a valuable Parmesan cheese')]),
 head(['A small fire that became a disaster', 'Why the flames spread', 'A slow response', 'An eyewitness account', 'The scale of the damage', 'Rebuilding the city', 'Changes in safety and remembrance', 'The plague of 1665', 'How to bake bread'],
  [('A', 0, 'a fire broke out in a bakery'), ('B', 1, 'Several things allowed the fire to spread so quickly'), ('C', 2, 'The authorities were slow to act'), ('D', 3, 'The most famous account of the fire'), ('E', 4, 'about thirteen thousand houses'), ('F', 5, 'The rebuilding of London took more than ten years'), ('G', 6, 'The fire also left a lasting mark')]),
 info([
  ('a reference to the heat of the fire', 'B', 'a heat that could be felt a mile away'),
  ('a mention of a royal person fighting the fire', 'C', 'King Charles II'),
  ('a description of the colour of the sky', 'D', 'as red as a furnace'),
  ('the number of London churches Wren designed', 'F', 'fifty-one new churches'),
  ('the number of steps on a monument', 'G', '311 steps'),
 ]),
 ends(['burned for four days.', 'were full of oil, tallow and coal.', 'hesitated to give the order.', 'wrote a famous diary.', 'was built in the 1970s.', 'was founded by Pepys.', 'was made of brick.'], [
  ('The fire', 0, 'A', 'burn for four days'),
  ('The warehouses beside the river', 1, 'B', 'full of oil, tallow and coal'),
  ('The Lord Mayor', 2, 'C', 'hesitated to give the order'),
  ('Samuel Pepys', 3, 'D', 'written by Samuel Pepys'),
 ]),
 flow('Complete the flow chart. Write NO MORE THAN TWO WORDS from the passage for each answer.',
  ['Sparks from the oven set light to a pile of [[1]].', 'A strong [[2]] from the east carries burning pieces from roof to roof.', 'Houses are blown up with [[3]] to make wide gaps.', 'By Wednesday the fire is brought under [[4]].'],
  [(['firewood'], 'A', 'a pile of firewood'), (['wind'], 'B', 'a strong wind from the east'), (['gunpowder'], 'E', 'with gunpowder'), (['control'], 'E', 'brought under control')], 1),
 table('Complete the notes. Write NO MORE THAN TWO WORDS from the passage for each answer.', ['Topic', 'Detail'],
  [['Date', 'The fire began on 2 [[1]] 1666'], ['Damage', '[[2]] churches were destroyed'], ['Law', 'Houses must be of brick or [[3]]'], ['Monument', 'It is [[4]] feet high']],
  [(['september'], 'A', 'Sunday 2 September 1666'), (['eighty-seven'], 'E', 'eighty-seven churches'), (['stone'], 'F', 'brick or stone'), (['202'], 'G', '202 feet high')], 1),
 sent(2, [
  ('The baker was called Thomas ___.', ['farriner'], 'A', 'Thomas Farriner'),
  ('The king\'s brother was the Duke of ___.', ['york'], 'C', 'the Duke of York'),
  ('Wren designed a new St ___.', ['paul\'s', 'pauls'], 'F', 'a new St Paul\'s'),
  ('The first fire ___ companies were founded soon afterwards.', ['insurance'], 'G', 'fire insurance companies'),
 ]),
 short(3, [
  ('Which street was the bakery in?', ['pudding lane'], 'A', 'Pudding Lane'),
  ('What was Pepys\'s job?', ['government official', 'a government official'], 'D', 'a government official'),
  ('How many of the city\'s eighty thousand inhabitants lost their homes?', ['seventy thousand', '70,000', '70000'], 'E', 'Roughly seventy thousand'),
 ]),
])
