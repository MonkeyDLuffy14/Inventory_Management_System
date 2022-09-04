from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from employee import EmpClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")


        ##------Title------##
        self.icon = PhotoImage(file="Images/inventory_icon.png")
        title = customtkinter.CTkLabel(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon, compound=LEFT, text_font=("times new roman", 40, "bold"), bg_color="#41514E", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        ##------Button_Logout------##
        logout_btn = customtkinter.CTkButton(self.root, text="LOGOUT", text_font=("times new roman", 15, "bold"), bg_color="#41514E", cursor="hand2", fg_color="#F4F4BF",text_color="#445552")
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
        btn_supplier = customtkinter.CTkButton(sidebar, text="Supplier",  text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = customtkinter.CTkButton(sidebar, text="Category", text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = customtkinter.CTkButton(sidebar, text="Products", text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = customtkinter.CTkButton(sidebar, text="Sales", text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_billing = customtkinter.CTkButton(sidebar, text="Billing", text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = customtkinter.CTkButton(sidebar, text="Exit", text_font=("Times New Roman", 20, "bold"), fg_color="#222831", corner_radius=0, bd=2, cursor="hand2").pack(side=TOP, fill=X)


        ##-------Main Content------##
        self.lbl_emp = Label(self.root,text="Total Employee \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#D12C5C",bd=5,fg="white")
        self.lbl_emp.place(x=400,y=150,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#577A38",bd=5,fg="white")
        self.lbl_supplier.place(x=800,y=150,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#BD50B5",bd=5,fg="white")
        self.lbl_category.place(x=1200,y=150,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#53B0D3",bd=5,fg="white")
        self.lbl_product.place(x=400,y=350,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales \n[ 0 ] ",font=("Times New Roman",20), relief=RIDGE,bg="#D5AC55",bd=5,fg="white")
        self.lbl_sales.place(x=800,y=350,height=150,width=300)

        ##--------Footer-----##
        lbl_footer = Label(self.root, text="IMS-Inventory Management System || Zoro Private Limited\n For any Query contact 87979xx087", font=("times new roman", 12), bg="grey").pack(side=BOTTOM,fill=X)

    ##-------------------------------Functions------------------------------------------------##

    def employee(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.emp_obj = EmpClass(self.new_window)




if __name__ == "__main__":
    root = customtkinter.CTk()
    root.set_appearance_mode("blue")
    obj = IMS(root)
    root.mainloop()
