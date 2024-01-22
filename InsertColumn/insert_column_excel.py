import pandas as pd
from openpyxl import load_workbook

# Get dataframe from excel
excel_file_path = "C:/Users/Michael/Desktop/ExcelData\Client_Data.xlsx"
df = pd.read_excel(excel_file_path)

# Creae
col_index =df.columns.get_loc('Weight (kg)')
df.insert(col_index+1, 'BMI2', None)
df['BMI'] = df['Weight (kg)'] / (df['Height (cm)']/100)**2

# Update excel file with new column
df.to_excel(excel_file_path, index=False)

# Video title: 
# Insert empty column and calculate values from two other columns | Python Pandas
# How to calculate values in empty column




















