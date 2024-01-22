def is_light(pixel: tuple) -> bool:
    """"""

    return


# Test?
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(is_light(light_pixel))  # True
print(is_light(light_gray))  # True
print(is_light(dark_gray))  # False
print(is_light(dark_pixel))  # False