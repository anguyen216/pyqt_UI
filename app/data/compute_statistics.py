"""
helper file containing computation methods for the summary statistics
and rankings to support display in charts/tables
"""

import numpy as np
import pandas as pd 

def getSummaryStatistics(data):
    """
    compute median, mean, 25%, 75%, and stdev of each metric in the data
    returns values as numerics
    """
    summary = data.describe().T
    data_max = summary['max'].values
    data_min = summary['min'].values
    data_median = summary['50%'].values
    percentile25 = summary['25%'].values
    percentile75 = summary['75%'].values
    sd = summary['std'].values
    data_mean = summary['mean'].values
    index_val = summary.index.values
    d = {'Median': data_median, '25th': percentile25, 'Mean': data_mean,
         '75th': percentile75, 'Stdev': sd, 'Min': data_min, 'Max': data_max}
    report = pd.DataFrame(data=d, index=index_val)
    return report

def getSummaryStatisticsFormatted(data):
    """
    compute median, mean, 25%, 75%, and stdev of each metric in the data
    returns values as formatted strings
    """
    summary = data.describe().T
    data_max = summary['max'].map('{:,.2f}'.format).values
    data_min = summary['min'].map('{:,.2f}'.format).values
    data_median = summary['50%'].map('{:,.2f}'.format).values
    percentile25 = summary['25%'].map('{:,.2f}'.format).values
    percentile75 = summary['75%'].map('{:,.2f}'.format).values
    sd = summary['std'].map('{:,.2f}'.format).values
    data_mean = summary['mean'].map('{:,.2f}'.format).values
    index_val = summary.index.values
    d = {'Median': data_median, '25th': percentile25, 'Mean': data_mean,
         '75th': percentile75, 'Stdev': sd, 'Min': data_min, 'Max': data_max}
    report = pd.DataFrame(data=d, index=index_val)
    return report

def getStatisticsRanking(data, metrics):
    """
    get the bottom 5 lowest ranked github users for each metric in the data
    """
    ranking = []
    cols = ['1st', '2nd', '3rd', '4th', '5th']
    for metric in metrics[1:]:
        bottom5 = data.nsmallest(5, metric)[metrics[0]].values
        ranking.append(bottom5)
    result = pd.DataFrame(data=ranking, index=metrics[1:], columns=cols)
    return result

def getHistogramData(data, metric):
    """
    get the data that will go into the histogram display for the given metric
    
    note: the work for generating the histogram is being done
    in app.gui.metric_detail_window.MetricDetailWindow
    """
    histogram_data = data.loc[:,metric]
    return histogram_data
