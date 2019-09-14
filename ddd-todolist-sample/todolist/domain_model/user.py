from abc import ABCMeta, abstractmethod


class User:
    """ ユーザーを表現した Value Object. """

    def __init__(self, user_id: int, name: str) -> None:
        """ ユーザーを表現したValueObjectのコンストラクタ.

        Args:
            user_id (int): ユーザーID
            name (str): ユーザー名

        Returns:
            None: None Return.
        """
        assert isinstance(user_id, int)
        assert isinstance(name, str)
        self.__user_id = user_id
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name


class UserService:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_current_user(self):
        """現在ログイン中のユーザーを返す

        :rtype: User
        """
