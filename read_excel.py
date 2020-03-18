import xlrd

execlDir = r'C:\Users\11198\Desktop\国安冻结——生产和基地.xlsx'

workbook = xlrd.open_workbook(execlDir)

print(workbook.sheet_names())

worksheet = workbook.sheet_by_name('Sheet1')

rows = worksheet.row_values(1)

clos = worksheet.col_values(1)

cell_1 = worksheet.cell_value(1, 1)

cell_2 = worksheet.cell(1,2).value

print(type(cell_2))

