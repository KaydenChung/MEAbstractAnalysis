# Imports
import re
from collections import Counter

# Stop Words to Ignore
stopWords = [
    "All", "Although", "An", "As", "Despite", "In", "It", "One", "Our", "Some", 
    "The", "These", "They", "This", "To", "We", "While", "about", "according", 
    "across", "addition", "also", "among", "an", "as", "be", "because", "been", 
    "being", "between", "both", "but", "can", "could", "does", "either", 
    "especially", "even", "every", "from", "had", "has", "have", "how", "if", 
    "into", "is", "it", "its", "may", "not", "of", "or", "our", "out", "over", 
    "should", "than", "that", "the", "their", "them", "there", "these", "they", 
    "this", "to", "under", "until", "up", "was", "we", "were", "what", "when", 
    "where", "which", "while", "who", "will", "with", "would"
]

# Check for Valid Word
def isValid(word):
    return re.match("^[A-Za-z]+$", word) is not None

# Get Unique Words from Abstracts
def getWords(abstracts):

    # Combine Abstracts into 1 String
    text = " ".join(abstracts)
    
    # Split Text into a Set of Unique Words
    words = set(word for word in text.split() if word not in stopWords and isValid(word))
    
    # Convert Set to List
    uniqueWords = sorted(list(words))

    return uniqueWords

# Count Words in Abstracts
def countWords(abstracts, list):

    wordCounts = []

    # Iterate Through Each Abstract
    for abstract in abstracts:

        # Split Abstract into Words
        words = [word for word in abstract.split() if word not in stopWords and isValid(word)]
        
        # Count Occurrences of Each Word
        count = Counter(words)
        
        # Create Dictionary of Unique Word Counts
        counts = {word: count.get(word, 0) for word in list}

        # Sort Dictionary Alphabetically
        counts = dict(sorted(counts.items()))
        
        # Append Dictionary to List
        wordCounts.append(counts)
    
    return wordCounts
