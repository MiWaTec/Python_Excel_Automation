import pandas as pd

# Get dataframe from excel file
file_path = "C:/Users/Michael/Desktop/ExcelData\Client_Data.xlsx"
df = pd.read_excel(file_path)

# Insert an empty column 
col_index =df.columns.get_loc('Weight (kg)')
df.insert(col_index+1, 'BMI2', None)
df['BMI'] = df['Weight (kg)'] / (df['Height (cm)']/100)**2

# Update excel file with new column
df.to_excel(file_path, index=False)
