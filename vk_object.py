from params import Params
from request_manager import Manager


class Vk_object:
    def __init__(self, method):
        self.method = method
        self.params = Params()
        self.manager = Manager(self.method)
        self.list = 'Try to get_batch or get_all'

    def _get_batch_(self, count=100, offset=0):

        self.params.add(count=count)
        self.params.add(offset=offset)
        batch = self.manager.get(self.params)
        self.params.pop('count')
        self.params.pop('offset')
        return batch

    def get_all(self):
        if self.method in ('groups.getMembers', 'friends.get', 'wall.get', 'wall.getComments'):
            self.list = []
            for i in range((self.count // 100) + 1):
                self.list.append(self._get_batch_(count=100, offset=i*100))
            return self.list
        else:
            print('Nothing to get. Method "'+self.method+'" does not have id to get as list.')
