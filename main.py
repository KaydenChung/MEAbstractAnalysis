# Import
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
filename = "data/ES + technologies + aesthetic.xlsx"
GPT = False
NUM = 10

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
        response = askGPT(data[i][3])
        parsedResponse = response.split("\n")

        # Extract Answer and Analysis
        answer = parsedResponse[0] if len(parsedResponse) > 0 else ""
        analysis = parsedResponse[2] if len(parsedResponse) > 1 else ""
        answerAndAnalysis.append([answer, analysis])

        # Print Answer and Analysis
        print(f"Article #{i+1}:")
        print(f"Answer: {answer}")
        print(f"Analysis: {analysis}\n")
        print("")

# Extract Abstracts from Data
abstracts = [item[3] for item in data[:NUM]]

# Get Unique Words from Abstracts
uniqueWords = getWords(abstracts)

# Count Words in Abstracts
counts = countWords(abstracts, uniqueWords)

# Create Occupancy Matrix
occupancyMatrix = createOccupancyMatrix(counts)

# Create Scatter Plot
createScatterPlot(occupancyMatrix, NUM)

# Create Similarity Matrix
similarityMatrix = createSimilarityMatrix(occupancyMatrix, NUM)

# Create Dendrogram
createDendrogram(similarityMatrix, NUM)

# Save Data to CSV File
saveToCSV(data, answerAndAnalysis, NUM)
