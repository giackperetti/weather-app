from datetime import datetime

class User:
    def __init__(self, username: str, password: str, id: int, creation_date: datetime, favorite_city: str) -> None:
        '''
        __init__: Method that constructs a User object from the User class

        :param str username: username of the user account
        :param str password: user password to login to the app
        :param int id: unique identifier different for each user
        :param datetime creation_date: date at which the user account was created
        '''
        
        self.__username = username
        self.__password = password
        self.__id = id
        self.__creation_date = creation_date
        self.__favorite_city = favorite_city

    def get_username(self) -> str:
        return self.__username
    
    def set_username(self, new_username) -> None:
        self.__username = new_username
    
    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, new_password) -> None:
        self.__password = new_password
    
    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, new_id) -> None:
        self.__id = new_id

    def get_creation_date(self) -> datetime:
        return self.__creation_date

    def get_favorite_city(self) -> str:
        return self.__favorite_city
    
    def set_favorite_city(self, new_favorite_city) -> None:
        self.__favorite_city = new_favorite_city
        