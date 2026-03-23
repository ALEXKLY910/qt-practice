from PySide6.QtWidgets import *
from PySide6.QtCore import Slot

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.outer = QVBoxLayout()

        form = QFormLayout()

        self.surname_edit = QLineEdit()
        self.surname_edit.setPlaceholderText("Иванов")
        form.addRow("Фамилия:", self.surname_edit)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Иван")
        form.addRow("Имя:", self.name_edit)

        self.patronymic_edit = QLineEdit()
        self.patronymic_edit.setPlaceholderText("Иванович")
        form.addRow("Отчество:", self.patronymic_edit)

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("example@mail.ru")
        form.addRow("Почта:", self.email_edit)

        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("9201231212")
        form.addRow("Телефон:", self.phone_edit)

        topics_layout = QVBoxLayout()

        for topic in [
            "Машинное обучение",
            "Сетевые технологии",
            "Облачные сервисы",
            "Тестирование ПО",
            "Информационная безопасность",
        ]:
            checkbox = QCheckBox(topic)
            topics_layout.addWidget(checkbox)

        form.addRow("Темы:", topics_layout)

        self.consent_checkbox = QCheckBox("Согласие на обработку персональных данных (обязательно)")
        self.newsletter_checkbox = QCheckBox("Согласие на рассылку (необязательно)")
        form.addRow("", self.consent_checkbox)
        form.addRow("", self.newsletter_checkbox)

        self.outer.addLayout(form)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        self.result_label.hide()

        self.outer.addWidget(self.result_label)

        self.check_btn = QPushButton("Проверить ввод")
        self.check_btn.clicked.connect(self.check_input)
        self.outer.addWidget(self.check_btn)



        self.setLayout(self.outer)
    


    def set_result_label(self, text):        
        self.result_label.setText(text)
        self.result_label.show()

    @Slot()
    def check_input(self):
        if not self.consent_checkbox.isChecked():
            self.set_result_label("Для продолжения вам нужно согласиться с обработкой данных")
            return

        fields = [
            self.surname_edit.text().strip(),
            self.name_edit.text().strip(),
            self.patronymic_edit.text().strip(),
            self.email_edit.text().strip(),
            self.phone_edit.text().strip(),
        ]

        if any(not x for x in fields):
            self.set_result_label("Не все поля введены")
        else:
            self.set_result_label("Поля корректены")


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec()