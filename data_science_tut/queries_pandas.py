import pandas as pd


def foo():
    df = pd.read_csv('people.csv', delimiter=',')
    df.set_index('SSN', inplace=True)
    print(df)

    # loc - location
    # from df select * where age >= 45
    print(df.loc[(df['Age'] >= 45)])

    # u can add ifs
    print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)])

    # u can also add what columns u want target...
    print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)]['Name'])

    return


if __name__ == '__main__':
    foo()
