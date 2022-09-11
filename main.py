# Third party modules
from numpy import asarray, array
from PIL import Image

image_path = "challenge-image.png"
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
    outputImage.save("test.png")

main()