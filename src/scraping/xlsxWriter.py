import openpyxl
from utils import (
    XLSX_HEADERS,
    REPORTS_PATH,
    getExcelPath,
    isFileCreated,
    createReportsDir,
    getCurrentTime,
)


def writeXlsxFile(formatedData: list, username: str):
    EXCEL_PATH = getExcelPath(username)

    currentTime = getCurrentTime()

    # Checks if the file is created
    if not isFileCreated(REPORTS_PATH):
        createReportsDir(REPORTS_PATH)

    if isFileCreated(EXCEL_PATH):
        # Load the existing workbook
        workbook = openpyxl.load_workbook(filename=EXCEL_PATH)

        # Create a new sheet with a unique name
        sheet_name = f"{currentTime}_Cesusc"
        worksheet = workbook.create_sheet(sheet_name)

    else:
        # Create a new workbook and worksheet with openpyxl
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = f"{currentTime}_Cesusc"

    # Create all the headers
    for col, header in enumerate(XLSX_HEADERS, start=1):
        worksheet.cell(row=1, column=col, value=header)

    ###########################################
    ######NEED TO WRITE THE REST OF THE DATA HERE#####
    ###########################################

    # Save the workbook
    workbook.save(filename=EXCEL_PATH)
