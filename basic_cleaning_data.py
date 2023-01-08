# Import libraries
import pandas as pd
import numpy as np

# Import Dataset
sale = pd.read_excel('D:/Datasets/Kaggle/E-Commerce Sales Dataset/Amazon Sale Report.xlsx')
print("E-commerce Sales Dataset")
print(sale.head(10))
print("")

# Explore Dataset
print("Dataset shape")
print(sale.shape)
print("")
print("Dataset datatypes each column")
print(sale.dtypes)
print("")

# Numeric variables
print("Numeric variables exploration")
print(sale.describe())
print("")

# Categorical Variables
cat_sale = sale.dtypes[sale.dtypes == "object"].index
print("Categorical variables")
print(cat_sale)
print("")
print("Categorical variables exploration")
print(sale[cat_sale].describe())
print("")

# Remove Columns/Variables
sale = sale.drop(["Unnamed: 22", "fulfilled-by"], axis = 1)

# Check Duplicates
print("Number of duplicates rows on entire dataset")
print(sale.duplicated().sum())
print("")
print("Number of duplicates rows on unique column (index)")
print(sale.index.duplicated().sum())
print("")

# Remove Duplicates
sale.drop_duplicates(inplace = True)

# Check missing value
print("Total missing values on entire dataset")
print(pd.isnull(sale).sum().sum())
print("")
print("Distribution of missing values each column")
print(sale.isnull().mean())
print("")

# Dealing with missing values 1
Courier_missing = np.where(sale["Courier Status"].isnull() == True)
print("Number of missing value on Courier Status column")
print(len(Courier_missing[0]))
new_courier_var = np.where(sale["Courier Status"].isnull(),             # Logical check
                                "Cancelled",                            # Value if check is true
                                sale["Courier Status"])                 # Value if check is false
sale["Courier Status"] = new_courier_var 
print("Missing values percentage on ourier Status column after replacement ")
print(sale["Courier Status"].isnull().mean())
print("")

# Dealing with missing values 2
currency_missing = np.where(sale["currency"].isnull() == True)
print("Number of missing value on currency column")
print(len(currency_missing[0]))
new_currency_var = np.where(sale["currency"].isnull(),
                                 "INR",
                                 sale["currency"])
sale["currency"] = new_currency_var 
print("Missing values percentage on currency column after replacement")
print(sale["currency"].isnull().mean())
print("")

# Dealing with missing values 3
Amount_missing = np.where(sale["Amount"].isnull() == True)
print("Number of missing value on Amount column")
print(len(Amount_missing[0]))
new_Amount_var = np.where(sale["Amount"].isnull(),
                                0,
                                sale["Amount"])
sale["Amount"] = new_Amount_var 
print("Missing values percentage on Amount column after replacement")
print(sale["Amount"].isnull().mean())
print("")

# Dealing with missing values 4
columns = list(sale.columns)
columns = ['ship-city', 'ship-state', 'ship-postal-code', 'ship-country']
for column in columns:
    sale[column] = sale[column].fillna("Unknown")
print("Missing values percentage after replacement")
print(sale[columns].isnull().mean())
print("")

# Dealing with missing values 5
promo_missing = np.where(sale["promotion-ids"].isnull() == True)
print("Number of missing value on promotion-ids column")
print(len(promo_missing[0]))
new_promo_var = np.where(sale["promotion-ids"].isnull(),
                              "No Promotion",
                              sale["promotion-ids"])
sale["promotion-ids"] = new_promo_var 
print("Missing values percentage on promotion-ids column after replacement")
print(sale["promotion-ids"].isnull().mean())
print("")

# Dealing with missing values 6
B2B_missing = np.where(sale["B2B"].isnull() == True)
print("Number of missing value on B2B column")
print(len(B2B_missing[0]))
new_B2B_var = np.where(sale["B2B"].isnull(),
                            "FALSE", 
                            sale["B2B"])
sale["B2B"] = new_B2B_var 
print("Missing values percentage on B2B column after replacement")
print(sale["B2B"].isnull().mean())
print("")

# removing leading and trailing characters from columns with str type
sale["ship-state"].str.strip()