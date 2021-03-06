import inject

from .repositories import QuestionRepository
from .services import (
    ChoiceAggregateService,
    LatestQuestionService,

    VoteService,
)
from .exceptions import ChoiceDoesNotExist, QuestionDoesNotExist


class ShowVoteIndexUsecase:
    def __init__(self, service=LatestQuestionService):
        self._latest_question_service = service()

    def execute(self) -> dict:
        # 最新の投票内容を取得
        service = self._latest_question_service
        latest_questions_result = service.get_latest_questions()

        # 整形処理
        context = {
            "latest_question_list": latest_questions_result[0],
            "output": latest_questions_result[1]
        }

        return context


class ShowVoteDetailUsecase:

    @inject.params(question_repo=QuestionRepository)
    def __init__(self, question_repo: QuestionRepository):
        self._question_repo = question_repo

    def execute(self, question_id: int) -> dict:
        # 投票内容を取り出す
        question = self.get_question(question_id)

        if not question:
            error_message = "Question does not exist."
            raise QuestionDoesNotExist(error_message)

        return question

    def get_question(self, question_id: int):
        return self._question_repo.get_question(
            question_id
        )


class ShowVoteResultsUsecase:

    @inject.params(question_repo=QuestionRepository)
    def __init__(
        self,
        question_repo: QuestionRepository,
        service=ChoiceAggregateService
    ):
        self._question_repo = question_repo
        self._choice_aggregate_service = service()

    def execute(self, question_id: int) -> dict:
        # 投票内容を取り出す
        question = self._question_repo.get_question(
            question_id
        )

        if not question:
            error_message = "Question does not exist."
            raise QuestionDoesNotExist(error_message)

        # 集計する
        max, min, avg = self.aggregate()

        # 整形処理
        results = {"question": question, "max": max, "min": min, "avg": avg}

        return results

    def aggregate(self) -> tuple:
        """集計する."""

        # ドメインサービスを呼び出す
        service = self._choice_aggregate_service
        aggregates = service.show_max_min_avg_aggregate()

        # 整形処理
        max = aggregates[0]
        min = aggregates[1]
        avg = aggregates[2]

        return max, min, avg


class VoteUsecase:
    """ 投票のUsecase. """

    def __init__(self):
        self._vote_service = VoteService()

    def execute(self, question_id: int, choice_id: int) -> dict:
        question, selected_choice = self.add_vote(
            question_id, choice_id
        )

        if not question:
            error_message = "Question does not exist."
            raise QuestionDoesNotExist(error_message)

        if not selected_choice:
            error_message = "You didn't select a choice."
            raise ChoiceDoesNotExist(question, error_message)

        return question

    def add_vote(self, question_id: int, choice_id: int):
        return self._vote_service.add_vote(
            question_id, choice_id
        )


class CreateUserUsecase:
    def __init__(self, user_repo, user_service):
        self._user_repo = user_repo
        self._user_service = user_service

    # def execute(user_data: UserData) -> User:
    # do stuff
    # user_repo.create(user_dto)
    # do more stuff
