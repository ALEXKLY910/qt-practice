from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
    
        



if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

