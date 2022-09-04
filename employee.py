from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk


class EmpClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+310+170")
        self.root.focus_force()
        self.root.config(bg="#898AA6")

        ##-----All variables-----##

        self.var_emp_srchby = StringVar()
        self.var_emp_srchtxt = StringVar()
        self.var_emp_id=StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_paswd = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_salary = StringVar()


        ##----Search Frame-----##
        lbl_SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Goudy old style", 12, "bold"),bd=2,relief=RIDGE, bg="#D3EBCD")
        lbl_SearchFrame.place(x=350, y=20, width=650, height=80)

        ##---Combo box---##
        cmb_search = ttk.Combobox(lbl_SearchFrame,textvariable=self.var_emp_srchby,values=("Select","Email","Name","EmpId","Contact"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=200)
        cmb_search.current(0)
        txt_search = Entry(lbl_SearchFrame,textvariable=self.var_emp_srchtxt,font=("goudy old style",15),bg="lightyellow").place(x=220,y=10)
        btn_search = Button(lbl_SearchFrame,text="Search",font=("goudy old style",15),bg="lightblue",cursor="hand2").place(x=500,y=10,width=130,height=32)

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
        txt_pass = Entry(self.root, textvariable=self.var_emp_paswd, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=570, y=270, width=220)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_emp_utype,values=("Admin", "Employee"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=1020, y=270, width=220)
        cmb_utype.current(0)

        ##-----row4----##
        lbl_add = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=50, y=320)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=570, y=320)

        self.txt_add = Text(self.root, font=("goudy old style", 15, "bold"),bg="lightyellow")
        self.txt_add.place(x=170, y=320, width=380,height=80)
        txt_salary = Entry(self.root, textvariable=self.var_emp_salary, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=650, y=320, width=220)

        ##----button---##
        btn_save = customtkinter.CTkButton(self.root,text="Save",text_font=("groud old style",15,"bold"),bg_color="#898AA6",fg_color="blue",cursor="hand2").place(x=460,y=300,width=110,height=28)
        btn_update = customtkinter.CTkButton(self.root, text="Update", text_font=("groud old style", 15, "bold"),bg_color="#898AA6",fg_color="green",cursor="hand2").place(x=560, y=300,width=110,height=28)
        btn_delete = customtkinter.CTkButton(self.root,text="Delete",text_font=("groud old style",15,"bold"),bg_color="#898AA6",fg_color="red",cursor="hand2").place(x=660,y=300,width=110,height=28)
        btn_clear = customtkinter.CTkButton(self.root, text="Clear", text_font=("groud old style", 15, "bold"),bg_color="#898AA6",fg_color="black",cursor="hand2").place(x=760, y=300,width=110,height=28)


        ##---Emplyee Table---##

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=420,relwidth=1,height=200)
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmpTable = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
        self.EmpTable.pack(fill=BOTH,expand=1)


if __name__ == "__main__":
    root = customtkinter.CTk()
    root.set_appearance_mode("blue")
    obj = EmpClass(root)
    root.mainloop()
