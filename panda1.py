#  Data analysis  lifecycle - Collect → Clean → Analyze → Visualize → Report.

"""
Series Example in Pandas

Definition:
-----------
A Pandas Series is a one-dimensional labeled array that can hold any data type 
(such as integers, strings, floats, Python objects, etc.). It is similar to a 
column in a spreadsheet or a single column in a DataFrame. Each element in a 
Series has an associated index label, which can be either the default integer 
index or custom labels provided by the user.

This script demonstrates:
1. How to create a Pandas Series from a list and a dictionary.
2. How to filter and access Series elements.
3. The difference between loc[] (label-based indexing) and iloc[] (position-based indexing).
"""

# Import the pandas library
import pandas as pd

# -----------------------------------------------------
# 1. Creating a Series from a Python list
# -----------------------------------------------------

# Define a list of numerical data
data = [1, 3, 4, 4, 5]

# Convert the list into a Pandas Series
# If no custom index is provided, pandas will assign a default integer index (0, 1, 2, ...)
series = pd.Series(data, index=[101, 102, 103, 104, 105])

# Display the Series
print("Series created from a list:")
print(series)

# -----------------------------------------------------
# 2. Filtering and accessing elements in a Series
# -----------------------------------------------------

# Filter elements greater than 4 using a conditional expression
# print("\nElements greater than 4:")
print(series[series > 4])


# Access an element using loc[] (label-based indexing)
# Here, the label is the default integer index
print("\nElement at index label 1 using loc:")
print(series.loc[104])

# Access an element using iloc[] (position-based indexing)
print("\nElement at position 1 using iloc:")
print(series.iloc[1])

# -----------------------------------------------------
# 3. Creating a Series from a dictionary
# -----------------------------------------------------

# Define a dictionary with days of the week
weeks = {
    "Day 1": "Monday",
    "Day 2": "Tuesday",
    "Day 3": "Wednesday",
    "Day 4": "Thursday",
    "Day 5": "Friday",
    "Day 6": "Saturday",
    "Day 7": "Sunday"
}

# Convert the dictionary into a Series
# Dictionary keys become index labels and dictionary values become data
day_series = pd.Series(weeks)

# Display the Series
print("\nSeries created from a dictionary:")
print(day_series)

# Access the first element using iloc[] (position-based indexing)
print("\nFirst element using iloc:")
print(day_series.iloc[0])


"""
📊 Demonstration of creating a Pandas DataFrame from a Python dictionary.

A **DataFrame** is a two-dimensional, tabular data structure in Pandas 
with labeled rows and columns — similar to a table in a database or an Excel sheet.

- Each column in a DataFrame is a pandas Series.
- DataFrames are mutable (we can modify data after creation).
- They are widely used for data cleaning, analysis, and visualization.
"""

# 📦 Import the pandas library
import pandas as pd

# -----------------------------------------------------
# 1️⃣ Define a dictionary containing data
# -----------------------------------------------------
# - Keys represent column names
# - Values are lists representing column data
dataset = {
    'name': ['John', 'Rahul', 'Arun'],  # Column 1: Names of people
    'age': [29, 34, 32]                 # Column 2: Corresponding ages
}

# -----------------------------------------------------
# 2️⃣ Convert the dictionary into a Pandas DataFrame
# -----------------------------------------------------
# - Each key becomes a column header
# - Each list element becomes a row under that column
df = pd.DataFrame(dataset)

# -----------------------------------------------------
# 3️⃣ Display the resulting DataFrame
# -----------------------------------------------------
# - Shows tabular data with row index (0,1,2 by default)
# - Columns: 'name' and 'age'
print(df)
print(df.loc[1])


import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, None, 30, 28],
    "City": ["New York", "London", None, "Paris"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Drop rows with any NaN
clean_df = df.dropna()
print("\nAfter dropna():")
print(clean_df)

