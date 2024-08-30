# Import
import os
import sys
from utilities.retrieve import getData
from utilities.gpt import askGPT
from utilities.words import getWords
from utilities.words import countWords
from utilities.graphs import createOccupancyMatrix
from utilities.graphs import createScatterPlot
from utilities.graphs import createSimilarityMatrix
from utilities.graphs import createDendrogram
from utilities.export import saveToCSV

# Supress Warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Curlm already closed!")

# Variables
directory = "data/"
files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]
GPT = True
NUM = 0

# Text-Based Menu UI
print("\nSelect File to Analyze:\n")
for i, file in enumerate(files, 1):
    print(f"{i}: {file}")
choice = int(input("\nEnter Corresponding Number: ")) - 1
print("\n")
filename = os.path.join(directory, files[choice])
outputDirectory = os.path.join("output", os.path.splitext(files[choice])[0])
os.makedirs(outputDirectory, exist_ok = True)

# Get Data
data = getData(filename)

# Iterate Entire Dataset
if NUM == 0:
    NUM = len(data)

# Fetch GPT Response
answerAndAnalysis = []
if(GPT):
    for i in range(0, NUM):
        try:
            # Ask GPT and Parse Response
            response = askGPT(data[i][4])
            parsedResponse = response.split("\n")

            # Extract Answer and Analysis
            answer = parsedResponse[0] if len(parsedResponse) > 0 else ""
            analysis = parsedResponse[2] if len(parsedResponse) > 1 else ""
            
            # Ensure Answer is not an Error Message
            if "too many messages in a row" in answer or "ip:" in answer:
                answerAndAnalysis.append(["Error", "Failed to Retrieve Analysis"])
            else:
                answerAndAnalysis.append([answer, analysis])

        except Exception as e:
            print(f"Error Processing Abstract {i+1}: {str(e)}")
            answerAndAnalysis.append(["Error", "Failed to Retrieve Analysis"])
        
        # Calculate Progress
        progress = round(((i + 1) / NUM) * 100)
        bar = 50
        fill = int(bar * progress // 100)
        bar = '█' * fill + '-' * (bar - fill)

        # Clear Terminal and Print Progress Bar
        sys.stdout.write("\033[F")
        print(f'Processing: |{bar}| {progress}% Complete')

    print("Processing Complete!\n")

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

if(NUM > 1):
    # Create Scatter Plot
    createScatterPlot(occupancyMatrix, data, NUM, outputDirectory)

    # Create Similarity Matrix
    similarityMatrix = createSimilarityMatrix(occupancyMatrix, data, NUM, outputDirectory)

    # Create Dendrogram
    createDendrogram(similarityMatrix, data, NUM, outputDirectory)
