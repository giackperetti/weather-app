import sqlite3
from user import User
from typing import Tuple


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

    def add_user(self, user: User) -> Tuple[str, bool]:
        """
        add_user: Method that creates a new user and saves it to the database

        :param User User: The user that has to be added
        :return bool adding_success: boolean flag that is True if the user is added successfully and is False if the user creation doesnt go well
        """
        adding_success: bool = None
        status: str = None
        username: str = user.get_username()
        user_password: str = user.get_password()
        user_city: str = user.get_favorite_city()

        try:
            self.db_cursor.execute(
                "INSERT INTO users (name, password, favorite_city) VALUES (?, ?, ?)",
                (
                    username,
                    user_password,
                    user_city,
                ),
            )

            self.db_cursor.execute(
                "SELECT id, creation_date FROM users WHERE name = ?", (username,)
            )
            row = self.db_cursor.fetchone()
            if row:
                user.set_id(row["id"])
                user.set_creation_date(row["creation_date"])
            self.connection.commit()
            adding_success = True
            status = "user added succesfully"
        except Exception as e:
            adding_success = False
            status = f"There was an error: {e}"

        return status, adding_success


def main() -> None:
    user = User("nome", "password", "test")
    db = DB_Interactions()
    print(db.add_user(user=user))

    print(user.get_id())

if __name__ == "__main__":
    main()
