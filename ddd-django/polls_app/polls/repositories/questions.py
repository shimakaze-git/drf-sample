from datetime import datetime

from polls_app.polls.repositories import PollsRepository

from polls_app.polls.models import Question


class QuestionRepository(PollsRepository):
    def __init__(self, db_repo):
        self.__db_repo = db_repo

    def get_question(self, question_id: int):
        return self.__db_repo.filter_by_question_id(question_id)

    def get_all(self):
        return self.__db_repo.get_all()

    def get_selected_choice(self, choice_id: int):
        return self.__db_repo.get_selected_choice(choice_id)

    def create_vote(self, choice_id: int, vote_count=1):
        return self.__db_repo.add_vote(
            choice_id,
            vote_count
        )


class QuestionDBRepository(QuestionRepository):
    def __init__(self):
        self.question_orm = Question

    def filter_by_question_id(self, question_id: int):
        """
        Questionオブジェクトのquestion_idを元にフィルタリング処理を行う.

        Args:
            question_id (int): question_id

        Returns:
            [type]: [description]
        """
        assert isinstance(question_id, int)
        return self.question_orm.objects.filter(
            pk=question_id
        ).first()

    def get_all(self):
        return self.question_orm.objects.all()

    def get_latest_questions(
        self, timezone_now: datetime, count=5
    ):
        """
        公開日が現在時刻より下回る最新の投票を取り出す.

        Args:
            timezone_now (datetime): 現在時刻.
            count (int, optional): 取り出す数. Defaults to 5.
        """
        return self.question_orm.objects.filter(
            pub_date__lte=timezone_now
        ).order_by("-pub_date")[:count]

    def get_selected_choice(self, question: Question, choice_id: int):
        assert isinstance(question, int)
        assert isinstance(choice_id, int)

        selected_choice = question.choice_set.filter(
            pk=choice_id
        )
        return selected_choice

    def create_vote(
        self, question_id: int, choice_id: int, vote_count=1
    ):
        """
        投票処理を行う.

        実際に投稿処理が行われ、投票数がカウントされる/

        Args:
            question_id (int): questionのpk.
            choice_id (int): 選択項目のpk.
            vote_count (int, optional): 投票数. Defaults to 1.
        """
        # 投票内容を取り出す
        question = self.filter_by_question_id(question_id)

        # choiceの選択後
        selected_choice = self.get_selected_choice(
            question,
            choice_id
        )

        if not selected_choice:
            selected_choice.votes += vote_count
            selected_choice.save()
        return question, selected_choice
