from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class billingClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing")
        self.root.geometry("1100x500+310+170")
        self.root.config(bg="#898AA6")


        #--All varaibles--#
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_category = StringVar()
        self.cat_list = []
        self.prod_list = []
        self.fetch_cat()
        # self.fetch_prod()
        self.var_product = StringVar()
        self.var_qty = StringVar()
        self.var_total = StringVar()
        self.var_status = StringVar()

        #---billing Frame---#
        bill_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#D3EBCD")
        bill_Frame.place(x=10,y=10,width=550,height=600)

        lbl_title = Label(bill_Frame,text="Billing Details",font=("goudy old style",15,"bold"),bg="blue",fg="white").pack(side=TOP,fill=X)

        lbl_name = Label(bill_Frame,text="Name",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=60)
        lbl_contact = Label(bill_Frame,text="Contact",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=120)
        lbl_cat = Label(bill_Frame,text="Category",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=180)
        lbl_prod = Label(bill_Frame,text="Product",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=240)
        lbl_qty = Label(bill_Frame,text="Qunatity",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=300)
        lbl_total = Label(bill_Frame,text="Total",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=360)
        lbl_status = Label(bill_Frame,text="Status",font=("goudy old style",15,"bold"),bg="#D3EBCD").place(x=30,y=420)

        #--Input--#
        txt_name=Entry(bill_Frame,textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=150,y=60,width=200)
        txt_contact = Entry(bill_Frame,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=120, width=200)

        cmb_cat=ttk.Combobox(bill_Frame,textvariable=self.var_category,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_cat['values'] = self.cat_list
        cmb_cat.place(x=150,y=180,width=200)
        cmb_cat.current(0)
        self.var_category.trace('w',self.fetch_prod)

        cmb_prod=ttk.Combobox(bill_Frame,textvariable=self.var_product,values=self.prod_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_prod['values'] = self.prod_list
        cmb_prod.place(x=150,y=240,width=200)
        # cmb_prod.current(0)

        txt_qty=Entry(bill_Frame,textvariable=self.var_qty, font=("goudy old style",15),bg="lightyellow").place(x=150,y=300,width=200)
        txt_total=Entry(bill_Frame,textvariable=self.var_total,state='readonly', font=("goudy old style",15),bg="lightyellow").place(x=150,y=360,width=200)

        cmb_status=ttk.Combobox(bill_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_status.place(x=150,y=420,width=200)
        cmb_status.current(0)

        ##-----All Function-----##
    def fetch_cat(self):
        self.cat_list.append("Empty")
        try:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            cur.execute("Select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    def fetch_prod(self, cmb_prod=None, *args):
        self.prod_list.append("Empty")
        try:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            cur.execute("select name from product where Category=?",(self.var_category.get(),))
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.prod_list[:]
                self.prod_list.append("Select")
                for i in sup:
                    self.prod_list.append(i[0])
                self.prod_list = [i for i,in sup]
            print(self.prod_list)
            cmb_prod['values'] = self.prod_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = billingClass(root)
    root.mainloop()