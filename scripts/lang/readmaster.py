# Parametric reading texts. Each text has 5 facts; each fact has 4 values (English label, English reference sentence).
# Per language (src/read/<id>.txt) gives a skeleton with {1}..{5} and the 4 sentences per fact. Each attempt draws a random value per fact,
# so one text has 4^5 = 1024 variants; the questions' correct answers follow the draw.
def T(id, en, lv, facts): return dict(id=id, en=en, lv=lv, facts=facts)
def F(q, *vs): return dict(q=q, v=[(a, b) for a, b in vs])
MASTER = [
 T('r1', 'About me', 'A1', [
  F("How old is the writer?", ("20", "I am 20 years old."), ("25", "I am 25 years old."), ("30", "I am 30 years old."), ("35", "I am 35 years old.")),
  F("Who does the writer live with?", ("Alone", "I live alone."), ("A sister", "I live with my sister."), ("A friend", "I live with a friend."), ("A cousin", "I live with my cousin.")),
  F("Where does the writer work?", ("In a bank", "I work in a bank."), ("In a school", "I work in a school."), ("In a shop", "I work in a shop."), ("In a hospital", "I work in a hospital.")),
  F("What does the writer do on Sundays?", ("Goes swimming with friends", "On Sundays I go swimming with my friends."), ("Watches TV", "On Sundays I watch TV."), ("Goes to the market", "On Sundays I go to the market."), ("Works", "On Sundays I work.")),
  F("What colour is the writer's cat?", ("White", "It is white."), ("Brown", "It is brown."), ("Grey", "It is grey."), ("Black", "It is black."))]),
 T('r2', 'My day', 'A1', [
  F("What time does the writer get up?", ("Six", "I get up at six o'clock."), ("Seven", "I get up at seven o'clock."), ("Eight", "I get up at eight o'clock."), ("Nine", "I get up at nine o'clock.")),
  F("What does the writer have for breakfast?", ("Tea and bread", "For breakfast I have tea and bread."), ("Eggs and rice", "For breakfast I have eggs and rice."), ("Milk and cake", "For breakfast I have milk and cake."), ("Only fruit", "For breakfast I have only fruit.")),
  F("How does the writer go to school?", ("On foot", "I go to school on foot."), ("By bus", "I go to school by bus."), ("By car", "I go to school by car."), ("By bike", "I go to school by bike.")),
  F("What does the writer do at five o'clock?", ("Homework", "At five o'clock I do my homework."), ("Reads a book", "At five o'clock I read a book."), ("Plays football", "At five o'clock I play football with my friends."), ("Goes shopping", "At five o'clock I go shopping.")),
  F("What time does the writer go to bed?", ("Nine", "I go to bed at nine o'clock."), ("Ten", "I go to bed at ten o'clock."), ("Eleven", "I go to bed at eleven o'clock."), ("Midnight", "I go to bed at midnight."))]),
 T('r3', 'At the market', 'A1', [
  F("When does the writer go to the market?", ("Sunday morning", "On Sunday morning I go to the market with my mother."), ("Friday evening", "On Friday evening I go to the market with my mother."), ("Saturday evening", "On Saturday evening I go to the market with my mother."), ("Saturday morning", "On Saturday morning I go to the market with my mother.")),
  F("How far is the market from the house?", ("Five minutes", "It is five minutes from our house."), ("Ten minutes", "It is ten minutes from our house."), ("Twenty minutes", "It is twenty minutes from our house."), ("One hour", "It is one hour from our house.")),
  F("How many kilos of apples do they buy?", ("One", "We buy one kilo of apples."), ("Two", "We buy two kilos of apples."), ("Three", "We buy three kilos of apples."), ("Four", "We buy four kilos of apples.")),
  F("What does the old man sell?", ("Honey", "He sells honey."), ("Cheese", "He sells cheese."), ("Bread", "He sells bread."), ("Tomatoes", "He sells tomatoes.")),
  F("What does the writer do at home?", ("Sleeps", "At home I sleep."), ("Helps cook lunch", "At home I help my mother cook lunch."), ("Watches TV", "At home I watch TV."), ("Does homework", "At home I do my homework."))]),
 T('r4', 'My family', 'A1', [
  F("Where does the writer's family live?", ("In a flat", "We live in a flat."), ("In a house", "We live in a house."), ("In a village", "We live in a village."), ("In the city centre", "We live in the city centre.")),
  F("What is the writer's father's job?", ("Doctor", "My father is a doctor."), ("Teacher", "My father is a teacher."), ("Nurse", "My father is a nurse."), ("Driver", "My father is a driver.")),
  F("Where does the writer's mother work?", ("In a school", "My mother works in a school."), ("In a hospital", "My mother works in a hospital."), ("In a shop", "My mother works in a shop."), ("In a bank", "My mother works in a bank.")),
  F("How old is the writer's brother?", ("Ten", "My brother is ten years old."), ("Eight", "My brother is eight years old."), ("Nine", "My brother is nine years old."), ("Twelve", "My brother is twelve years old.")),
  F("When does the grandmother cook?", ("Every day", "She cooks every day."), ("On Fridays", "She cooks on Fridays."), ("On Saturdays", "She cooks on Saturdays."), ("On Sundays", "She cooks on Sundays."))]),
 T('r5', 'A weekend trip', 'A2', [
  F("How many friends went with the writer?", ("Two", "Last Saturday I went to the mountains with two friends."), ("Three", "Last Saturday I went to the mountains with three friends."), ("Four", "Last Saturday I went to the mountains with four friends."), ("Five", "Last Saturday I went to the mountains with five friends.")),
  F("How long did the train journey take?", ("One hour", "The journey took one hour."), ("Two hours", "The journey took two hours."), ("Three hours", "The journey took three hours."), ("Four hours", "The journey took four hours.")),
  F("What was the weather like?", ("Rainy", "It was rainy."), ("Hot", "It was hot."), ("Windy", "It was windy."), ("Sunny but cold", "It was sunny but cold.")),
  F("What did the writer forget?", ("The gloves", "I forgot my gloves."), ("The camera", "I forgot my camera."), ("The lunch", "I forgot my lunch."), ("The ticket", "I forgot my ticket.")),
  F("Why did they take a taxi?", ("They missed the last bus", "We took a taxi because we missed the last bus."), ("They were tired", "We took a taxi because we were tired."), ("The bus was full", "We took a taxi because the bus was full."), ("The train was cancelled", "We took a taxi because the train was cancelled."))]),
 T('r6', 'An invitation', 'A2', [
  F("When is the party?", ("Next Friday evening", "The party is next Friday evening."), ("Next Saturday afternoon", "The party is next Saturday afternoon."), ("Next Sunday morning", "The party is next Sunday morning."), ("Next Thursday evening", "The party is next Thursday evening.")),
  F("Where is the party?", ("In a restaurant", "The party is in a restaurant."), ("At the writer's house", "The party is at my house."), ("In a park", "The party is in the park."), ("At a friend's house", "The party is at my friend's house.")),
  F("Who is going to make the cake?", ("The writer's sister", "My sister is going to make the cake."), ("The writer's mother", "My mother is going to make the cake."), ("A friend", "A friend is going to make the cake."), ("The writer", "I am going to make the cake myself.")),
  F("What does the writer ask the friend to bring?", ("Music", "Please bring some music."), ("Food", "Please bring some food."), ("Games", "Please bring some games."), ("Drinks", "Please bring some drinks.")),
  F("When must the friend reply?", ("By Monday", "Tell me by Monday if you can come."), ("By Tuesday", "Tell me by Tuesday if you can come."), ("By Wednesday", "Tell me by Wednesday if you can come."), ("Tomorrow", "Tell me tomorrow if you can come."))]),
 T('r7', 'My town', 'A1', [
  F("Where does the writer live?", ("In a big city", "I live in a big city."), ("In a small town", "I live in a small town."), ("In a village", "I live in a village."), ("In a town by the sea", "I live in a town by the sea.")),
  F("What is near the writer's house?", ("A park", "Near my house there is a park."), ("A school", "Near my house there is a school."), ("A station", "Near my house there is a station."), ("A supermarket", "Near my house there is a supermarket.")),
  F("How often does the bus come?", ("Every five minutes", "The bus comes every five minutes."), ("Every ten minutes", "The bus comes every ten minutes."), ("Every twenty minutes", "The bus comes every twenty minutes."), ("Every thirty minutes", "The bus comes every thirty minutes.")),
  F("What is the writer's favourite place?", ("The library", "My favourite place is the library."), ("The cinema", "My favourite place is the cinema."), ("The river", "My favourite place is the river."), ("The old market", "My favourite place is the old market.")),
  F("What are the people in the town like?", ("Friendly", "The people in my town are friendly."), ("Busy", "The people in my town are very busy."), ("Quiet", "The people in my town are quiet."), ("Funny", "The people in my town are funny."))]),
 T('r8', 'My home', 'A1', [
  F("How many rooms does the flat have?", ("Two", "My flat has two rooms."), ("Three", "My flat has three rooms."), ("Four", "My flat has four rooms."), ("Five", "My flat has five rooms.")),
  F("Which floor is the flat on?", ("The first", "It is on the first floor."), ("The second", "It is on the second floor."), ("The third", "It is on the third floor."), ("The fourth", "It is on the fourth floor.")),
  F("What is the writer's favourite room?", ("The kitchen", "My favourite room is the kitchen."), ("The bedroom", "My favourite room is the bedroom."), ("The living room", "My favourite room is the living room."), ("The balcony", "My favourite room is the balcony.")),
  F("What colour are the bedroom walls?", ("Blue", "The walls of my bedroom are blue."), ("Green", "The walls of my bedroom are green."), ("White", "The walls of my bedroom are white."), ("Yellow", "The walls of my bedroom are yellow.")),
  F("What does the writer have in the bedroom?", ("A desk", "In my bedroom I have a big desk."), ("A bookcase", "In my bedroom I have a big bookcase."), ("A computer", "In my bedroom I have a new computer."), ("A guitar", "In my bedroom I have an old guitar."))]),
 T('r9', 'My friend', 'A1', [
  F("How old is the writer's friend?", ("18", "He is 18 years old."), ("20", "He is 20 years old."), ("22", "He is 22 years old."), ("24", "He is 24 years old.")),
  F("What does the friend do?", ("Student", "He is a student."), ("Doctor", "He is a doctor."), ("Teacher", "He is a teacher."), ("Driver", "He is a driver.")),
  F("What does the friend like?", ("Cooking", "He likes cooking."), ("Reading", "He likes reading."), ("Football", "He likes football."), ("Chess", "He likes chess.")),
  F("Where is the friend from?", ("A village", "He is from a village."), ("The capital", "He is from the capital."), ("A port city", "He is from a port city."), ("The mountains", "He is from the mountains.")),
  F("How often do they meet?", ("Every day", "We meet every day."), ("Every week", "We meet every week."), ("On Saturdays", "We meet on Saturdays."), ("Every month", "We meet every month."))]),
 T('r10', 'At the café', 'A1', [
  F("Who is with the writer?", ("A sister", "I am with my sister."), ("A friend", "I am with my friend."), ("A mother", "I am with my mother."), ("A brother", "I am with my brother.")),
  F("What does the writer drink?", ("Tea", "I have tea."), ("Coffee", "I have coffee."), ("Juice", "I have juice."), ("Water", "I have water.")),
  F("What do they eat?", ("Soup", "We also eat soup."), ("Salad", "We also eat salad."), ("Cake", "We also eat cake."), ("Sandwiches", "We also eat sandwiches.")),
  F("What time do they arrive?", ("Two o'clock", "We arrive at two o'clock."), ("Three o'clock", "We arrive at three o'clock."), ("Four o'clock", "We arrive at four o'clock."), ("Five o'clock", "We arrive at five o'clock.")),
  F("How does the writer pay?", ("With cash", "I pay with cash."), ("By card", "I pay by card."), ("With a phone", "I pay with my phone."), ("Half each", "We pay half each."))]),
 T('r11', 'Last holiday', 'A2', [
  F("Where did the writer go?", ("To the sea", "Last summer we went to the sea."), ("To the mountains", "Last summer we went to the mountains."), ("To a big city", "Last summer we went to a big city."), ("To a village", "Last summer we went to a village.")),
  F("How did they travel?", ("By plane", "We travelled by plane."), ("By train", "We travelled by train."), ("By bus", "We travelled by bus."), ("By car", "We travelled by car.")),
  F("How long did they stay?", ("Three days", "We stayed for three days."), ("One week", "We stayed for one week."), ("Ten days", "We stayed for ten days."), ("Two weeks", "We stayed for two weeks.")),
  F("What did they do every morning?", ("Went for a walk", "Every morning we went for a walk."), ("Slept late", "Every morning we slept late."), ("Had a big breakfast", "Every morning we had a big breakfast."), ("Took photos", "Every morning we took photos.")),
  F("What was the best thing?", ("The food", "The best thing was the food."), ("The weather", "The best thing was the weather."), ("The people", "The best thing was the people."), ("The hotel", "The best thing was the hotel."))]),
 T('r12', 'My timetable', 'A2', [
  F("What is the first lesson on Monday?", ("Maths", "On Monday my first lesson is maths."), ("English", "On Monday my first lesson is English."), ("History", "On Monday my first lesson is history."), ("Biology", "On Monday my first lesson is biology.")),
  F("What is the writer's favourite subject?", ("Geography", "My favourite subject is geography."), ("Music", "My favourite subject is music."), ("Physics", "My favourite subject is physics."), ("Art", "My favourite subject is art.")),
  F("When must the homework be handed in?", ("On Tuesday", "We must hand in our homework on Tuesday."), ("On Wednesday", "We must hand in our homework on Wednesday."), ("On Thursday", "We must hand in our homework on Thursday."), ("On Friday", "We must hand in our homework on Friday.")),
  F("Which club does the writer go to after school?", ("The music club", "After school I go to the music club."), ("The football club", "After school I go to the football club."), ("The chess club", "After school I go to the chess club."), ("The drawing club", "After school I go to the drawing club.")),
  F("What is the English teacher like?", ("Kind", "My English teacher is very kind."), ("Strict", "My English teacher is very strict."), ("Funny", "My English teacher is very funny."), ("Young", "My English teacher is very young.")),
 ]),
]
