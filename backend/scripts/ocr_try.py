import sys
from app.services.ocr_engine import read_image_text

image_text = read_image_text(sys.argv[1])

print(image_text)

print(repr(image_text))