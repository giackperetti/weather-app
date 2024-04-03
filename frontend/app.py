import tkinter as tk
from tkinter import ttk
        
class App(tk.Tk):
    """
    Classe per l'inizializzazione dell'applicazione

    :param tkinter-widget tk.Tk: finestra principale dell'applicazione
    :author dichiara lorenzo
    """
    def __init__(self) -> None:
        """
        metodo costruttore che inzializza l'applicazione
        """
        tk.Tk.__init__(self)
        self.frame = None
        self.switch_frame(SignUpPage)

        self.title("Pinin meteo")
        self.geometry("1280x720")
        self.resizable(False, False)

    def switch_frame(self, frame_class:tk.Frame):
        """
        metodo per cambiare frame

        :param tk.Frame frame_class: classe frame da visualizzare
        :author dichiara lorenzo
        """
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

        

class LoginPage(tk.Frame):
    """
    Classe per la creazione di una pagina login

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """
    def __init__(self,master) -> None:
        """
        metodo costruttore che inzializza un frame LoginPage

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)

        #widget
        self.frame_login:tk.Frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_login.pack(pady=30, ipadx=200, ipady=400)

        self.label:ttk.Label = ttk.Label(self.frame_login, text="Login", font=("Cascadia Code",40))
        self.label.pack(pady=10)

        self.username:ttk.Label = ttk.Label(self.frame_login, text="Username", font=("Cascadia Code",15))
        self.username.place(y=180, x=120)

        self.entry_username:ttk.Entry = ttk.Entry(self.frame_login, width=30, font=("Cascadia Code",15))
        self.entry_username.place(y=220, x=120)

        self.password:ttk.Label = ttk.Label(self.frame_login, text="Password", font=("Cascadia Code",15))
        self.password.place(y=260, x=120)

        self.entry_password:ttk.Entry = ttk.Entry(self.frame_login, width=30, font=("Cascadia Code",15))
        self.entry_password.place(y=300, x=120)

        self.link_sign_up:tk.Label = tk.Label(self, text="Are you not registered yet ?",fg="blue" ,font=("Cascadia Code",12, "underline"), cursor="hand2")
        self.link_sign_up.place(y=380, x=160)
        self.link_sign_up.bind("<Button-1>", lambda e: master.switch_frame(SignUpPage))

        self.button:tk.Button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2", command=self.login)
        self.button.place(y=430, x=250)

    def login(self):
        pass

class SignUpPage(tk.Frame):
    """
    classe per la creazione di una pagina signUp

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """
    def __init__(self, master:tk.Tk) -> None:
        """
        metodo costruttore che inizializza un frame SignUpPage 

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)

        #widget

        self.frame_sign_up:tk.Frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_sign_up.pack(pady=30, ipadx=200, ipady=400)

        self.label:ttk.Label = ttk.Label(self.frame_sign_up, text="Sign Up", font=("Cascadia Code",40))
        self.label.pack(pady=10)

        self.username:ttk.Label = ttk.Label(self.frame_sign_up, text="Username", font=("Cascadia Code",15))
        self.username.place(y=180, x=120)

        self.entry_username:ttk.Entry = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_username.place(y=220, x=120)

        self.password:ttk.Label = ttk.Label(self.frame_sign_up, text="Password", font=("Cascadia Code",15))
        self.password.place(y=260, x=120)

        self.entry_password:ttk.Entry = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_password.place(y=300, x=120)

        self.favourite_city:tk.Label = ttk.Label(self.frame_sign_up, text="City", font=("Cascadia Code",15))
        self.favourite_city.place(y=340, x=120)

        self.entry_favourite_city:tk.Entry = ttk.Entry(self.frame_sign_up, width=30, font=("Cascadia Code",15))
        self.entry_favourite_city.place(y=380, x=120)

        self.link_sign_up:tk.Label = tk.Label(self, text="Are you already registered ?", font=("Cascadia Code",12, "underline"), cursor="hand2" , fg="blue")
        self.link_sign_up.place(y=480, x=175)

        self.link_sign_up.bind("<Button-1>", lambda e: master.switch_frame(LoginPage))

        self.button:tk.Button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2", command=self.signup)
        self.button.place(y=530, x=270)

    def signup(self):
        pass


class WeatherApp(tk.Frame):
    """
    classe per la creazione di una pagina weather-app

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """

    def __init__(self, master:tk.Tk) -> None:
        """
        metodo costruttore che inizializza un frame per la pagina WeatherApp

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)

        # Widget
        self.frame_weather_app:tk.Frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_weather_app.pack(pady=30, ipadx=200, ipady=400)

        self.title:ttk.Label = ttk.Label(self.frame_weather_app, text="Weather App", font=("Cascadia Code", 40))
        self.title.pack(pady=10)

        self.temperature:ttk.Label = ttk.Label(self.frame_weather_app, text="25°", font=("Cascadia Code", 30))
        self.temperature.place(relx=0.5, rely=0.4, anchor="center")

        self.location:ttk.Label = ttk.Label(self.frame_weather_app, text="Venezia", font=("Cascadia Code", 30))
        self.location.place(relx=0.5, rely=0.5, anchor="center")

        self.location_entry:ttk.Entry = ttk.Entry(self.frame_weather_app, font=("Cascadia Code", 20), justify="center")
        self.location_entry.place(relx=0.5, rely=0.7, anchor="center")

        self.change_location_button:tk.Button = tk.Button(self.frame_weather_app, text="Cambia Località", font=("Cascadia Code", 15),command=self.change_location, cursor="hand2")
        self.change_location_button.place(relx=0.5, rely=0.8, anchor="center")

    def change_location(self):
        """
        Metodo per cambiare la località utilizzando l'input dell'utente.
        """
        new_location = self.location_entry.get()
        if new_location == "":
            self.location.config(text="Inserisci una località")
        else:
            self.location.config(text=new_location)
        

if __name__ == "__main__":
    root = App()
    root.mainloop()

#https://api.openweathermap.org/data/3.0/onecall?temp={temperature}&current[weather][icon]={icon}&timezone={city}&units={metric}&appid={API key}