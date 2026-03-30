from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFileDialog, QLineEdit, QListView, QMainWindow, QMenu, QVBoxLayout

from PySide6.QtGui import QAction, QPixmap

from PySide6.QtCore import QAbstractListModel, QModelIndex, QSize, Qt, Slot

class ListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        # self.__images_list = self.__create_default_data()
        self.__images_list = []

    # def __create_default_data(self):
    #     return ["/home/alex/Sync/Documents/University/3rdCOURSE/2ndSemester/qt-practice/practice_7/task_2/images/bay.jpeg", "/home/alex/Sync/Documents/University/3rdCOURSE/2ndSemester/qt-practice/practice_7/task_2/images/bay_2.jpeg", "/home/alex/Sync/Documents/University/3rdCOURSE/2ndSemester/qt-practice/practice_7/task_2/images/bay_3.jpeg", "/home/alex/Sync/Documents/University/3rdCOURSE/2ndSemester/qt-practice/practice_7/task_2/images/bay_4.jpeg"]
    
    def rowCount(self, parent=None):
        return len(self.__images_list)

    def data(self, index, role=Qt.DecorationRole):
        if not index.isValid():
            return None

        path = self.__images_list[index.row()]
        if role == Qt.DecorationRole:
            pixmap = QPixmap(path)
            if pixmap.isNull():
                return None
            return pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        return None
        
    def addImage(self, path):
        row = len(self.__images_list)
        self.beginInsertRows(QModelIndex(), row, row)
        self.__images_list.append(path)
        self.endInsertRows()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__imagesModel = ListModel()
        
        self.imagesView = QListView()
        self.imagesView.setModel(self.__imagesModel)

        self.setCentralWidget(self.imagesView)

        menuBar = self.menuBar()
        actionAdd = menuBar.addAction("Добавить")
        actionAdd.triggered.connect(self.pick_images)

    def pick_images(self):
        paths, _ = QFileDialog.getOpenFileNames(self, "Выберите изображения","/home/alex/Sync/Documents/University/3rdCOURSE/2ndSemester/qt-practice/practice_7/task_2/images", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All files (*)")
        if not paths:
            return
        
        for path in paths:
            self.__imagesModel.addImage(path)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    with open("styles.qss", "r") as f:
        styles = f.read()
        app.setStyleSheet(styles)

    app.exec()