class Words:

    def space(self, space_num):
        spaces = ""
        for x in range(space_num):
            spaces += " "
            #print(" ", end="")
        return spaces

    def letters(self, letter, number):
        letters = ""
        for x in range(number):
            letters += letter
            #print(letter, end="")
        return letters

    def lsl(self, letter, letter_num, space_num):
        lsl = ""
        lsl += self.letters(letter, letter_num)
        lsl += self.space(space_num)
        lsl += self.letters(letter, letter_num)
        return lsl

    def eight_line(self, letter):
        return self.letters(letter, 8)

    def six_line(self, letter):
        return self.letters(letter, 6)

    def two_line(self, letter):
        return self.letters(letter, 2)
    
    def a(self, line_num):
        temp = []
        match line_num:
            case 1: 
                temp.append(self.space(7))
                temp.append(self.letters("A", 1))
                temp.append(self.space(7))
            case 2:
                temp.append(self.space(5))
                temp.append(self.letters("A", 3))
                temp.append(self.space(7))
            case 3:
                temp.append(self.space(3))
                temp.append(self.lsl("A", 1, 6))
                temp.append(self.space(4))  
            case 4:
                temp.append(self.space(2))
                temp.append(self.lsl("A", 2, 4))
                temp.append(self.space(5))
            case 5:
                temp.append(self.space(1))
                temp.append(self.letters("A", 6))
                temp.append(self.space(8))
            case 6:
                temp.append(self.lsl("A", 2, 8))
                temp.append(self.space(3))

        return temp

    def c(self, line_num):
        temp = []
        match line_num:
            case 1:
                temp.append(self.space(5))
                temp.append(self.eight_line("C"))
                temp.append(self.space(2))
            case 2:
                temp.append(self.space(4))
                temp.append(self.two_line("C"))
                temp.append(self.space(20))
            case 3:
                temp.append(self.space(6))
                temp.append(self.two_line("C"))
                temp.append(self.space(20))
            case 4:
                temp.append(self.space(3))
                temp.append(self.two_line("C"))
                temp.append(self.space(20))
            case 5:
                temp.append(self.two_line("C"))
                temp.append(self.space(20))
            case 6:
                temp.append(self.eight_line("C"))
                temp.append(self.space(2))

        return temp

    def i(self):
        temp = []
        temp.append(self.space(4))
        temp.append(self.two_line("I"))
        temp.append(self.space(4))

        return temp

    def r(self, line_num):
        temp = []
        match line_num:
            case 1:
                temp.append(self.space(7))
                temp.append(self.letters("R", 7))
                temp.append(self.space(4))
            case 2:
                temp.append(self.space(4))
                temp.append(self.lsl("R", 2, 8))
                temp.append(self.space(6))
            case 3:
                temp.append(self.space(6))
                temp.append(self.six_line("R"))
                temp.append(self.space(9))
            case 4:
                temp.append(self.space(3))
                temp.append(self.lsl("R", 2, 4))
                temp.append(self.space(9))
            case 5:
                temp.append(self.lsl("R", 2, 5))
                temp.append(self.space(8))
            case 6:
                temp.append(self.space(3))
                temp.append(self.lsl("R", 2, 8))
                temp.append(self.space(5))
            
        return temp

    def s(self, line_num):
        temp = []
        match line_num:
            case 1:
                temp.append(self.space(4))
                temp.append(self.eight_line("S"))
                temp.append(self.space(2))
            case 2:
                temp.append(self.letters("S", 3))
                temp.append(self.space(11))
            case 3:
                temp.append(self.space(6))
                temp.append(self.letters("S", 3))
                temp.append(self.space(5))
            case 4:
                temp.append(self.space(7))
                temp.append(self.letters("S", 3))
                temp.append(self.space(4))
            case 5: 
                temp.append(self.space(8))
                temp.append(self.letters("S", 3))
                temp.append(self.space(3))
            case 6:
                temp.append(self.eight_line("S"))
                temp.append(self.space(6))

        return temp
    
    def t(self, line_num):
        temp = []
        if line_num == 1:
                temp.append(self.eight_line("T"))
                temp.append(self.space(2))
        else:
            temp.append(self.space(3))
            temp.append(self.two_line("T"))
            temp.append(self.space(5))

        return temp
            
    
    def ascii_art_word(self):
        ascii_list = []
        art_list = []
        for x in range(1,7):
            a_temp = self.a(x)
            for i in a_temp:
                ascii_list.append(i)
            s_temp = self.s(x)
            for i in s_temp:
                ascii_list.append(i)
            c_temp = self.c(x)
            for i in c_temp:
                ascii_list.append(i)
            i_temp = self.i()
            for i in i_temp:
                ascii_list.append(i)
            i_temp_2 = self.i()
            for i in i_temp_2:
                ascii_list.append(i)
        
            ascii_list.append("\n")

        ascii = "".join(ascii_list)
    
        for x in range(1,7):
            space_temp = self.space(12)
            for i in space_temp:
                art_list.append(i)
            a_temp = self.a(x)
            for i in a_temp:
                art_list.append(i)
            r_temp = self.r(x)
            for i in r_temp:
                art_list.append(i)
            t_temp = self.t(x)
            for i in t_temp:
                art_list.append(i)
            art_list.append("\n")
        art = "".join(art_list)
        whole_word = ascii + "\n" + art + "\n"
       
        return whole_word