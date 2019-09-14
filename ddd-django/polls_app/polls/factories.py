from .use_cases import (
    ShowVoteResultsUsecase,
    ShowVoteDetailUsecase,
    ShowVoteIndexUsecase,
)


def build_show_vote_results_use_case() -> ShowVoteResultsUsecase:
    return ShowVoteResultsUsecase()


def build_show_vote_detail_use_case() -> ShowVoteDetailUsecase:
    return ShowVoteDetailUsecase()


def build_show_vote_index_use_case() -> ShowVoteIndexUsecase:
    return ShowVoteIndexUsecase()
