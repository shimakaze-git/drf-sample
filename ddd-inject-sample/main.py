import inject

# from services import UserService
from services import UserServiceTwo

# from repositories import UserRepository, UserRedisRepository
from repositories import UserRepository, UserMemoryRepository


def inject_config(binder):
    # binder.bind(UserRepository, UserRedisRepository())
    binder.bind(UserRepository, UserMemoryRepository())


if __name__ == "__main__":
    inject.configure(inject_config)

    # user_service = UserService()
    user_service = UserServiceTwo()

    name = 'foo'
    created_user = user_service.create_user(name)
    print(created_user)

    identity = created_user.identity
    stored_user = user_service.find_by_identity(identity)
    print(stored_user)

    assert created_user == stored_user
