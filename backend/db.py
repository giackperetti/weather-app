import sqlite3
from user import User
from typing import Tuple


class DB:
    def __init__(self) -> None:
        """
        __init__: Method that constructs an oject of class DB, creating a connection to the database and creating a cursorto browse the daatbase's conents
        """
        self.connection = self.handle_connection()
        self.db_cursor: sqlite3.Cursor = self.connection.cursor()

    def handle_connection(self) -> sqlite3.Connection:
        """
        create_connection: Method that handles the creation of the connection to the database

        :return sqlite3.Connection: the connection to the database itself
        """
        self.connection = sqlite3.connect("./backend/users.db")
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def close_connection(self) -> bool:
        connection_closing_success: bool = True

        try:
            self.connection.close()
            connection_closing_success = True
        except Exception as e:
            connection_closing_success = False

        return connection_closing_success

    def add_user(self, user: User) -> Tuple[str, bool]:
        """
        add_user: Method that creates a new user and saves it to the database

        :param User user: The user that has to be added
        :return Tuple[str, bool]: the first value in the tuple is a string that contatins a message about the creation of the user, the second value is a boolean value that is True if the user is added correctly and False if there is a problem
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
            status = "User added succesfully"
        except Exception as e:
            adding_success = False
            status = f"There was an error: {e}"

        return status, adding_success

    def delete_user(self, user: User) -> Tuple[str, bool]:
        """
        delete_user: Method that deletes an existing user and saves it to the database

        :param User user: The user that has to be deleted
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the deletion of the user, the second value is a boolean value that is True if the user is deleted correctly and False if there is a problem
        """

        deletion_success: bool = None
        status: str = None
        user_id: int = user.get_id()

        try:
            self.db_cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.connection.commit()
            deletion_success = True
            status = "User deleted successfully"
        except Exception as e:
            deletion_success = False
            status = f"There was an error: {e}"

        return status, deletion_success

    def edit_user(
        self, user: User, new_username: str, new_password: str, new_favorite_city: str
    ) -> Tuple[str, bool]:
        """
        edit_user: Method that edits an existing user and saves it to the database

        :param User user: The user that has to be edited
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the editing of the user, the second value is a boolean value that is True if the user is edited correctly and False if there is a problem
        """

        editing_success: bool = None
        status: str = "User's "
        user_id: int = user.get_id()

        try:
            if new_username != "":
                self.db_cursor.execute(
                    "UPDATE users SET name = ? WHERE id = ?",
                    (
                        new_username,
                        user_id,
                    ),
                )
                user.set_username(new_username)
                status += "username, "

            if new_password != "":
                self.db_cursor.execute(
                    "UPDATE users SET password = ? WHERE id = ?",
                    (
                        new_password,
                        user_id,
                    ),
                )
                user.set_password(new_password)
                status += "password, "

            if new_favorite_city != "":
                self.db_cursor.execute(
                    "UPDATE users SET favorite_city = ? WHERE id = ?",
                    (
                        new_favorite_city,
                        user_id,
                    ),
                )
                user.set_favorite_city(new_favorite_city)
                status += "favorite city, "

            self.connection.commit()
            editing_success = True
            status += "edited successfully"

        except Exception as e:
            editing_success = False
            status = f"There was an error: {e}"

        return status, editing_success
