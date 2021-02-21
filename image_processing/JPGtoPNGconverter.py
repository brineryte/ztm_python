from PIL import Image
import sys
import os

folder = sys.argv[1]
newFolder = sys.argv[2]

if not os.path.isdir(newFolder):
    os.mkdir(newFolder)

for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        img = Image.open(f"{folder}/{filename}")
        img.save(f"{newFolder}/{filename.replace('jpg', 'png')}", "png")
