from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, 
                               QPushButton, QLabel, QCheckBox, QDialogButtonBox, QWidget)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Соглашение")
        self.setMinimumSize(300, 150)
        
        layout = QVBoxLayout()
        
        self.btn = QPushButton("Принять соглашение")
        self.btn.clicked.connect(self.open_dialog)
        
        self.status_label = QLabel("Соглашение НЕ принято")
        self.status_label.setObjectName("statusLabel")
        self.status_label.setProperty("status", "rejected")  
        
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
            self.status_label.setProperty("status", "accepted")  
        else:
            self.status_label.setText("Соглашение НЕ принято")
            self.status_label.setProperty("status", "rejected")  
        
        self.status_label.style().polish(self.status_label)


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Подтверждение")
        layout = QVBoxLayout()

        self.checkbox = QCheckBox("Я прочитал и принимаю условия")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        layout.addWidget(self.checkbox)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    with open("styles.qss", "r") as f:
        styles = f.read()
        app.setStyleSheet(styles)
    app.exec()