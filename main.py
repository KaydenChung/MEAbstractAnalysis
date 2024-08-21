# Import
import os
from utilities.retrieve import getData
from utilities.gpt import askGPT
from utilities.words import getWords
from utilities.words import countWords
from utilities.graphs import createOccupancyMatrix
from utilities.graphs import createScatterPlot
from utilities.graphs import createSimilarityMatrix
from utilities.graphs import createDendrogram
from utilities.export import saveToCSV

# Variables
directory = "data/"
files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]

GPT = True
NUM = 10

# Text-Based Menu UI
print("\nSelect File to Analyze:\n")
for i, file in enumerate(files, 1):
    print(f"{i}: {file}")
choice = int(input("\nEnter Corresponding Number: ")) - 1
print("")
filename = os.path.join(directory, files[choice])
outputDirectory = os.path.join("output", os.path.splitext(files[choice])[0])
os.makedirs(outputDirectory, exist_ok = True)

# Get Data
data = getData(filename)

# Itterate Entire Dataset
if NUM == 0:
    NUM = len(data)

# Fetch GPT Response
answerAndAnalysis = []
if(GPT):
    for i in range(0, NUM):

        # Ask GPT and Parse Response
        response = askGPT(data[i][4])
        parsedResponse = response.split("\n")

        # Extract Answer and Analysis
        answer = parsedResponse[0] if len(parsedResponse) > 0 else ""
        analysis = parsedResponse[2] if len(parsedResponse) > 1 else ""
        answerAndAnalysis.append([answer, analysis])

        # Print Answer and Analysis
        print(f"Article #{i+1}:")
        print(f"Answer: {answer}")
        print(f"Analysis: {analysis}")
        print("")

    # Save Data to CSV File
    saveToCSV(data, answerAndAnalysis, NUM, outputDirectory)

# Extract Abstracts from Data
abstracts = [item[4] for item in data[:NUM]]

# Get Unique Words from Abstracts
uniqueWords = getWords(abstracts)

# Count Words in Abstracts
counts = countWords(abstracts, uniqueWords)

# Create Occupancy Matrix
occupancyMatrix = createOccupancyMatrix(counts)

# Create Scatter Plot
createScatterPlot(occupancyMatrix, data, NUM, outputDirectory)

# Create Similarity Matrix
similarityMatrix = createSimilarityMatrix(occupancyMatrix, data, NUM, outputDirectory)

# Create Dendrogram
createDendrogram(similarityMatrix, data, NUM, outputDirectory)
