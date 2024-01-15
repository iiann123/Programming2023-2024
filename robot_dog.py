# Functions that help wither colours

from PIL import Image

import colour_helper

red_pixels = []
RED_PIXEL = (160,0,0)


RED_PIXEL = (160,0,0)

boy_ball= Image.open("./images/Red Ball.jpeg")
# Visit every pixel in the image
for y in range(boy_ball.height):
    for x in range(boy_ball.width):
    # Get the pixel information
        current_pixel = boy_ball.getpixel((x,y))
    # If this pixel is red
        if colour_helper.pixel_to_name(current_pixel) == "red":
        # Store its location somewhere
            red_pixels.append((x,y))
print(red_pixels)
max_x_val = max(red_pixels)
print(max_x_val)
max_y_val = max(red_pixels, key=lambda x: x[1])
print(max_y_val)

min_x_val = min(red_pixels)
print(min_x_val)
min_y_val = min(red_pixels, key=lambda x: x[1])
print(min_y_val)


sum_x = max_x_val[0] + min_x_val[0]
sum_y = max_y_val[1] + min_y_val[1]
mid_x = sum_x/2
mid_y = sum_y/2

print(f"your mid point is {mid_x},{mid_y}")