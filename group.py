from vk_object import Vk_object
from wall import Wall


class Group(Vk_object):

    def __init__(self, group_id, **kwargs):
        super().__init__('groups.get')
        self.params.add(group_id=group_id)
        self.group_id = group_id
        self.init_request = self.manager.get(self.params)
        self.count = self.init_request['count']
        self.members = self.Members(group_id)
        self.wall = Wall(-group_id)

    class Members(Vk_object):

        def __init__(self, group_id):
            super().__init__('groups.getMembers')
            self.params.add(group_id=group_id)
            self.group_id = group_id
            self.init_request = self.manager.get(self.params)
            self.count = self.init_request['count']
            self.list = self.init_request['users']
