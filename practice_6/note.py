from datetime import datetime

class Note:
    def __init__(self, text):
        self.__date = datetime.now()
        if not isinstance(text, str) or text.strip() == "":
            raise AttributeError("text должен быть непустой строкой, содержащий значимые символы")
        self.__text = text
    
    def text(self):
        return self.__text
    
    def date(self):
        return self.__date.strftime("%d:%m:%Y")

    def __str__(self):
        return f"{self.date()}\n{self.text()}"
