from vk_object import Vk_object


class Wall(Vk_object):
    def __init__(self, owner_id):
        super().__init__('wall.get')
        self.owner_id = owner_id
        self.params.add(owner_id=self.owner_id)
        self.init_request = self.manager.get(self.params)
        self.count = self.init_request['count']