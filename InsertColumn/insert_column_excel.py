import pandas as pd

# Get dataframe from excel file
file_path = "C:/Users/warsi/Desktop/ExcelData\Client_Data.xlsx"
df = pd.read_excel(file_path)

# Insert an empty column 
col_index = df.columns.get_loc('Weight (kg)')
df.insert(col_index+1, 'BMI', None)
df['BMI'] = round(df['Weight (kg)'] / (df['Height (cm)']/100)**2, 1)

# Update excel file with new column
df.to_excel(file_path, index=False)
