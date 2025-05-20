"""
Used to store the windows of the app.

"""

from tkinter import Tk,PhotoImage
import os

WIDTH=1000
HEIGHT=610
XSTART=400
YSTART=150

class Window():
    @staticmethod
    def create_window():
        """
        Used to create the window.

        """
        root=Tk()
        root.title("MySQL Quick Connect")
        root.geometry(f"{WIDTH}x{HEIGHT}+{XSTART}+{YSTART}")
        #window_icon=PhotoImage(file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        #root.iconphoto(False,window_icon)
        root.resizable(width=False,height=False)
        return root


if __name__=='__main__':
    root=Window.create_window()
    root.mainloop()
