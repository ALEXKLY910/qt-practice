from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)

        self.square = QWidget(self)
        self.square.setFixedSize(60, 60)
        self.square.setStyleSheet("background: green;")
        self.square.move(40, 40)

        self.other = QPushButton("Кнопка", self)
        self.other.resize(90, 30)
        self.other.move(450, 300)

        square_anim = QPropertyAnimation(self.square, b"pos", self)
        square_anim.setDuration(4000)
        square_anim.setStartValue(QPoint(40, 40))
        square_anim.setKeyValueAt(0.33, QPoint(300, 50))
        square_anim.setKeyValueAt(0.66, QPoint(120, 250))
        square_anim.setEndValue(QPoint(420, 180))
        square_anim.setEasingCurve(QEasingCurve.Linear)

        other_anim = QPropertyAnimation(self.other, b"pos", self)
        other_anim.setDuration(4000)
        other_anim.setStartValue(QPoint(450, 300))
        other_anim.setEndValue(QPoint(80, 320))
        other_anim.setEasingCurve(QEasingCurve.InExpo)

        self.group = QParallelAnimationGroup(self)
        self.group.addAnimation(square_anim)
        self.group.addAnimation(other_anim)
        self.group.start()

if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec()