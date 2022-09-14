from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales")
        self.root.geometry("1100x500+310+170")
        self.root.config(bg="#898AA6")


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = salesClass(root)
    root.mainloop()