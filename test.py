import pytesseract
from PIL import Image, ImageGrab

def trim_str(raw_txt):
    new_txt = ""
    for i in range(len(raw_txt)):
        if ord(raw_txt[i]) != 32:
            new_txt += raw_txt[i]
        elif ord(raw_txt[i+1]) < 3585:
            new_txt += raw_txt[i]
    return new_txt

if __name__ == "__main__":
    img = Image.open('1113.png')
    result = pytesseract.image_to_string(img, lang="tha+eng")
    new_txt = trim_str(result)
    print(new_txt)