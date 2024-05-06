""" 
CSV file: AviationData.csv
Kaggle: https://www.kaggle.com/datasets/yassereleraky/aviation-accident-ntsb
"""
from myfunctions import *
import csv
import pprint

def main():
    # get directory for csv file AviationData.csv
    csv_dir = 'data/AviationData.csv'
    
    # open csv file
    with open(csv_dir, 'r', encoding='latin-1') as file:
        # convert csv file to a dictionary
        reader = csv.DictReader(file)
        # create a list of dictionaries
        data = list(reader)

    # print a numbered list of the keys in the dictionary
    for i, key in enumerate(data[0].keys()):
        print(f"{i+1}. {key.replace('.', ' ')}")

    # get user input for key
    index = int(input("Enter the number of the key you want to filter by: ")) - 1
    
    # Get the selected key
    selected_key = list(data[0].keys())[index]

    # Get the unique values for the selected key
    unique_values = set(row[selected_key] for row in data)

    # Print the numbered list of unique values
    for i, value in enumerate(unique_values):
        print(f"{i+1}. {value}")

    pprint.pprint(filter_and(data, {'Model':'DC9', 'Country': 'United States'}))

if __name__ == '__main__':
    main()