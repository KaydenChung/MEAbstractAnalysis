# Import
import csv

# Save Data to CSV File
def saveToCSV(data, answerAndAnalysis, rows):

    # Create Header and New Data List
    if(answerAndAnalysis):
        header = ["Article Title", "Authors", "Publication Year", "Abstract", "Answer", "Analysis"]
    else:
        header = ["Article Title", "Authors", "Publication Year", "Abstract"]
    newData = [header]

    # Append Answer and Analysis to Each Row
    for i in range(0, rows):
        if(answerAndAnalysis):
            newRow = list(data[i]) + answerAndAnalysis[i]
        else:
            newRow = list(data[i])
        newData.append(newRow)

    # Writing to CSV File
    with open('output/data.csv', mode='w', newline='') as file:
        csv.writer(file).writerows(newData)
