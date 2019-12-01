from vk_object import Vk_object
from request_manager import Manager


class Group(Vk_object):

    def __init__(self, group_id):
        super().__init__()
        self.group_id = group_id
        self.params.add(group_id=group_id)
        self.members = self.Members(group_id)

    class Members(Vk_object):

        def __init__(self, group_id):
            super().__init__()
            self.params.add(group_id=group_id)
            self.method = 'groups.getMembers'
            self.manager = Manager('groups.getMembers')
            self.init_request = self.manager.get_request_result(self.params)
            self.count = self.init_request['count']
            self.list = self.init_request['users']

        def get_batch(self, count=100, offset=0):
            self.params.add('count', count)
            self.params.add('offset', offset)
            members_batch = self.manager.get_request_result(self.params)
            self.params.remove('count')
            self.params.remove('offset')
            return members_batch['users']

        def get_all(self):
            self.list = []
            for i in range(1, (self.count // 100) + 1):
                self.list = self.list + self.get_members_batch(count=100, offset=i * 100)
