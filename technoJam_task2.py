# *NOTE* -> Uncomment any print() function to view its output

# importing required libraries
import pandas as pd

df = pd.read_csv("data.csv")

# print(df.shape)

df.head()

# Printing unique values in rows
# print(df.iloc[0, :].unique())
# print(df.iloc[1, :].unique())
# print(df.iloc[2, :].unique())

# Dropping first three rows
df.drop([0, 1, 2], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
# print(df)

# Dropping values in plain years
df.drop(df.columns[1::3], axis=1, inplace=True)
# print(df.head(3)) # printing first 3 columns only

# Printing columns containing the average value
for i in range(1, 85):
    df.iloc[:, i] = df.iloc[:, i].str.split(expand=True)[0]
# print(df.head())

# Converting a wide dataframe into a narrow one
small_dataframe = df.melt(id_vars=['Unnamed: 0'], value_name='obesity_rate')
# print(small_dataframe.head())

# Splitting variable column into 'year' and 'gender'
small_dataframe[['Year', 'Gender']] = small_dataframe.iloc[:, 1].str.split('.', expand=True)
# print(small_dataframe.head())

small_dataframe.drop('variable', axis=1, inplace=True) # removing variable column

Gender = {'1': 'male', '2': 'female'} # changing gender identifiers
small_dataframe.Gender.replace(Gender, inplace=True)

small_dataframe.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)
small_dataframe.rename(columns={'obesity_rate': 'Obesity_Rate'}, inplace=True)
# print(small_dataframe.head())

# print(small_dataframe.shape)
# print(small_dataframe.isna().sum())
# print(small_dataframe.dtypes)

# Changing datatype of 'Obesity_Rate' column to a float
country_name_array = small_dataframe[small_dataframe.Obesity_Rate == 'No']['Country'].unique()
# print(country_name_array)

omit = small_dataframe[small_dataframe.Obesity_Rate == 'No']['Country'].unique()
small_dataframe[small_dataframe.Country.isin(omit)]['Obesity_Rate'].unique()
small_dataframe = small_dataframe[~small_dataframe.Country.isin(omit)]

small_dataframe = small_dataframe.astype({'Obesity_Rate': 'float32'})
# print(small_dataframe.dtypes)

# Printing cleaned dataframe
print(small_dataframe)

# Printing entire dataset
# print(df)
