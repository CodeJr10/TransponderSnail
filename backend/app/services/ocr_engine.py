from app.config import settings
import pytesseract
from PIL import Image

if settings.tesseract_cmd is not None:

    pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd

def read_image_text(image_path: str) -> str:
    image = Image.open(image_path)

    image_text = pytesseract.image_to_string(image)

    return image_text


