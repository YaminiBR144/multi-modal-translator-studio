from PIL import Image
import pytesseract
from googletrans import Translator

translator = Translator()

def image_translate(image, lang="en"):
    # Convert uploaded file to PIL Image if needed
    if not isinstance(image, Image.Image):
        image = Image.open(image)

    text = pytesseract.image_to_string(image)
    translated = translator.translate(text, dest=lang).text
    return text, translated
