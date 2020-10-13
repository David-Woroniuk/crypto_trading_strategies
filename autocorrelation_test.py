import statsmodels.api as sm




def autocorrelation_and_partial_test(data, lags):
  '''
  This function conducts ACF and PACF tests using the statsmodels package.

  Inputs:   data: the data series to be tested (Pandas Series).
            lags: the number of lags to be tested (integer).

  Outputs:  N/A.
  '''
  # print ACF and PACF stats:
  print('*'*100)
  print('Autocorrelation structure:' , sm.graphics.tsa.acf(data, nlags = lags))
  print('Partial Autocorrelation structure:' , sm.graphics.tsa.pacf(data, nlags = lags))
  print('*'*100)

  # plot ACF and PACF:
  sm.graphics.tsa.plot_acf(data, lags = lags).show()
  sm.graphics.tsa.plot_pacf(data, lags= lags).show()
