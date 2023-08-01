import pandas as pd


def foo():
    data = {
        'SSN': [1, 2, 3, 4],
        'Name': ['Anna', 'Bob', 'John', 'Mike'],
        'Age': [29, 46, 57, 11],
        'Height': [176, 166, 200, 198],
        'Gender': ['f', 'm', 'm', 'm']
    }

    df = pd.DataFrame(data)
    df.set_index('SSN', inplace=True)

    print(df.count())  # result per column
    print(df['Age'].count())  # count of specific column

    print(df['Age'].sum())  # count of specific column
    print(df.sum())

    print(df['Age'].product())

    print("Mean: ", df['Height'].mean())  # sum / count
    print("Median: ", df['Height'].median())  # middle one
    print("most occurred: \n", df['Height'].mode())  # most occurred number
    print("Deviation: ", df['Height'].std())  # how much on average the values deviate from mean
    print("Min, max: ", df['Height'].min(), df.Height.max())
    print(df.describe())

    return


if __name__ == '__main__':
    foo()
