import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


ONE_ARG_FOO = {'get_stock_price', 'calculate_RSI',
               'calculate_MACD', 'plot_stock_price'}


def get_stock_price(ticker: str):
    # stock prices are number, but we want to string for better manipulation
    # further with chatbot and so on...
    # iloc[-1] = most current/last position
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)


# basic calculation function -> simple moving average
def calculate_SMA(ticker, window):
    """
    calculates the rolling average of the closing prices for the specified window size
    and returns the result as a string.
    The rolling average is calculated up to the most recent data point, which represents the latest closing price average.
    The window parameter can be adjusted to change the size of the rolling window and, consequently,
     the length of the rolling average calculation.
    """

    # ticker is a variable that holds the stock symbol you want to retrieve data for.
    # The Ticker object is used to fetch historical data for the given stock symbol.
    # .history(period='1y'): fetches the historical data for the specified stock symbol for 1 year
    # .Close: is a property of the data returned by the history() method ->
    # It represents the stock's closing price at the end of each trading day.
    data = yf.Ticker(ticker).history(period='1y').Close
    # The rolling() method is used to create a rolling window view of the data. This method is applied to a pandas Series or DataFrame
    # The window parameter specifies the size of the rolling window, which determines the number of data points to consider in each window.
    # The mean() method is applied to the rolling window view created in the previous step. It calculates the mean (average) value of each window. In this context, it calculates the rolling average of the closing prices.
    # .iloc[] method is used for integer-location-based indexing in pandas. In this case we retrievig last elem -> [-1]
    return str(data.rolling(window=window).mean().iloc[-1])


# exponential moving average
# https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/ema#:~:text=Exponential%20Moving%20Average%20(EMA)%20is,data%20that%20is%20more%20current.
def calculate_EMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    # .ewm() method calculates the Exponential Moving Average
    # span parameter specifies the span of the EMA window, which controls the "decay" factor of the average
    # it's the equivalent of the window parameter used in .rolling() but behaves differently in terms of smoothing
    #
    return str(data.ewm(span=window, adjust=False).mean().iloc[-1])


# relative strength index
def calculate_RSI(ticker):
    """
    The function is designed to calculate the Relative Strength Index (RSI) for the given stock symbol.
    """
    # fetches the historical closing prices for the specified stock symbol
    # using the yfinance module and stores them in the data variable.
    data = yf.Ticker(ticker).history(period='1y').Close
    #  calculates the differences between consecutive closing prices
    #  to get the price changes over time
    delta = data.diff()
    # creates a new Series, up, which contains only the positive changes (price increases) from the delta Series
    # .clip(lower=0) method sets all negative values in delta to 0
    up = delta.clip(lower=0)
    # creates another new Series, down, which contains only the negative changes (price decreases) from the delta Series
    # .clip(upper=0) method sets all positive values in delta to 0, -1 * is used to invert the sign of the remaining negative values
    down = -1 * delta.clip(upper=0)
    # ewm - exponential movement average of the positive changes (up.ewm),
    # com -> determines the window size,
    # adjust=false -> bias is calculated without bias correction
    ema_up = up.ewm(com=14-1, adjust=False).mean()
    # ewm - exponential movement average of the negative changes (down.ewm),
    ema_down = down.ewm(com=14-1, adjust=False).mean()
    # relative strength positive changes / negative changes
    rs = ema_up / ema_down
    return str(100 - (100 / (1 + rs)).iloc[-1])


def calculate_MACD(ticker):
    """The function is designed to calculate the Moving Average Convergence Divergence (MACD) for the given stock symbol."""
    data = yf.Ticker(ticker).history(period='1y').Close
    short_EMA = data.ewm(span=12, adjust=False).mean()
    long_EMA = data.ewm(span=26, adjust=False).mean()

    # calculates the Moving Average Convergence Divergence (MACD) line:
    MACD = short_EMA - long_EMA
    # calculates the signal line, which is a 9-day EMA of the MACD line.
    signal = MACD.ewm(span=9, adjust=False).mean()
    MACD_histogram = MACD - signal
    return f'{MACD[-1]},  {signal[-1]}, {MACD_histogram[-1]}'


def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    # new figure with a specified size of 10 inches width and 5 inches height
    plt.figure(figsize=(10, 5))
    # plots the historical closing prices on the figure
    # .index = date index of the data Series, which is used as the x-axis
    # .Close represents the closing prices, which are used as the y-axis.
    plt.plot(data.index, data.Close)
    plt.title(f"{ticker} Stock price over last year")
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    # adds gridlines to the plot, making it easier to read and interpret.
    plt.grid(True)
    # aves the plot as an image file named 'stock.png', (saved in cwd)
    plt.savefig('stock.png')
    plt.close()


# to make gpt use those functions we need to define them in a list containing dicts...
# its like a json file... like so:
# (this is what chatgpt gets from us to know what functions, what they do,
# what params they take and from this description decides what to do w them...)
functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given a ticker of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_SMA',
        'description': 'Calculate the simple moving average (SMA) for a given stock ticker and a window',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_EMA',
        'description': 'Calculate the exponential moving average (EMA) for a given stock ticker and a window',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_RSI',
        'description': 'The function is designed to calculate the Relative Strength Index (RSI) for the given stock symbol',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_MACD',
        'description': 'The function is designed to calculate the Moving Average Convergence Divergence (MACD) for the given stock symbol. takes ticker as parameter',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'plot_stock_price',
        'description': 'fetches the historical closing prices for a given stock symbol (ticker) using the yfinance module, plots the stock price over the last year using matplotlib.pyplot, adds labels, title, and gridlines to the plot, and then saves the plot as an image file named \'stock.png\' in the current working directory.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'
                }
            },
            'required': ['ticker']
        }
    }
]

# functions dictionary str:function
available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'calculate_RSI': calculate_RSI,
    'calculate_MACD': calculate_MACD,
    'plot_stock_price': plot_stock_price,
}
