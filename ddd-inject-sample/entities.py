import uuid


class User:
    def __init__(
        self,
        identity: uuid.uuid4(),
        name: str
    ) -> None:
        """User Entity.

        Args:
            identity (uuid.uuid4): uuid identity.
            name (str): name of str type.

        Returns:
            None: return None.
        """
        self.identity = identity
        self.name = name
