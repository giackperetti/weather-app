import requests
import validators

class Request:
    def __init__(self, api_url: str) -> None:
        self.__api_url: str = api_url

    def get_api_url(self) -> str:
        '''
        get_api_url: Method that returns the api's endpoint url

        :return str api_url: url that gets used in the api request
        '''
        return self.__api_url
    
    def set_api_url(self, new_api_url: str) -> None:
        '''
        set_api_url: Method that updates the api's endpoint url

        :param str new_api_url: new url to change the value of the request's api url 
        '''
        self.__api_url: str = new_api_url

    def is_url_valid(self) -> bool:
        is_valid = True
        if(not validators.url(self.__api_url)):
            is_valid = False;

        return is_valid