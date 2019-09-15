from .exceptions import VoteCountException


class VoteCount:
    """投票回数のValueObject."""
    ERR_MESSAGE = '規程の投票回数を超えています'

    def __init__(self, count: int):
        self.__count = count

    def add_count(self, count=1):
        if self.validate_count():
            self.__count += count
        else:
            raise VoteCountException(self.ERR_MESSAGE)

    def validate_count(self):
        if 3 >= self.__count:
            return True
        return False

    @property
    def count(self):
        return self.__count
