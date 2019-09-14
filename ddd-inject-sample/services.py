import uuid
import inject

from entities import User
from repositories import AbstractUserRepository


class UserService:

    repo = inject.attr(AbstractUserRepository)

    def create_user(self, name):
        user = User(uuid.uuid4(), name)
        self.repo.store(user)

        return user

    def find_by_identity(self, identity):
        return self.repo.find_by_identity(identity)


class UserServiceTwo:

    @inject.params(repo=AbstractUserRepository)
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def create_user(self, name: str):
        user = User(uuid.uuid4(), name)
        self.repo.store(user)

        return user

    def find_by_identity(self, identity: uuid.uuid4()):
        return self.repo.find_by_identity(identity)
