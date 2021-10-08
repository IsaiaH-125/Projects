# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)

image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Get dimensions (size) of the image



# Grab r, g, b,

pixel = (red, green, blue)

red = pixel[0]
green = pixel[1]
blue = pixel[2]

red, green, blue = pixel

average = int((red + green + blue) / 3)

gray_pixel = (average, average, average)

output_image.save('grayscale.jpg')

# Put that in the new image

output_image.putpixel((x, y), gray_pixel)
# Calculate the average
# Create a gray pixel
# TODO: put that in the new image




# Modify the image to convert it from color to grayscale
# (r , g , b) ---> ( ?, ? , ?)



