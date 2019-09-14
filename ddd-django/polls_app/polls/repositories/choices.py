from django.db.models import Avg, Max, Min

from polls_app.polls.repositories import PollsRepository

from polls_app.polls.models import Choice


class ChoiceRepository(PollsRepository):
    def __init__(self, db_repo):
        self.__db_repo = db_repo

    def get_vote_aggregates(self):
        return self.__db_repo.get_vote_aggregates()

    def get_choice(self, choice_id: int):
        return self.__db_repo.filter_by_choice_id(choice_id)

    def get_all(self):
        return self.__db_repo.get_all()


class ChoiceDBRepository(ChoiceRepository):

    def __init__(self):
        self.choice_orm = Choice

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

    def filter_by_choice_id(self, choice_id: int):
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
