from abc import ABCMeta, abstractmethod


class EventBus:
    """ ドメインイベントの通知インタフェース. """

    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, event):
        """ ドメインイベントを通知する. """
