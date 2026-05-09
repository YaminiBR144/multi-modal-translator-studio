import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator

translator = Translator()

def voice_translate(lang="en"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st_text = "Listening..."
        print(st_text)
        audio = r.listen(source)

    text = r.recognize_google(audio)
    translated = translator.translate(text, dest=lang).text

    # Convert back to speech
    tts = gTTS(translated, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")

    return text, translated
