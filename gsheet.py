import pygsheets

# Writes the 'values' list to the given spreadsheet.
# Will insert at the first non-empty row.
# Assumes there are no empty rows in between non-empty rows.
def write_google_sheet(values, spreadsheet_name, sheet_number, credentials_filename):

    # Authorize with google
    gc = pygsheets.authorize(service_account_file=credentials_filename)

    # Get working sheet
    sheets = gc.open(spreadsheet_name)
    wks = sheets[sheet_number]

    # Extract all non-empty rows
    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    nonEmptyRows = []
    for i in cells:
        if i != []:
            nonEmptyRows.append(i)

    # Get length of all non-empty rows 
    countOfnonEmptyRows = len(nonEmptyRows)    
    
    # Insert at the first empty row
    wks.insert_rows(countOfnonEmptyRows, 1, values, inherit=True)
    
