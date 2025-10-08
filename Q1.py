# -----------------------------------------------------
# 1️⃣ Series from a list with filtering
# -----------------------------------------------------
# Task:
# - Create a Series from the list [10, 20, 30, 40, 50]
# - Use loc[] to access the element with index 3
# - Use iloc[] to access the second element
# - Filter and print elements greater than 25

# -----------------------------------------------------
# 2️⃣ Series from a dictionary
# -----------------------------------------------------
# Task:
# - Create a Series from the dictionary: {"A": 5, "B": 15, "C": 25, "D": 35}
# - Access the value of key "B" using loc[]
# - Access the first element using iloc[]
# - Filter and print values greater than 20

# -----------------------------------------------------
# 3️⃣ DataFrame from a dictionary
# -----------------------------------------------------
# Task:
# - Create a DataFrame with columns: "Name", "Age", "City"
#   Data: ["Alice", "Bob", "Charlie"], [25, 30, 35], ["Delhi", "Mumbai", "Chennai"]
# - Print the entire DataFrame
# - Print the row at index 1 using loc[]
# - Print the first row using iloc[]

# -----------------------------------------------------
# 4️⃣ Conditional filtering in DataFrame
# -----------------------------------------------------
# Task:
# - Using the above DataFrame, filter rows where Age > 28
# - Filter rows where City is "Delhi"
# - Print the filtered DataFrames



# -----------------------------------------------------
# Import pandas library
# -----------------------------------------------------
import pandas as pd

# -----------------------------------------------------
# 1️⃣ Series from a list with filtering
# -----------------------------------------------------
# Create a Series from the list [10, 20, 30, 40, 50]
series_list = pd.Series([10, 20, 30, 40, 50], index=[0, 1, 2, 3, 4])

# Access the element with index 3 using loc[]
print("Element at index 3 using loc[]:", series_list.loc[3])

# Access the second element using iloc[]
print("Second element using iloc[]:", series_list.iloc[1])

# Filter and print elements greater than 25
print("Elements greater than 25:")
print(series_list[series_list > 25])

# -----------------------------------------------------
# 2️⃣ Series from a dictionary
# -----------------------------------------------------
# Create a Series from the dictionary
series_dict = pd.Series({"A": 5, "B": 15, "C": 25, "D": 35})

# Access the value of key "B" using loc[]
print("\nValue of key 'B' using loc[]:", series_dict.loc["B"])

# Access the first element using iloc[]
print("First element using iloc[]:", series_dict.iloc[0])

# Filter and print values greater than 20
print("Values greater than 20:")
print(series_dict[series_dict > 20])

# -----------------------------------------------------
# 3️⃣ DataFrame from a dictionary
# -----------------------------------------------------
# Create a DataFrame with columns: "Name", "Age", "City"
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Chennai"]
})

# Print the entire DataFrame
print("\nEntire DataFrame:")
print(df)

# Print the row at index 1 using loc[]
print("\nRow at index 1 using loc[]:")
print(df.loc[1])

# Print the first row using iloc[]
print("\nFirst row using iloc[]:")
print(df.iloc[0])

# -----------------------------------------------------
# 4️⃣ Conditional filtering in DataFrame
# -----------------------------------------------------
# Filter rows where Age > 28
age_filtered = df[df["Age"] > 28]
print("\nRows where Age > 28:")
print(age_filtered)

# Filter rows where City is "Delhi"
city_filtered = df[df["City"] == "Delhi"]
print("\nRows where City is 'Delhi':")
print(city_filtered)


# 📊 Pandas Workout Problems - CSV: laptops.csv
# Columns: Brand, Resolution, Size, Selling Price, Original Price, Operating System, Rating

# 1️⃣ Filtering based on condition
# Q1: Display all rows where the Brand is "SAMSUNG" AND the Selling Price is less than 50000.

# 2️⃣ Conditional filtering with multiple conditions
# Q2: Display only the Brand, Size, and Rating columns for laptops where the Operating System is "Android " AND Rating is greater than or equal to 4.0.

# 3️⃣ Drop rows with missing values
# Q3: Drop all rows where the Rating column has NaN values. 


# 4️⃣ Fill missing values
# Q4: Replace all NaN values in the Operating System column with the string "Unknown".

# 5️⃣ Rename columns
# Q5: Rename the column "Selling Price" to "Current Price" and "Original Price" to "MRP".

# 6️⃣ Count occurrences using value_counts()
# Q6: Find how many laptops are available for each Brand using value_counts().


# 7️⃣ Grouping and aggregation
# Q7: Group the DataFrame by Brand and calculate the sum of Selling price for each brand.
# Then, sort the result in descending order of average selling price.

# 8️⃣ Sorting values
# Q9: Sort the DataFrame first by Selling Price in ascending order and then by Rating in descending order.


# 9️⃣ Groupby with sort
# Q10: Find the top 3 brands with the highest selling price.
# Display their brand names .
