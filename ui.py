import customtkinter as ctk

from logic import *


__all__ = ["UI"]

class UI(ctk.CTk):
    def __init__(self):
        self.logic = Logic()

        super().__init__()
        self.title("2048")
        self.geometry("1000px 1000px")


        self.mainloop()
