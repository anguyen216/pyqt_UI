import os
import sys
from PyQt6 import uic
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QTableWidgetItem, QMainWindow
)

from app.data.compute_statistics import getSummaryStatistics, getSummaryStatisticsFormatted, getStatisticsRanking, getHistogramData

## get the path to the designer file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DESIGNER_OPEN_FILE = os.path.join(ROOT_DIR,"designer","report_window.ui")

## Display and add functionality to the Main Report window
class ReportWindow(QMainWindow):
    def __init__(self, parent, filename, data):
        super(ReportWindow, self).__init__()

        self.parent = parent
        self.data = data
        self.ui = uic.loadUi(DESIGNER_OPEN_FILE, self)
        self.setUpReportLabel(filename)
        self.fillInSummaryTable(data)
        self.fillInRankingTable(data)

        self.initializeMenuEvents()
        self.initializeMetricDetailButtons()

    def initializeMenuEvents(self):
        """
        hook up main window file menu events
        """
        # close the window / application
        self.ui.loadCSVAction.triggered.connect(self.openNewFile)

        # close the window / application
        self.ui.closeAction.triggered.connect(self.close)

    def initializeMetricDetailButtons(self):
        """
        Hook up our metric detail event buttons
        TODO: there is probably a better way to do this to support dynamic metric creation
        """
        self.ui.metricDay.clicked.connect(lambda: self.getMetricDetails("lifespan"))
        self.ui.metricA.clicked.connect(lambda: self.getMetricDetails("A"))
        self.ui.metricB.clicked.connect(lambda: self.getMetricDetails("B"))
        self.ui.metricC.clicked.connect(lambda: self.getMetricDetails("C"))
        self.ui.metricD.clicked.connect(lambda: self.getMetricDetails("D"))
        self.ui.metricE.clicked.connect(lambda: self.getMetricDetails("E"))
        self.ui.metricF.clicked.connect(lambda: self.getMetricDetails("F"))
        self.ui.metricG.clicked.connect(lambda: self.getMetricDetails("G"))
        self.ui.metricH.clicked.connect(lambda: self.getMetricDetails("H"))
        self.ui.metricI.clicked.connect(lambda: self.getMetricDetails("I"))
        self.ui.metricJ.clicked.connect(lambda: self.getMetricDetails("J"))
        self.ui.metricK.clicked.connect(lambda: self.getMetricDetails("K"))
        self.ui.metricL.clicked.connect(lambda: self.getMetricDetails("L"))
        self.ui.metricM.clicked.connect(lambda: self.getMetricDetails("M"))

    ## show the filename the report is for
    def setUpReportLabel(self, filename):
        self._getFileName(filename)
        self.ui.fileNameText.setText("File loaded: " + self.filename)

    ## fill in summary table
    def fillInSummaryTable(self, data):
        self._getSummaryData(data)
        self._fillTable(self.summary_data, self.ui.summaryTable)

    ## fill in ranking table
    def fillInRankingTable(self, data):
        self._getRankingData(data)
        self._fillTable(self.ranking_data, self.ui.lowestRankTable)

    ## fill in table using dataframe 
    def _fillTable(self, data, table_obj):
        num_rows = len(data.index)
        num_cols = len(data.columns)
        for row in range(num_rows):
            for col in range(num_cols):
                val = data.iloc[row, col]
                table_obj.setItem(row, col, QTableWidgetItem(val))

    ## get the filename of data from its path
    def _getFileName(self, filename):
        filename = filename.replace("\\", "/")
        self.filename = filename.split("/")[-1]

    ## get the summary statistics of the data in dataframe format
    def _getSummaryData(self, data):
        self.summary_data = getSummaryStatisticsFormatted(data)
        self.summary_data_numeric = getSummaryStatistics(data)
    
    ## get the lowest ranking users of the data in dataframe format
    def _getRankingData(self, data):
        self.ranking_data = getStatisticsRanking(data, data.columns.values)

    ## get the binned data for histogram display
    def _getHistogramData(self, data, metric):
        return getHistogramData(data, metric)

    ## display the report window
    def displayWindow(self):
        self.show()

    def openNewFile(self):
        """
        open a new FileWindow to allow user to select new CSV
        then close this window
        this method is called when the File -> Load CSV menu action is selected
        """
        self.parent.openFileWindow()

    def getMetricDetails(self, metric):
        histogram_data = self._getHistogramData(self.data, metric)

        self.parent.openMetricDetailWindow(metric, self.summary_data_numeric, histogram_data)
        
