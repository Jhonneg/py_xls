import gspread

gc = gspread.service_account("service-account-credentials.json")

spreadsheet = gc.open("Python Gsheets")

ws = spreadsheet.sheet1

ws.update_acell("A1", "Hello from Python")

new_spreadsheet = gc.create("Python Gsheets2")

new_spreadsheet.share("jonee4339@gmail.com", perm_type="user", role="writer")

