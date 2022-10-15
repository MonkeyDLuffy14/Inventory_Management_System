from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import re


class billingClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing")
        self.root.geometry("1100x500+310+170")
        self.root.config(bg="#898AA6")

        # --All varaibles--#
        self.var_bid = StringVar()
        self.bill_txt = StringVar()
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

        # ---billing Frame---#
        bill_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#D3EBCD")
        bill_Frame.place(x=10, y=10, width=550, height=600)

        lbl_title = Label(bill_Frame, text="Billing Details", font=("goudy old style", 15, "bold"), bg="blue",fg="white").pack(side=TOP, fill=X)

        lbl_name = Label(bill_Frame, text="Name", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30, y=60)
        lbl_contact = Label(bill_Frame, text="Contact", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30,y=120)
        lbl_cat = Label(bill_Frame, text="Category", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30,y=180)
        lbl_prod = Label(bill_Frame, text="Product", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30,y=240)
        lbl_qty = Label(bill_Frame, text="Qunatity", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30,y=300)
        lbl_total = Label(bill_Frame, text="Total", font=("goudy old style", 15, "bold"), bg="#D3EBCD").place(x=30,y=360)


        # --Input--#
        txt_name = Entry(bill_Frame, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=60, width=200)
        txt_contact = Entry(bill_Frame, textvariable=self.var_contact, font=("goudy old style", 15),bg="lightyellow").place(x=150, y=120, width=200)

        cmb_cat = ttk.Combobox(bill_Frame, textvariable=self.var_category, state='readonly', justify=CENTER,font=("goudy old style", 15))
        cmb_cat['values'] = self.cat_list
        cmb_cat.place(x=150, y=180, width=200)
        cmb_cat.current(0)
        self.var_category.trace('w', self.fetch_prod)

        self.cmb_prod = ttk.Combobox(bill_Frame, textvariable=self.var_product, state='readonly',justify=CENTER, font=("goudy old style", 15))
        self.cmb_prod['values'] = self.prod_list
        self.cmb_prod.place(x=150, y=240, width=200)

        txt_qty = Entry(bill_Frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=300, width=200)
        txt_total = Entry(bill_Frame, textvariable=self.var_total, state='readonly', font=("goudy old style", 15),bg="lightyellow").place(x=150, y=360, width=200)

        ##--Btn--#
        btn_add=Button(bill_Frame,text="SAVE",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=30,y=450,width=100, height=40)
        btn_total=Button(bill_Frame,text="GENERATE",command=self.total,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=380,y=360,width=150, height=30)
        btn_delete=Button(bill_Frame,text="DELETE",command=self.delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=170,y=450,width=100, height=40)
        btn_clear=Button(bill_Frame,text="CLEAR" ,command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=310,y=450,width=100, height=40)

        ##--Billing--##
        bill_txt = Label(self.root,textvariable=self.bill_txt,justify=LEFT,font=("goudy old style",15,"bold"),bg="grey",fg="white",bd=3,relief=RIDGE).place(x=620,y=350,width=700,height=250)


        ##--Billing Treeview--##
        bill_view = Frame(self.root, bd=3, relief=RIDGE)
        bill_view.place(x=620, y=10, width=700, height=310)
        scrolly = Scrollbar(bill_view, orient=VERTICAL)
        scrollx = Scrollbar(bill_view, orient=HORIZONTAL)

        self.BillingTable = ttk.Treeview(bill_view,columns=("bid","name","contact","category","product","quantity","total"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.BillingTable.xview)
        scrolly.config(command=self.BillingTable.yview)

        self.BillingTable.heading("bid", text="Bill ID")
        self.BillingTable.heading("name", text="Name")
        self.BillingTable.heading("contact", text="Contact")
        self.BillingTable.heading("category", text="Category")
        self.BillingTable.heading("product", text="Product")
        self.BillingTable.heading("quantity", text="Quantity")
        self.BillingTable.heading("total", text="Total")
        self.BillingTable["show"] = "headings"

        self.BillingTable.column("bid", width=90)
        self.BillingTable.column("name", width=100)
        self.BillingTable.column("contact", width=100)
        self.BillingTable.column("category", width=100)
        self.BillingTable.column("product", width=100)
        self.BillingTable.column("quantity", width=100)
        self.BillingTable.column("total",  width=100)
        self.BillingTable.pack(fill=BOTH,expand=1)
        self.BillingTable.bind("<ButtonRelease-1>",self.get_data)  #bind is type of event on selecting will invoke a function

        self.show()

    ##--Functions--##
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

    def fetch_prod(self, *args):
        self.cmb_prod['values'] = "Empty"
        self.prod_list.append("Empty")
        try:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            cur.execute("select name from product where Category=?", (self.var_category.get(),))
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.prod_list[:]
                self.prod_list.append("Select")
                for i in sup:
                    self.prod_list.append(i[0])
                self.prod_list = [i for i, in sup]
            self.cmb_prod['values'] = self.prod_list
            self.cmb_prod.current(0)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    def total(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        cur.execute("Select price from product where name=?",(self.var_product.get(),))
        row = cur.fetchone()
        price = int(row[0])
        qt = int(self.var_qty.get())
        if row == None:
            messagebox.showerror("Error","Product Price not Available")
        else:
            total = price * qt
        self.var_total.set(str(total))

        if self.var_name.get() == "" or self.var_contact.get() == "":
            messagebox.showerror("Error","Customer Details Required !!")
        else:
            self.bill_txt.set("*****************************************************************\n"
                              +" \t\t\tBilling\t\t\t\n"
                              +"  Customer Name: "+str(self.var_name.get())+"\n"
                              +"  Contact Number: "+str(self.var_contact.get())+"\n"
                              +"  Product: "+str(self.var_product.get())+"\n"
                              +"  Quantity: "+str(self.var_qty.get())+"\n"
                              +"  Total Amount: "+str(self.var_total.get())+"\n")

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            name = r'\D+[^!@#$%&*()_>?":]'
            num = r'\d+'
            if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_product.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required ",parent=self.root)
            if(re.fullmatch(name,str(self.var_name.get()))):
                if(re.fullmatch(num,str(self.var_contact.get()))):
                    if (re.fullmatch(num, str(self.var_qty.get()))):
                            cur.execute("Insert into billing (name,contact,category,product,quantity,total) values(?,?,?,?,?,?)",(
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.var_category.get(),
                                self.var_product.get(),
                                self.var_qty.get(),
                                self.var_total.get(),
                            ))
                            con.commit()
                            messagebox.showinfo("Success","Product Added Successfully !!",parent=self.root)
                            self.show()
                    else:
                        messagebox.showerror("Error","Invalid Quantity",parent=self.root)
                else:
                    messagebox.showerror("Error","Invalid Contact",parent=self.root)
            else:
                messagebox.showerror("Error","Invalid Name",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    ##---show data--##
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from billing")
            rows=cur.fetchall()
            self.BillingTable.delete(*self.BillingTable.get_children()) #delete all children(value)
            for row in rows:
                self.BillingTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    ##---getData---##
    def get_data(self,ev):
        f=self.BillingTable.focus()
        content=(self.BillingTable.item(f))
        row=content['values']
        self.var_bid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_category.set(row[3]),
        self.var_product.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_total.set(row[6]),

    ##---delete data---##
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_bid.get()=="":
                messagebox.showerror("Error","Please Select Bill From List ",parent=self.root)
            else:
                cur.execute("Select * from billing where bid=?",(self.var_bid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Billing ID",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirmation", "Do you really want to Delete",parent=self.root)
                    if op == True:
                        cur.execute("delete from billing where bid=?",(self.var_bid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Bill Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def clear(self):
        self.var_bid.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_category.set("Select")
        self.var_product.set("")
        self.var_qty.set("")
        self.var_total.set("")
        self.show()


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = billingClass(root)
    root.mainloop()
