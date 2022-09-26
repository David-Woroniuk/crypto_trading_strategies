from scipy.stats import shapiro, normaltest, anderson
import pandas as pd


def shapiro_wilks_test(data: pd.Series, confidence_level: (float, int), verbose: bool = True):
    """
    This function calculates the Shapiro Wilks test. The function firstly checks that
    the input arguments are of the correct type, followed by checking that the confidence
    level is an accepted argument for the Shapiro Wilks test. Following this, the Shapiro
    Wilks test is calculated with an associated p-value, where the p-value is then presented
    and tested against the confidence level passed as an input argument.

    :param data: the Pandas Series to be assessed. (pd.Series)
    :param confidence_level: the confidence level threshold against which to analyse the Shapiro Wilks test. (float)
    :param verbose: determines if the status is printed. (bool)
    """
    if not isinstance(data, pd.Series):
        raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")

    if not isinstance(confidence_level, float):
        raise TypeError("confidence_level argument must be a float.")
    if confidence_level not in [0.01, 0.05, 0.1]:
        raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

    stat, p_val = shapiro(data)
    if verbose:
        print('*' * 100)
        print('Statistic: %.3f, p val: %.3f' % (stat, p_val))
        print('*' * 100)

    print('*' * 100)
    if p_val > confidence_level:
        print('Sample appears to be Gaussian, fail to reject null hypothesis')
    elif p_val <= confidence_level:
        print('Sample does not appear Gaussian, reject null hypothesis')
    print('*' * 100)


def dagostino_ksquared_test(data: pd.Series, confidence_level: float, verbose: bool = True):
    """
    This function calculates the Dagostino K Squared test. The function firstly checks that
    the input arguments are of the correct type, followed by checking that the confidence
    level is an accepted argument for the Dagostino K Squared test. Following this, the Dagostino K Squared
    test is calculated with an associated p-value, where the p-value is then presented
    and tested against the confidence level passed as an input argument.

    :param data: the Pandas Series to be assessed. (pd.Series)
    :param confidence_level: the confidence level threshold against which to analyse the Shapiro Wilks test. (float)
    :param verbose: determines if the status is printed. (bool)
    """
    if not isinstance(data, pd.Series):
        raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")
    if not isinstance(confidence_level, float):
        raise TypeError("confidence_level argument must be a float.")
    if confidence_level not in [0.01, 0.05, 0.1]:
        raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

    stat, p_val = normaltest(data)
    if verbose:
        print('*' * 100)
        print('Statistic: %.3f, p val: %.3f' % (stat, p_val))
        print('*' * 100)

    print('*' * 100)
    if p_val > confidence_level:
        print('Sample appears to be Gaussian, fail to reject null hypothesis')
    elif p_val <= confidence_level:
        print('Sample does not appear Gaussian, reject null hypothesis')
    print('*' * 100)


def anderson_darling_test(data: pd.Series, confidence_level: float, verbose: bool = True):
    """
    This function calculates the Anderson Darling test. The function firstly checks that
    the input arguments are of the correct type, followed by checking that the confidence
    level is an accepted argument for the Andeerson Darling test. Following this, the Anderson Darling
    test is calculated with an associated p-value, where the p-value is then presented
    and tested against the confidence level passed as an input argument.

    :param data: the Pandas Series to be assessed. (pd.Series)
    :param confidence_level: the confidence level threshold against which to analyse the Shapiro Wilks test. (float)
    :param verbose: determines if the status is printed. (bool)
    """
    if not isinstance(data, pd.Series):
        raise TypeError("data argument must be a Pandas Series or DataFrame Column, data['Series'].")
    if not isinstance(confidence_level, float):
        raise TypeError("confidence_level argument must be a float.")
    if confidence_level not in [0.01, 0.05, 0.1]:
        raise TypeError("confidence_level argument must be equal to 0.01 (1%), 0.05 (5%) or 0.1 (10%).")

    result = anderson(data)
    if verbose:
      print('*' * 100)
      print('Statistic: %.3f' % result.statistic)
      print('*' * 100)

    p = 0
    print('*' * 100)
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
    print('*' * 100)


if __name__ == "__main__":
    dataset = pd.DataFrame(
        {
            "ticker": ["A", "B", "C", "D", "E"],
            "mktcap": [100, 400, 399, 120, 30],
            "volatility": [0.3, 0.8, 0.02, 0, 1],
        }
    )
    shapiro_wilks_test(dataset['mktcap'], 0.1)
    dagostino_ksquared_test(dataset['mktcap'], 0.05)
    anderson_darling_test(dataset['mktcap'], 0.01)
