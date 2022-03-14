from PIL import Image

#make sure the images are in a folder called "images" in the script directory

#load the image
image_background = Image.open("images/beach.jpg")
image_foreground = Image.open("images/penguin.jpg")

#get the width and height and write to variables
width, height = image_foreground.size

#get pixels
pixels_background = image_background.load()
pixels_foreground = image_foreground.load()

#combine the two images with a greenscreen effect
#absolute value for the green used is 44, 207, 64
for h in range(height):
    for w in range(width):
        r, g, b, = pixels_foreground[w, h]
        if r > 50 or g < 200 or b > 70:
           pixels_background[w, h] = (r, g, b) 

print("Wrote file to images/out.jpg")
image_background.save("images/out.jpg")
