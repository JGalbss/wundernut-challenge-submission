# Third party modules
from numpy import asarray, array
from PIL import Image
import pytesseract

image_path = "challenge-image.png"
image_path2 = "output.png"
image = Image.open(image_path, "r")

def main():
    imageData = asarray(image)
    # to bypass readonly
    imageData = imageData.copy()
    for count, value in enumerate(imageData):
        # O(n^2) >:(
        for count2, value2 in enumerate(value):
            if value2[2] != 229:
                imageData[count][count2] = [0, 0, 0]

    outputImage = Image.fromarray(imageData, "RGB")
    outputImage.save("output.png")
    extractTextImage = Image.open(image_path2)
    text = pytesseract.image_to_string(extractTextImage)

main()