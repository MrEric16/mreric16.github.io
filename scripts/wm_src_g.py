# -*- coding: utf-8 -*-
G = []
def add(**k): G.append(k)

add(id='t1g-landlord', task='t1g', type='Formal letter', title='Complaint about heating',
 prompt='You rent a flat, and the heating has not worked for two weeks. You have already phoned the landlord twice. Write a letter to the landlord. In your letter, explain the problem, say what effect it has had on you, and say what you want him to do.\nBegin your letter: Dear Mr Hughes,',
 model=[
 'Dear Mr Hughes,',
 'I am writing to complain about the heating in my flat at 14 Park Road, which has not worked for the past two weeks.',
 'The problem began on 3 November, when the radiators suddenly turned cold. I telephoned your office on 5 November and again on 10 November, and on both occasions I was promised that an engineer would visit within two days. Unfortunately, nobody has come, and the situation has not improved.',
 'This is causing me considerable difficulty. Temperatures in the flat have dropped to about ten degrees at night, which makes it hard to sleep, and I have caught a bad cold as a result. In addition, I am studying for important examinations and cannot work comfortably in such cold conditions.',
 'I would therefore be grateful if you could arrange for a qualified engineer to inspect and repair the boiler by the end of this week. If the repair takes longer, I would also appreciate it if you would provide electric heaters in the meantime. Should the problem continue, I will have no alternative but to contact the local housing office.',
 'I look forward to hearing from you as soon as possible.',
 'Yours sincerely,','Eric Walker'],
 notes={'Task Achievement':'All three bullet points are covered in full: the problem (with dates), its effect, and two clear requests. The purpose is stated in the first sentence.',
  'Coherence':'Each paragraph has one function. Dates and the earlier phone calls give a logical timeline.',
  'Lexical Resource':'Formal register without being stiff: I would be grateful if, in the meantime, no alternative but to, considerable difficulty.',
  'Grammar':'Conditionals (I would be grateful if you could), inversion ("Should the problem continue") and a mix of tenses. "Yours sincerely" is used because the letter begins with a name.'},
 lang=['I am writing to complain about','on both occasions','considerable difficulty','I would be grateful if you could','in the meantime','Should the problem continue','no alternative but to','I look forward to hearing from you'])

add(id='t1g-leave', task='t1g', type='Semi-formal letter', title='Asking for time off',
 prompt='You would like to take two weeks of unpaid leave from your job to attend a course. Write a letter to your manager. In your letter, explain what course you want to attend, say why it would be useful for your work, and suggest how your work could be covered while you are away.\nBegin your letter: Dear Ms Carter,',
 model=[
 'Dear Ms Carter,',
 'I am writing to ask whether I could take two weeks of unpaid leave in March, from the 10th to the 21st, in order to attend an intensive course in business English at the City Language Centre.',
 'The course focuses on writing reports and giving presentations, which are two areas in which I would like to improve. Since many of our clients are based abroad, I believe that stronger communication skills would help me to deal with them more effectively. I am confident that the company would benefit directly from this training.',
 'I have thought carefully about how my duties could be covered. Most of my regular tasks, such as answering enquiries and updating the database, can be completed in advance or shared between my colleagues. Mr Brown has kindly agreed to handle any urgent client calls, and I would be happy to prepare a detailed handover note before I leave.',
 'I realise that this is a busy period, so I would be very grateful for your consideration. If you would like to discuss the arrangements, I am available at any time that suits you.',
 'Thank you for your time.',
 'Yours sincerely,','Eric Walker'],
 notes={'Task Achievement':'Each of the three bullets gets its own developed paragraph. The request is specific (dates, place) and the answer anticipates the manager\'s main worry, who will cover the work.',
  'Coherence':'Purpose, benefit, practical solution, polite close. Reference words (this training, such as) tie paragraphs together.',
  'Lexical Resource':'Natural business collocations: intensive course, handover note, deal with clients, urgent calls.',
  'Grammar':'Reported/embedded questions ("whether I could take"), relative clauses, and a first conditional in the final paragraph.'},
 lang=['I am writing to ask whether','in order to attend','focuses on','I am confident that','I have thought carefully about','handover note','I would be very grateful for your consideration','at any time that suits you'])

add(id='t1g-friend', task='t1g', type='Informal letter', title='A friend is coming to visit',
 prompt='A friend from another country is going to visit you for a week. Write a letter to your friend. In your letter, say how pleased you are that your friend is coming, suggest some things you could do together, and advise your friend what to bring.\nBegin your letter: Dear Sam,',
 model=[
 'Dear Sam,',
 'Thanks so much for your last email. I was thrilled to hear that you are finally coming to Tashkent! It feels like ages since we last met, and I can\'t wait to show you around.',
 'We have plenty to do in a week. If the weather is good, we could spend a day in the old town and have lunch at the Chorsu Bazaar, where you can try fresh bread and the best plov in the city. I\'d also love to take you to Samarkand by high-speed train, which only takes a couple of hours, so we could easily go there and back in a day. And if you fancy something more relaxing, we could just wander through the parks and have a coffee.',
 'As for packing, bring comfortable shoes, because we\'ll be walking a lot. The days are still hot in September, so a hat and sun cream are a must, but evenings can be cool, so don\'t forget a light jacket. Oh, and if you have room in your bag, a few photos from your trip last year would be great!',
 'Let me know your flight details and I\'ll pick you up from the airport. I\'m really looking forward to seeing you.',
 'Take care,','Eric'],
 notes={'Task Achievement':'All three points covered with specific, personal detail. The tone fits the reader, a close friend.',
  'Coherence':'Warm opening, plans, practical advice, friendly close. Informal linkers (As for, Oh, and) keep the flow natural.',
  'Lexical Resource':'Informal but accurate: thrilled, ages, fancy, a must, wander. Contractions are normal in this register.',
  'Grammar':'First conditional (If the weather is good, we could...), modal verbs for suggestions, and "which" clauses. Note the comma splices are avoided even though the style is relaxed.'},
 lang=['I was thrilled to hear that','It feels like ages since','I can\'t wait to','If you fancy','As for packing','a must','Let me know','I\'m really looking forward to seeing you'])
