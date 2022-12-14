from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import re
import sqlite3


class empClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+310+170")
        self.root.title("Employee Record")
        self.root.config(bg="#898AA6")

        ##-----All variables-----##

        self.var_emp_srchby = StringVar()
        self.var_emp_srchtxt = StringVar()
        self.var_emp_id = StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_pass = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_depart = StringVar()


        ##----Search Frame-----##
        lbl_SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="#D3EBCD")
        lbl_SearchFrame.place(x=350, y=20, width=650, height=80)

        ##---Combo box---##
        cmb_search = ttk.Combobox(lbl_SearchFrame, textvariable=self.var_emp_srchby, values=("Select", "Email", "Name", "Contact"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=200)
        cmb_search.current(0)
        txt_search = Entry(lbl_SearchFrame,textvariable=self.var_emp_srchtxt,font=("goudy old style",15),bg="lightyellow").place(x=220,y=10)
        btn_search = Button(lbl_SearchFrame,text="Search",command=self.Search,font=("goudy old style",15),bg="lightblue",cursor="hand2").place(x=500,y=10,width=130,height=32)

        ##----title----##
        lbl_title = Label(self.root,text="Employee Details",font=("goudy old style",15,"bold"),bg="blue",fg="white").place(x=50,y=110,width=1270)

        ##------Content-----##
        ##-----row1--------##
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 15, "bold"),bg="#898AA6").place(x=50, y=170)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=450, y=170)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=900, y=170)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=170, y=170,width=220)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_emp_gender,values=("Select", "Male", "Female","Other"), state="readonly",justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=570, y=170, width=220)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_emp_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=1020, y=170,width=220)

        ##----row2----##
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"),bg="#898AA6").place(x=50, y=220)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=450, y=220)
        lbl_doj = Label(self.root, text="D.O.J", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=900, y=220)

        txt_name = Entry(self.root, textvariable=self.var_emp_name, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=170, y=220,width=220)
        txt_dob = Entry(self.root, textvariable=self.var_emp_dob, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=570, y=220,width=220)
        txt_doj = Entry(self.root, textvariable=self.var_emp_doj, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=1020, y=220,width=220)

        ##----row3----##
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=50, y=270)
        lbl_pass = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=450, y=270)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=900, y=270)

        txt_email = Entry(self.root, textvariable=self.var_emp_email, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=170, y=270, width=220)
        txt_pass = Entry(self.root, textvariable=self.var_emp_pass, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=570, y=270, width=220)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_emp_utype,values=("Admin", "Employee"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=1020, y=270, width=220)
        cmb_utype.current(0)

        ##-----row4----##
        lbl_add = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=50, y=320)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=570, y=320)
        lbl_depart = Label(self.root, text="Department", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=890, y=320)

        self.txt_add = Text(self.root, font=("goudy old style", 15, "bold"),bg="lightyellow")
        self.txt_add.place(x=170, y=320, width=380,height=80)
        txt_salary = Entry(self.root, textvariable=self.var_emp_salary, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=650, y=320, width=220)
        cmb_depart = ttk.Combobox(self.root, textvariable=self.var_emp_depart, values=("Staff","IT","Finance","Worker","Supplier","Security","Manager"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_depart.place(x=1020, y=320, width=220)
        cmb_depart.current(0)
        ##----button---##
        btn_save = customtkinter.CTkButton(self.root,text="Save",command=self.add,text_font=("groud old style",15,"bold"),bg_color="#898AA6",fg_color="blue",cursor="hand2").place(x=460,y=300,width=110,height=28)
        btn_update = customtkinter.CTkButton(self.root, text="Update",command=self.update, text_font=("groud old style", 15, "bold"),bg_color="#898AA6",fg_color="green",cursor="hand2").place(x=560, y=300,width=110,height=28)
        btn_delete = customtkinter.CTkButton(self.root,text="Delete",command=self.delete,text_font=("groud old style",15,"bold"),bg_color="#898AA6",fg_color="red",cursor="hand2").place(x=660,y=300,width=110,height=28)
        btn_clear = customtkinter.CTkButton(self.root, text="Clear",command=self.clear, text_font=("groud old style", 15, "bold"),bg_color="#898AA6",fg_color="black",cursor="hand2").place(x=760, y=300,width=110,height=28)


        ##---Emplyee Table---##

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=420,relwidth=1,height=200)
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmpTable = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary","depart"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmpTable.xview)
        scrolly.config(command=self.EmpTable.yview)

        self.EmpTable.heading("eid",text="EMP ID")
        self.EmpTable.heading("name", text="Name")
        self.EmpTable.heading("email", text="Email")
        self.EmpTable.heading("gender", text="Gender")
        self.EmpTable.heading("contact", text="Contact")
        self.EmpTable.heading("dob", text="D.O.B")
        self.EmpTable.heading("doj", text="D.O.J")
        self.EmpTable.heading("pass", text="Password")
        self.EmpTable.heading("utype", text="User Type")
        self.EmpTable.heading("address", text="Address")
        self.EmpTable.heading("salary", text="Salary")
        self.EmpTable.heading("depart", text="Department")
        self.EmpTable["show"]="headings"

        self.EmpTable.column("eid", width=90)
        self.EmpTable.column("name", width=100)
        self.EmpTable.column("email", width=100)
        self.EmpTable.column("gender", width=100)
        self.EmpTable.column("contact", width=100)
        self.EmpTable.column("dob", width=100)
        self.EmpTable.column("doj", width=100)
        self.EmpTable.column("pass", width=100)
        self.EmpTable.column("utype", width=100)
        self.EmpTable.column("address", width=100)
        self.EmpTable.column("salary", width=100)
        self.EmpTable.column("depart", width=100)
        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable.bind("<ButtonRelease-1>",self.get_data)  #bind is type of event on selecting will invoke a function

        self.show()
##-------------------------------------------------Func Query----------------------------##
    ##---Insert--##
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            dob = r'\d{4}-\d{2}-\d{2}'
            number = r'\d{10}'
            salary = r'\d+'
            name = '[A-Za-z]+'
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Required ",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID Already Assigned,try different",parent=self.root)
                if (re.fullmatch(name,str(self.var_emp_name.get()))):
                    if (re.fullmatch(regex, str(self.var_emp_email.get()))):
                         if (re.fullmatch(dob, str(self.var_emp_dob.get()))) and (re.fullmatch(dob, str(self.var_emp_dob.get()))):
                             if (re.fullmatch(number, str(self.var_emp_contact.get()))):
                                if (re.fullmatch(salary, str(self.var_emp_salary.get()))):
                                   cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary,depart) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                       self.var_emp_id.get(),
                                       self.var_emp_name.get(),
                                       self.var_emp_email.get(),
                                       self.var_emp_gender.get(),
                                       self.var_emp_contact.get(),
                                       self.var_emp_dob.get(),
                                       self.var_emp_doj.get(),
                                       self.var_emp_pass.get(),
                                       self.var_emp_utype.get(),
                                       self.txt_add.get('1.0',END),
                                       self.var_emp_salary.get(),
                                       self.var_emp_depart.get(),
                                   ))
                                   con.commit()
                                   messagebox.showinfo("Success","Employee Added Successfully !!",parent=self.root)
                                   self.show()
                                else:
                                   messagebox.showerror("Error", "Invalid Salary ", parent=self.root)
                             else:
                                messagebox.showerror("Error", "Invalid Contact Number", parent=self.root)
                         else:
                             messagebox.showerror("Error", "Invalid Date Format", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
                else:
                    messagebox.showerror("Error","Invalid Name Format",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    ##---show data--##
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmpTable.delete(*self.EmpTable.get_children()) #delete all children(value)
            for row in rows:
                self.EmpTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    ##=---getData---##
    def get_data(self,ev):
        f=self.EmpTable.focus()
        content=(self.EmpTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_email.set(row[2])
        self.var_emp_gender.set(row[3])
        self.var_emp_contact.set(row[4])
        self.var_emp_dob.set(row[5])
        self.var_emp_doj.set(row[6])
        self.var_emp_pass.set(row[7])
        self.var_emp_utype.set(row[8])
        self.txt_add.delete('1.0', END)
        self.txt_add.insert(END,row[9])
        self.var_emp_salary.set(row[10])
        self.var_emp_depart.set(row[11])

    ##---Update Data---##
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Required ",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update  employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=?,depart=?  where eid=?",(
                                    self.var_emp_name.get(),
                                    self.var_emp_email.get(),
                                    self.var_emp_gender.get(),
                                    self.var_emp_contact.get(),
                                    self.var_emp_dob.get(),
                                    self.var_emp_doj.get(),
                                    self.var_emp_pass.get(),
                                    self.var_emp_utype.get(),
                                    self.txt_add.get('1.0',END),
                                    self.var_emp_salary.get(),
                                    self.var_emp_depart.get(),
                                    self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Empployee Updated Successfully !!",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    ##---delete data---##
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Required ",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirmation", "Do you really want to Delete")
                    if op == True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    ##---Clear Data---##
    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        self.var_emp_pass.set("")
        self.var_emp_utype.set("Admin")
        self.txt_add.delete('1.0', END)
        self.var_emp_salary.set("")
        self.var_emp_depart.set("")
        self.var_emp_srchtxt.set("")
        self.var_emp_srchby.set("Select")
        self.show()

    ##---Search---##
    def Search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_srchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_emp_srchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_emp_srchby.get()+" LIKE '%"+self.var_emp_srchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmpTable.delete(*self.EmpTable.get_children())  # delete all children(value)
                    for row in rows:
                         self.EmpTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No Record Found ",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = empClass(root)
    root.mainloop()
