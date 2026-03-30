
from PySide6.QtWidgets import QLineEdit, QMainWindow, QPushButton, QWidget, QWizard, QMessageBox, QWizardPage, QLabel, QVBoxLayout, QCheckBox, QApplication



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Основное окно")

        layout = QVBoxLayout()
        self.btn = QPushButton("Зарегистрироваться")
        self.btn.clicked.connect(self.run_wizard)

        self.result_label = QLabel("Вы не зарегистрированы")
        
        layout.addWidget(self.btn)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def run_wizard(self):
        wizard = Wizard(self)
        if wizard.exec():
            summary = wizard.getSummary()
            self.result_label.setText(summary)


class Wizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.summary = ""
        self.addPage(Registration())
        self.addPage(Identity())
        self.addPage(Themes())
        self.setWindowTitle("Регистрация")

    def accept(self):
        QMessageBox.information(None, "Регистрация", "Регистрация пройдена")
        login = self.field("login")
        password = self.field("password")
        first_name = self.field("first_name")
        last_name = self.field("last_name")
        second_name = self.field("second_name")
        reading_books_check_box = self.field("reading_books_check_box")
        watching_films_check_box = self.field("watching_films_check_box")
        playing_games_check_box = self.field("playing_games_check_box")
        worldwide_news_check_box = self.field("worldwide_news_check_box")
        regional_news_check_box = self.field("regional_news_check_box")
        self.summary = f"Логин: {login}\nПароль: {password}\nИмя: {first_name}\nФамилия: {last_name}\nОтчество: {second_name}\nЧтение книг: {reading_books_check_box}\nПросмотр фильмов: {watching_films_check_box}\nПрохождение видеоигр: {playing_games_check_box}\nМировые СМИ: {worldwide_news_check_box}\nРегиональные СМИ: {regional_news_check_box}"
        super(Wizard, self).accept()

    def getSummary(self):
        return self.summary

class Registration(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Логин и пароль")
        self.login = QLineEdit()
        self.login.setPlaceholderText("Введите логин")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Введите пароль")

        self.registerField("login*", self.login)
        self.registerField("password*", self.password)

        layout = QVBoxLayout(self)
        layout.addWidget(self.login)
        layout.addWidget(self.password)

class Identity(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("ФИО")
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Введите имя")
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Введите фамилию")
        self.second_name = QLineEdit()
        self.second_name.setPlaceholderText("Введите отчество")

        self.registerField("first_name*", self.first_name)
        self.registerField("last_name*", self.last_name)
        self.registerField("second_name", self.second_name)

        layout = QVBoxLayout(self)
        layout.addWidget(self.first_name)
        layout.addWidget(self.last_name)
        layout.addWidget(self.second_name)


class Themes(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Интересные темы")
        self.reading_books_check_box = QCheckBox("Чтение книг")
        self.watching_films_check_box = QCheckBox("Просмотр фильмов")
        self.playing_games_check_box = QCheckBox("Прохождение видеоигр")
        self.worldwide_news_check_box = QCheckBox("Мировые СМИ")
        self.regional_news_check_box = QCheckBox("Региональные СМИ")

        self.registerField("reading_books_check_box", self.reading_books_check_box)
        self.registerField("watching_films_check_box", self.watching_films_check_box)
        self.registerField("playing_games_check_box", self.playing_games_check_box)
        self.registerField("worldwide_news_check_box", self.worldwide_news_check_box)
        self.registerField("regional_news_check_box", self.regional_news_check_box)

        layout = QVBoxLayout(self)
        layout.addWidget(self.reading_books_check_box)
        layout.addWidget(self.watching_films_check_box)
        layout.addWidget(self.playing_games_check_box)
        layout.addWidget(self.worldwide_news_check_box)
        layout.addWidget(self.regional_news_check_box)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
