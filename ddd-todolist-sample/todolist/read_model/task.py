import inject
import json
import redis

# from todolist.adapter.redis.task import TaskDao
from todolist.domain_model.task import TaskStatus


class TaskDto:
    """ 読み出し用タスク. """

    def __init__(self, task_id, user_id, name, status):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.status = status


class TaskQuery:
    """ タスク用の Query クラス. """

    _redis_client = inject.attr(redis.StrictRedis)

    def __init__(self):
        """[summary]
        """
        self._dao = []
        # self._dao = TaskDto

    def find_all(self) -> list:
        """ 全ユーザの全タスク一覧を取得. """
        # tasks = []
        json_strs = self._dao.tasks.hgetall()
        values = [
            json.loads(x.decode('utf-8')) for x in json_strs.values()
        ]
        return [self._from_dict(x) for x in values]

    def find_by_user_id(self, user_id: int) -> list:
        assert isinstance(user_id, int)
        keys = self._dao.user_tasks(user_id=user_id).smembers()
        # tasks = []
        if not keys:
            return []
        json_strs = self._dao.tasks.hmget(*keys)
        values = [json.loads(x.decode('utf-8')) for x in json_strs]
        return [self._from_dict(x) for x in values]

    def find_todo_by_user_id(self, user_id: int) -> list:
        assert isinstance(user_id, int)
        keys = self._dao.todo(user_id=user_id).smembers()
        # tasks = []
        if not keys:
            return []
        json_strs = self._dao.tasks.hmget(*keys)
        values = [json.loads(x.decode('utf-8')) for x in json_strs]
        return [self._from_dict(x) for x in values]

    def find_done_by_user_id(self, user_id: int) -> list:
        assert isinstance(user_id, int)
        keys = self._dao.done(user_id=user_id).smembers()
        # tasks = []
        if not keys:
            return []
        json_strs = self._dao.tasks.hmget(*keys)
        values = [json.loads(x.decode('utf-8')) for x in json_strs]
        return [self._from_dict(x) for x in values]

    def _from_dict(self, value):
        return TaskDto(
            task_id=value['task_id'],
            user_id=value['user_id'],
            name=value['name'],
            status=TaskStatus(value['status'])
        )
