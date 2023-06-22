import os
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QDialog, QMessageBox, QFileDialog
)

from app.data.construct_metrics import Metrics

## get the path to the designer file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DESIGNER_OPEN_FILE = os.path.join(ROOT_DIR,"designer","file_window.ui")

## Display and add functionalities to the OpenFile Dialog window
class FileWindow(QDialog):
    def __init__(self, parent):
        super(FileWindow, self).__init__()

        self.parent = parent
        self.setFixedWidth(400)
        self.setFixedHeight(125)
        self.filename = ''
        self.ui = uic.loadUi(DESIGNER_OPEN_FILE, self)
        self.ui.browseButton.clicked.connect(self.browseFile)
        self.ui.loadFileButton.clicked.connect(self.openReport)

    ## browse csv file using file explorer
    def browseFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.', 'CSV Files (*.csv)')
        self.filename = filename[0]
        self.ui.pathToFileTextbox.setText(self.filename)

    ## open metric report window
    def openReport(self):
        self.loadFile()

        ## trigger GUI parent class to open report window with the loaded file/data
        ## this will close this open file window
        self.parent.openReportWindow(self.filename, self.data)

    ## load csv file 
    def loadFile(self):
        if not self._isValidFile():
            return self.raiseMissingFilenameError()
        metric_constructor = Metrics(self.filename)
        metric_constructor.constructMetricsTable()
        self.data = metric_constructor.get_datatable()

    ## raise error if user enter invalid file
    def raiseMissingFilenameError(self):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Icon.Critical)
        error_msg.setText('Error: Invalid path to file')
        error_msg.setWindowTitle("Error")
        error_msg.exec()
    
    ## check the validity of user-entered filename
    def _isValidFile(self):
        return self.filename and os.path.isfile(self.filename) and self.filename[-4:] == '.csv'
