from django.db.models import Avg, Max, Min
from .models import Choice, Question


class ShowVoteResultsUsecase:

    # def __init__(self):
    #     pass

    def execute(self, question_id: int) -> dict:
        # 投票内容を取り出す
        question = Question.objects.filter(pk=question_id).first()

        # 集計する
        aggregates = self.aggregate()

        # 整形処理
        max = aggregates[0]
        min = aggregates[1]
        avg = aggregates[2]

        results = {
            'question': question,
            'max': max,
            'min': min,
            'avg': avg
        }

        return results

    def aggregate(self) -> tuple:
        """集計する."""

        max = Choice.objects.aggregate(Max('votes'))['votes__max']
        min = Choice.objects.aggregate(Min('votes'))['votes__min']
        avg = Choice.objects.aggregate(Avg('votes'))['votes__avg']

        return max, min, avg


class CreateUserUsecase:
    def __init__(self, user_repo, user_service):
        self._user_repo = user_repo
        self._user_service = user_service

    # def execute(user_data: UserData) -> User:
        # do stuff
        # user_repo.create(user_dto)
        # do more stuff
