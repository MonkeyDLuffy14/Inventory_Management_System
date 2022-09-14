from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+310+170")
        self.root.title("Category")
        self.root.config(bg="#898AA6")

        ##----All Variable---##
        self.var_cat_id = StringVar()
        self.var_cat_name = StringVar()

        #---Title---#
        lbl_title=Label(self.root,text="Manage Category ",font=("goudy old style",30, "bold"), bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 30),bg="#898AA6").place(x=50,y=100)
        txt_name = Entry(self.root,textvariable=self.var_cat_name, font=("goudy old style", 18), bg="lightyellow").place(x=50, y=170,width=400)

        btn_add = customtkinter.CTkButton(self.root, text="ADD",command=self.add,text_font=("groud old style", 15, "bold"), bg_color="#898AA6",fg_color="green", cursor="hand2").place(x=380, y=135,width=150,height=40)
        btn_delete = customtkinter.CTkButton(self.root, text="DELETE",command=self.delete,text_font=("groud old style", 15, "bold"), bg_color="#898AA6",fg_color="red", cursor="hand2").place(x=510, y=135,width=150,height=40)

        ##---category details----##
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=850, y=100, width=480, height=120)
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid", text="CID")
        self.categoryTable.heading("name", text="Name")
        self.categoryTable["show"] = "headings"

        self.categoryTable.column("cid", width=90)
        self.categoryTable.column("name", width=120)
        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)  # bind is type of event on selecting will invoke a function

        ##---Images---##
        self.img1 = Image.open("Images/category2.jpg")
        self.img1 = self.img1.resize((650,350),Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.lbl_img = Label(self.root,image=self.img1,bd=2,relief=RAISED)
        self.lbl_img.place(x=50,y=240)

        self.img2 = Image.open("Images/category.jpg")
        self.img2 = self.img2.resize((650,350),Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.img2)

        self.lbl_im2 = Label(self.root,image=self.img2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=710,y=240)
        self.show()
        ##----Add Query----##
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Category name must be required ", parent=self.root)
            else:
                cur.execute("Select * from category where name=?", (self.var_cat_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Category Already Exist,try different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",
                                (
                                    self.var_cat_name.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully !!", parent=self.root)
                    self.show()
                    self.var_cat_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    ##----show data----##
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())  # delete all children(value)
            for row in rows:
                self.categoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    ##=---getData---##
    def get_data(self, ev):
        f = self.categoryTable.focus()
        content = (self.categoryTable.item(f))
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_cat_name.set(row[1])

    ##---delete data---##
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Select Category ", parent=self.root)
            else:
                cur.execute("Select * from Category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Try Again !!!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirmation", "Do you really want to Delete",parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_cat_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = categoryClass(root)
    root.mainloop()
