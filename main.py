""" 
CSV file: Global-YouTube-Statistics.csv
Top 995 YouTube channels with their statistics
Kaggle: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
"""
from myfunctions import *
import csv

def top_youtuber_by_country(data, country):
    filters = {'Country': country}
    return entry_max(filter_or(data, filters), 'subscribers')

def main():
    # get directory for csv file AviationData.csv
    csv_dir = 'data/Global-YouTube-Statistics.csv'
    
    # open csv file
    with open(csv_dir, 'r', encoding='latin-1') as file:
        # convert csv file to a dictionary
        reader = csv.DictReader(file)
        # store a list of dictionaries
        data = list(reader)
    # user menu
    while True:
        print("1. View top YouTube channel by country")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            country = input("Enter the country: ")
            top_youtuber = top_youtuber_by_country(data, country)
            print(f"The top YouTube channel in {country} is {top_youtuber['Youtuber']} with {top_youtuber['subscribers']} subscribers.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()