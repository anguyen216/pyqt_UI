import pandas as pd
import os
import pytest
import numpy as np
import pytest
from app.gui.file_window import FileWindow
from app.data.compute_statistics import getSummaryStatistics, getHistogramData
from app.data.construct_metrics import Metrics

@pytest.fixture
def file_window(qtbot):
# Create a FileWindow instance for testing and show it
    file_window = FileWindow(None)
    file_window.show()
# Test that the browseFile method opens the file dialog
    with qtbot.waitSignal(file_window.ui.pathToFileTextbox.textChanged):
        file_window.browseFile()
        assert file_window.filename != ''

# Test that the loadFile method loads the file correctly
    file_window.loadFile()
    assert file_window.data is not None
    qtbot.addWidget(file_window)
    return file_window
    

def test_is_valid_file(qtbot, file_window, monkeypatch):
    # Test if the file is valid
    filename = "CSV Files (*.csv)"
    file_window.filename = filename
    def mock_return(*args, **kwargs):
        return True
    monkeypatch.setattr(os.path, "isfile", mock_return)
   

def test_invalid_file(qtbot, file_window, monkeypatch):
    # Test if the file is invalid
    filename = "TXT Files (*.txt)"
    file_window.filename = filename
    def mock_return(*args, **kwargs):
        return False
    monkeypatch.setattr(os.path, "isfile", mock_return)
   


# Create some test data
data = pd.DataFrame({
    'metric1': np.random.rand(100),
    'metric2': np.random.rand(100),
    'metric3': np.random.rand(100),
})

def test_getSummaryStatistics():
    # Test that the function returns a DataFrame
    result = getSummaryStatistics(data)
    assert isinstance(result, pd.DataFrame)

    # Test that the DataFrame has the expected columns
    expected_columns = ['Median', '25th', 'Mean', '75th', 'Stdev', 'Min', 'Max']
    assert result.columns.tolist() == expected_columns

    # Test that the DataFrame has the expected index
    expected_index = data.columns.tolist()
    assert result.index.tolist() == expected_index



def test_getHistogramData():
    # Test that the function returns a Series
    metric = data.columns[0]
    result = getHistogramData(data, metric)
    assert isinstance(result, pd.Series)

    # Test that the Series has the expected length
    expected_length = len(data)
    assert len(result) == expected_length

    # Test that the values are numeric
    assert result.dtype == 'float64'

# Fixture for Metrics object
@pytest.fixture(scope='module')
def metrics_obj():
    # Load test data
    path_to_test_data = os.path.join(os.getcwd(), 'tests', 'F2020.csv')
    # Create a Metrics object
    return Metrics(path_to_test_data)

# Test for constructMetricsTable method
def test_constructMetricsTable(metrics_obj):
    # Test the output of the method
    metrics_obj.constructMetricsTable()
    df = metrics_obj.get_datatable()
    assert 'lifespan' in df.columns
    assert 'A' in df.columns
    assert 'B' in df.columns
    assert 'C' in df.columns
    assert 'D' in df.columns
    assert 'E' in df.columns
    assert 'F' in df.columns
    assert 'G' in df.columns
    assert 'H' in df.columns
    assert 'I' in df.columns
    assert 'J' in df.columns
    assert 'K' in df.columns
    assert 'L' in df.columns
    assert 'M' in df.columns
    assert df.shape == (52, 15)
