""" 
CSV file: Global-YouTube-Statistics.csv.csv
Kaggle: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
"""
from myfunctions import *
import csv
import pprint

def main():
    # get directory for csv file AviationData.csv
    csv_dir = 'data/Global-YouTube-Statistics.csv'
    
    # open csv file
    with open(csv_dir, 'r', encoding='latin-1') as file:
        # convert csv file to a dictionary
        reader = csv.DictReader(file)
        # create a list of dictionaries
        data = list(reader)

    # print a numbered list of the keys in the dictionary
    for i, key in enumerate(data[0].keys()):
        print(f"{i+1}. {key.replace('_', ' ')}")

if __name__ == '__main__':
    main()