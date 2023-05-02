# /usr/bin/python

from PIL import Image

from os import path, mkdir
import pathlib

size = (256, 256)
errors: list[pathlib.Path] = []

if not path.exists("./dataset/"):
    mkdir("./dataset")

for input_folder in pathlib.Path("./images/").iterdir():
    output_folder = f"./dataset/{input_folder.name}/"
    if not path.exists(output_folder):
        mkdir(output_folder)
    for image in input_folder.iterdir():
        output_path = output_folder + (image.name.split(".")[0]) + "_resized.png"
        try:
            with Image.open(image) as im:
                out = im.resize(size)
                out.save(output_path, "PNG")
        except:
            errors.append(image)

    print(f"done with folder {input_folder}")

print("Problèmes : " + "\n\t".join(map(str, errors)))
