from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QLinearGradient, QPainter, QPen, QPolygon, QBrush
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.setWindowTitle("Рисование фигур")

    def paintEvent(self, arg__0):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black))

        square_rect = QRect(220, 180, 120, 120)
        gradient = QLinearGradient(square_rect.topLeft(), square_rect.bottomRight())
        gradient.setColorAt(0.0, Qt.red)
        gradient.setColorAt(1.0, Qt.yellow)
        painter.setBrush(QBrush(gradient))
        painter.drawRect(square_rect)

        painter.setBrush(Qt.green)
        painter.drawEllipse(60, 210, 140, 80)

        triangle = QPolygon([
            QPoint(280, 60),
            QPoint(220, 160),
            QPoint(340, 160),
        ])
        painter.drawPolygon(triangle)

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
