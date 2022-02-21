from PIL import Image

#make sure the images are in a folder called "images" in the script directory

#load the image
image_original = Image.open("images/beach.jpg")

#get the width and height and write to variables
width, height = image_original.size

#get pixels
pixels_original = image_original.load()

#create a square in the corner
for h in range(0, 64):
    for w in range(0, 64):
        pixels_original[w, h] = (235, 64, 52)

image_original.save("images/out.jpg")
