from django.db.models import Avg, Max, Min

from polls_app.polls.repositories import ChoiceRepository
from polls_app.polls.models import Choice


class ChoiceDBRepository(ChoiceRepository):

    def __init__(self, choice_orm=Choice):
        self.choice_orm = choice_orm

    def get_vote_aggregates(self):

        max = self.get_max()
        min = self.get_min()
        avg = self.get_avg()

        return max, min, avg

    def get_max(self):
        return self.choice_orm.objects.aggregate(
            Max("votes")
        )["votes__max"]

    def get_min(self):
        return self.choice_orm.objects.aggregate(
            Min("votes")
        )["votes__min"]

    def get_avg(self):
        return self.choice_orm.objects.aggregate(
            Avg("votes")
        )["votes__avg"]

    def get_choice(self, choice_id: int):
        """
        Questionオブジェクトのquestion_idを元にフィルタリング処理を行う.

        Args:
            choice_id (int): choice_id.
        """
        assert isinstance(choice_id, int)
        return self.choice_orm.objects.filter(
            pk=choice_id
        ).first()

    def get_all(self):
        return self.choice_orm.objects.all()
