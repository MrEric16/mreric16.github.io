# -*- coding: utf-8 -*-
T1 = []
def add(**k): T1.append(k)

add(id='t1-internet', task='t1a', type='Line graph', title='Internet users in three countries',
 prompt='The line graph shows the number of internet users per 100 people in three countries between 2000 and 2020. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',
 chart={'type':'line','title':'Internet users per 100 people','x':['2000','2005','2010','2015','2020'],'y':'Users per 100 people','max':100,
  'series':[{'name':'Country A','data':[10,35,60,80,92]},{'name':'Country B','data':[5,15,40,70,85]},{'name':'Country C','data':[30,45,55,60,62]}]},
 model=[
 'The line graph compares the number of internet users per 100 people in three countries over a twenty-year period, from 2000 to 2020.',
 'Overall, internet use rose in every country, but the increase was far more dramatic in Countries A and B than in Country C. Although Country C began with by far the highest figure, it had been overtaken by both of the others by 2015.',
 'In 2000, Country C led with 30 users per 100 people, compared with 10 in Country A and just 5 in Country B. Country A then climbed steeply, reaching 60 in 2010, which put it ahead of Country C, where the figure had risen to only 55. It continued to grow and finished the period at 92. Country B followed a similar but delayed pattern: its figure tripled to 15 in 2005 and then rose sharply to 70 in 2015 and 85 in 2020.',
 'By contrast, growth in Country C was slow and steady, and it levelled off at 62 users per 100 people in 2020. As a result, the country that had once led the group ended with the lowest figure, 30 below Country A.'],
 notes={'Task Achievement':'The overview (paragraph 2) states the two key trends and the one overtaking. Only selected figures are given, never every number. Every figure matches the graph.',
  'Coherence':'One paragraph per job: introduction, overview, detail on A and B, then C as the contrast. Linkers (although, then, by contrast, as a result) show relationships, not just sequence.',
  'Lexical Resource':'Precise movement language (climbed steeply, tripled, levelled off, overtaken) with no repetition of "increase".',
  'Grammar':'Mix of past simple, past perfect (had been overtaken, had risen) and a variety of structures such as "which put it ahead of" and "although" clauses.'},
 lang=['climbed steeply','tripled','levelled off at','finished the period at','by contrast','had been overtaken by','a similar but delayed pattern','by far the highest'])

add(id='t1-commute', task='t1a', type='Bar chart', title='How people travel to work',
 prompt='The bar chart shows the percentage of commuters in one city who used five different means of transport in 1990 and in 2020. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',
 chart={'type':'bar','title':'Commuters by means of transport (%)','groups':['Car','Bus','Train','Bicycle','Walking'],'y':'Percentage of commuters','max':50,
  'series':[{'name':'1990','data':[45,25,10,5,15]},{'name':'2020','data':[38,20,24,12,6]}]},
 model=[
 'The bar chart illustrates how commuters in one city travelled to work in 1990 and in 2020, using five means of transport.',
 'Overall, the car remained the most popular choice throughout the period, although its share fell. The most striking change was the rapid growth in rail travel, while walking declined sharply.',
 'In 1990, almost half of all commuters (45%) drove, and a quarter (25%) took the bus. By 2020, these figures had dropped to 38% and 20% respectively. Walking suffered the largest relative fall: it more than halved, from 15% to just 6%, so that by 2020 only one commuter in seventeen made the journey on foot.',
 'In contrast, two modes became considerably more popular. The proportion of people using the train more than doubled, from 10% to 24%, so that rail overtook the bus to become the second most common option. Cycling also expanded, from a mere 5% to 12%, although it remained a minority choice, used by fewer than one in eight commuters.'],
 notes={'Task Achievement':'The overview names the dominant mode and the biggest change. Comparisons across years and across modes are made, and the data is grouped logically (falling modes, then rising modes).',
  'Coherence':'Grouping by trend (decline, then growth) is more cohesive than describing bars one by one. "In contrast" and "so that" make the link between the two groups clear.',
  'Lexical Resource':'Fractions and ratios (almost half, a quarter, more than halved, more than doubled) replace repeated percentages.',
  'Grammar':'Accurate use of "respectively", a result clause ("so that rail overtook...") and comparatives.'},
 lang=['remained the most popular','the most striking change','more than halved','more than doubled','a mere 5%','respectively','a minority choice','suffered the largest relative fall'])

add(id='t1-energy', task='t1a', type='Pie charts', title='Sources of electricity',
 prompt='The pie charts show the sources of a country\'s electricity in 2000 and in 2020. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',
 chart={'type':'pie','title':'Sources of electricity (%)','charts':[{'label':'2000','parts':[['Coal',40],['Gas',25],['Nuclear',20],['Oil',10],['Renewables',5]]},{'label':'2020','parts':[['Coal',22],['Gas',30],['Nuclear',18],['Oil',4],['Renewables',26]]}]},
 model=[
 'The pie charts compare the proportion of electricity generated from five sources in one country in 2000 and 2020.',
 'Overall, the pattern changed considerably. Coal, which supplied the largest share at the start, was replaced by gas as the main source, and renewable energy grew from a very small base to become the second most important source.',
 'In 2000, coal accounted for 40% of electricity, well ahead of gas at 25% and nuclear power at 20%. Oil provided 10%, and renewables only 5%. By 2020, coal had fallen to 22%, whereas gas had risen slightly to 30% and so took first place. Renewable sources, which were negligible in 2000, were by then almost as important as gas.',
 'The most remarkable development was in renewables, whose share increased more than fivefold to 26%. Nuclear power declined only marginally, to 18%, while oil dropped to a negligible 4%, less than half its earlier level. Taken together, coal, oil and nuclear power supplied 70% of the total in 2000 but only 44% in 2020, which shows how far the country had moved away from traditional sources.'],
 notes={'Task Achievement':'The overview identifies the change in rank order, not just "some went up, some went down". Figures are accurate and the key comparison (renewables, fivefold) is highlighted.',
  'Coherence':'Paragraph 3 describes the starting position and what happened to the leaders; paragraph 4 describes the biggest riser and the smaller changes.',
  'Lexical Resource':'Varied vocabulary for proportion (accounted for, supplied, provided, share) so no word is repeated.',
  'Grammar':'Past perfect for changes seen from 2020 (had fallen, had risen), contrast with "whereas", and a relative clause ("whose share").'},
 lang=['accounted for','well ahead of','from a very small base','more than fivefold','declined only marginally','a negligible 4%','took first place','the most remarkable development'])

add(id='t1-spending', task='t1a', type='Table', title='Household spending in three countries',
 prompt='The table shows the percentage of household budgets spent on four categories in three countries. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',
 chart={'type':'table','title':'Share of household budget (%)','head':['','Country P','Country Q','Country R'],'rows':[['Food','28','15','40'],['Housing','22','30','18'],['Transport','12','18','10'],['Leisure','8','14','4']],'foot':'The remainder of each budget is spent on other items.'},
 model=[
 'The table compares how households in three countries divided their budgets between four categories of spending.',
 'Overall, food and housing together accounted for the largest part of spending in every country, between 45% and 58%, while leisure took the smallest share each time. Country R spent proportionally the most on basic necessities, whereas Country Q had the most to spend on transport and leisure.',
 'Food was the biggest item in Country P (28%) and, above all, in Country R, where it accounted for 40%, the highest figure in the table. In Country Q, however, food took only 15%, and housing was the main expense at 30%. Country P devoted 22% of its budget to housing, and Country R the lowest proportion, at 18%.',
 'Differences were also clear in discretionary spending. Country Q allocated 18% to transport and 14% to leisure, compared with 12% and 8% in Country P. Country R spent least on both, with only 10% on transport and a mere 4% on leisure, half the figure for Country P.'],
 notes={'Task Achievement':'Rather than reading across each row, the answer picks the highest and lowest figures and compares countries. Ratios such as "half the figure for Country P" are checked against the table before they are written.',
  'Coherence':'Paragraph 3 covers necessities, paragraph 4 covers discretionary spending.',
  'Lexical Resource':'Alternatives to "spend" (devote, allocate, take, account for) and the phrase "discretionary spending".',
  'Grammar':'Comparatives and superlatives, "compared with" and "whereas" for contrast.'},
 lang=['proportionally the most','above all','the highest figure in the table','discretionary spending','allocated','devoted','compared with','a mere 4%'])

add(id='t1-paper', task='t1a', type='Process', title='How paper is recycled',
 prompt='The diagram shows the process by which used paper is recycled into new paper. Summarise the information by selecting and reporting the main features.',
 chart={'type':'process','title':'The recycling of paper','steps':['Used paper is collected','Paper is delivered to a recycling plant','Paper is sorted and plastic and staples removed','Paper is mixed with water and chemicals in a pulper to make pulp','Pulp is screened and cleaned, and ink is removed','Pulp is pressed between rollers into a flat sheet','Sheet is dried on heated cylinders','Paper is wound on reels and cut to size']},
 model=[
 'The diagram shows how used paper is turned into new paper in a recycling plant.',
 'Overall, the process is linear and consists of eight stages, beginning with the collection of waste paper and ending with the cutting of the finished product, and no stage is repeated.',
 'First, used paper is collected and transported to a recycling plant, where it is sorted. At this stage, items such as plastic and staples are removed. The sorted paper is then combined with water and chemicals in a pulper, which turns it into pulp.',
 'Next, the pulp is passed through screens so that it can be cleaned and, at the same time, the ink is taken out. Once this has been done, the clean pulp is pressed between rollers to form a flat sheet. The sheet is subsequently dried on a series of heated cylinders. Finally, the dry paper is wound on to reels and cut to size, ready for use.'],
 notes={'Task Achievement':'The overview states the number of stages and the start and end points. Every stage is covered in order and nothing is invented.',
  'Coherence':'Sequencing words (first, then, next, once this has been done, subsequently, finally) are varied and not repeated.',
  'Lexical Resource':'Process vocabulary (pulper, screens, wound on to reels) taken from the diagram, plus verbs such as turn into and remove.',
  'Grammar':'Passive voice throughout (is collected, is removed, are cut), with relative clauses ("which breaks it down") and time clauses ("once this has been done").'},
 lang=['consists of eight stages','is then combined with','at the same time','once this has been done','subsequently','ready for use','is passed through','is wound on to'])

add(id='t1-islands', task='t1a', type='Line graph', title='Visitors to two islands',
 prompt='The line graph shows the number of visitors to two islands between 1995 and 2020. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',
 chart={'type':'line','title':'Visitors per year (thousands)','x':['1995','2000','2005','2010','2015','2020'],'y':'Visitors (thousands)','max':350,
  'series':[{'name':'Island X','data':[100,160,240,300,280,150]},{'name':'Island Y','data':[80,90,110,150,210,260]}]},
 model=[
 'The line graph shows how many people visited two islands, X and Y, every year from 1995 to 2020.',
 'Overall, visitor numbers on Island X rose strongly before falling back, whereas Island Y enjoyed steady growth throughout. As a result, Y ended the period as the more popular destination, having started well behind.',
 'In 1995, Island X attracted 100,000 visitors, compared with 80,000 for Island Y. The figure for X then tripled over the next fifteen years, peaking at 300,000 in 2010. After that, it declined slowly to 280,000 in 2015 and then dropped sharply to 150,000 in 2020, which was only half of its peak level.',
 'Island Y, by contrast, grew slowly at first, from 90,000 in 2000 to 110,000 in 2005. Growth then accelerated, and the number reached 150,000 in 2010 and 260,000 in 2020, an increase of more than threefold on the 1995 figure. The two lines crossed between 2015 and 2020, when Y overtook X.'],
 notes={'Task Achievement':'Peak, trough and crossing point are all reported. Figures are in thousands and are stated consistently.',
  'Coherence':'Each island is described chronologically in its own paragraph, and the overview already contains the comparison.',
  'Lexical Resource':'Peak, decline, drop, accelerate, overtake are all used precisely. "Fell back" is a natural phrasal verb.',
  'Grammar':'Present perfect is avoided because dates are given. Participle clause ("peaking at") and perfect participle ("having started well behind").'},
 lang=['fell back','peaking at','dropped sharply','which was only half of','accelerated','an increase of more than threefold','overtook','started well behind'])
