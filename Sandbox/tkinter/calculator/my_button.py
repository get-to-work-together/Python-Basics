import tkinter as tk


class MyButton(tk.Frame):

    FONT = ('Arial', 18)
    BACKGROUND = 'pink'
    FOREGROUND = 'white'
    BORDERCOLOR = 'red'
    RELIEF = 'flat'  # flat raised sunken ridge solid groove
    BORDERWIDTH = 10
    HEIGHT = None
    WIDTH = None
    ACTIVEBACKGROUND = '#345'
    ACTIVEFOREGROUND = 'white'
    ACTIVEBORDERCOLOR = 'red'
    JUSTIFY = tk.CENTER     # LEFT, CENTER, RIGHT
    STATE = tk.NORMAL      # tk.NORMAL or tk.DISABLED

    def __init__(self,
                 master,
                 text = '',
                 command = None,
                 font = FONT,
                 bd = 0,
                 borderwidth = BORDERWIDTH,
                 relief = RELIEF,
                 bg = BACKGROUND,
                 fg = FOREGROUND,
                 bordercolor = BORDERCOLOR,
                 height = HEIGHT,
                 width = WIDTH,
                 image = None,
                 padx = 0,
                 pady = 0,
                 ipadx = 10,
                 ipady = 6,
                 activebackground = ACTIVEBACKGROUND,
                 activeforeground = ACTIVEFOREGROUND,
                 activebordercolor = ACTIVEBORDERCOLOR,
                 justify = JUSTIFY,
                 state = STATE,
                 **kwargs):

        super().__init__(master, background = bordercolor, relief = 'raised', borderwidth = borderwidth)

        self.command = command

        label = tk.Label(self,
                         text = text,
                         font = font,
                         bd = 0,
#                         borderwidth = 20,
                         relief = 'flat',
                         bg = bg,
                         fg = fg,
                         activebackground = activebackground,
                         activeforeground = activeforeground,
                         justify = justify,
                         **kwargs)

        label.pack(padx = 0, pady = 0, ipadx = ipadx, ipady = ipady)
        self.pack(padx = 20, pady = 20, ipadx = 0, ipady = 0)

        # border_color = Frame(window, background="red")
        #
        # Label Widget inside the Frame
        # label = Label(border_color, text="This is a Label widget", bd=0)
        #
        # # Place the widgets with border Frame
        # label.pack(padx=1, pady=1)
        # border_color.pack(padx=40, pady=40)

        self.bind("<Button-1>", self.button)
        self.bind("<ButtonRelease-1>", self.button_release)

    def button(self, e, t):
        self.command(e)

    def button_release(self, e):
        pass

    def button_pressed(self, e):
        pass

if __name__ == '__main__':

    root = tk.Tk()

    root.title('My Button')
    root.geometry('300x200+300+300')

    button = MyButton(root, 'Click', command = lambda e: print('Clicked'))
    button.grid()

    root.mainloop()