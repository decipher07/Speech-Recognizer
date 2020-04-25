import speech_recognition as sr 
import webbrowser
import time 
import playsound 
import os 
import random 
from gtts import gTTS
from time import ctime

r = sr.Recognizer();

def test2Speech (audio):
    tts = gTTS(text=audio, lang='en')
    r = random.randint(1, 100000)
    audioFile = 'audio-' + str(r) + 'mp3'
    tts.save(audioFile)
    playsound.playsound(audioFile)
    print(audio)
    os.remove(audioFile)

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask :
            test2Speech (ask)
        print('Say Something')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError: 
            print('No Way : Not Able To Get You')
        except sr.RequestError:
            print('Error , Speech Service is Down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        test2Speech('My name is DLI')
    if 'what time is it' in voice_data:
        test2Speech(ctime())
    if 'search' in voice_data:
        search = record_audio('What Do You Want to Search For ?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        test2Speech('Here Is What I found Out' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the Location')
        url = 'https://google.nl/maps/place/'+location + '/&amp'
        webbrowser.get().open(url)
        test2Speech('Here Is What I found Out' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
test2Speech('How Can I Help You ')
while 1:
    voice_data = record_audio()
    respond(voice_data)