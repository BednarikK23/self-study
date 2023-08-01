import pandas as pd

names = {
    'SSN': [2, 5, 7, 8],
    'Name': ['Anna', 'Bob', 'John', 'Mike']
}

# have to have same index column or key column where we will join...
ages = {
    'SSN': [1, 2, 3, 5],
    'Age': [58, 34, 45, 62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

# so first of all we give two frames that we wanna merge asi parameters,
# then we also have to specify where and how to merge those frames...
# in this case we have same column with SocialSecurityNumbers...
# how: if the data that are not present in both will disaper, or from ne frame
# will stay from other vanish or stay from both and create free spaces in frame
# and so on: https://pandas.pydata.org/docs/user_guide/merging.html
# basic joins:
# left, -> only from left frame and where missing values set to NaN
# right -> only from right frame and where missing values set to NaN
# inner -> only where match, where rows overlap
# outer -> full, fill up wit NaN
df = pd.merge(df1, df2, on='SSN', how="outer")
df.set_index('SSN', inplace=True)

print(df)
