import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Now try your imports
from backend import db 
from backend import api_requests

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
        self.frame: tk.Frame = None
        self.current_user_city: str = None
        self.switch_frame(SignUpPage)

        self.title("Pinin meteo")
        self.geometry("1280x720")
        self.resizable(False, False)

    def switch_frame(self, frame_class: tk.Frame, *args):
        """
        metodo per cambiare frame

        :param tk.Frame frame_class: classe frame da visualizzare
        :author dichiara lorenzo
        """
        new_frame = frame_class(self, *args)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

    def login_success(self, username):
        """
        Metodo per gestire il successo del login.

        :param str username: nome utente
        :author dichiara lorenzo
        """
        database: db.DB = db.DB()
        self.current_user_city: str = database.user_city(username)
        self.switch_frame(WeatherApp, self.current_user_city)

        

class LoginPage(tk.Frame):
    """
    Classe per la creazione di una pagina login

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """
    def __init__(self, master) -> None:
        """
        metodo costruttore che inzializza un frame LoginPage

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)
        self.app: tk.Tk = master  # Salva l'istanza di App

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
        self.link_sign_up.bind("<Button-1>", lambda e: self.app.switch_frame(SignUpPage))

        self.button:tk.Button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2", command=self.login)
        self.button.place(y=430, x=250)

    def login(self):
        """
        Metodo per gestire il login dell'utente.
        :author dichiara lorenzo
        """
        user: str = self.entry_username.get()
        password: str = self.entry_password.get()

        if user is not None and password is not None:
            database: db.DB = db.DB()
            state, username, b = database.login(user, password)
            del database
            if state == "User logged in successfully":
                self.app.login_success(username)  # Chiamata al metodo login_success
            else:
                print("Invalid username or password")
        else:
            print("Campi di testo vuoti")

class SignUpPage(tk.Frame):
    """
    classe per la creazione di una pagina signUp

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """
    def __init__(self, master: tk.Tk) -> None:
        """
        metodo costruttore che inizializza un frame SignUpPage 

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)
        self.app: tk.Tk = master  # Salva l'istanza di App

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

        self.link_sign_up.bind("<Button-1>", lambda e: self.app.switch_frame(LoginPage))

        self.button:tk.Button = tk.Button(self, text="Invia", font=("cascadia Code",15), cursor="hand2", command=self.signup)
        self.button.place(y=530, x=270)

    def signup(self):
        """
        Metodo per gestire la registrazione di un nuovo utente.
        :author dichiara lorenzo
        """
        username: str = self.entry_username.get()
        password: str = self.entry_password.get()
        city: str = self.entry_favourite_city.get()

        if username is not None and password is not None and city is not None:
            database: db.DB = db.DB()
            database.signup(username, password, city)
            del database
            self.app.switch_frame(WeatherApp, city)  # Passa la città alla WeatherApp
        else:
            print("Campi di testo vuoti :)")



class WeatherApp(tk.Frame):
    """
    classe per la creazione di una pagina weather-app

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """

    def __init__(self, master: tk.Tk, city:str) -> None:
        """
        metodo costruttore che inizializza un frame per la pagina WeatherApp

        :param tk.Tk master: riferimento al widget padre
        """
        tk.Frame.__init__(self, master)
        self.city: str = city

        # Widget
        self.frame_weather_app:tk.Frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_weather_app.pack(pady=30, ipadx=100, ipady=250)

        self.title:ttk.Label = ttk.Label(self.frame_weather_app, text="Weather App", font=("Cascadia Code", 40))
        self.title.pack(pady=10)

        self.temperature:ttk.Label = ttk.Label(self.frame_weather_app, text="25°", font=("Cascadia Code", 30))
        self.temperature.place(relx=0.5, rely=0.4, anchor="center")

        self.location:ttk.Label = ttk.Label(self.frame_weather_app, text=city, font=("Cascadia Code", 30))  # Empty label
        self.location.place(relx=0.5, rely=0.5, anchor="center")

        self.submit_button:tk.Button = tk.Button(self.frame_weather_app, text="Invia", font=("Cascadia Code",15), cursor="hand2", command=self.request)
        self.submit_button.place(relx=0.5, rely=0.7, anchor="center")

    def login_success(self, username):
        """
        Metodo per gestire il successo del login.

        :param str username: nome utente
        :author dichiara lorenzo
        """
        database = db.DB()
        self.location.config(text=database.user_city(username))

    def request(self):
        """
        Metodo per gestire la richiesta meteo.
        :author dichiara lorenzo
        """
        city = self.location.cget("text")

        if city:
            geolocator = Nominatim(user_agent="Pinin meteo")
            location = geolocator.geocode(city)
            if location:
                print((location.latitude, location.longitude))
            else:
                print("Posizione non trovata per la città:", city)
        else:
            print("Il campo città è vuoto")

