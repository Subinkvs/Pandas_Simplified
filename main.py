import pandas as pd

# To Add a new column
data = {
    'Name': ['Karan', 'Meera', 'David', 'Anita'],
    'Age': [21, 23, 26, 22],
    'City': ['Bangalore', 'Pune', 'Hyderabad', 'Kolkata']
}

df = pd.DataFrame(data)

# To add a new column


df['Marks'] = [95, 76, 89, 82]

# Change the Name in the 3rd row (index 2) to 'Sonu'
df['Name'][2] = 'Sonu'

df.loc[2, 'Name'] = 'Sonu'

print(df)


# Count the number of missing values per column

data = {
    'Name': ['Karan', 'Meera', 'David', None],
    'Age': [19, None, 21, 28]
}

df = pd.DataFrame(data)
print(df.isnull().sum())