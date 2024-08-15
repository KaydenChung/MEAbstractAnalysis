# Import
import csv

# Save Data to CSV File
def saveToCSV(data, answerAndAnalysis, rows):

    # Create Header and New Data List
    header = ["Authors", "Publication Year", "Answer", "Analysis"]
    newData = [header]

    # Append Answer and Analysis to Each Row
    for i in range(0, rows):
        authors = data[i][1] + " et al."
        newRow = [authors, data[i][2], answerAndAnalysis[i][0], answerAndAnalysis[i][1]]
        newData.append(newRow)

    # Sort Data Based on Answer
    order = {"yes": 0, "maybe": 1, "no": 2}
    newData = [newData[0]] + sorted(newData[1:], key=lambda row: order.get(row[2].lower(), 3))

    # Writing to CSV File
    with open('output/data.csv', mode='w', newline='') as file:
        csv.writer(file).writerows(newData)
