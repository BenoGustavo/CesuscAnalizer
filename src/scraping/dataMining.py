from bs4.element import ResultSet

from scraping.scrapper import getPointsToBeAproved, getStudantGradeAverage


def formatData(
    tableRows: ResultSet,
    subjectName: str,
    maxClassMiss,
    yourMisses,
    frequencyInPercentage,
    HowMutchYouCanMiss,
) -> dict:
    # Getting the subject name and putting it on the list
    subjectData = [subjectName]

    # Passing through all the rows of the table to get all the grades
    for i in range(len(tableRows)):
        # Get the date of the exam and the grade too
        examDate = tableRows[i].find(attrs={"data-label": "Data de Avaliação"})
        gradeValue = tableRows[i].find(attrs={"data-label": "Nota"})

        # Append the date and the grade to the list
        if examDate is not None:
            subjectData.append(examDate.text)
        if gradeValue is not None:
            subjectData.append(gradeValue.text)

        # If the data of the next exam is not available, append a default value
        if len(tableRows) == 1 or examDate is None:
            subjectData.append("--/--/--")
            subjectData.append("-")
            subjectData.append("--/--/--")
            subjectData.append("-")

        if len(tableRows) == 2 and i == 1 or gradeValue is None:
            subjectData.append("--/--/--")
            subjectData.append("-")

    studantAverageGrade = getStudantGradeAverage(tableRows)
    pointsToTheStudantBeAproved = getPointsToBeAproved(tableRows)

    # Append all the itens to the list
    subjectData.append(studantAverageGrade)
    subjectData.append(pointsToTheStudantBeAproved)
    subjectData.append(maxClassMiss)
    subjectData.append(yourMisses)
    subjectData.append(HowMutchYouCanMiss)
    subjectData.append(frequencyInPercentage)

    # Return a dictionary with the subject name as the key and the list of exam dates and grades as the value
    return {subjectData[0]: subjectData[1:]}
