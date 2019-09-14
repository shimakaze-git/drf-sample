from .use_cases import ShowVoteResultsUsecase


def build_show_vote_results_use_case() -> ShowVoteResultsUsecase:
    return ShowVoteResultsUsecase()
