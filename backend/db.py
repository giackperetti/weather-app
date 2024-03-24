import sqlite3
from user import User
from typing import Tuple


class DB:
    # def __init__(self) -> None:
    #     """
    #     __init__: Method that constructs an oject of class DB, creating a connection to the database and creating a cursorto browse the daatbase's conents
    #     """
    #     self.connection = self.create_connection()
    #     self.db_cursor: sqlite3.Cursor = self.connection.cursor()

    def create_connection(self) -> sqlite3.Connection:
        """
        create_connection: Method that handles the creation of the connection to the database

        :return sqlite3.Connection: the connection to the database itself
        """
        try:
            connection = sqlite3.connect("./backend/users.db")
            connection.row_factory = sqlite3.Row
            return connection
        except Exception as e:
            print("Error: {e}")

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
            conn = self.create_connection()
            db_cursor = conn.cursor()
            db_cursor.execute(
                "INSERT INTO users (name, password, favorite_city) VALUES (?, ?, ?)",
                (
                    username,
                    user_password,
                    user_city,
                ),
            )

            db_cursor.execute(
                "SELECT max(id) as max_id, creation_date FROM users",
            )
            row = db_cursor.fetchone()
            if row:
                id = row["max_id"]
                date = row["creation_date"]
                user.set_id(id)
                user.set_creation_date(date)
            conn.commit()
            adding_success = True
            status = "User added succesfully"
        except Exception as e:
            adding_success = False
            status = f"There was an error: {e}"

        conn.close()
        return status, adding_success

    def delete_user(self, user: User) -> Tuple[str, bool]:
        """
        delete_user: Method that deletes an existing user and saves it to the database

        :param User user: The user that has to be deleted
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the deletion of the user, the second value is a boolean value that is True if the user is deleted correctly and False if there is a problem
        """

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()
            user_id = user.get_id()

            db_cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            deletion_success = True
            status = "User deleted successfully."
        except Exception as e:
            if conn:
                conn.rollback()
            deletion_success = False
            status = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()
        return status, deletion_success

    def edit_user(
        self,
        user: User,
        new_username: str = None,
        new_password: str = None,
        new_favorite_city: str = None,
    ) -> Tuple[str, bool]:
        """
        edit_user: Method that edits an existing user and saves it to the database

        :param User user: The user that has to be edited
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the editing of the user, the second value is a boolean value that is True if the user is edited correctly and False if there is a problem
        """

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()
            status = "User's "
            user_id = user.get_id()

            if new_username is not None and new_username != user.get_username():
                db_cursor.execute(
                    "UPDATE users SET name = ? WHERE id = ?", (new_username, user_id)
                )
                user.set_username(new_username)
                status += "username, "

            if new_password is not None and new_password != user.get_password():
                db_cursor.execute(
                    "UPDATE users SET password = ? WHERE id = ?",
                    (new_password, user_id),
                )
                user.set_password(new_password)
                status += "password, "

            if (
                new_favorite_city is not None
                and new_favorite_city != user.get_favorite_city()
            ):
                db_cursor.execute(
                    "UPDATE users SET favorite_city = ? WHERE id = ?",
                    (new_favorite_city, user_id),
                )
                user.set_favorite_city(new_favorite_city)
                status += "favorite city, "

            conn.commit()
            editing_success = True
            status += "edited successfully."
        except Exception as e:
            if conn:
                conn.rollback()
            editing_success = False
            status = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()

        return status, editing_success
