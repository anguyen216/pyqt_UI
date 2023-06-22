import os
import sys

# matplotlib code in this class referenced from 
# https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import uic
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QDialog
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

## get the path to the designer file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DESIGNER_OPEN_FILE = os.path.join(ROOT_DIR,"designer","metric_detail_window.ui")

# dictionary containing metric ID to description
METRIC_DESCRIPTIONS = {
    "lifespan": "Days of Github experience before class.",
    "A": "The number of private and public commits made by this user.",
    "B": "The number of comments made by this user in commits, issues, and pull request discussions.",
    "C": "The number of PR and PR reviews made by this user.",
    "D": "The number of issues, and projects created by this user.",
    "E": "The number of different languages used in user's type I repositories.",
    "F": "The size of code written in Github popular languages in user's type I repositories.",
    "G": "The number of different languages used in user's type II repositories.",
    "H": "The size of code written in Github popular languages in user's type II repositories.",
    "I": "The total number of type I, and type II repositories.",
    "J": "The total number of forks, stars, and watchers in type I repositories.",
    "K": "The total number of forks, stars, and watchers in type II repositories.",
    "L": "The total code size of type I repositories.",
    "M": "The total code size of type II repositories."
}

class MetricDetailWindow(QDialog):
    """
    QDialog based class for displaying Metric Detail Window.
    Contains two tabs for showing boxplot and histogram of provided
    metric and associated data
    """

    def __init__(self, parent, metric, summary_data, histogram_data):
        """
        initialize the metric detail window by setting metric label and description,
        and building matplotlib based boxplot and histogram visualizations
        """

        super(MetricDetailWindow, self).__init__()

        self.parent = parent
        self.metric = metric
        self.summary_data = summary_data
        self.histogram_data = histogram_data
        self.ui = uic.loadUi(DESIGNER_OPEN_FILE, self)

        self.setWindowLabel(metric)
        self.setWindowDescription(metric)
        self.initialzeBoxplot()
        self.initializeHistogram()


    def setWindowLabel(self, metric):
        """
        set window label based on input metric.
        if metric is 'lifespan' show label as 'Days'
        """

        if metric == 'lifespan':
            metric_label = 'Days'
        else:
            metric_label = metric

        self.ui.label_metric_name.setText("Metric: " + metric_label)

    def setWindowDescription(self, metric):
        """
        set window description based on the given metric
        from static dictionary METRIC_DESCRIPTIONS in this class
        """

        metric_description = METRIC_DESCRIPTIONS[metric]
        self.ui.label_metric_desc.setText(metric_description)


    def initialzeBoxplot(self):
        """
        Create a matplotlib-based boxplot widget
        constructed with this object's given metric/summary data
        """

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # get summary data row for our metric
        metric_summary_data = self.summary_data.loc[self.metric]

        # @see app.data.compute_statitics.getSummaryStatistics()
        # to see where this data comes from
        boxplot_data = [{
                            'label': "",
                            'whislo': float(metric_summary_data['Min']), 
                            'q1': float(metric_summary_data['25th']), 
                            'med': float(metric_summary_data['Median']), 
                            'q3': float(metric_summary_data['75th']), 
                            'whishi': float(metric_summary_data['Max']), 
                            'fliers': []
                        }]

        sc.axes.bxp(boxplot_data, showfliers=False)    
        self.ui.layout_boxplot.addWidget(sc)

    def initializeHistogram(self):
        """
        Create a matplotlib-based histogram widget
        constructed with this object's given metric/summary data
        """

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        sc.axes.hist(self.histogram_data)    
        self.ui.layout_histogram.addWidget(sc)

    ## display the report window
    def displayWindow(self):
        self.show()


class MplCanvas(FigureCanvasQTAgg):
    """
    matplotlib figure canvas:
    histogram/boxplot visuals are injected into the axes parameter of this object
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
