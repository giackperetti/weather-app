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
        
        self.__username: str = username
        self.__password: str = password
        self.__id: int = id
        self.__creation_date: datetime = creation_date
        self.__favorite_city: str = favorite_city

    def get_username(self) -> str:
        '''
        get_username: Method that returns the user's username

        :return str username: user's username
        '''
        return self.__username
    
    def set_username(self, new_username: str) -> None:
        '''
        set_username: Method that updates the user's username

        :param str new_username: new username to update the current value
        '''
        self.__username: str = new_username
    
    def get_password(self) -> str:
        '''
        get_password: Method that returns the user's password

        :return str password: user's password
        '''
        return self.__password
    
    def set_password(self, new_password: str) -> None:
        '''
        set_password: Method that updates the user's password

        :param str new_password: new password to update the current value 
        '''
        self.__password: str = new_password
    
    def get_id(self) -> int:
        '''
        get_id: Method that returns the user's unique id

        :return int id: user's unique id
        '''
        return self.__id
    
    def set_id(self, new_id: int) -> None:
        '''
        set_id: Method that updates the user's id

        :param int new_id: new id to update the current value
        '''
        self.__id: int = new_id

    def get_creation_date(self) -> datetime:
        '''
        get_creation_date: Method that returns the user's creation date

        :return datetime creation_date: user's creation date
        '''
        return self.__creation_date

    def get_favorite_city(self) -> str:
        '''
        get_favorite_city: Method that returns the user's favorite city

        :return str favorite_city: user's favorite city
        '''
        return self.__favorite_city
    
    def set_favorite_city(self, new_favorite_city: str) -> None:
        '''
        set_favorite_city: Method that updates the user's favorite city

        :param str new_favorite_city: new favorite city to update the current value
        '''
        self.__favorite_city: str = new_favorite_city
        