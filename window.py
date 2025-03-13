import tkinter as tk
from tkinter import*
from words import Words
import os
from PIL import Image, ImageTk
from img_art import ImgArt

class Window:

    def run(self):
        
        root = tk.Tk()
        root.title('ASCII Art Generator')
        intro_label = self.get_intro_label(root)

        img_listbox = self.get_img_listbox(root)

        result_label = Label(root, text="")
        img_label = Label(root)

        preview_btn = Button(root, 
                                text='Preview Image',
                                command= lambda: self.selected_img(img_listbox, result_label, img_label))
        
        intro_label.pack()
        img_listbox.pack()
        preview_btn.pack(side='bottom')
        result_label.pack()
        img_label.pack()
        root.mainloop()

    def get_intro_label(self, root):
        letter_art = Words()

        ascii_art = letter_art.ascii_art_word()
        intro = Label(root, 
                      text = ascii_art, 
                      justify = LEFT)
        return intro

    def get_img_listbox(self, root):
        path = "images"
        img_list = os.listdir(path)

        img_listbox = Listbox(root)

        for x in img_list:
            img_listbox.insert(END, x)
        
        return img_listbox

    def selected_img(self, img_listbox: Listbox, result_label: Label, img_label: Label):
        ascii_art = ImgArt()
        
        selected_index = img_listbox.curselection()

        if selected_index:
            selected_img = img_listbox.get(selected_index[0])
            result_label.config(text=f"Selected Image: {selected_img}")
            path = "images\\" + selected_img
            self.img = Image.open(path)
            self.img = ImageTk.PhotoImage(self.img)
            img_label.config(image = self.img)
            ascii_art.print_art(path)

        else:
            result_label.config(text="No image selected")

    def preview(self):
        print('Test')   

