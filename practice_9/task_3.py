import pandas as pd

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QValueAxis
)


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        data_frame = pd.read_csv("files/hurricanes.csv")

        month_names = data_frame["Month"].tolist()
        hurricanes_2007 = data_frame["2007"].tolist()

        year_names = data_frame.columns[2:].tolist()
        hurricanes_by_year = []
        for year_name in year_names:
            hurricanes_by_year.append(data_frame[year_name].sum())

        bar_set_2007 = QBarSet("2007")
        bar_set_2007.append(hurricanes_2007)

        series_2007 = QBarSeries()
        series_2007.append(bar_set_2007)

        chart_2007 = QChart()
        chart_2007.addSeries(series_2007)
        chart_2007.setTitle("Ураганы в 2007 по месяцам")

        axis_x_2007 = QBarCategoryAxis()
        axis_x_2007.append(month_names)
        chart_2007.addAxis(axis_x_2007, Qt.AlignBottom)
        series_2007.attachAxis(axis_x_2007)

        axis_y_2007 = QValueAxis()
        axis_y_2007.setTitleText("Число ураганов")
        axis_y_2007.setRange(0, max(hurricanes_2007) + 1)
        chart_2007.addAxis(axis_y_2007, Qt.AlignLeft)
        series_2007.attachAxis(axis_y_2007)

        chart_2007.legend().hide()

        chart_view_2007 = QChartView(chart_2007)
        chart_view_2007.setRenderHint(QPainter.Antialiasing)

        bar_set_years = QBarSet("Total")
        bar_set_years.append(hurricanes_by_year)

        series_years = QBarSeries()
        series_years.append(bar_set_years)

        chart_years = QChart()
        chart_years.addSeries(series_years)
        chart_years.setTitle("Всего ураганов по годам")

        axis_x_years = QBarCategoryAxis()
        axis_x_years.append(year_names)
        chart_years.addAxis(axis_x_years, Qt.AlignBottom)
        series_years.attachAxis(axis_x_years)

        axis_y_years = QValueAxis()
        axis_y_years.setTitleText("Число ураганов")
        axis_y_years.setRange(0, max(hurricanes_by_year) + 1)
        chart_years.addAxis(axis_y_years, Qt.AlignLeft)
        series_years.attachAxis(axis_y_years)

        chart_years.legend().hide()

        chart_view_years = QChartView(chart_years)
        chart_view_years.setRenderHint(QPainter.Antialiasing)

        central_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(chart_view_2007)
        layout.addWidget(chart_view_years)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication([])

    window = TestChart()
    window.show()

    app.exec()