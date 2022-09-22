import pandas as pd
import statsmodels.api as sm


def autocorrelation_and_partial_test(data_series: pd.Series, lags: int, verbose: bool = True):
    """
    This function creates the autocorrelation and partial autocorrelation tests (ACF / PACF).
    The function firstly checks the input arguments are of the correct type, followed by
    calculating the ACF and PACF, printing the autocorrelation structure if verbose, and
    displaying the plots.

    :param data_series: the series on which to test the ACF and PACF. (pd.Series)
    :param lags: the number of lags to be used. (int)
    :param verbose: determines if the print statements are printed. (bool)
    """
    if not isinstance(data_series, pd.Series):
        raise TypeError("data_series argument must be a Pandas Series, data['Series'].")
    if not isinstance(lags, int):
        raise TypeError("lags argument must be an integer.")

    if verbose:
        print('*' * 100)
        print('Auto Correlation Structure: {}'.format(sm.graphics.tsa.acf(data_series, nlags=lags)))
        print('*' * 100)
        print('Partial Auto Correlation Structure: {}'.format(sm.graphics.tsa.pacf(data_series, nlags=lags)))
        print('*' * 100)

    sm.graphics.tsa.plot_acf(data_series, lags=lags).show()
    sm.graphics.tsa.plot_pacf(data_series, lags=lags).show()


if __name__ == "__main__":
    dataset = pd.DataFrame(
        {
            "ticker": ["A", "B", "C", "D", "E"],
            "mktcap": [100, 400, 399, 120, 30],
            "volatility": [0.3, 0.8, 0.02, 0, 1],
        }
    )
  autocorrelation_and_partial_test(dataset['mktcap'], 40)
