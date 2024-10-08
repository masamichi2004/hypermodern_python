from app.repository.todo.todo import TodoRepo


class TodoService:
    def __init__(self, todo_repo: TodoRepo):
        self.repo = todo_repo

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
