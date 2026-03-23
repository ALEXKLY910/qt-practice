from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        curriculum_layout = QVBoxLayout()

        wednesday_container = QVBoxLayout()
        wednesday_label = QLabel("Среда")
        wednesday_label.setAlignment(Qt.AlignCenter)
        wednesday_layout = QGridLayout()

        lecture1_group1 = QLabel("Основы машинного обучения")
        lecture1_group1.setAlignment(Qt.AlignCenter)
        wednesday_layout.addWidget(lecture1_group1, 0, 0)
        
        lecture1_group2 = QLabel("Введение в сетевые технологии")
        lecture1_group2.setAlignment(Qt.AlignCenter)
        wednesday_layout.addWidget(lecture1_group2, 0, 1)

        lecture2 = QLabel("Методы разработки современных облачных сервисов")
        lecture2.setAlignment(Qt.AlignCenter)
        wednesday_layout.addWidget(lecture2, 1, 0, 1, 2)

        lecture3 = QLabel("Основы тестирования программного обеспечения")
        lecture3.setAlignment(Qt.AlignCenter)
        wednesday_layout.addWidget(lecture3, 2, 0, 1, 2)

        wednesday_container.addWidget(wednesday_label)
        wednesday_container.addLayout(wednesday_layout)

        thursday_container = QVBoxLayout()
        thursday_label = QLabel("Четверг")
        thursday_label.setAlignment(Qt.AlignCenter)
        thursday_layout = QGridLayout()

        lecture1_group1 = QLabel("Основы машинного обучения")
        lecture1_group1.setAlignment(Qt.AlignCenter)
        thursday_layout.addWidget(lecture1_group1, 0, 0)
        
        lecture1_group2 = QLabel("Введение в сетевые технологии")
        lecture1_group2.setAlignment(Qt.AlignCenter)
        thursday_layout.addWidget(lecture1_group2, 0, 1)

        lecture2 = QLabel("Методы разработки современных облачных сервисов")
        lecture2.setAlignment(Qt.AlignCenter)
        thursday_layout.addWidget(lecture2, 1, 0, 1, 2)

        lecture3 = QLabel("Основы тестирования программного обеспечения")
        lecture3.setAlignment(Qt.AlignCenter)
        thursday_layout.addWidget(lecture3, 2, 0, 1, 2)

        thursday_container.addWidget(thursday_label)
        thursday_container.addLayout(thursday_layout)
        
        curriculum_layout.addLayout(wednesday_container)
        curriculum_layout.addLayout(thursday_container)

        self.setLayout(curriculum_layout)


        



if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

