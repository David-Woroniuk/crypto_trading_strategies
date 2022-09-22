import pandas as pd
from numpy import log, polyfit, sqrt, std, subtract


def hurst_exponent(data_series: pd.Series, verbose: bool = True):
    """
    This function calculates the hurst exponent. The function firstly checks that the input arguments are of the
    correct type, followed by calculating the tau and poly values for the data_series, after which the outcome is
    printed as the hurst exponent.

    :param data_series: the series of data to be analysed. (pd.Series)
    :param verbose: determines if the status is printed. (bool)
    """
    if not isinstance(data_series, pd.DataFrame):
        raise TypeError("The data_series argument must be a Pandas Series.")

    lags = range(2, 100)
    tau = [sqrt(std(subtract(data_series[lag:], data_series[:-lag]))) for lag in lags]
    poly = polyfit(log(lags), log(tau), 1)
    if verbose:
        print('Hurst Exponent of {} is {}'.format(data_series.columns[0], (poly[0] * 2.0)))

