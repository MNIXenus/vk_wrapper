from params import Params
from request_manager import Manager


class Vk_object:
    def __init__(self, method):
        self.method = method
        self.params = Params()
        self.manager = Manager(self.method)
        self.list = 'Try to get_batch or get_all'

    def get_batch(self, count=100, offset=0):

        self.params.add(count=count)
        self.params.add(offset=offset)
        batch = self.manager.get(self.params)
        self.params.pop('count')
        self.params.pop('offset')
        self.list = batch
        return batch


    def get_all(self):
        if self.method in ('groups.getMembers', 'friends.get'):
            self.list = []
            for i in range((self.count // 100) + 1):
                self.list = self.list + self.get_batch(count=100, offset=i*100)
        else:
            print('Nothing to get. Method "'+self.method+'" does not have any data to get as list')
