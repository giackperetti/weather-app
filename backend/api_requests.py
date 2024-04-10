import requests
import validators


class Request:
    def __init__(self, api_url: str, params: dict) -> None:
        """
        __init__: Method that constructs a Request object of class Request

        :param str api_url: url that gets used in the api request
        """
        self.__api_url: str = api_url
        self.__params: dict = params

    def get_api_url(self) -> str:
        """
        get_api_url: Method that returns the api's endpoint url

        :return str api_url: url that gets used in the api request
        :author Giacomo Peretti
        """
        return self.__api_url

    def set_api_url(self, new_api_url: str) -> None:
        """
        set_api_url: Method that updates the api's endpoint url

        :param str new_api_url: new url to change the value of the request's api url
        :author Giacomo Peretti
        """
        self.__api_url: str = new_api_url

    def get_params(self) -> str:
        """
        get_params: Method that returns the api's endpoint url

        :return str params: parameters that have to be passed to the endpoint
        :author Giacomo Peretti
        """
        return self.__params

    def set_params(self, new_params: dict) -> None:
        """
        set_params: Method that updates the api's endpoint url

        :param str new_params: new parameters to change the value of existing params
        :author Giacomo Peretti
        """
        self.__params: str = new_params

    def __is_url_valid(self) -> bool:
        """
        is_url_valid: Method that checks if a url is valid

        :return bool is_valid: returns True if the url is valid, False if it isn't
        :author Giacomo Peretti
        """
        is_valid = True
        if not validators.url(self.__api_url):
            is_valid = False

        return is_valid

    def make_get_request(self) -> dict:
        """
        make_get_request: Method that makes a get request to the specified api_url

        :return dict response.json: response from the request in json format
        :author Giacomo Peretti
        """

        if not self.__is_url_valid(self.__api_url):
            return "The URL isn't valid"

        try:
            response = requests.get(self.__api_url, params=self.__params)
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
