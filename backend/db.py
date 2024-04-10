import sqlite3
from typing import Tuple


class DB:
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

    def signup(
        self, username: str, user_password: str, user_city: str
    ) -> Tuple[str, bool]:
        """
        signup: Method that creates a new user and saves it to the database

        :param str username: The username of the user that has to be added
        :param str user_password: The password of the user that has to be added
        :param str user_city: The favorite city of the user that has to be added
        :return Tuple[str, bool]: The first value in the tuple is a string that contains a message about the creation of the user, the second value is a boolean value that is True if the user is added correctly and False if there is a problem
        :author Giacomo Peretti
        """

        adding_success: bool = None
        status: str = None
        # username: str = user.get_username()
        # user_password: str = user.get_password()
        # user_city: str = user.get_favorite_city()

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()

            db_cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
            existing_user = db_cursor.fetchall()

            if existing_user:
                adding_success = False
                status = "User already exists"
                return status, adding_success

            db_cursor.execute(
                "INSERT INTO users (name, password, favorite_city) VALUES (?, ?, ?)",
                (
                    username,
                    user_password,
                    user_city,
                ),
            )

            # db_cursor.execute(
            #     "SELECT max(id) as max_id, creation_date FROM users WHERE name = ?",
            #     (username,),
            # )
            # row = db_cursor.fetchone()
            # if row:
            #     id = row["max_id"]
            #     date = row["creation_date"]
            # user.set_id(id)
            # user.set_creation_date(date)
            conn.commit()
            adding_success = True
            status = "User added successfully"
        except Exception as e:
            adding_success = False
            status = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()

        return status, adding_success

    def login(self, input_username: str, input_password: str) -> Tuple[str, str, bool]:
        """
        login: Method that checks if a user exists

        :param str input_username: The username of the user that has to log in
        :param str input_password: The password of the user that has to log in
        :return Tuple[str, bool]: The first value in the tuple is a string that contains a message about the existence of the user, the second value is a boolean value that is True if the user is exists and False if it doesn't
        :author Giacomo Peretti
        """

        login_success: bool = None
        status: str = None
        return_username: str = None

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()

            db_cursor.execute(
                "SELECT * FROM users WHERE name = ? AND password = ?",
                (
                    input_username,
                    input_password,
                ),
            )

            if db_cursor.fetchone():
                login_success = True
                status = "User logged in successfully"
                return_username = input_username
            else:
                login_success = False
                status = "Invalid username or password"
                return_username = ""
        except Exception as e:
            login_success = False
            status = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()

        return status, return_username, login_success

    def user_city(self, username: str) -> str:
        return_success: bool = None
        city: str = None

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()

            db_cursor.execute(
                "SELECT favorite_city FROM users WHERE name = ?",
                (username,),
            )

            row = db_cursor.fetchone()
            if row:
                city = row["favorite_city"]
                return_success = True
            else:
                city = ""
                return_success = False
        except Exception as e:
            login_success = False
            city = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()

        return city

    def edit_user_city(self, username: str, new_favorite_city: str) -> Tuple[str, bool]:
        """
        edit_user: Method that edits an existing user and saves it to the database

        :param User user: The user that has to be edited
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the editing of the user, the second value is a boolean value that is True if the user is edited correctly and False if there is a problem
        """

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()
            status: str = None
            if new_favorite_city is not None:
                db_cursor.execute(
                    "UPDATE users SET favorite_city = ? WHERE name = ?",
                    (new_favorite_city, username),
                )
                status += "User's favorite city has been updated"

            conn.commit()
            editing_success = True
        except Exception as e:
            if conn:
                conn.rollback()
            editing_success = False
            status = f"There was an error: {e}"
        finally:
            if conn:
                conn.close()

        return status, editing_success

    def delete_user(self, username: str, user_password: str, user_city: str) -> Tuple[str, bool]:
        """
        delete_user: Method that deletes an existing user and saves it to the database

        :param User user: The user that has to be deleted
        :return Tuple[str, bool]: the first value in the tuple is a string that contains a message about the deletion of the user, the second value is a boolean value that is True if the user is deleted correctly and False if there is a problem
        """

        try:
            conn = self.create_connection()
            db_cursor = conn.cursor()

            db_cursor.execute("SELECT id FROM users WHERE (name, password, favorite_city) VALUES (?, ?, ?)", (username, user_password, user_city))
            row = db_cursor.fetchone()
            if row:
                user_id = row["id"]
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
