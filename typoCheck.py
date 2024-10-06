from PIL import Image
from spellchecker import SpellChecker
import pytesseract
import sys

#takes image from backend
#
#
#

#image = ...
imagePath = sys.argv[1]

def typoChecker(image_path):
    try:
        spell = SpellChecker()
        
        image = Image.open(image_path) #opens image

        text = pytesseract.image_to_string(image) #runs the image through ocr
        
        parse = text.split() # splits the string into a list

        wordsParsed = spell.unknown(parse) #stores mispelled words in a list

        numTypo = len(wordsParsed)

        print(f"Misspelled words: {list(wordsParsed)}")
        print(numTypo)

    except:
        print('There was an error processing the image to be checked for typos')

typoChecker(imagePath)