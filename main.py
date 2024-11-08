import gspread

gc = gspread.service_account("service-account-credentials.json")

spreadsheet = gc.open("Python Gsheets")
