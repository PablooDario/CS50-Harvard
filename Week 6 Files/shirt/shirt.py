import sys
import os
from PIL import Image, ImageOps

# Paste an image into another, this program recives 2 arguments (path of the image, path of the image after we paste the second image)

def filesValidation():
    extensions = [".jpg", ".jpeg", ".png"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input, output = sys.argv[1], sys.argv[2]

    input_extension = os.path.splitext(input)[1].lower()
    output_extension = os.path.splitext(output)[1].lower()

    if output_extension not in extensions:
        sys.exit("Invalid output")
    elif input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    return input, output


def main():
    input, output = filesValidation()

    #Open the shirt image and get the size
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        #Open the image where we are going to paste the second image
        with Image.open(input) as im:
            #Resize, paste and save
            aux = ImageOps.fit(im, size)
            aux.paste(shirt, shirt)
            aux.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
