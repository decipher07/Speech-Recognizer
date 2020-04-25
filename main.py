import speech_recognition as sr 
import webbrowser
from time import ctime

r = sr.Recognizer();

def record_audio(ask = False):
    with sr.Microphone() as source:
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

print('How Can I Help You ')
voice_data = record_audio()
print(voice_data)

respond(voice_data)