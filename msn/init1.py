import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

# Define the number of products
num_products = 10

# Generate unique product codes
product_codes = ['P' + str(i).zfill(4) for i in range(1, num_products + 1)]

# Generate random demand values for each product
random_demand = np.random.randint(100, 1000, size=num_products)

# Create a DataFrame
df = pd.DataFrame({
    'Product Code': product_codes,
    'Demand': random_demand
})

# Print the DataFrame
print(df)



############################################

import pandas as pd
import numpy as np

# Define the number of products
num_products = 10

# Generate unique product codes
product_codes = ['P' + str(i).zfill(4) for i in range(1, num_products + 1)]

# Generate random demand values for each product
random_demand = np.random.randint(100, 1000, size=num_products)

# Generate random quantities for parts required for each product
part_columns = ['Part_{}'.format(i+1) for i in range(10)]  # Creates column names for parts
part_quantities = np.random.randint(0, 7, size=(num_products, 10))  # Generates random quantities

# Create a DataFrame
df = pd.DataFrame({
    'Product Code': product_codes,
    'Demand': random_demand
})

# Add part columns to DataFrame
for i, part in enumerate(part_columns):
    df[part] = part_quantities[:, i]

# Print the DataFrame
print(df)

# Rename df to products_df
products_df = df

# Print the products_df DataFrame
print(products_df)

#########################################################

import pandas as pd
import numpy as np

# Define the parts
parts = ['Part_{}'.format(i+1) for i in range(10)]  # List of parts from Part_1 to Part_10

# Generate random supply values for each part
random_supply = np.random.randint(500, 1501, size=10)  # Random integers between 500 and 1500

# Create the DataFrame
parts_supp_df = pd.DataFrame({
    'Part_Num': parts,
    'Supply': random_supply
})

# Print the DataFrame
print(parts_supp_df)
