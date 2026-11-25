import sys
from app.services.ocr_engine import read_image_text

if len(sys.argv) > 2:
    psm = int(sys.argv[2])
else:
    psm = 3

print(psm)

image_text = read_image_text(sys.argv[1],psm)

  
    

print(image_text)

print(repr(image_text))