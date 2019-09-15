from datetime import datetime
from abc import ABCMeta, abstractmethod

from polls_app.polls.models import Question


class ChoiceRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_vote_aggregates(self):
        raise NotImplementedError

    @abstractmethod
    def get_max(self):
        raise NotImplementedError

    @abstractmethod
    def get_min(self):
        raise NotImplementedError

    @abstractmethod
    def get_avg(self):
        raise NotImplementedError

    @abstractmethod
    def get_choice(
        self, choice_id: int
    ):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError


class QuestionRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_question(self, question_id: int):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_latest_questions(
        self, timezone_now: datetime, count=5
    ):
        raise NotImplementedError

    @abstractmethod
    def get_selected_choice(
        self, question: Question, choice_id: int
    ):
        raise NotImplementedError

    @abstractmethod
    def create_vote(
        self, question_id: int, choice_id: int, vote_count=1
    ):
        raise NotImplementedError
