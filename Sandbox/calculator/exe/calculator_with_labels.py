import tkinter as tk
#from tkinter import ttk
from functools import partial

from src.processor import Processor

LARGEFONT = ("Helvetica", 46)
SMALLFONT = ("Arial", 22)

class CalculatorFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.processor = Processor()
        self.grid(sticky = tk.N + tk.S + tk.E + tk.W)
        self.configure(bg='#504e4d')
        self.create_widgets()

    def create_widgets(self):
        for row in range(6):
            self.grid_rowconfigure(row, weight = 1)
        for column in range(4):
            self.grid_columnconfigure(column, weight = 1, uniform="columns")

        # field options
        options = {'padx': (1, 0),
                   'pady': (1, 0),
                   'ipadx': 0,
                   'ipady': 0}

        # display
        self.display = tk.Label(self,
                                text = '0',
                                font = LARGEFONT,
                                fg = '#ededed',
                                bg = '#504e4d',
                                borderwidth = 0)
        self.display.grid(column = 0,
                          row = 0,
                          columnspan = 4,
                          sticky = tk.E,
                          padx = 0,
                          pady = 0,
                          ipadx = 6,
                          ipady = 0
                        )

        # buttons
        colors = {
            'background': '#504e4d',
            'gray': '#7e7c7b',
            'darkgray': '#625e5d',
            'orange': '#ff9f0a'
        }
        buttons_settings = [
            {'text': 'AC', 'row': 1, 'column': 0, 'bg': colors['darkgray']},
            {'text': '+/−', 'row': 1, 'column': 1, 'bg': colors['darkgray']},
            {'text': '%', 'row': 1, 'column': 2, 'bg': colors['darkgray']},
            {'text': '÷', 'row': 1, 'column': 3, 'bg': colors['orange']},
            {'text': '7', 'row': 2, 'column': 0, 'bg': colors['gray']},
            {'text': '8', 'row': 2, 'column': 1, 'bg': colors['gray']},
            {'text': '9', 'row': 2, 'column': 2, 'bg': colors['gray']},
            {'text': '×', 'row': 2, 'column': 3, 'bg': colors['orange']},
            {'text': '4', 'row': 3, 'column': 0, 'bg': colors['gray']},
            {'text': '5', 'row': 3, 'column': 1, 'bg': colors['gray']},
            {'text': '6', 'row': 3, 'column': 2, 'bg': colors['gray']},
            {'text': '−', 'row': 3, 'column': 3, 'bg': colors['orange']},
            {'text': '1', 'row': 4, 'column': 0, 'bg': colors['gray']},
            {'text': '2', 'row': 4, 'column': 1, 'bg': colors['gray']},
            {'text': '3', 'row': 4, 'column': 2, 'bg': colors['gray']},
            {'text': '+', 'row': 4, 'column': 3, 'bg': colors['orange']},
            {'text': '0', 'row': 5, 'column': 0, 'bg': colors['gray'], 'columnspan': 2},
            {'text': '.', 'row': 5, 'column': 2, 'bg': colors['gray']},
            {'text': '=', 'row': 5, 'column': 3, 'bg': colors['orange']},
        ]

        self.buttons = []
        for d in buttons_settings:
            button = tk.Label(self,
                              text = d['text'],
                              font = SMALLFONT,
                              bd = 0,
                              borderwidth = 0,
                              relief="solid",
                              bg = d['bg'],
                              fg = '#ededed')
            button.bind("<Button-1>", lambda e, t = d['text']: self.keypressed(t))
            button.grid(column = d['column'],
                        row = d['row'],
                        sticky = tk.N + tk.E + tk.S + tk.W,
                        columnspan = d.get('columnspan', 1),
                        padx = (0 if d['column'] == 0 else 1, 0),
                        pady = (0 if d['row'] == 0 else 1, 0)
            )
            self.buttons.append(button)

        self.grid(padx=0, pady=0, sticky=tk.NSEW)

    def keypressed(self, key):
        self.processor.keyPressed(key)
        self.display['text'] = self.processor.getDisplay()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.title('Calculator')
        self.geometry('234x294')
        self.configure(bg='#504e4d')
        # self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    CalculatorFrame(app)
    app.mainloop()
