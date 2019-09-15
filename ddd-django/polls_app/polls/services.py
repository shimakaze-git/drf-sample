from django.utils import timezone

from .repositories.choices import ChoiceRepository, ChoiceDBRepository
# from .repositories.questions import QuestionRepository, QuestionDBRepository
from .repositories.questions import QuestionDBRepository


class ChoiceAggregateService:
    def __init__(self):
        self._choice_repo = ChoiceRepository(ChoiceDBRepository())

    def show_max_min_avg_aggregate(self):
        """ max, min, avgを集計する. """
        max, min, avg = self._choice_repo.get_vote_aggregates()
        return max, min, avg

    def show_max_min_diff(self):
        """ maxとminの差分を返す. """

        max = self.get_max()
        min = self.get_min()
        return max - min


GET_COUNT = 5


class LatestQuestionService:
    def __init__(self):
        self._question_repo = QuestionDBRepository()

    def get_latest_questions(self, pub_date_flag=True) -> tuple:
        """
        最新の投票内容を取得する.

        Args:
            pub_date_flag (bool, optional):
                Flaseの場合は全ての投票内容を取り出す. Defaults to True.

        Returns:
            tuple: latest_questions, output
        """
        get_count = GET_COUNT
        timezone_now = timezone.now()

        if pub_date_flag:
            # 投票内容を取り出す
            latest_questions = self._question_repo.get_latest_questions(
                timezone_now, get_count
            )
        else:
            latest_questions = self._question_repo.get_all()

        # , 区切りの投票タイトルの文字列
        output = ", ".join(
            [q.question_text for q in latest_questions]
        )

        return latest_questions, output


class VoteService:
    def __init__(self):
        # self._question_repo = QuestionRepository(
        #     QuestionDBRepository()
        # )
        self._question_repo = QuestionDBRepository()

    def execute(self, question_id: int, choice_id: int):
        return self.add_vote(question_id, choice_id)

    def add_vote(self, question_id: int, choice_id: int):
        """ 投票を行う. """
        return self._question_repo.create_vote(
            question_id, choice_id
        )
