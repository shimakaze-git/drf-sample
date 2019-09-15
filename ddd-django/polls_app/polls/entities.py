class User:
    def __init__(self, identification: int, name: str, email: str):
        self.__identification = identification
        self.__name = name
        self.__email = email


class Question:

    def __init__(self, identification: int, text: str, pub_date: str):
        self.__identification = identification
        self.__text = text
        self.__pub_date = pub_date

    @property
    def text(self):
        return self.__text

    @property
    def pub_date(self):
        return self.__pub_date

    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
