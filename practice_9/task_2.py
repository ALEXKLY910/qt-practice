from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        graph_widget = pg.PlotWidget()
        self.setCentralWidget(graph_widget)

        data_frame = pd.read_csv("files/trees.csv")

        ids = data_frame["ID"].tolist()
        height_values = data_frame["Height"].tolist()

        graph_widget.setBackground("w")
        graph_widget.setLabel("left", "Height")
        graph_widget.setLabel("bottom", "ID")
        graph_widget.showGrid(x=True, y=True)

        graph_widget.plot(
            ids,
            height_values,
            pen=None,
            symbol="o"
        )


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()