from todolist.domain_model.user import User, UserService


class SimpleUserService(UserService):
    """ 現在ログイン中のユーザを返す. """

    def get_current_user(self) -> User:
        return User(1, "junya")
