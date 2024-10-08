from app.repository.user.user import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.repo = user_repo

    def get_all(self):
        return self.repo.bulk_get()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        return self.repo.create(data)

    def update(self, id, data):
        return self.repo.update(id, data)

    def delete(self, id):
        return self.repo.delete(id)
