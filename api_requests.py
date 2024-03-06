import requests
import validators

class Request:
    def __init__(self, api_url: str) -> None:
        '''
        __init__: Method that constructs a Request object of class Request

        :param str api_url: url that gets used in the api request
        '''
        self.__api_url: str = api_url

    def get_api_url(self) -> str:
        '''
        get_api_url: Method that returns the api's endpoint url

        :return str api_url: url that gets used in the api request
        :author Giacomo Peretti
        '''
        return self.__api_url
    
    def set_api_url(self, new_api_url: str) -> None:
        '''
        set_api_url: Method that updates the api's endpoint url

        :param str new_api_url: new url to change the value of the request's api url
        :author Giacomo Peretti
        '''
        self.__api_url: str = new_api_url

    def is_url_valid(self) -> bool:
        '''
        is_url_valid: Method that checks if a url is valid

        :return bool is_valid: returns True if the url is valid, False if it isn't
        :author Giacomo Peretti
        '''
        is_valid = True
        if(not validators.url(self.__api_url)):
            is_valid = False;

        return is_valid
    
    def make_get_request(self, params: list[str]) -> dict:
        '''
        make_get_request: Method that makes a get request to the specified api_url

        :param list[str] params: specified parameters for the request 
        :return dict response.json: response from the request in json format
        :author Giacomo Peretti
        '''
        try:
            response = requests.get(self.__api_url, params=params)
            response.raise_for_status()
        except requests.HTTPError as e:
            if response.status_code == 404:
                return "Not Found"
            elif response.status_code == 401:
                return "Unauthorized"
            else:
                return f"HTTP Error: {response.status_code}"
        except requests.RequestException as e:
            return f"Request Exception: {e}"
        except Exception as e:
            return f"Generic Exception: {e}"
        return response.json()