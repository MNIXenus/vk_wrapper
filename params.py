import keyring


class Params(dict):

    def __init__(self, **kwargs):
        self['v'] = '5.7'
        self['access_token'] = keyring.get_password('vk_api_user_tok', 'MNIXenus')
        self['lang'] = 'ru'
        self.add(**kwargs)

    def __call__(self):
        return self

    def add(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = str(value)