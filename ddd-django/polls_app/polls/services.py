from .repositories.choices import ChoiceRepository, ChoiceDBRepository
from .repositories.questions import QuestionRepository, QuestionDBRepository


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


class VoteService:
    def __init__(self):
        self._question_repo = QuestionRepository(
            QuestionDBRepository()
        )

    def execute(self, question_id: int, choice_id: int):
        question, selected_choice = self.add_vote(question_id, choice_id)

    def add_vote(self, question_id: int, choice_id: int):
        """ 投票を行う. """

        return self._question_repo.add_vote(
            question_id, choice_id
        )
        # "error_message": "You didn't select a choice."

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
