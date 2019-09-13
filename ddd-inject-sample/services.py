import uuid
import inject

from entities import User
from repositories import UserRepository


class UserService:

    repo = inject.attr(UserRepository)

    def create_user(self, name):
        user = User(uuid.uuid4(), name)
        self.repo.store(user)

        return user

    def find_by_identity(self, identity):
        return self.repo.find_by_identity(identity)
