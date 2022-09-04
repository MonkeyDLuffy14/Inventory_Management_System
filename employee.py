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

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150, y=170,width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_emp_gender,values=("Select", "Male", "Female","Other"), state="readonly",justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=550, y=170, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_emp_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=1000, y=170,width=180)

        ##----row2----##
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"),bg="#898AA6").place(x=50, y=220)
        lbl_dob = Label(self.root, text="DOB", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=450, y=220)
        lbl_doj = Label(self.root, text="DOJ", font=("goudy old style", 15, "bold"), bg="#898AA6").place(x=900, y=220)

        txt_name = Entry(self.root, textvariable=self.var_emp_name, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150, y=220,width=180)
        txt_dob = Entry(self.root, textvariable=self.var_emp_dob, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=550, y=220,width=180)
        txt_doj = Entry(self.root, textvariable=self.var_emp_doj, font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=1000, y=220,width=180)


if __name__ == "__main__":
    root = customtkinter.CTk()
    root.set_appearance_mode("blue")
    obj = EmpClass(root)
    root.mainloop()
