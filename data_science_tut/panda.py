import pandas as pd
import matplotlib.pyplot as plt  # to show

# https://pandas.pydata.org/docs/user_guide/dsintro.html#series


def mysquare(x):
    return x ** 2


# pandas are created on top of matplotlib and numpy,
# we will use it to create plots but to show we still gonna use matplotlib

# Series is a one-dimensional labeled array capable of holding any data type

if __name__ == '__main__':
    # series: dictionary like - key/value pairs
    #                   values              keys
    series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])
    series.name = "My series"
    print(series, "\n", series['D'])

    s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    s2 = pd.Series([7, 5, 1, 2, 3], ['c', 'b', 'a', 'd', 'G'])

    # agian pandas are for science, so it will not merge dicts but add value
    print(s1 + s2)
    print(s1.head(2))  # first two rows
    print(s1.tail(3))  # first three rows
    print(s1.get('a', 0))  # same as in dicts, very useful

    print(s1.apply(mysquare))

    # s1.plot()
    # s1.plot.bar()
    s1.plot.pie()
    plt.show()
