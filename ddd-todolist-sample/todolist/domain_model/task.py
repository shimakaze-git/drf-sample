from abc import ABCMeta, abstractmethod

import inject
from enum import Enum

# from todolist.port.eventbus import EventBus


class TaskStatus(Enum):
    """ タスクステータス. """
    todo = "todo"
    done = "done"


class TaskCreated:
    """ タスク作成イベント. """

    def __init__(self, task_id, user_id, name):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id
        )


class TaskDone:
    """ タスク完了イベント. """

    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id
        )


class TaskRenamed:
    """ タスク名変更イベント. """

    def __init__(self, task_id, user_id, name):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id
        )


class TaskRepository:

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_id(self):
        u""" タスクIDを生成する
        :rtype: int
        """

    @abstractmethod
    def get(self, task_id):
        u""" タスクを取得する
        :type task_id: int
        :rtype: (Task|None)
        """

    @abstractmethod
    def save(self, task):
        u""" タスクを保存する
        :type task: Task
        """


class Task:

    # _eventbus = inject.attr(EventBus)
    _repo = inject.attr(TaskRepository)

    def __init__(
        self, task_id: int, user_id: int, name: str, status: TaskStatus
    ) -> None:
        """Taskコンストラクタ.

        新規のタスクを作成する際には create メソッドを利用すること.

        Args:
            task_id (int): タスクID.
            user_id (int): ユーザID.
            name (str): タスク名.
            status (TaskStatus): ステータス.

        Returns:
            None: None Return.
        """
        assert isinstance(task_id, int)
        assert isinstance(user_id, int)
        assert isinstance(name, str)
        assert isinstance(status, TaskStatus)

        self._task_id = task_id
        self._user_id = user_id
        self._name = name
        self._status = status

    def __repr__(self):
        return "<{}: task_id={}>".format(
            self.__class__.__name__, self.task_id
        )

    @classmethod
    def create(cls, user_id: int, name: str) -> object:
        """タスクを生成する.

        Args:
            user_id (int): ユーザーiD.
            name (str): ユーザー名.

        Returns:
            object: return Task Object.
        """
        repo = inject.instance(TaskRepository)
        # eventbus = inject.instance(eventBus)

        # タスクを生成して保存する
        task_id = repo.generate_id()
        task = cls(task_id, user_id, name, TaskStatus.todo)
        repo.save(task)

        # タスク生成イベントを通知する
        # event = TaskCreated(task_id, user_id, name)
        # eventbus.publish(event)
        return task

    @property
    def task_id(self):
        return self._task_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    def rename(self, name: str):
        """タスク名を変更する.

        Args:
            name (str): 変更したい名前.
        """
        self._name = name
        self._repo.save(self)

        # 名前の変更を通知する
        # event = TaskRenamed(self.task_id, self._user_id, self.name)
        # self._eventbus.publish(event)

    def done(self):
        """タスクを終了させる."""
        self._status = TaskStatus.done
        self._repo.save(self)

        # タスクの終了を通知する
        # event = TaskDone(self.task_id, self.user_id)
        # self._eventbus.publish(event)
