
import pygsheets
import pandas as pd

def write_google_sheet(values):

    # Authorize with google
    gc = pygsheets.authorize(service_account_file="gs_credentials.json")

    sheets = gc.open("Python to Google Sheets test")

    wks = sheets[0]

    #res = working_sheet.append_table(all_values, start="A2", end="F2", dimension="ROWS", overwrite=False)
    #print(res)
    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    
    #extract all non empty rows
    nonEmptyRows = []
    for i in cells:
        if i != []:
            nonEmptyRows.append(i)

    #calculating the length 
    countOfnonEmptyRows = len(nonEmptyRows)    
    
    #insert at the first empty row
    wks.insert_rows(countOfnonEmptyRows, 1, values, inherit=True)
    
