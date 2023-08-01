import pandas as pd
import numpy as np


def foo():
    data = {
        'SSN': [1, 2, 3, 4],
        'Name': ['Anna', 'Bob', 'John', 'John'],
        'Age': [29, 29, 57, 11],
        'Height': [176, 166, 200, 198],
        'Gender': ['f', 'm', 'm', 'm']
    }
    df = pd.DataFrame(data)
    df.set_index('SSN', inplace=True)

    print(df.Height.apply(lambda x: x * 100))

    # for x in df: print(x)
    # for x in df['Age']: print(x)

    # for key, value in df.Age.itertuples():
    #     print("{}: {}".format(key, value))

    for row in df.iterrows():
        print(row)

    df.sort_index(inplace=True)
    print(df)

    df.sort_values(by=['Name', 'Age'], inplace=True)
    print(df)

    df.sort_values(by=['Age', 'Name'], inplace=True)
    print(df)

    return


if __name__ == '__main__':
    foo()
