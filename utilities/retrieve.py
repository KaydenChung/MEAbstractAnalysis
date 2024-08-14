# Import
import pandas as pd
  
# Get Data from Excel File
def getData(filename):

    # Create the DataFrame
    excel = pd.read_excel(filename)
    dataFrame = pd.DataFrame(excel)

    # Extract Data from the DataFrame
    data = []
    for index, row in dataFrame.iterrows():
        title = row['Article Title']
        author = row['Authors'].split(';')[0].split(',')[0].strip()
        year = row['Publication Year']
        abstract = row['Abstract']
        data.append((title, author, year, abstract))
    return data
