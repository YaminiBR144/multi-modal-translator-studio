from googletrans import Translator

translator = Translator()

def text_translate(text, lang="en"):
    return translator.translate(text, dest=lang).text
