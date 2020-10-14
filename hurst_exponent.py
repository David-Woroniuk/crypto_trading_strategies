import pandas as pd
from numpy.random import randn
from numpy import cumsum, log, polyfit, sqrt, std, subtract


def hurst_exponent(data_series):
  '''
  This function calculates the hurst exponent.
  
  Inputs:   data_series: the Pandas Series to be tested (Series).

  Outputs:  N/A.
  '''
  if isinstance(data_series, pd.DataFrame) is False:
    raise TypeError("data_series argument must be a Pandas Series, data[['Series']].")
    
  lags = range(2, 100)
  tau = [sqrt(std(subtract(data_series[lag:], data_series[:-lag]))) for lag in lags]
  poly = polyfit(log(lags), log(tau), 1)

  print('Hurst Exponent of {} is {}'.format(data_series.columns[0], (poly[0]*2.0)))



hurst_exponent(dataset[['Open']])
