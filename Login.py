from tkinter import *
import customtkinter
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")

        # ===images=======
        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=120, width=450)

        # ===Login_Frame====
        self.employee_id = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Product Sans", 30, "bold"), bg="white").place(x=0, y=30,relwidth=1)

        lbl_user = Label(login_frame, text="user", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)

        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15),bg="#ECECEC").place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=190)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15),bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login = Button(login_frame, text="Log In", command=self.login, font=("Arial Rounded MT Bold", 15),bg="#f6836b", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300,width=250,height=35)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)

        hr = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15, "bold")).place(x=150, y=355)

        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 13,), bg="white",fg="#f6836b", bd=0, activebackground="white", activeforeground="#00759E").place(x=100,y=390)

        # ===Frame2=======
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        lbl_reg = Label(register_frame, text="Welcome:)", font=("times new roman", 13), bg="white", fg="#f6836b").place(x=0, y=20, relwidth=1)


    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', "All fields are required", parent=self.root)

            else:
                cur.execute("select * from employee where eid =? AND pass=? AND utype=?",
                            (self.employee_id.get(), self.password.get(),"Admin"))
                user = cur.fetchone()

                if user == None:
                    messagebox.showerror("Error", "Invalid USERNAME/PASSWORD", parent=self.root)


                else:
                    self.root.destroy()
                    os.system("python dashboard.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


root = Tk()
obj = Login_System(root)
root.mainloop()

