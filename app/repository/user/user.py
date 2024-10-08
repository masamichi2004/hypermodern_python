from abc import ABC, abstractmethod


class UserRepo(ABC):
    @abstractmethod
    def bulk_get(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def bulk_create(self, users):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def delete(self, id):
        pass
