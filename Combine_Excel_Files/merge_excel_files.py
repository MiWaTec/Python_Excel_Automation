import os

excel_folder = 'C:/Users/Michael/Desktop/Python_Projects/mwtestcodes/ExcelReaderScript'
merged_excel_folder = ''
merged_excel_name = ''

# Get all excel files from the folder
excel_list = []
print(os.walk(excel_folder))
for folder, subfolder, files in os.walk(excel_folder):
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):
            excel_list.append(os.path.join(folder, file))
print(excel_list)

# Merge all excel files
