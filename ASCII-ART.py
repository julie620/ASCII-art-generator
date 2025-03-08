from PIL import Image
import numpy as np
import math

def get_img_height() :
    img = Image.open("test.jpg")
    height = img.height
    return height

def get_img_width():
    img = Image.open("test.jpg")
    width = img.width
    return width

def get_pixels(height, width):
    img = Image.open("test.jpg")
    pixel_matrix = np.empty([height, width], dtype='i,i,i')   
    
    for y in range (height):
        for x in range (width):
           pixel_matrix[y][x] = img.getpixel((x,y))

    return pixel_matrix

def get_brightness(height, width, pixel_matrix):
    brightness_matrix = np.empty([height, width])

    for y in range (height):
        for x in range (width):
            current_tuple = pixel_matrix[y][x]
            r = current_tuple[0]
            g = current_tuple[1]
            b = current_tuple[2]
            brightness_matrix[y][x] = (r + g + b) / 3

    return brightness_matrix

def get_char(height, width, brightness_matrix):
    char_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    char_matrix = np.empty([height, width], dtype='S')

    for y in range (height):
        for x in range (width):
            calc = math.floor(brightness_matrix[y][x] / 4)
            char_matrix[y][x] = char_string[calc]

    return char_matrix

def print_art(height, width, char_matrix):
    for y in range (height):
        for x in range (width):
            print(char_matrix[y][x].decode('utf-8'), end="")
            print(char_matrix[y][x].decode('utf-8'), end="")
            print(char_matrix[y][x].decode('utf-8'), end="")
        print()

def main() :
    height = get_img_height()
    width = get_img_width()
    pixel_matrix = get_pixels(height, width)
    brightness_matrix = get_brightness(height, width, pixel_matrix)
    char_matrix = get_char(height, width, brightness_matrix)
    print_art(height, width, char_matrix)


if __name__ == "__main__":
    main()