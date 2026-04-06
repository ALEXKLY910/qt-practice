import math

from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QSplineSeries


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        sine_series = QSplineSeries()
        sine_series.setName("sin(x)")

        cosine_series = QSplineSeries()
        cosine_series.setName("cos(x)")

        point_count = 31
        start_x = 0
        end_x = 2 * math.pi
        step = (end_x - start_x) / (point_count - 1)

        for point_index in range(point_count):
            x_value = start_x + point_index * step
            sine_series.append(x_value, math.sin(x_value))
            cosine_series.append(x_value, math.cos(x_value))

        chart = QChart()
        chart.addSeries(sine_series)
        chart.addSeries(cosine_series)

        chart.createDefaultAxes()

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)


if __name__ == "__main__":
    app = QApplication([])

    window = TestChart()
    window.resize(600, 500)

    window.show()

    app.exec()