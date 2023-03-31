from datetime import datetime
import speech_recognition as sr
import  pyttsx3
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
activationWord = 'hello' 

browser_path = r"C:\Users\Nischal\AppData\Local\Programs\Opera\opera.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(browser_path))


def speak(text, rate = 120):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Reconizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
    except Exception as exception:
        print('I did not quite get what ur saying.')
        speak('I did not quite get wht you were saying')
        print(exception)
        return 'None'
    return query

if __name__ ==  '__main__':
    speak('System Ready.')

    while True:
        query = parseCommand().lower().split()
        if query[0] == activationWord:
            query.pop(0)
            dqu = ' '.join(query[1:])
            print('your query was : ' + dqu)
            if query[0] == 'shutdown':
                speak('Shutting Down')
                exit()
                break
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('opera').open_new(query)
        
        else:
            speak('Unauthorized.')