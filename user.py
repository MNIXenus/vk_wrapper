from vk_object import Vk_object
from wall import Wall


class User(Vk_object):

    def __init__(self, uid):
        super().__init__('users.get')
        self.id = uid
        self.wall = Wall(uid)
        self.friends = self.Friends(uid)
        self.groups = self.Groups(uid)
        self.params.add(id=uid)

    class Friends(Vk_object):

        def __init__(self, user_id):
            super().__init__('friends.get')
            self.params.add(user_id=user_id)
            self.init_request = self.manager.get(self.params)
            self.count = self.init_request['count']
            self.list = self.init_request['items']

    class Groups(Vk_object):

        def __init__(self, user_id):
            super().__init__('groups.get')
            self.params.add(user_id=user_id)
            self.init_request = self.manager.get(self.params)
            self.count = self.init_request['count']
            self.list = self.init_request['items']

    def get_user_info(self, fields):
        self.params.add(fields=fields)
        self.info = self.manager.get(self.params)
        return self.info


class Users(Vk_object):

    def __init__(self, uid):
        super().__init__('users.get')
        self.id = uid
        self.params.add(user_ids=uid)

    def get_user_info(self, fields):
        self.params.add(fields=fields)
        self.info = self.manager.get(self.params)
        return self.info