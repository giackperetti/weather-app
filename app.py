import tkinter as tk
from tkinter import ttk, font
        
class App(tk.Tk):
    """
    _summary_

    :param _type_ tk: _description_
    :author dichiara lorenzo
    """
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.frame = None
        self.switch_frame(LoginPage)

        self.title("Pinin meteo")
        self.geometry("1280x720")
        self.resizable(False, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

        #widget
        

class LoginPage(tk.Frame):
    """
    _summary_

    :param _type_ tk: _description_
    :author dichiara lorenzo
    """
    def __init__(self,master) -> None:
        tk.Frame.__init__(self, master)

        #widget
        self.frame_login = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_login.pack(pady=30, ipadx=200, ipady=400)

        self.label = ttk.Label(self.frame_login, text="Login", font=("Cascadia Code",40))
        self.label.pack(pady=10)

        self.username = ttk.Label(self.frame_login, text="Username", font=("Cascadia Code",15))
        self.username.place(y=180, x=120)

        self.entry_username = ttk.Entry(self.frame_login, width=30, font=("Cascadia Code",15))
        self.entry_username.place(y=220, x=120)

        self.password = ttk.Label(self.frame_login, text="Password", font=("Cascadia Code",15))
        self.password.place(y=260, x=120)

        self.entry_password = ttk.Entry(self.frame_login, width=30, font=("Cascadia Code",15))
        self.entry_password.place(y=300, x=120)

        self.link_sign_up = tk.Label(self, text="Are you not registered yet ?",fg="blue" ,font=("Cascadia Code",12, "underline"), cursor="hand2")
        self.link_sign_up.place(y=380, x=160)
        self.link_sign_up.bind("<Button-1>", lambda e: master.switch_frame(SignUpPage))

        self.button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2")
        self.button.place(y=430, x=250)

class SignUpPage(tk.Frame):
    """
    _summary_

    :param _type_ tk: _description_
    :author dichiara lorenzo
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame_sign_up = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_sign_up.pack(pady=30, ipadx=200, ipady=400)

        self.label = ttk.Label(self.frame_sign_up, text="Sign Up", font=("Cascadia Code",40))
        self.label.pack(pady=10)

        self.username = ttk.Label(self.frame_sign_up, text="Username", font=("Cascadia Code",15))
        self.username.place(y=180, x=120)

        self.entry_username = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_username.place(y=220, x=120)

        self.password = ttk.Label(self.frame_sign_up, text="Password", font=("Cascadia Code",15))
        self.password.place(y=260, x=120)

        self.entry_password = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_password.place(y=300, x=120)

        self.favourite_city = ttk.Label(self.frame_sign_up, text="City", font=("Cascadia Code",15))
        self.favourite_city.place(y=340, x=120)

        self.entry_favourite_city = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_favourite_city.place(y=380, x=120)

        self.link_sign_up = tk.Label(self, text="Are you already registered ?", font=("Cascadia Code",12, "underline"), cursor="hand2" , fg="blue")
        self.link_sign_up.place(y=480, x=175)

        self.link_sign_up.bind("<Button-1>", lambda e: master.switch_frame(LoginPage))

        self.button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2")
        self.button.place(y=530, x=250)
        

if __name__ == "__main__":
    root = App()
    root.mainloop()