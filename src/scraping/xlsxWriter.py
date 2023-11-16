import openpyxl
from scraping.utils import (
    XLSX_HEADERS,
    getReportsPath,
    getExcelPath,
    isFileCreated,
    createReportsDir,
    getCurrentTime,
)


def writeXlsxFile(formatedData: list[dict], username: str):
    REPORTS_PATH = getReportsPath(username)
    EXCEL_PATH = getExcelPath(REPORTS_PATH)

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

    row = 2
    for subject in formatedData:
        # the first value is the subject name || tranforming the dict keys into a string
        worksheet.cell(row=row, column=1, value=str(list(subject.keys())))

        for key, listOfSubjectData in subject.items():
            for col, value in enumerate(listOfSubjectData, start=2):
                worksheet.cell(row=row, column=col, value=value)
        row += 1

    # Save the workbook
    workbook.save(filename=EXCEL_PATH)
