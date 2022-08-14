"""
References:
    - https://pyshark.com/basic-gui-calculator-in-python/
"""

from tkinter import *


class Calculator:

    def __init__(self, master):

        self.master = master  # assign reference to the main window

        master.title("Calculator")  # title

        self.equation = Entry(master, width=36, borderwidth=5)  # create equation line

        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # assign position to equation line

        self.createButton()  # execute create button

    def createButton(self):  # method to create button

        # create buttons
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton("+")
        b_sub = self.addButton("-")
        b_mult = self.addButton("*")
        b_div = self.addButton("/")
        b_clear = self.addButton("c")
        b_equal = self.addButton("=")

        # arrange buttons
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mult]
        row4 = [b_clear, b0, b_equal, b_div]

        # assign locations to buttons
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def addButton(self, value):  # method to add button

        return Button(
            self.master,
            text=value,
            width=9,
            command=lambda: self.clickButton(str(value)),
        )

    def clickButton(self, value):  # method for button clicks

        current_equation = str(self.equation.get())

        if value == "c":  # "c" clears the screen
            self.equation.delete(-1, END)

        elif value == "=":  # "=" computes
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        else:  # add input to the equation line
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation + value)


if __name__ == "__main__":
    root = Tk()  # create main window
    my_gui = Calculator(root)  # tell calc. class to use window
    root.mainloop()  # user input loop
