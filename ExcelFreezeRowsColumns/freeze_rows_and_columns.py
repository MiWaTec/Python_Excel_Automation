from openpyxl import Workbook
from openpyxl import load_workbook

excel_file_path = "C:/Users/Michael/Desktop/ExcelData\Client_Data.xlsx"
wb = load_workbook(excel_file_path)
ws = wb.active

# First column and row that will not be freezed
column = 'B'
row = '2'
ws.freeze_panes = '{}{}'.format(column, row)

# ws.freeze_panes = 'A1'

wb.save(excel_file_path)