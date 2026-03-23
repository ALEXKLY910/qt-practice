from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QListView, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QAbstractItemView
)

class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.model = QStringListModel([])

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите заметку...")

        self.add_button = QPushButton("Добавить")

        self.view = QListView()
        self.view.setModel(self.model)

        top_row = QHBoxLayout()
        top_row.addWidget(self.input)
        top_row.addWidget(self.add_button)

        layout = QVBoxLayout()
        layout.addLayout(top_row)
        layout.addWidget(self.view)

        self.setLayout(layout)

        self.view.clicked.connect(self.clicked)
        self.add_button.clicked.connect(self.add_note)

    def clicked(self, modelIndex):
        self.model.removeRow(modelIndex.row())

    def add_note(self):
        text = self.input.text().strip()
        if not text:
            return
        row_number = self.model.rowCount()
        self.model.insertRow(row_number)

        self.model.setData(self.model.index(row_number, 0), text, Qt.DisplayRole)

        self.input.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()