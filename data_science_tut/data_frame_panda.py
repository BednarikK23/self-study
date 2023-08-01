import pandas as pd
import matplotlib.pyplot as plt

# data frames are main in pandas, they look like a sql a bit,
# made from rows and columns

def foo():
    data = {
        'SSN': [1, 2, 3, 4],
        'Name': ['Anna', 'Bob', 'John', 'Mike'],
        'Age': [29, 46, 57, 11],
        'Height': [176, 166, 200, 198],
        'Gender': ['f', 'm', 'm', 'm']
    }

    df = pd.DataFrame(data)
    #  we can set indexing - the first table column with this:
    df.set_index('SSN', inplace=True)  # inplace so the changes would apply asap
    print(df)

    print(df.tail(2), df.head(1), df.shape, df.ndim, sep="\n")  # dim=dimension
    print(df.dtypes)
    print(df.T)  # Transpose -> switched columns and rows
    # iloc - is nice iterator makes indexing objects very easy, or we have to
    # index by the indexing we defined (now - ssn)
    print(df['Name'][1], df['Name'].iloc[1])  # see the diff
    print(df.iloc[0:2])

    # pandas are smart and on default will show us all values/graphs w numbers
    df.hist()  # histagram, we could do plot() as well, df.plot.bar()
    plt.show()
    plt.close()
    df.Age.plot()
    plt.show()


if __name__ == '__main__':
    foo()
