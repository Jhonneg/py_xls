import openpyxl

wb = openpyxl.load_workbook("my-workbook.xlsx")

ws = wb.active

ws["A1"] = "Hello Excel"

wb.save("my-workbook.xlsx")
