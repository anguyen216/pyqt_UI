import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from app.gui.file_window import FileWindow
from app.gui.report_window import ReportWindow
from app.gui.metric_detail_window import MetricDetailWindow

class Main():
    """
    Entry point class for our application

    This class also functions as a singleton controller of all our UI windows
    such that we can have an overarching object that has visibility/access to 
    all GUI windows
    """

    def __init__(self):
        """
        Initialize the qt application and create the initial file open window
        """
        app = QApplication(sys.argv)
        self.openFileWindow()
        app.exec()

    def openFileWindow(self):
        """
        Close the report window if it is open
        Then open a new file browse window
        """
        self.closeReportWindow()

        self.fileWindow = FileWindow(self)
        self.fileWindow.show()

    def closeFileWindow(self):
        """
        If the file window is open, ask it to close
        """
        if hasattr(self, 'fileWindow'):
            self.fileWindow.close()

    def openReportWindow(self, filename, data):
        """
        Close the file browse window if it is open
        Then open a new report window with the given file/data
        """
        self.closeFileWindow()

        self.reportWindow = ReportWindow(self, filename, data)
        self.reportWindow.displayWindow()
    
    def closeReportWindow(self):
        """
        If the report window is open, ask it to close
        """
        if hasattr(self, 'reportWindow'):
            self.reportWindow.close()

    def openMetricDetailWindow(self, metric, summary_data, histogram_data):
        self.metricDetailWindow = MetricDetailWindow(self, metric, summary_data, histogram_data)
        self.metricDetailWindow.displayWindow()

    def close(self):
        """
        Close the entire applicaiton
        """
        QApplication.quit()