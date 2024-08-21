# Import
import os
import csv

# Save Data to CSV File
def saveToCSV(data, answerAndAnalysis, rows, outputDirectory):

    # Create Header and New Data List
    newData = [["Index", "Article Title", "Authors", "Publication Year", "Answer", "Analysis"]]

    # Append Answer and Analysis to Each Row
    for i in range(0, rows):
        authors = data[i][2] + " et al."
        newRow = [data[i][0], data[i][1], authors, data[i][3], answerAndAnalysis[i][0], answerAndAnalysis[i][1]]
        newData.append(newRow)

    # Sort Data Based on Answer
    order = {"yes": 0, "maybe": 1, "no": 2}
    newData = [newData[0]] + sorted(newData[1:], key=lambda row: order.get(row[4].lower(), 3))

    # Writing to CSV File
    path = os.path.join(outputDirectory, 'data.csv')
    with open(path, mode='w', newline='') as file:
        csv.writer(file).writerows(newData)
