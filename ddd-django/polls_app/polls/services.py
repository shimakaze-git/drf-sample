import inject

from django.utils import timezone

from .repositories import QuestionRepository, ChoiceRepository


class ChoiceAggregateService:
    @inject.params(choice_repo=ChoiceRepository)
    def __init__(self, choice_repo: ChoiceRepository):
        self._choice_repo = choice_repo

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
    @inject.params(question_repo=QuestionRepository)
    def __init__(self, question_repo: QuestionRepository):
        self._question_repo = question_repo

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
    @inject.params(question_repo=QuestionRepository)
    def __init__(self, question_repo: QuestionRepository):
        self._question_repo = question_repo

    def execute(self, question_id: int, choice_id: int):
        return self.add_vote(question_id, choice_id)

    def add_vote(self, question_id: int, choice_id: int):
        """ 投票を行う. """
        return self._question_repo.create_vote(
            question_id, choice_id
        )
