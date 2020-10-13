def dickey_fuller(series, regression_type, criterion):
  '''
  This function conducts the augmented dickey fuller test.

  Inputs:   series: This can be a Pandas DataFrame column, or Pandas Series to be tested.
            regression_type: “c” (constant only),”ct” (constant and trend),”ctt” (constant, linear & quadratic trend),”nc” (no constant or trend).
            criterion: "BIC" or "AIC" - Bayesian or Akaike Information Criteria.

  Prints:   ADF Statistic: test statistic.
            p-value: associated p-value.
            critical values: confidence levels at which to accept or reject null.
            
  Outputs:  result[0]: ADF Statistic.
            values_list: Critical Values at the 1%, 5% and 10% values.
  '''

  # set X as values of input series, input conditions into statsmodels adf test:
  X = series.values
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

  return result[0], values_list
