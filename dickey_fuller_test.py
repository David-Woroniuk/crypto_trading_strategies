import pandas as pd
from statsmodels.tsa.stattools import adfuller

def augmented_dickey_fuller(data_series, regression_type, criterion):
  '''
  This function conducts the augmented dickey fuller test.
  Inputs:   data_series: the data series to be tested (Pandas Series).
            regression_type: “c” (constant only),”ct” (constant and trend),”ctt” (constant, linear & quadratic trend),”nc” (no constant or trend).
            criterion: "BIC" or "AIC" - Bayesian or Akaike Information Criteria.

  Prints:   ADF Statistic: test statistic.
            p-value: associated p-value.
            critical values: confidence levels at which to accept or reject null.   
  '''

  if isinstance(data_series, pd.Series) is False:
    raise TypeError("data_series argument must be a Pandas Series, data['Series'].")
  
  if isinstance(regression_type, str) is False:
    raise TypeError("regression_type argument must be a string.")
  while regression_type not in ['c', 'ct', 'ctt', 'nc']:
    raise TypeError("regression_type argument must be equal to 'c', 'ct','ctt' or 'nc'.")

  if isinstance(criterion, str) is False:
    raise TypeError("criterion argument must be a string.")
  while criterion not in ['BIC', 'AIC']:
    raise TypeError("criterion argument must be equal to 'BIC' or 'AIC'.")
  
  # set X as values of input series, input conditions into statsmodels adf test:
  X = data_series.values
  result = adfuller(X, regression = regression_type, autolag = criterion)

  # print outcomes:
  print('*' * 100)
  print('ADF Statistic: %f' % result[0])
  print('p-value: %f' % result[1])
  print('Critical Values:')
  for key, value in result[4].items():
	  print('\t%s: %.3f' % (key, value))
  print('*' * 100)

  # assign critical values to a list:
  values_list = list(result[4].values())
  
  # if the absolute value of the ADF Stat is larger than absolute Critical Value at 1%:
  if abs(result[0]) > abs(values_list[0]):
    print("ADF Statistic Indicates significance at 1%, therefore reject the null hypothesis of unit-root")
  # if the absolute value of the ADF Stat is larger than absolute Critical Value at 5%:
  elif abs(result[0]) > abs(values_list[1]):
    print("ADF Statistic Indicates significance at 5%, therefore reject the null hypothesis of unit-root") 
  # if the absolute value of the ADF Stat is larger than absolute Critical Value at 10%:
  elif abs(result[0]) > abs(values_list[2]):
    print("ADF Statistic Indicates significance at 10%, fail to reject null hypothesis of unit-root") 
  else:
    print("Insignificant, fail to reject null hypothesis of unit root")
  print('*' * 100)



augmented_dickey_fuller(dataset['Open'], 'c','BIC')
