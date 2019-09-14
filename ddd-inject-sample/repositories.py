from abc import ABCMeta, abstractmethod
from entities import User


class AbstractUserRepository:
    """Base class of User Repository.

    Raises:
        NotImplementedError: store method.
        NotImplementedError: find_by_identity method.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def store(self, user):
        raise NotImplementedError

    @abstractmethod
    def find_by_identity(self, identity):
        raise NotImplementedError


class UserRedisRepository(AbstractUserRepository):
    """User Repository on Redis."""

    def store(self, user):
        # TODO: write code here
        pass

    def find_by_identity(self, identity):
        # TODO: write code here
        pass


class UserMemoryRepository(AbstractUserRepository):
    """User Repository on memory.

    Args:
        UserRepository ([type]): [description]

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self):
        self._users = {}

    def store(self, user):
        """store.

        Args:
            user ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if not isinstance(user, User):
            raise TypeError
        self._users[user.identity] = user

    def find_by_identity(self, identity):
        """find_by_identity.

        Args:
            identity ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._users[identity]
