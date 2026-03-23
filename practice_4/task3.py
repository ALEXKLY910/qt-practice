from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        if event.position().y() < self.height() / 2:
            self.create_widget(event.position().x(), event.position().y())

    def create_widget(self, pos_x, pos_y):
        print(pos_x, pos_y)
        newWidget = DragWidget()
        newWidget.setParent(self)
        newWidget.setStyleSheet("background-color:#000000")
        newWidget.setGeometry(pos_x, pos_y, 40, 40)
        newWidget.show()

class DragWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

