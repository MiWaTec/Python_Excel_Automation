from openpyxl import load_workbook
from openpyxl.styles import Font

# Open workbook
excel_file_path = r"C:/Users/warsi/Desktop/ExcelData\Client_Data.xlsx"
wb = load_workbook(excel_file_path)
ws = wb.active

# Define colors
color_dict = {
    'Female': 'a30000',
    'Male': '0515f0'
}

# Get column index
for cell in ws[1]:
    if cell.internal_value == 'Gender':
        col_index = cell.col_idx
        break

# Color string values
for cells_in_row in ws.iter_rows(min_row=2,
                                 min_col=col_index,
                                 max_col=col_index):
    cell_value = cells_in_row[0].internal_value
    if cell_value in list(color_dict):
        cells_in_row[0].font = Font(color=color_dict[cell_value],
                                    bold=True,
                                    italic=True)

# Save workbook
wb.save(r"C:/Users/warsi/Desktop/ExcelData\Client_Data_colored.xlsx")