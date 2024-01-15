 #Jan 9, 2024
# Version #1
# - count red pixels/ Beans
# - Re[prt pm the [ercemtage pf a;; red beans
from PIL import Image

import colour_helper

red_pixels = []
pink_pixels = []

RED_PIXEL = (160,0,0)
PINK_PIXELS = (212, 91, 152)
jelly_bean_img = Image.open("./images/Jelly Beans.jpg")
# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
    # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x,y))
    # If this pixel is red
        if colour_helper.pixel_to_name(current_pixel) == "red":
        # Store its location somewhere
            red_pixels.append((x,y))
        elif colour_helper.pixel_to_name(current_pixel) == "pink":
            pink_pixels.append((x,y))

# Create a map of all red pixels "found"
# Create a new image that sores the map
#   - the new image should be the same size as original
orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height

# ----

pink_pixel_map = Image.new("RGB",(orig_image_width,orig_image_height))
# For every pixel location in the red_pixels list
    # Place a red pixel at that location
for pixel_loc in red_pixels:
    pink_pixel_map.putpixel(pixel_loc, PINK_PIXELS)
# Save the image
pink_pixel_map.save("./Images/red_pixel_map.jpg")
pink_pixel_map.close()

# ----


# Count every red pixel in the list
# Divide that number by the total pixels in the image
pink_percentage = len(pink_pixels) / (jelly_bean_img.width * jelly_bean_img.height)
# TODO: Pink jelly bean report
print(pink_percentage * 100) 