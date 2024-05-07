""" 
CSV file: AviationData.csv
Kaggle: https://www.kaggle.com/datasets/yassereleraky/aviation-accident-ntsb
"""
from myfunctions import *
import csv
import pprint

def correct_data(data):
    """ 
    https://en.wikipedia.org/wiki/1996_Charkhi_Dadri_mid-air_collision
    """
    for row in data:
        if row["Accident.Number"] == "DCA97WA007B":
            row["Model"] = "Il-76TD"
            row["Make"] = "Ilyushin"
            row["Total.Fatal.Injuries"] = "37"
        if row["Accident.Number"] == "DCA97WA007A":
            row["Total.Fatal.Injuries"] = "312"

def main():
    # get directory for csv file AviationData.csv
    csv_dir = 'data/AviationData.csv'
    
    # open csv file
    with open(csv_dir, 'r', encoding='latin-1') as file:
        # convert csv file to a dictionary
        reader = csv.DictReader(file)
        # create a list of dictionaries
        data = list(reader)
    correct_data(data)

    # print a numbered list of the keys in the dictionary
    for i, key in enumerate(data[0].keys()):
        print(f"{i+1}. {key.replace('.', ' ')}")

    # pprint.pprint(filter_and(data, {'Model':'DC9', 'Country': 'United States'}))
    # pprint.pprint(filter_or(data, {'Event.Date': '2001-09-11'}))
    pprint.pprint(entry_max(data, 'Total.Fatal.Injuries'))

if __name__ == '__main__':
    main()