from img_art import ImgArt
from words import Words

def main():
    letter_art = Words()
    art = ImgArt()

    letter_art.print_ascii_art()
    art.print_art()

if __name__ == "__main__":
    main()