import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
import sys
import os
from dotenv import dotenv_values

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

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
        self.switch_frame(LoginPage)

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
        self.app: tk.Tk = master

        # widget
        self.frame_login: tk.Frame = tk.Frame(
            self, highlightbackground="black", highlightthickness=2, background="gray18"
        )
        self.frame_login.pack(pady=30, ipadx=200, ipady=400)

        self.label: ttk.Label = ttk.Label(
            self.frame_login,
            text="Login",
            font=("Cascadia Code", 40),
            background="gray18",
            foreground="white smoke",
        )
        self.label.pack(pady=10)

        self.username: ttk.Label = ttk.Label(
            self.frame_login,
            text="Username",
            font=("Cascadia Code", 15),
            background="gray18",
            foreground="white smoke",
        )
        self.username.place(rely=0.3, relx=0.5, anchor="center")

        self.entry_username: ttk.Entry = ttk.Entry(
            self.frame_login, width=30, font=("Cascadia Code", 15), background="gray18"
        )
        self.entry_username.place(rely=0.36, relx=0.5, anchor="center")

        self.password: ttk.Label = ttk.Label(
            self.frame_login,
            text="Password",
            font=("Cascadia Code", 15),
            background="gray18",
            foreground="white smoke",
        )
        self.password.place(rely=0.43, relx=0.5, anchor="center")

        self.entry_password: ttk.Entry = ttk.Entry(
            self.frame_login, width=30, font=("Cascadia Code", 15), show="*"
        )
        self.entry_password.place(rely=0.49, relx=0.5, anchor="center")

        self.link_sign_up: tk.Label = tk.Label(
            self,
            text="Are you not registered yet ?",
            fg="steel blue",
            font=("Cascadia Code", 12, "underline"),
            cursor="hand2",
            background="gray18",
        )
        self.link_sign_up.place(rely=0.55, relx=0.5, anchor="center")
        self.link_sign_up.bind(
            "<Button-1>", lambda e: self.app.switch_frame(SignUpPage)
        )

        self.button: tk.Button = tk.Button(
            self,
            text="Invia",
            font=("cascadia Code", 15),
            cursor="hand2",
            command=self.login,
        )
        self.button.place(rely=0.65, relx=0.5, anchor="center")

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
                self.app.login_success(username)
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
        self.app: tk.Tk = master

        # widget

        self.frame_sign_up: tk.Frame = tk.Frame(
            self, highlightbackground="black", highlightthickness=2, background="gray18"
        )
        self.frame_sign_up.pack(pady=30, ipadx=200, ipady=400)

        self.title: ttk.Label = ttk.Label(
            self.frame_sign_up,
            text="Sign Up",
            font=("Cascadia Code", 40),
            background="gray18",
            foreground="white smoke",
        )
        self.title.pack(pady=10)

        self.username: ttk.Label = ttk.Label(
            self.frame_sign_up,
            text="Username",
            font=("Cascadia Code", 15),
            background="gray18",
            foreground="white smoke",
        )
        self.username.place(rely=0.3, relx=0.5, anchor="center")

        self.entry_username: ttk.Entry = ttk.Entry(
            self.frame_sign_up, width=30, font=("Cascadia Code", 15)
        )
        self.entry_username.place(rely=0.36, relx=0.5, anchor="center")

        self.password: ttk.Label = ttk.Label(
            self.frame_sign_up,
            text="Password",
            font=("Cascadia Code", 15),
            background="gray18",
            foreground="white smoke",
        )
        self.password.place(rely=0.42, relx=0.5, anchor="center")

        self.entry_password: ttk.Entry = ttk.Entry(
            self.frame_sign_up, width=30, font=("Cascadia Code", 15), show="*"
        )
        self.entry_password.place(rely=0.48, relx=0.5, anchor="center")

        self.favourite_city: tk.Label = ttk.Label(
            self.frame_sign_up,
            text="City",
            font=("Cascadia Code", 15),
            background="gray18",
            foreground="white smoke",
        )
        self.favourite_city.place(rely=0.54, relx=0.5, anchor="center")

        self.entry_favourite_city: tk.Entry = ttk.Entry(
            self.frame_sign_up, width=30, font=("Cascadia Code", 15)
        )
        self.entry_favourite_city.place(rely=0.6, relx=0.5, anchor="center")

        self.link_sign_up: tk.Label = tk.Label(
            self,
            text="Are you already registered ?",
            font=("Cascadia Code", 12, "underline"),
            cursor="hand2",
            fg="steel blue",
            background="gray18",
        )
        self.link_sign_up.place(rely=0.66, relx=0.5, anchor="center")

        self.link_sign_up.bind("<Button-1>", lambda e: self.app.switch_frame(LoginPage))

        self.button: tk.Button = tk.Button(
            self,
            text="Invia",
            font=("cascadia Code", 15),
            cursor="hand2",
            command=self.signup,
        )
        self.button.place(rely=0.74, relx=0.5, anchor="center")

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
            self.app.switch_frame(WeatherApp, city)
        else:
            print("Campi di testo vuoti :)")


class WeatherApp(tk.Frame):
    """
    classe per la creazione di una pagina weather-app

    :param tkinter-widget tk.Frame: frame contenente altri widget
    :author dichiara lorenzo
    """

    def __init__(self, master: tk.Tk, city: str) -> None:
        """
        metodo costruttore che inizializza un frame per la pagina WeatherApp

        :param tk.Tk master: riferimento al widget padre
        :param str city: città selezionata dall'utente
        """
        tk.Frame.__init__(self, master)
        self.city: str = city

        # Widget
        self.frame_weather_app: tk.Frame = tk.Frame(
            self,
            highlightbackground="white smoke",
            highlightthickness=2,
            background="gray18",
        )
        self.frame_weather_app.pack(pady=30, ipadx=100, ipady=250)

        self.title: ttk.Label = ttk.Label(
            self.frame_weather_app,
            text="Weather App",
            font=("Cascadia Code", 40),
            background="gray18",
            foreground="white smoke",
        )
        self.title.pack(pady=10)

        self.temperature: ttk.Label = ttk.Label(
            self.frame_weather_app,
            text="",
            font=("Cascadia Code", 32),
            background="gray18",
            foreground="white smoke",
        )
        self.temperature.place(relx=0.52, rely=0.3, anchor="center")

        self.location: ttk.Label = ttk.Label(
            self.frame_weather_app,
            text=city,
            font=("Cascadia Code", 30),
            background="gray18",
            foreground="white smoke",
        )
        self.location.place(relx=0.5, rely=0.4, anchor="center")

        self.description: ttk.Label = ttk.Label(
            self.frame_weather_app,
            text="",
            font=("Cascadia Code", 18),
            background="gray18",
            foreground="white smoke",
        )
        self.description.place(relx=0.5, rely=0.5, anchor="center")

        self.city_entry: ttk.Entry = ttk.Entry(
            self.frame_weather_app, width=30, font=("Cascadia Code", 15)
        )
        self.city_entry.place(relx=0.5, rely=0.7, anchor="center")
        self.submit_button: tk.Button = tk.Button(
            self.frame_weather_app,
            text="Invia",
            font=("Cascadia Code", 15),
            cursor="hand2",
            command=self.changeCity,
        )
        self.submit_button.place(relx=0.5, rely=0.8, anchor="center")
        self.request()

    def changeCity(self):
        """
        metodo per cambiare la città e le sue relative informazioni
        :author dichiara lorenzo
        """
        city = self.city_entry.get()
        self.location.config(text=f"{city}")
        self.request()

    def request(self):
        """
        Metodo per gestire la richiesta meteo.
        :author dichiara lorenzo
        """
        city: str = self.location.cget("text")
        api_key: str = dotenv_values(".env").get("API_KEY")
        result: dict = {}

        if city:
            geolocator = Nominatim(user_agent="Pinin meteo")
            location = geolocator.geocode(city)
            if location:
                url: str = f"https://api.openweathermap.org/data/2.5/weather"
                params: dict = {
                    "units": "metric",
                    "lat": location.latitude,
                    "lon": location.longitude,
                    "lang": "It",
                    "appid": api_key,
                }
                req: api_requests.Request = api_requests.Request(url, params)
                result = req.make_get_request()
                temp: float = result["main"]["temp"]
                description = result["weather"][0]["description"]
                self.temperature.config(text=f"{temp}°")
                self.description.config(text=f"{description}")
            else:
                print("Posizione non trovata per la città:", city)
        else:
            print("Il campo città è vuoto")
