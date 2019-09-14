from .repositories.questions import QuestionRepository, QuestionDBRepository
from .services import ChoiceAggregateService, VoteService


class ShowVoteResultsUsecase:
    def __init__(self):
        self._question_repo = QuestionRepository(QuestionDBRepository())

    def execute(self, question_id: int) -> dict:
        # 投票内容を取り出す
        question = self._question_repo.get_question(
            question_id
        )

        # 集計する
        max, min, avg = self.aggregate()

        # 整形処理
        results = {"question": question, "max": max, "min": min, "avg": avg}

        return results

    def aggregate(self) -> tuple:
        """集計する."""

        # ドメインサービスを呼び出す
        service = ChoiceAggregateService()
        aggregates = service.show_max_min_avg_aggregate()

        max = aggregates[0]
        min = aggregates[1]
        avg = aggregates[2]

        return max, min, avg


class CreateUserUsecase:
    def __init__(self, user_repo, user_service):
        self._user_repo = user_repo
        self._user_service = user_service

    # def execute(user_data: UserData) -> User:
    # do stuff
    # user_repo.create(user_dto)
    # do more stuff


class VoteUsecase:
    """ 投票のUsecase. """

    def __init__(self):
        self._vote_service = VoteService()
        self._question_repo = QuestionRepository(QuestionDBRepository())

    def execute(self, question_id: int, choice_id: int) -> dict:
        self._vote_service.add_vote(question_id, choice_id)

    #     question = self._question_repo.get_question(
    #         question_id
    #     )

    #     # 集計する
    #     max, min, avg = self.aggregate()

    #     # 整形処理
    #     results = {"question": question, "max": max, "min": min, "avg": avg}

    #     return results


    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     print("question.choice_set", question.choice_set)
    #     print("request.POST['choice']", request.POST["choice"])
    #     # print(dir(question))

    #     selected_choice = question.choice_set.get(pk=request.POST["choice"])
    #     print("selected_choice", selected_choice)
    # except (KeyError, Choice.DoesNotExist):
    #     # request.POST['choice'] は KeyError を送出
    #     return render(
    #         request,
    #         "polls/detail.html",
    #         {"question": question, "error_message": "You didn't select a choice."},
    #     )
    # else:
    #     # selected_choice.votes += 1
    #     # selected_choice.save()

    #     return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))