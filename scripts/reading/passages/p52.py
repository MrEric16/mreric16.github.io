from lib import *
from svgs import *
A = """Sound is a form of energy that travels through the air as a wave. When something vibrates, such as a guitar string or a loudspeaker, it pushes the air around it, creating areas where the air is squeezed together and areas where it is stretched apart. These changes of pressure spread outwards in all directions and reach the ear, where they are converted into signals for the brain. Because sound is carried by matter, it cannot travel through a vacuum, which is why there is no sound in space."""
B = """Scientists describe sound waves by two main properties. The first is frequency, the number of vibrations in each second, measured in hertz. A high frequency produces a high note, and a low frequency a low one. A human ear can hear frequencies from about 20 hertz to 20,000 hertz, though the upper limit falls with age. Dogs hear sounds up to about 45,000 hertz, and bats and dolphins can detect even higher frequencies, which they use to find their way and their food in the dark or in murky water."""
C = """The second property is amplitude, the height of the wave, which determines how loud a sound is. A large amplitude means that the air is pushed hard, and the sound is loud, while a small amplitude gives a quiet sound. Loudness is measured in decibels. A whisper is about 30 decibels, normal conversation about 60, and a rock concert more than 100. Sounds above 85 decibels can damage hearing if they are heard for many hours, and very loud sounds can cause harm in a few minutes."""
D = """Sound travels at different speeds in different materials. In air at room temperature the speed is about 343 metres per second, which is roughly 1,200 kilometres an hour. In water it is more than four times faster, and in steel about fifteen times faster, since the particles are closer together and pass on the vibration more quickly. This is why a person can hear a train coming by putting an ear to the rail long before the sound arrives through the air. The difference between the speed of light and that of sound also explains why we see lightning before we hear thunder."""
E = """When a sound wave meets a hard surface, it bounces back as an echo. If the surface is more than about seventeen metres away, the echo comes back late enough to be heard as a separate sound. Bats and dolphins use echoes to find their way: they send out a series of high-pitched clicks and listen to the returning echoes, which tell them how far away an object is. Ships use a similar device, called sonar, to measure the depth of the sea and to find submarines and shoals of fish."""
F = """Music depends on regular vibrations. Each instrument produces a particular mixture of frequencies, which gives it its own character, called timbre; this is why a violin and a flute can play the same note yet sound completely different. In string instruments the pitch depends on the length, thickness and tension of the string. A shorter string vibrates faster and gives a higher note, which is why a guitarist presses a string against the fingerboard to shorten the part that vibrates."""
G = """Not all sounds are welcome, and unwanted sound is called noise. In cities, traffic, building work and aircraft produce noise that can cause stress, poor sleep and even heart disease. Dr Lena Fischer, an acoustic engineer, says that noise is among the most underestimated forms of pollution. Cities can reduce it by using quieter road surfaces, by planting trees and by building walls beside busy roads. Individuals can protect themselves with earplugs, and by turning down the volume of their headphones."""
P = passage('p52', 'The Science of Sound', 'Physics', 2, 'You should spend about 20 minutes on this passage.', [A, B, C, D, E, F, G], [
 pic('Which wave pattern, A to D, shows each sound described in the passage?', [(wave('tight'), 160, 120), (wave('sine'), 160, 120), (wave('flat'), 160, 120), (wave('tall'), 160, 120)], [
  ('a note of high frequency', 0, 'B', 'A high frequency produces a high note'),
  ('a note of low frequency', 1, 'B', 'a low frequency a low one'),
  ('a sound with a small amplitude', 2, 'C', 'a small amplitude gives a quiet sound'),
  ('a sound with a large amplitude', 3, 'C', 'A large amplitude means that the air is pushed hard'),
 ]),
 tfng([
  ('Sound travels through a vacuum.', 'F', 'A', 'it cannot travel through a vacuum'),
  ('Sound is a form of energy.', 'T', 'A', 'a form of energy'),
  ('Frequency is measured in hertz.', 'T', 'B', 'measured in hertz'),
  ('The upper limit of human hearing rises with age.', 'F', 'B', 'the upper limit falls with age'),
  ('Dogs can hear higher sounds than humans.', 'T', 'B', 'Dogs hear sounds up to about 45,000 hertz'),
  ('Loudness is measured in decibels.', 'T', 'C', 'measured in decibels'),
  ('Sound travels faster in water than in air.', 'T', 'D', 'more than four times faster'),
  ('Sound travels at the same speed in all materials.', 'F', 'D', 'Sound travels at different speeds in different materials'),
  ('Sonar was invented during a war.', 'NG', 'E', 'Ships use a similar device, called sonar', 'The origin of sonar is not mentioned.'),
 ]),
 mcq([
  ('What does amplitude determine?', ['How high a note is.', 'How loud a sound is.', 'How fast sound travels.', 'How far an echo travels.'], 1, 'C', 'determines how loud a sound is'),
  ('Why do we see lightning before we hear thunder?', ['Light is faster than sound.', 'Thunder is quiet.', 'Sound is stopped by clouds.', 'Lightning is closer.'], 0, 'D', 'The difference between the speed of light and that of sound'),
  ('Why does a violin sound different from a flute?', ['It is louder.', 'It has a different timbre.', 'It is made of wood.', 'It plays lower notes.'], 1, 'F', 'which gives it its own character, called timbre'),
 ]),
 multi('Which TWO animals are mentioned as using echoes in paragraph E?', ['Bats.', 'Dolphins.', 'Whales.', 'Owls.', 'Dogs.'], [0, 1], [('E', 'Bats and dolphins use echoes'), ('E', 'Bats and dolphins use echoes')]),
 head(['How sound travels', 'Pitch and frequency', 'Loudness', 'Speed in different materials', 'Bouncing waves and their uses', 'The sound of instruments', 'Unwanted sound', 'The invention of the radio', 'How the ear works'],
  [('A', 0, 'Sound is a form of energy'), ('B', 1, 'Scientists describe sound waves by two main properties'), ('C', 2, 'determines how loud a sound is'), ('D', 3, 'Sound travels at different speeds in different materials'), ('E', 4, 'it bounces back as an echo'), ('F', 5, 'Music depends on regular vibrations'), ('G', 6, 'unwanted sound is called noise')]),
 info([
  ('an example of a source of vibration', 'A', 'a guitar string or a loudspeaker'),
  ('a figure for the speed of sound in air', 'B' if False else 'D', 'about 343 metres per second'),
  ('a figure for the loudness of a whisper', 'C', 'about 30 decibels'),
  ('a mention of how to hear a train early', 'D', 'putting an ear to the rail'),
  ('a mention of walls beside roads', 'G', 'building walls beside busy roads'),
 ]),
 ends(['produces a high note.', 'is measured in decibels.', 'comes back after about seventeen metres.', 'gives an instrument its character.', 'is found only in water.', 'is the speed of light.', 'cannot be heard by humans.'], [
  ('A high frequency', 0, 'B', 'A high frequency produces a high note'),
  ('Loudness', 1, 'C', 'Loudness is measured in decibels'),
  ('An echo', 2, 'E', 'more than about seventeen metres away'),
  ('Timbre', 3, 'F', 'gives it its own character, called timbre'),
 ]),
 sent(2, [
  ('Sound cannot travel through a ___.', ['vacuum'], 'A', 'through a vacuum'),
  ('Human ears can hear up to about 20,000 ___.', ['hertz'], 'B', '20,000 hertz'),
  ('Loudness is measured in ___.', ['decibels'], 'C', 'measured in decibels'),
  ('Dr Fischer is an acoustic ___.', ['engineer'], 'G', 'an acoustic engineer'),
 ]),
 short(3, [
  ('At what speed does sound travel in air?', ['343 metres'], 'D', 'about 343 metres per second'),
  ('What do ships use to measure sea depth?', ['sonar'], 'E', 'called sonar'),
  ('What does a guitarist press against the fingerboard?', ['a string', 'string'], 'F', 'presses a string against the fingerboard'),
 ]),
 summ('Complete the summary using the list of words below. Choose the correct word for each gap.',
  'A high [[1]] gives a high note, and a large [[2]] gives a loud sound. Sound travels faster in [[3]] than in air. An [[4]] is a sound that bounces back from a hard surface.',
  [(['frequency'], 'B', 'A high frequency'), (['amplitude'], 'C', 'A large amplitude'), (['water'], 'D', 'In water it is more than four times faster'), (['echo'], 'E', 'as an echo')], 1,
  bank=['frequency', 'amplitude', 'water', 'echo', 'light', 'noise', 'wind', 'timbre']),
])
