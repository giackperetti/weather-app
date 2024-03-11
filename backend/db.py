import sqlite3
from user import User


class DB_Interactions:
    def __init__(self) -> None:
        """
        __init__: Method that constructs an oject of class DB_Interactions, creating a connection to the database and creating a cursorto browse the daatbase's conents
        """
        self.connection = self.create_connection()
        self.db_cursor: sqlite3.Cursor = self.connection.cursor()

    def create_connection(self) -> sqlite3.Connection:
        """
        create_connection: Method that handles the creation of the connection to the database

        :return sqlite3.Connection: the connection to the database itself
        """
        self.connection = sqlite3.connect("./backend/users.db")
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def add_user(self, User: User) -> bool:
        """
        add_user: Method that creates a new user and saves it to the database

        :param User User: The user that has to be added
        :return bool adding_success: boolean flag that is True if the user is added successfully and is False if the user creation doesnt go well
        """
        adding_success: bool
        user_id: int = User.get_id()
        user_creation_date = User.get_creation_date()
        username: str = User.get_username()
        user_password: str = User.get_password()
        user_city: str = User.get_favorite_city()

        try:
            self.db_cursor.execute(
                "INSERT INTO users (id, creation_date, name, password, favorite_city) VALUES (?, ?, ?, ?, ?)",
                (
                    user_id,
                    user_creation_date,
                    username,
                    user_password,
                    user_city,
                ),
            )
            self.connection.commit()
            adding_success = True
        except Exception as e:
            print(e)
            adding_success = False

        return adding_success
