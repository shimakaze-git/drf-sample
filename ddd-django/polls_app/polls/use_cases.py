class ShowVoteResultsUsecase:

    def __init__(self):
        pass

    def execute(self):
        return None


class CreateUserUsecase:
    def __init__(self, user_repo, user_service):
        self._user_repo = user_repo
        self._user_service = user_service

    # def execute(user_data: UserData) -> User:
        # do stuff
        # user_repo.create(user_dto)
        # do more stuff
