import re
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


        ##----All variables---##
        self.var_pid = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

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


        #--category combobox--#
        cmb_cat=ttk.Combobox(Product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        # --supplier combobox--#
        cmb_sup=ttk.Combobox(Product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_sup.place(x=150,y=120,width=200)
        cmb_sup.current(0)

        #--Product name price qty--#
        txt_product=Entry(Product_Frame,textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=150,y=180,width=200)
        txt_price=Entry(Product_Frame,textvariable=self.var_price, font=("goudy old style",15),bg="lightyellow").place(x=150,y=240,width=200)
        txt_qty=Entry(Product_Frame,textvariable=self.var_qty, font=("goudy old style",15),bg="lightyellow").place(x=150,y=300,width=200)

        #--status--#
        cmb_status=ttk.Combobox(Product_Frame,textvariable=self.var_status,values=("Active","Inctive"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_status.place(x=150,y=360,width=200)
        cmb_status.current(0)

        #---Button---#
        btn_add=Button(Product_Frame,text="SAVE",command=self.add ,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=30,y=450,width=100, height=40)
        btn_update=Button(Product_Frame,text="UPDATE",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=150,y=450,width=100, height=40)
        btn_delete=Button(Product_Frame,text="DELETE",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=270,y=450,width=100, height=40)
        btn_clear=Button(Product_Frame,text="CLEAR",command=self.clear ,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=390,y=450,width=100, height=40)

        ##----Search Frame-----##
        lbl_SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="#D3EBCD")
        lbl_SearchFrame.place(x=620, y=10, width=700, height=80)
        ##---Combo box---##
        cmb_search = ttk.Combobox(lbl_SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=200)
        cmb_search.current(0)
        txt_search = Entry(lbl_SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=220,y=10)
        btn_search = Button(lbl_SearchFrame,text="Search",command=self.Search,font=("goudy old style",15),bg="lightblue",cursor="hand2").place(x=500,y=10,width=130,height=32)

        #--Product Treeview--#

        prod_frame = Frame(self.root,bd=3,relief=RIDGE)
        prod_frame.place(x=620,y=100,width=700,height=510)
        scrolly = Scrollbar(prod_frame,orient=VERTICAL)
        scrollx = Scrollbar(prod_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(prod_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid",text="Product ID")
        self.ProductTable.heading("Category", text="Category")
        self.ProductTable.heading("Supplier", text="Supplier")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="Quantity")
        self.ProductTable.heading("status", text="Status")
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid", width=90)
        self.ProductTable.column("Category", width=100)
        self.ProductTable.column("Supplier", width=100)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)  #bind is type of event on selecting will invoke a function

        self.show()

    ##-------Functions-------##
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:

                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

##---Insert--##
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            name = r'\D+[^!@#$%&*()_>?":]'
            num = r'\d+'
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required ",parent=self.root)
            if(re.fullmatch(name,str(self.var_name.get()))):
                if(re.fullmatch(num,str(self.var_price.get()))):
                    if (re.fullmatch(num, str(self.var_qty.get()))):
                        cur.execute("Select * from product where name=?",(self.var_name.get(),))
                        row=cur.fetchone()
                        if row!=None:
                             messagebox.showerror("Error","This Product Already Exist,try different",parent=self.root)
                        else:
                            cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                self.var_status.get(),
                            ))
                            con.commit()
                            messagebox.showinfo("Success","Product Added Successfully !!",parent=self.root)
                            self.show()
                    else:
                        messagebox.showerror("Error","Invalid Quantity",parent=self.root)
                else:
                    messagebox.showerror("Error","Invalid Price",parent=self.root)
            else:
                messagebox.showerror("Error","Invalid Name",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    ##---show data--##
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children()) #delete all children(value)
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    ##---getData---##
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),

    ##---Update Data---##
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product From List ",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    cur.execute("Update  product set Category=?,Supplier=?,name=?,price=?,qty=?,status=?  where pid=?",(
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully !!",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    ##---delete data---##
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product From List ",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirmation", "Do you really want to Delete")
                    if op == True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    ##---Clear Data---##
    def clear(self):
        self.var_pid.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    ##---Search---##
    def Search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())  # delete all children(value)
                    for row in rows:
                         self.ProductTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No Record Found ",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = productClass(root)
    root.mainloop()