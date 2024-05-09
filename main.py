""" 
CSV file: Global-YouTube-Statistics.csv
Top 995 YouTube channels with their statistics
Kaggle: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
"""
from myfunctions import *
import csv

def top_youtuber_by_country(data, country):
    return entry_min(filter_or(data, {'Country': country}), 'country_rank')

def print_options():
    print("1. View top YouTube channel by country")
    print("q to Exit")

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
        print_options()
        choice = input("Enter your choice: ")

        if choice == "1":
            # list all countries
            print(get_column(filter_or(data, {'Country': 'nan'}, True), 'Country'))
            while True:
                country = input("Enter the country: ").title()
                if country not in get_column(data, 'Country'):
                    print("Invalid country. Please try again.")
                    continue
                else:
                    break
            top_channel = top_youtuber_by_country(data, country)
            print(f"The top YouTube channel in {country} is {top_channel['Youtuber']} with {top_channel['subscribers']} subscribers.")
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == '__main__':
    main()