import pandas as pd
from statsmodels.tsa.stattools import adfuller


def augmented_dickey_fuller(data_series: pd.Series, regression_type: str, criterion: str, verbose: bool = True):
    """
    This function creates the augmented dickey fuller test. The function firstly checks that the input arguments are
    of the correct type, followed by checking that the input arguments are accepted arguments. If verbose, the ADF
    statistics are printed, with the associated p-value also printed, with confirmation against the critical values
    printed.

    :param data_series: the pd.Series of data to be analysed. (pd.Series)
    :param regression_type: the type of regression to be used. (str)
    :param criterion: the criteria of the regression to be used. (str)
    :param verbose: determines if the print statements are printed. (bool)
    """
    if not isinstance(data_series, pd.Series):
        raise TypeError("data_series argument must be a Pandas Series.")
    if not all(isinstance(v, str) for v in [regression_type, criterion]):
        raise TypeError("The 'regression_type' and 'criterion' arguments must be string types.")
    if regression_type not in ['c', 'ct', 'ctt', 'nc']:
        raise TypeError("regression_type argument must be equal to 'c', 'ct','ctt' or 'nc'.")
    if criterion not in ['BIC', 'AIC']:
        raise TypeError("criterion argument must be equal to 'BIC' or 'AIC'.")

    X = data_series.values
    result = adfuller(X, regression=regression_type, autolag=criterion)

    if verbose:
        print('*' * 100)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))
    print('*' * 100)

    # Critical Values:
    values_list = list(result[4].values())

    # If the absolute value of the ADF Stat is larger than absolute Critical Value at 1%:
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


if __name__ == "__main__":
    dataset = pd.DataFrame(
        {
            "ticker": ["A", "B", "C", "D", "E"],
            "mktcap": [100, 400, 399, 120, 30],
            "volatility": [0.3, 0.8, 0.02, 0, 1],
        }
    )
    augmented_dickey_fuller(dataset['mktcap'], 'c', 'BIC')
