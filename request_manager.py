from json import JSONDecoder, JSONDecodeError
import requests


class Manager:
    def __init__(self, method):
        self.vk_api = 'https://api.vk.com/method/'
        self.method = method

    def get(self, params):
        try:
            raw_result = requests.get(self.vk_api + self.method, params=params)
            result = JSONDecoder().decode(raw_result.text)
            if 'response' in result.keys():
                return result['response']
            else:
                print(result['error']['error_msg'])
        except requests.exceptions.ConnectionError as err:
            raise 'Connection error' + err
        except JSONDecodeError:
            print('Can\'t decode, return empty string')
            return ''


