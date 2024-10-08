from abc import ABC, abstractmethod


class TodoRepo(ABC):
    @abstractmethod
    def bulk_get(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, todo):
        pass
    
    @abstractmethod
    def bulk_create(self, todos):
        pass

    @abstractmethod
    def update(self, todo):
        pass

    @abstractmethod
    def delete(self, id):
        pass
