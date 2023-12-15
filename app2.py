import pandas as pd

# Specify the input Excel file path
input_excel_file_path = "Datasets.xlsx"

# Specify the output Excel file path
output_excel_file_path = "Datasets_Updated.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(input_excel_file_path, engine="openpyxl")

# Split the "Data" column into a list of values for each row
split_data = df['Data'].str.split('|').tolist()

# Determine the maximum number of splits in any row
max_splits = max(len(row) for row in split_data)

# Create new columns based on the number of splits
columns = [f"Split_{i+1}" for i in range(max_splits)]
df[columns] = pd.DataFrame(split_data, index=df.index)

# Strip whitespace from the new columns
df[columns] = df[columns].apply(lambda x: x.str.strip())

# Drop the original "Data" column
df = df.drop(columns=['Data'])

# Export the DataFrame to a new Excel file
df.to_excel(output_excel_file_path, index=False, engine="openpyxl")

print(f"Data has been loaded, split, and exported to {output_excel_file_path}")