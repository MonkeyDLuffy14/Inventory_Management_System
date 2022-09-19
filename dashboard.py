from tkinter import *
import sqlite3
import customtkinter
from PIL import Image, ImageTk
from employee import empClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import billingClass
import os

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        #self.root.geometry("1600x780+0+0")


        #All variables

        self.emp = StringVar()
        self.supp = StringVar()
        self.cat = StringVar()
        self.prod = StringVar()
        ##------Title------##
        self.icon = PhotoImage(file="Images/inventory_icon.png")
        title = customtkinter.CTkLabel(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon, compound=LEFT, text_font=("times new roman", 40, "bold"), bg_color="#41514E", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        ##------Button_Logout------##
        logout_btn = customtkinter.CTkButton(self.root, text="LOGOUT", command=self.logout, text_font=("times new roman", 15, "bold"), bg_color="#41514E", cursor="hand2", fg_color="#F4F4BF",text_color="#445552")
        logout_btn.place(x=1210, y=12, height=40, width=130)
        ##------Label_Clock--------##
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YY\t\t Time:hh-mm-ss", font=("times new roman", 15), bg="grey")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        ##--------------------SideBar_Menu------------------##
        self.Menu_logo = Image.open("Images/side_menu.png")
        self.Menu_logo = self.Menu_logo.resize((300, 300), Image.Resampling.LANCZOS)
        self.Menu_logo = ImageTk.PhotoImage(self.Menu_logo)

        sidebar = Frame(self.root, bd=2, relief=RIDGE, bg="#353941")
        sidebar.place(x=0, y=101, height=730, width=300)

        lbl_menulogo=Label(sidebar, image=self.Menu_logo)
        lbl_menulogo.pack(side=TOP, fill=X)

        lbl_menu=Label(sidebar, text="Menu", font=("Times New Roman", 20), bg="#009688").pack(side=TOP, fill=X)

        #self.icon_side = PhotoImage(file="Images/side.png")
        #btn_emp = Button(sidebar, text="Employee", font=("Times New Roman", 20, "bold"),image=self.icon_side,compound=LEFT,padx=10,anchor="w",bd=3,cursor="hand2",bg="#222831",activebackground="light blue").pack(side=TOP,fill=X)
        btn_emp = customtkinter.CTkButton(sidebar, text="Employee", text_font=("Times New Roman", 20, "bold"), command=self.employee, fg_color="#222831", corner_radius=0,bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = customtkinter.CTkButton(sidebar, text="Supplier",  text_font=("Times New Roman", 20, "bold"),command=self.supplier, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = customtkinter.CTkButton(sidebar, text="Category", text_font=("Times New Roman", 20, "bold"),command=self.category, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = customtkinter.CTkButton(sidebar, text="Products", text_font=("Times New Roman", 20, "bold"),command=self.product, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = customtkinter.CTkButton(sidebar, text="Sales", text_font=("Times New Roman", 20, "bold"),command=self.sales, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_billing = customtkinter.CTkButton(sidebar, text="Billing", text_font=("Times New Roman", 20, "bold"),command=self.billing, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = customtkinter.CTkButton(sidebar, text="Exit", text_font=("Times New Roman", 20, "bold"), command=self.exit, fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)


        ##-------Main Content------##
        self.lbl_emp = Label(self.root,text="Total Employee \n[ 0 ] ",textvariable=self.emp,font=("Times New Roman",20), relief=RIDGE,bg="#D12C5C",bd=5,fg="white")
        self.lbl_emp.place(x=400,y=150,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier \n[ 0 ] ",textvariable=self.supp,font=("Times New Roman",20), relief=RIDGE,bg="#577A38",bd=5,fg="white")
        self.lbl_supplier.place(x=800,y=150,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category \n[ 0 ] ",textvariable=self.cat,font=("Times New Roman",20), relief=RIDGE,bg="#BD50B5",bd=5,fg="white")
        self.lbl_category.place(x=1200,y=150,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product \n[ 0 ] ",textvariable=self.prod,font=("Times New Roman",20), relief=RIDGE,bg="#53B0D3",bd=5,fg="white")
        self.lbl_product.place(x=400,y=350,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#D5AC55",bd=5,fg="white")
        self.lbl_sales.place(x=800,y=350,height=150,width=300)

        self.emptotal()
        self.suppliertotal()
        self.categorytotal()
        self.producttotal()


        ##--------Footer-----##
        lbl_footer = Label(self.root, text="IMS-Inventory Management System || Zoro Private Limited\n For any Query contact 87979xx087", font=("times new roman", 12), bg="grey").pack(side=BOTTOM,fill=X)

    ##-------------------------------Functions------------------------------------------------##

    def employee(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.emp_obj = empClass(self.new_window)
    def supplier(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.supp_obj = supplierClass(self.new_window)
    def category(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.cat_obj = categoryClass(self.new_window)
    def product(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.prod_obj = productClass(self.new_window)
    def sales(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.sale_obj = salesClass(self.new_window)
    def billing(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.bill_obj = billingClass(self.new_window)
    def logout(self):
        self.root.destroy()
        os.system("python Login.py" )
    def exit(self):
        self.root.destroy()


    def emptotal(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select COUNT(eid) from employee")
            row = cur.fetchone()
            count = list(str(row)).pop(1)
            self.emp.set(str("Total Employee \n"+"["+count+"]"))
        except Exception as ex:
            print(ex)
    def suppliertotal(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select COUNT(invoice) from supplier")
            row = cur.fetchone()
            count = list(str(row)).pop(1)
            self.supp.set(str("Total Supplier \n"+"["+count+"]"))
        except Exception as ex:
            print(ex)
    def categorytotal(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select COUNT(cid) from category")
            row = cur.fetchone()
            count = list(str(row)).pop(1)
            self.cat.set(str("Total Category \n"+"["+count+"]"))
        except Exception as ex:
            print(ex)
    def producttotal(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select COUNT(pid) from product")
            row = cur.fetchone()
            count = list(str(row)).pop(1)
            self.prod.set(str("Total Product \n"+"["+count+"]"))
        except Exception as ex:
            print(ex)



if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = IMS(root)
    root.mainloop()
