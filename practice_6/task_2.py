from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLineEdit, QListView, QMainWindow, QMenu, QVBoxLayout

from PySide6.QtGui import QAction

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot

from note import Note

class NoteDialog(QDialog):
    def __init__(self, noteText):
        super().__init__()
        self.setWindowTitle("Заметка")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.textEdit = QLineEdit(noteText)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def getText(self):
        return self.textEdit.text()

    


class ListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.__notes_list = self.__create_default_data()

    def __create_default_data(self):
        return [Note("alskdjflaskdjf laskdjf laksjdf"), Note("skdfhksjdf hskjfd hgskfdj g"), Note("skfdg hkjsfd gskdfg sf ")]
    
    def rowCount(self, parent=None):
        return len(self.__notes_list)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return str(self.__notes_list[index.row()])
        return None
    
    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return None
        
        row = index.row()

        if row < 0 or row >= len(self.__notes_list):
            return None

        if role == Qt.EditRole:
            self.__notes_list[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
        
        return None
    
    def addNote(self, text):
        row = len(self.__notes_list)
        self.beginInsertRows(QModelIndex(), row, row)
        self.__notes_list.append(Note(text))
        self.endInsertRows()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__notesModel = ListModel()
        
        self.notesView = QListView()
        self.notesView.setModel(self.__notesModel)

        self.setCentralWidget(self.notesView)

        menuBar = self.menuBar()
        actionAdd = menuBar.addAction("Добавить")
        actionAdd.triggered.connect(self.clickAdd)

    def contextMenuEvent(self, e):
        index = self.notesView.indexAt(e.pos())

        context = QMenu(self)
        actionAdd = context.addAction("Добавить")
        actionAdd.triggered.connect(self.clickAdd)

        if index.isValid():
            actionEdit = context.addAction("Изменить")
            actionEdit.triggered.connect(lambda checked, idx=index: self.clickEdit(idx))

        context.exec(e.globalPos())

    
    @Slot()
    def clickAdd(self):
        dialog = NoteDialog("")
        result = dialog.exec()

        if result == QDialog.Accepted:
            text = dialog.getText().strip()
            if text:
                self.__notesModel.addNote(text)

    
    @Slot()
    def clickEdit(self, index):
        dialog = NoteDialog("")
        result = dialog.exec()

        if result == QDialog.Accepted:
            text = dialog.getText().strip()
            if text:
                self.__notesModel.setData(index, Note(text))


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()