from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Products")
        self.root.geometry("1100x500+310+170")
        self.root.config(bg="#898AA6")
        #self.root.resizable(False, False)


        ##---Product Frame---##
        Product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#D3EBCD")
        Product_Frame.place(x=10,y=10,width=550,height=600)

        #--Title--#
        lbl_title = Label(Product_Frame,text="Manage Product Details",font=("goudy old style",15,"bold"),bg="blue",fg="white").pack(side=TOP,fill=X)

        lbl_category = Label(Product_Frame,text="Category",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=60)
        lbl_supplier = Label(Product_Frame,text="Supplier",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=120)
        lbl_product = Label(Product_Frame,text="Name",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=180)
        lbl_price = Label(Product_Frame,text="Price",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=240)
        lbl_quantity = Label(Product_Frame,text="Quantity",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=300)
        lbl_status = Label(Product_Frame,text="Status",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=360)

        txt_category = Entry(Product_Frame,textvariable="Category",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=60)



if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = productClass(root)
    root.mainloop()