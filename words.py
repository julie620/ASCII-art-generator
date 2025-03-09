class Words:

    def space(self, line_num):
        for x in range(line_num):
            print(" ", end="")

    def letters(self, letter, number):
        for x in range(number):
            print(letter, end="")

    def lsl(self, letter, letter_num, space_num):
        self.letters(letter, letter_num)
        self.space(space_num)
        self.letters(letter, letter_num)

    def eight_line(self, letter):
        self.letters(letter, 8)

    def six_line(self, letter):
        self.letters(letter, 6)

    def two_line(self, letter):
        self.letters(letter, 2)
    
    def a(self, line_num):
        match line_num:
            case 1: 
                self.space(5)
                self.letters("A", 1)
                self.space(8)
                
            case 2:
                self.space(4)
                self.letters("A", 3)
                self.space(7)
                
            case 3:
                self.space(3)
                self.lsl("A", 1, 3)
                self.space(6)
                
            case 4:
                self.space(2)
                self.lsl("A", 2, 3)
                self.space(5)
                
            case 5:
                self.space(1)
                self.letters("A", 9)
                self.space(4)
                
            case 6:
                self.lsl("A", 2, 7)
                self.space(3)

    def c(self, line_num):
        match line_num:
            case 1:
                self.space(2)
                self.eight_line("C")
                self.space(2)
            case 2:
                self.two_line("C")
                self.space(10)
            case 3:
                self.two_line("C")
                self.space(10)
            case 4:
                self.two_line("C")
                self.space(10)
            case 5:
                self.two_line("C")
                self.space(10)
            case 6:
                self.space(2)
                self.eight_line("C")
                self.space(2)

    def i(self, line_num):
        self.space(4)
        self.two_line("I")
        self.space(4)

    def r(self, line_num):
        match line_num:
            case 1:
                self.eight_line("R")
                self.space(2)
            case 2:
                self.lsl("R", 2, 4)
                self.space(2)
            case 3:
                self.six_line("R")
                self.space(4)
            case 4:
                self.lsl("R", 2, 4)
                self.space(2)
            case 5:
                self.lsl("R", 2, 5)
                self.space(1)
            case 6:
                self.lsl("R", 2, 6)

    def s(self, line_num):
        match line_num:
            case 1:
                self.space(1)
                self.eight_line("S")
                self.space(3)
            case 2:
                self.letters("S", 3)
                self.space(9)
            case 3:
                self.space(2)
                self.letters("S", 3)
                self.space(7)
            case 4:
                self.space(4)
                self.letters("S", 3)
                self.space(5)
            case 5: 
                self.space(6)
                self.letters("S", 3)
                self.space(3)
            case 6:
                self.eight_line("S")
                self.space(4)
    
    def t(self, line_num):
        if line_num == 1:
                self.eight_line("T")
                self.space(2)
        else:
            self.space(3)
            self.two_line("T")
            self.space(5)
            
    def print_ascii_art(self):
        for x in range(1,7):
            self.a(x)
            self.s(x)
            self.c(x)
            self.i(x)
            self.i(x)
            print()
        print()
        for x in range(1,7):
            self.space(12)
            self.a(x)
            self.r(x)
            self.t(x)
            print()
        print()