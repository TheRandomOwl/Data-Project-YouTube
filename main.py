""" 
CSV file: Global-YouTube-Statistics.csv
Top 995 YouTubers with their statistics
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

    # print a numbered list of the keys in the dictionary
    for i, key in enumerate(data[0].keys()):
        print(f"{i+1}. {key.replace('_', ' ')}")

    # print the most common category
    print(f"Most common category: \n{most_frequent(data, 'category')}\n")

    # print the least common category
    print(f"Least common category: \n{least_frequent(data, 'category')}\n")

    # print channal with the most views
    most_views = entry_max(data, 'video views')
    print(f"Channel with the most views: \n{most_views['Youtuber']}\nViews: {most_views['video views']}\n")

    # print average uploads per channel
    print(f"Average uploads per channel: \n{avg_val(data, 'uploads')}\n")

    # print channel with the most subscribers in the category 'Comedy'
    filters = {'category': 'Comedy'}
    most_subs = entry_max(filter_or(data, filters), 'subscribers')
    print(f"Channel with the most subscribers in the category 'Comedy': \n{most_subs['Youtuber']}\nSubscribers: {most_subs['subscribers']}\n")

    # Youtuber with the most subscribers not in the category 'Entertainment' or 'Music'
    filters = {'category': ('Entertainment', 'Music', 'nan')}
    most_subs = entry_max(filter_or(data, filters, True), 'subscribers')
    print(f"Youtube channel with the most subscribers not in the category 'Entertainment' or 'Music': \n{most_subs['Youtuber']}\nCategory: {most_subs['category']}\nSubscribers: {most_subs['subscribers']}\n")

    countries = filter_or(data, {'Country':'nan'}, True)
    for country in get_column(countries, 'Country'):
        youtuber = top_youtuber_by_country(data, country)
        print(f"Top Youtube Channel in {country}: \n{youtuber['Youtuber']}\nSubscribers: {youtuber['subscribers']}\n")

if __name__ == '__main__':
    main()