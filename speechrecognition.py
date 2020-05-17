import speech_recognition as sr
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
  with sr.Microphone() as source:
    if ask:
      MrHacker_speak(ask)
    MrHacker_speak('Please say something')
    audio = r.listen(source)
    try:
       voice_data = r.recognize_google(audio)
       #print(voice_data)
    except sr.UnknownValueError:
      MrHacker_speak('Sorry, I did not get that')
    except sr.RequestError:
       MrHacker_speak('Sorry, my speech service is down')
    return voice_data

def MrHacker_speak(audio_string):
  tts = gTTS(text=audio_string, lang='en')
  r = random.randint(1, 10000000)
  audio_file = 'audio' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string, [...])
  os.remove(audio_file)
  
def respond(voice_data):
  if 'what is your name' in voice_data:
    MrHacker_speak('My name is Mr Hacker')
  if 'what is the time' in voice_data:
    MrHacker_speak(ctime())
  if 'search' in voice_data:
    search = record_audio('what do you want to search for?')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    MrHacker_speak('here is what I found for' + search)
  #if 'find location' in voice_data:
   # location

MrHacker_speak('Hello How can I help you? I am powered by my programmer which remains to stay anonymous')
voice_data = record_audio()
respond(voice_data)

