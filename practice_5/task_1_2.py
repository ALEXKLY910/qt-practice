import sys
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget,
    QListView, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)


class NotesModel(QAbstractItemModel):
    def __init__(self, notes, parent=None):
        super().__init__(parent)
        self.notes = notes

    def rowCount(self, parent=None):
        return len(self.notes)

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.column() != 0:
            return None

        row = index.row()
        if row < 0 or row >= len(self.notes):
            return None

        return self.notes[row]

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or index.column() != 0:
            return False
        if role not in (Qt.EditRole, Qt.DisplayRole):
            return False

        row = index.row()
        if row < 0 or row >= len(self.notes):
            return False

        self.notes[row] = str(value)
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
        return True

    # ---- structural changes ----

    def insertRows(self, row, count, parent=None):
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return False
        if count <= 0:
            return False
        if row < 0 or row > len(self.notes):
            return False

        self.beginInsertRows(QModelIndex(), row, row + count - 1)
        for _ in range(count):
            self.notes.insert(row, "")
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=None):
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return False
        if count <= 0:
            return False
        if row < 0 or row + count > len(self.notes):
            return False

        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        del self.notes[row:row + count]
        self.endRemoveRows()
        return True


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.model = NotesModel([])

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
        if modelIndex.isValid():
            self.model.removeRow(modelIndex.row())

    def add_note(self):
        text = self.input.text().strip()
        if not text:
            return

        row_number = self.model.rowCount()
        self.model.insertRow(row_number)
        self.model.setData(self.model.index(row_number, 0), text, Qt.EditRole)

        self.input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())