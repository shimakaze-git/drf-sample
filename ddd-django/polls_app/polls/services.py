from .repositories.choices import ChoiceRepository, ChoiceDBRepository


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
