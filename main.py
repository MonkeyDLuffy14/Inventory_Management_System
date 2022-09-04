import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root_tk = customtkinter.CTk()
root_tk.geometry("600x400")

def btn_function():
    print("Pressed Button")
btn = customtkinter.CTkButton(root_tk,text="CTKButton",command = btn_function)
btn.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
root_tk.mainloop()