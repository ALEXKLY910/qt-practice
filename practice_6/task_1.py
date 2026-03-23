from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, 
                               QPushButton, QLabel, QCheckBox, QDialogButtonBox)
from PySide6.QtWidgets import QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Соглашение")
        
        layout = QVBoxLayout()
        
        self.btn = QPushButton("Принять соглашение")
        self.btn.clicked.connect(self.open_dialog)
        
        
        self.status_label = QLabel("Соглашение НЕ принято")
        
        layout.addWidget(self.btn)
        layout.addWidget(self.status_label)
    
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_dialog(self):
        dlg = CustomDialog()

        dlg.exec()
        
        if dlg.checkbox.isChecked():
            self.status_label.setText("Соглашение принято")
        else:
            self.status_label.setText("Соглашение НЕ принято")

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Диалог")
        layout = QVBoxLayout()

        self.checkbox = QCheckBox("Принимаю соглашение")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        layout.addWidget(self.checkbox)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
