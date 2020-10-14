from scipy.stats import shapiro, normaltest, anderson
import pandas as pd


def shapiro_wilks_test(data, confidence_level):
  '''
  This function conducts the shapiro wilks test.

  Inputs:   data: the DataFrame Column or Pandas Series to be tested (DataFrame Column or Series).
            confidence_level: the p-value threshold level (float).

  Outputs:  N/A.
  '''
  if isinstance(data, pd.Series) is False:
    raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")
  
  if isinstance(confidence_level, float) is False:
    raise TypeError("confidence_level argument must be a float.")
  while confidence_level not in [0.01, 0.05, 0.1]:
    raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

  stat, p_val = shapiro(data)
  print('*'* 100)
  print('Statistic: %.3f, p val: %.3f' % (stat, p_val))

  if p_val > confidence_level:
    print('Sample appears to be Gaussian, fail to reject null hypothesis')
  elif p_val <= confidence_level:
    print('Sample does not appear Gaussian, reject null hypothesis')
  print('*'*100)
  
  
  
  
def dagostino_ksquared_test(data, confidence_level):
  '''
  This function conducts D'agostino's K squared test.

  Inputs:   data: the Dataframe Column or Pandas Series to be tested (DataFrame or Series).
            confidence_level: the p-value threshold level (float).

  Outputs:  N/A.
  '''
  if isinstance(data, pd.Series) is False:
    raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")
  
  if isinstance(confidence_level, float) is False:
    raise TypeError("confidence_level argument must be a float.")
  while confidence_level not in [0.01, 0.05, 0.1]:
    raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

  stat, p_val = normaltest(data)
  print('*'* 100)
  print('Statistic: %.3f, p val: %.3f' % (stat, p_val))

  if p_val > confidence_level:
    print('Sample appears to be Gaussian, fail to reject null hypothesis')
  elif p_val <= confidence_level:
    print('Sample does not appear Gaussian, reject null hypothesis')
  print('*'*100)
  
  
  
  
def anderson_darling_test(data, confidence_level):
  '''
  This function conducts anderson darling test.

  Inputs:   data: the Dataframe Column or Pandas Series to be tested (DataFrame or Series).
            confidence_level: the p-value threshold level (float).
  Outputs:  N/A.
  '''
  if isinstance(data, pd.Series) is False:
    raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")
  
  if isinstance(confidence_level, float) is False:
    raise TypeError("confidence_level argument must be a float.")
  while confidence_level not in [0.01, 0.05, 0.1]:
    raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

  result = anderson(data)
  print('*'*100)
  print('Statistic: %.3f' % result.statistic)
  p = 0
  for i in range(len(result.critical_values)):
	  sl, cv = result.significance_level[i], result.critical_values[i]
	  if result.statistic < result.critical_values[i]:
		  print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	  else:
		  print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
  print('*'*100)




shapiro_wilks_test(dataset['Close'], 0.1)
dagostino_ksquared_test(dataset['Close'], 0.05)
anderson_darling_test(dataset['Close'], 0.01)
