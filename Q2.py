# 1️⃣ Series from List
# ------------------------------------------------------------
# Create a Pandas Series from the list [5, 10, 15, 20, 25]
# - Display the third element using both iloc and loc
# - Display all elements greater than 10


# 2️⃣ DataFrame Creation
# ------------------------------------------------------------
# Create a DataFrame using:
# {
#   'Name': ['Riya', 'Amit', 'Sara', 'John'],
#   'Age': [22, 25, 24, 28],
#   'City': ['Delhi', 'Mumbai', 'Chennai', 'Delhi']
# }
# - Display only the columns Name and City
# - Display the first two rows only


# 3️⃣ Conditional Filtering
# ------------------------------------------------------------
# From the above DataFrame:
# - Display rows where Age > 23
# - Display rows where City == 'Delhi' and Age > 23


# 4️⃣ Add and Modify Columns
# ------------------------------------------------------------
# Add a new column "Marks" = [85, 92, 78, 88]
# Change the Name in the 3rd row (index 2) to 'Rahul'


# 5️⃣ Drop / Rename Columns
# ------------------------------------------------------------
# Drop the column "City"
# Rename the column "Marks" to "Score"


# 6️⃣ Handling Missing Values
# ------------------------------------------------------------
# Create a DataFrame:
# {
#   'Name': ['Amit', 'Riya', 'Sara', None],
#   'Age': [25, None, 22, 30]
# }

# - Count the number of missing values per column
# - Replace missing values in 'Age' with the mean age


# 7️⃣ Sorting



# ------------------------------------------------------------
# Using this data:
# {
#   'Name': ['Riya', 'Amit', 'Sara', 'John'],
#   'Marks': [85, 92, 78, 88]
# }
# - Sort the DataFrame by Marks (ascending)
# - Then sort again by Marks (descending)


# 8️⃣ Grouping & Aggregation
# ------------------------------------------------------------
# {
#   'City': ['Delhi', 'Delhi', 'Chennai', 'Mumbai', 'Mumbai'],
#   'Marks': [80, 90, 70, 85, 95]
# }
# - Find average Marks per City
# - Find maximum Marks per City
