import speech_recognition as sr
import gtts
import time
from playsound import playsound


r = sr.Recognizer()
# file = sr.AudioFile('Audioen.wav')

with sr.Microphone() as source:
 r.adjust_for_ambient_noise(source)
 data = r.record(source, duration=5)
 print('here is the text')
 text = r.recognize_google(data,language='en')
 print(text)

# with file as source:
#  r.adjust_for_ambient_noise(source)
#  audio = r.record(source)
#  result = r.recognize_google(audio,language='en')
# print(result)

# tts = gtts.gTTS(result)
# tts.save("audiooo.mp3")
# playsound("audiooo.mp3")

# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
#     try:
#         # using google speech recognition
#         print("Text: "+r.recognize_google(audio_text))
#     except:
#          print("Sorry, I did not get that")

# ttss=r.recognize_google(audio_text)
# # time.sleep(1)
# tts = gtts.gTTS(text)
# tts.save("audiooo.mp3")
# # time.sleep(1)
sentence = text
word = 'name'

if word in sentence:
    print('Word found.')
    playsound("teest.mp3")

