# Imports
import os
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import seaborn as sns

# Create an Occupancy Matrix
def createOccupancyMatrix(wordCounts):
    
    # Create 2D Matrix of Word Counts
    occupancyMatrix = np.array([list(counts.values()) for counts in wordCounts])
    
    return occupancyMatrix

def createScatterPlot(occupancyMatrix, data, NUM, outputDirectory):

    # Scale Data
    scaler = StandardScaler()
    scaledData = scaler.fit_transform(occupancyMatrix)

    # Perform PCA to reduce the dimensionality for visualization
    pca = PCA(n_components = 2)
    pcaResult = pca.fit_transform(scaledData)

    # Create Scatter Plot
    plt.figure(figsize = (10, 7))
    plt.scatter(pcaResult[:, 0], pcaResult[:, 1], c = 'blue', marker = 'o')

    # Create Label for Each Point
    for i, index in enumerate(range(NUM)):
        plt.text(pcaResult[i, 0], pcaResult[i, 1], f"{data[i][0]}", fontsize = 6)
    plt.title("Scatter Plot of Article Abstracts Grouped by Word Counts")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    
    # Save the Graph
    path = os.path.join(outputDirectory, "scatterPlot.png")
    plt.savefig(path)
    plt.close()

# Create Similarity Matrix
def createSimilarityMatrix(occupancyMatrix, data, NUM, outputDirectory):

    # Calculate Cosine Distance and Convert to Similarity
    cosineDistances = pdist(occupancyMatrix, metric = 'cosine')
    similarityMatrix = 1 - squareform(cosineDistances)

    # Create Similarity Matrix
    plt.figure(figsize = (10, 6))
    ax = sns.heatmap(similarityMatrix, annot = True, cmap = "YlGnBu", xticklabels = [f"{data[i][0]}" for i in range(NUM)], yticklabels = [f"{data[i][0]}" for i in range(NUM)], annot_kws = {"size": 6})
    ax.set_xticklabels(ax.get_xticklabels(), fontsize = 6)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize = 6)
    plt.title("Similarity Matrix of Article Abstracts")
    
    # Save the Graph
    path = os.path.join(outputDirectory, "similarityMatrix.png")
    plt.savefig(path)
    plt.close()

    return similarityMatrix

# Create Dendrogram
def createDendrogram(similarityMatrix, data, NUM, outputDirectory):

    # Create Dendrogram Using Hierarchical Clustering
    linkageMatrix = linkage(similarityMatrix, method = 'ward')
    plt.figure(figsize = (10, 6))
    dendrogram(linkageMatrix, labels = [f"{data[i][0]}" for i in range(NUM)])
    ax = plt.gca()
    plt.xticks(fontsize = 6)
    plt.yticks(fontsize = 6)
    plt.title("Dendrogram of Article Abstracts")
    plt.xlabel("Article")
    plt.ylabel("Distance")
    
    # Save the Graph
    path = os.path.join(outputDirectory, "dendrogram.png")
    plt.savefig(path)
    plt.close()
