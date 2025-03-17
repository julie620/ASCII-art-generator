from PIL import Image
import numpy as np
import math

class ImgArt:

    def get_img_height(self, file_name):
        img = Image.open(file_name)
        height = img.height
        return height

    def get_img_width(self, file_name):
        img = Image.open(file_name)
        width = img.width
        return width

    def get_pixels(self, height, width, file_name):
        img = Image.open(file_name)
        img = img.resize((width, height))
        pixel_matrix = np.empty([height, width], dtype='i,i,i')   
        
        for y in range (height):
            for x in range (width):
                pixel_matrix[y][x] = img.getpixel((x,y))

        return pixel_matrix

    def get_brightness(self, height, width, pixel_matrix):
        brightness_matrix = np.empty([height, width])

        for y in range (height):
            for x in range (width):
                current_tuple = pixel_matrix[y][x]
                r = current_tuple[0]
                g = current_tuple[1]
                b = current_tuple[2]
                brightness_matrix[y][x] = (r + g + b) / 3

        return brightness_matrix

    def get_char(self, height, width, brightness_matrix):
        char_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

        char_matrix = np.empty([height, width], dtype='S')

        for y in range (height):
            for x in range (width):
                calc = math.floor(brightness_matrix[y][x] / 4)
                char_matrix[y][x] = char_string[calc]

        return char_matrix
    
    def get_resize_factor(self, width, height):
        if width >= 700 or height >= 700:
            return 7
        elif width >= 600 or height >= 600:
            return 6
        elif width >= 500 or height >= 500:
            return 5
        elif width >= 400 or height >= 400:
            return 4
        elif width >= 300 or height >= 300:
            return 3
        elif width >= 200 or height >= 200:
            return 2
        elif width >= 100 or height >= 100:
            return 1
        

    def print_art(self, file_name):
        resize_factor = self.get_resize_factor(self.get_img_width(file_name),self.get_img_height(file_name))
        height = self.get_img_height(file_name) // resize_factor
        width = self.get_img_width(file_name) // resize_factor
        print('width: ' + str(width))
        print('height: ' + str(height))
        pixel_matrix = self.get_pixels(height, width, file_name)
        brightness_matrix = self.get_brightness(height, width, pixel_matrix)
        char_matrix = self.get_char(height, width, brightness_matrix)
        for y in range (height):
            for x in range (width):
                print(char_matrix[y][x].decode('utf-8'), end="")
                print(char_matrix[y][x].decode('utf-8'), end="")
                #print(char_matrix[y][x].decode('utf-8'), end="")
            print()
