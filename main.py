import speech_recognition as sr 
import webbrowser
import time 
from time import ctime

r = sr.Recognizer();

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask :
            print (ask)
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
        print('My name is DLI')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What Do You Want to Search For ?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        print('Here Is What I found Out' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the Location')
        url = 'https://google.nl/maps/place/'+location + '/&amp'
        webbrowser.get().open(url)
        print('Here Is What I found Out' + location)
    if 'exit' in voice_data:
        exit()
        
time.sleep(1)
print('How Can I Help You ')
while 1:
    voice_data = record_audio()
    respond(voice_data)