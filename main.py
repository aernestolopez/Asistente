import speech_recognition as sr
import pyttsx3
import pywhatkit

name = 'eva'
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 1.3)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec


def run_eva():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No te entendí, intenta de nuevo")
            continue
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)


if __name__ == '__main__':
    run_eva()
