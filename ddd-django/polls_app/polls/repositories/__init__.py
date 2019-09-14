from abc import ABCMeta, abstractmethod


class PollsRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self):
        """ 全てのオブジェクトを取得する. """
