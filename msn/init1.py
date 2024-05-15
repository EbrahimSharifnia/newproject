import pandas as pd
import numpy as np

# Define the number of products
num_products = 10
num_parts = 12

# Generate unique product codes
product_codes = ['FAP' + str(i).zfill(4) for i in range(1, num_products + 1)]

# Generate random demand values for each product
random_demand = np.random.randint(500, 1000, size=num_products)

# Generate random quantities for parts required for each product
part_columns = ['Part_{}'.format(i+1) for i in range(num_parts)]  # Creates column names for parts
part_quantities = np.random.randint(5, 10, size=(num_products, num_parts))  # Generates random quantities

# Create a DataFrame
products_df = pd.DataFrame({
    'Product Code': product_codes,
    'Demand': random_demand
})

# Add part columns to DataFrame
for i, part in enumerate(part_columns):
    products_df[part] = part_quantities[:, i]

# Print the products_df DataFrame
print(products_df)

#########################################################

# Define the parts
parts = ['Part_{}'.format(i+1) for i in range(num_parts)]  # List of parts from Part_1 to Part_10

# Generate random supply values for each part
random_supply = np.random.randint(30000, 40000, size=num_parts)  # Random integers between 500 and 1500

# Create the DataFrame
parts_supp_df = pd.DataFrame({
    'Part_Num': parts,
    'Supply': random_supply
})

# Print the DataFrame
print(parts_supp_df)

########################################################

# Generate random priority scores for each product
priority_scores = np.random.randint(1, 5, size=num_products)  # Random integers between 1 and 10

# Create the DataFrame
products_priority_df = pd.DataFrame({
    'Product Code': product_codes,
    'Priority Score': priority_scores
})

# Print the DataFrame
print(products_priority_df)

#################################################

# def optimize_production(products_df, parts_supp_df, products_priority_df):
#     # Merge data on product codes to bring all relevant data together
#     merged_df = products_df.merge(products_priority_df, on='Product Code')
#     merged_df = merged_df.sort_values('Priority Score', ascending=False)

#     # Create a dictionary from the parts supply DataFrame for easy access
#     parts_supply = parts_supp_df.set_index('Part_Num')['Supply'].to_dict()

#     # Prepare the output DataFrame
#     output_df = pd.DataFrame(columns=['Product Code', 'Optimized Production'])

#     # Calculate the maximum number of each product that can be assembled
#     for _, row in merged_df.iterrows():
#         product_code = row['Product Code']
#         demand = row['Demand']
#         min_possible = demand  # Start with the demand as the maximum possible

#         # Check for each part
#         for part in parts_supply.keys():
#             if part in row and parts_supply[part] > 0:
#                 required = row[part]
#                 if required > 0:
#                     # Calculate the maximum number of this product that can be made with the available parts
#                     max_product_from_part = parts_supply[part] // required
#                     min_possible = min(min_possible, max_product_from_part)
        
#         # Deduct the used parts from the parts supply
#         for part in parts_supply.keys():
#             if part in row and parts_supply[part] > 0:
#                 required = row[part]
#                 if required > 0:
#                     parts_supply[part] -= required * min_possible

#         # Append to the output DataFrame
#         output_df = output_df.append({'Product Code': product_code, 'Optimized Production': min_possible}, ignore_index=True)

#     return output_df



# def optimize_production(products_df, parts_supp_df, products_priority_df):
#     # Merge data on product codes to bring all relevant data together
#     merged_df = products_df.merge(products_priority_df, on='Product Code')
#     merged_df = merged_df.sort_values('Priority Score', ascending=False)

#     # Create a dictionary from the parts supply DataFrame for easy access
#     parts_supply = parts_supp_df.set_index('Part_Num')['Supply'].to_dict()

#     # Prepare the output DataFrame
#     output_data = []

#     # Calculate the maximum number of each product that can be assembled
#     for _, row in merged_df.iterrows():
#         product_code = row['Product Code']
#         demand = row['Demand']
#         min_possible = demand  # Start with the demand as the maximum possible

#         # Check for each part
#         for part, required in row.iteritems():
#             if part.startswith('Part_') and required > 0:
#                 if part in parts_supply and parts_supply[part] > 0:
#                     # Calculate the maximum number of this product that can be made with the available parts
#                     max_product_from_part = parts_supply[part] // required
#                     min_possible = min(min_possible, max_product_from_part)

#         # Deduct the used parts from the parts supply
#         if min_possible > 0:
#             for part, required in row.iteritems():
#                 if part.startswith('Part_') and required > 0 and part in parts_supply:
#                     parts_supply[part] -= required * min_possible

#         # Append results to the output list
#         output_data.append({'Product Code': product_code, 'Optimized Production': min_possible})

#     # Create the output DataFrame from the list
#     output_df = pd.DataFrame(output_data)

#     return output_df


# # Example function call
# optimized_df = optimize_production(products_df, parts_supp_df, products_priority_df)
# print(optimized_df)

# # Example DataFrames (these need to be properly populated as per your actual data schema)
# products_df = pd.DataFrame({
#     'Product Code': ['FAP0001', 'FAP0002'],
#     'Demand': [100, 150],
#     'Part_1': [4, 2],
#     'Part_2': [1, 3],
# })

# parts_supp_df = pd.DataFrame({
#     'Part_Num': ['Part_1', 'Part_2'],
#     'Supply': [400, 450]
# })

# products_priority_df = pd.DataFrame({
#     'Product Code': ['FAP0001', 'FAP0002'],
#     'Priority Score': [10, 20]
# })

import pandas as pd

def optimize_production(products_df, parts_supp_df, products_priority_df):
    # Merge data on product codes to bring all relevant data together
    merged_df = products_df.merge(products_priority_df, on='Product Code')
    merged_df = merged_df.sort_values('Priority Score', ascending=False)

    # Create a dictionary from the parts supply DataFrame for easy access
    parts_supply = parts_supp_df.set_index('Part_Num')['Supply'].to_dict()

    # Prepare the output list
    output_data = []

    # Calculate the maximum number of each product that can be assembled
    for _, row in merged_df.iterrows():
        product_code = row['Product Code']
        demand = row['Demand']
        min_possible = demand  # Start with the demand as the maximum possible

        # Check for each part and calculate minimum production possible based on part availability
        for part, supply in parts_supply.items():
            if part in row.index and row[part] > 0:
                max_product_from_part = supply // row[part]
                min_possible = min(min_possible, max_product_from_part)
        
        # Deduct the used parts from the parts supply and update for each part
        if min_possible > 0:
            for part, required in row.iteritems():
                if part in parts_supply and required > 0:
                    parts_supply[part] -= required * min_possible

        # Calculate backorder
        backorder = demand - min_possible

        # Collect the production data, remaining parts, and backorder
        product_data = {
            'Product Code': product_code,
            'Optimized Production': min_possible,
            'Backorder': backorder
        }

        # Append remaining parts supply for each part
        for part, remaining in parts_supply.items():
            product_data[part + ' Remaining'] = remaining

        # Append results to the output list
        output_data.append(product_data)

    # Create the output DataFrame from the list
    output_df = pd.DataFrame(output_data)

    return output_df

# Example function call
optimized_df = optimize_production(products_df, parts_supp_df, products_priority_df)
print(optimized_df)

import openpyxl
import os
import pandas as pd

# Assuming 'optimized_df' is your DataFrame

# Specify the directory name where you want to save the file
directory = 'msn'

# Check if the directory exists, and if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Specify the path to the Excel file
file_path = os.path.join(directory, 'optimized_production.xlsx')

# Save the DataFrame to an Excel file
optimized_df.to_excel(file_path, index=False, engine='openpyxl')
