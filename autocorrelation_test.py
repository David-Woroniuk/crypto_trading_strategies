import pandas as pd 
import statsmodels.api as sm

def autocorrelation_and_partial_test(data_series, lags):
  '''
  This function conducts ACF and PACF tests using the statsmodels package.

  Inputs:   data_series: the data series to be tested (Pandas Series).
            lags: the number of lags to be tested (integer).

  Outputs:  N/A.
  '''
  if isinstance(data_series, pd.Series) is False:
      raise TypeError("data_series argument must be a Pandas Series, data['Series'].")
  
  if isinstance(lags, int) is False:
    raise TypeError("lags argument must be an integer.")

  # print ACF and PACF stats:
  print('*'*100)
  print('Autocorrelation structure:' , sm.graphics.tsa.acf(data_series, nlags = lags))
  print('*'*100)
  print('Partial Autocorrelation structure:' , sm.graphics.tsa.pacf(data_series, nlags = lags))
  print('*'*100)

  # plot ACF and PACF:
  sm.graphics.tsa.plot_acf(data_series, lags = lags).show()
  sm.graphics.tsa.plot_pacf(data_series, lags= lags).show()



autocorrelation_and_partial_test(dataset['Close'], 40)
