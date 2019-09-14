from polls_app.polls.repositories import PollsRepository

from polls_app.polls.models import Question


class QuestionRepository(PollsRepository):
    def __init__(self, db_repo):
        self.__db_repo = db_repo

    def get_question(self, question_id: int):
        return self.__db_repo.filter_by_question_id(question_id)

    def get_all(self):
        return self.__db_repo.get_all()


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
