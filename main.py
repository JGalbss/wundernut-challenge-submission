from numpy import asarray
from PIL import Image
from wordsegment import load, segment
import requests

# Image Paths
image_path = "challenge-image.png"
image_path2 = "output.png"
image = Image.open(image_path, "r")

# Api Key
api_key = YOUR API KEY HERE

def revealText():
    imageData = asarray(image)
    # to bypass readonly
    imageData = imageData.copy()
    for count, value in enumerate(imageData):
        for count2, value2 in enumerate(value):
            if value2[2] != 229:
                # setting pixel to rgb black
                imageData[count][count2] = [0, 0, 0]

    revealedImage= Image.fromarray(imageData, "RGB")
    revealedImage.save("output.png")
    return open("output.png", 'rb')

def extractTextFromImage(image):
    payload = {
        "isOverlayRequired": True,
        'apikey': api_key
    }

    r = requests.post('https://api.ocr.space/parse/image',
                      headers={'apikey': api_key},
                      files={"file": image},
                      data=payload
                      )
    data = r.json()['ParsedResults'][0]['TextOverlay']['Lines']

    ParsedText = data[0]['LineText']
    for number in range(1, len(data)):
        ParsedText += data[number]['LineText']

    return ParsedText


def decrypt(parsedText):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decryption = str
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in parsedText:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        # After sifting through the console, it's evident the matching key is 21
        if key == 21:
            decryption = translated
            break
    return decryption

def main():
    outputImage = revealText()
    parsedText = extractTextFromImage(outputImage)
    decryptedText = decrypt(parsedText)
    load()
    parsedAnswer = segment(decryptedText)
    print(parsedAnswer)

main()