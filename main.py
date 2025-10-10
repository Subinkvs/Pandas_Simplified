import pandas as pd

# ------------------------------------------------------------
# 1️⃣ Create DataFrame
# ------------------------------------------------------------
data = {
    'Name': ['Karan', 'Meera', 'David', 'Karan'],
    'Age': [19, None, 21, 28]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df, "\n")

# ------------------------------------------------------------
# 2️⃣ Add a new column
# ------------------------------------------------------------
df['Marks'] = [95, 76, 89, 82]
print("After adding 'Marks' column:")
print(df, "\n")

# ------------------------------------------------------------
# 3️⃣ Count the number of missing values per column
# ------------------------------------------------------------
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# ------------------------------------------------------------
# 4️⃣ Modify a specific cell value
# ------------------------------------------------------------
df.loc[2, 'Name'] = 'Sonu'
print("After changing Name in 3rd row (index 2) to 'Sonu':")
print(df, "\n")

# ------------------------------------------------------------
# 5️⃣ Add new rows to DataFrame
# ------------------------------------------------------------
new_rows = pd.DataFrame([
    {'Name': 'Kumar', 'Age': 20, 'Marks': 90},
    {'Name': 'Rahul', 'Age': 26, 'Marks': 85}
])
df = pd.concat([df, new_rows], ignore_index=True)
print("After adding new rows:")
print(df, "\n")

# ------------------------------------------------------------
# 6️⃣ Access specific columns
# ------------------------------------------------------------
print("Accessing 'Name' and 'Marks' columns:")
print(df[['Name', 'Marks']], "\n")

# ------------------------------------------------------------
# 7️⃣ Access Name and Marks of a specific row (index 0)
# ------------------------------------------------------------
print("Accessing Name and Marks of row index 0:")
print(df.loc[0, ['Name', 'Marks']], "\n")

# ------------------------------------------------------------
# 8️⃣ Access Name and Marks using slicing (rows 0 to 3)
# ------------------------------------------------------------
print("Accessing Name and Marks from rows 0 to 3:")
print(df.loc[0:3, ['Name', 'Marks']], "\n")

# ------------------------------------------------------------
# 9️⃣ Access specific rows and columns using iloc
# ------------------------------------------------------------
print("Accessing specific rows and columns using iloc (rows 0,2 | columns 0,1):")
print(df.iloc[0:3:2, 0:2], "\n")

# ------------------------------------------------------------
# 🔟 Aggregate functions on numeric column
# ------------------------------------------------------------
print("Aggregate Functions on 'Age' column:")
print("Mean Age  :", df['Age'].mean())
print("Min Age   :", df['Age'].min())
print("Max Age   :", df['Age'].max())
print("Count Age :", df['Age'].count(), "\n")

# ------------------------------------------------------------
# 1️⃣1️⃣ Grouping by 'Name' and computing mean of 'Age'
# ------------------------------------------------------------
print("Mean Age for each Name (GroupBy):")
group = df.groupby('Name')
print(group['Age'].mean())
