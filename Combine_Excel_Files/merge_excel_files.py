import os
import pandas as pd

# Get all excel files from the folder
all_files = os.walk('C:/Users/Michael/Desktop/ExcelData')
excel_list = []
for folder, subfolder, files in all_files:
    for file in files:
        if file.endswith('.xlsx'):
            excel_list.append(os.path.join(folder, file))

# Merge all data of the excel files
df_merged = pd.DataFrame()
for excel_file in excel_list:
    df = pd.read_excel(excel_file)
    df_merged = pd.concat([df_merged, df], axis=1)
print(df_merged)
# Write merged dataframe into a new excel file
df_merged.to_excel('C:/Users/Michael/Desktop/Merged_Excel.xlsx')
