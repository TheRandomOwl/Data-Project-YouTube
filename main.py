""" 
CSV file: Global-YouTube-Statistics.csv
Top 995 YouTube channels in 2023 with their statistics
Kaggle: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
"""
from myfunctions import *
import os
import csv

def clear_console():
    command = 'clear' if os.name == 'posix' else 'cls'
    os.system(command)

def top_channel_by_country(data):
    # print avalible countries ignore "nan"
    countries = get_column(filter_or(data, {"Country": "nan"}, True), "Country")
    for country in sorted(countries):
        print(country)

    # get the country from the user
    while True:
        country = input("Enter a country: ").title()
        if country in countries:
            break
        elif country == "Q":
            break
        else:
            print("Invalid country. Please try again.")

    # get the top channel from the country else return to main menu
    if country == "Q":
        return
    channels = filter_or(data, {"Country": country})
    channel = entry_min(channels, "country_rank")

    # print the top channel and number of subscribers
    print(f"The top channel in {country} is {channel['Title']} with {channel['subscribers']} subscribers\n")

def top_channel_by_category(data):
    # print avalible categories ignore "nan"
    categories = get_column(filter_or(data, {"category": "nan"}, True), "category")
    for category in sorted(categories):
        print(category)

    # get the category from the user
    while True:
        category = input("Enter a category: ").title()
        if category in categories:
            break
        elif category == "Q":
            break
        else:
            print("Invalid category. Please try again.")

    # get the top channel from the category else return to main menu
    if category == "Q":
        return
    
    # get the top channel from the category
    channels = filter_or(data, {"category": category})
    channel = entry_max(channels, "subscribers")

    # print the top channel and number of subscribers
    print(f"The top channel in {category} is {channel['Title']} with {channel['subscribers']} subscribers\n")

def avg_views(data):
    # get the average number of views
    avg = avg_val(data, "video views")
    print(f"The average number of views is {avg}\n")

def popular_categories(data):
    # get top 3 most popular categories
    data_copy = filter_or(data, {"category": "nan"}, True)
    frequent = [most_frequent(data_copy, "category")]

    print("The top 3 most popular categories are:")
    for i in range(3):
        item = most_frequent(data_copy, "category")
        print(f"{i+1}.) {item}")
        data_copy = filter_and(data_copy, {"category": tuple(frequent)}, True)
        frequent.append(most_frequent(data_copy, "category"))
    print()

def youtube_channels_creation_year(data):
    # get the creation year of the youtube channels. Asks for year, month, and day
    while True:
        year = input("Enter the year of creation (YYYY): ").strip()
        if year.lower() == "q":
            return
        elif not year.isdigit() or len(year) != 4:
            print("Invalid year. Please enter a valid 4-digit year.")
            continue
        
        month = input("Enter the month of creation (Jan-Dec) or press Enter to skip: ").title().strip()
        if month and month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
            print("Invalid month. Please enter a valid month (Jan-Dec) or press Enter to skip.")
            continue
        day = ""
        if month:
            day = input("Enter the day of creation (DD) or press Enter to skip: ").strip()
            if day and (not day.isdigit() or int(day) < 1 or int(day) > 31):
                print("Invalid day. Please enter a valid day (1-31) or press Enter to skip.")
                continue

        break

    # filter channels based on creation date
    filters = {"created_year": year}
    if month:
        filters["created_month"] = month
    if day:
        filters["created_date"] = day
    channels = filter_and(data, filters)
    date = " ".join(f"{month} {day} {year}".split())
    
    # print the channels that match the creation date
    if channels:
        print(f"The following channel(s) were created {date}:")
        for channel in channels:
            print(channel["Title"])
    else:
        print(f"No channels were created {date}.")
    print()

def least_popular_category(data):
    # get the least popular category
    data_copy = filter_or(data, {"category": "nan"}, True)
    category = least_frequent(data_copy, "category")
    print(f"The least popular category is {category}\n")

def top_ten_total_uploads(data):
    # get the top 10 channels
    channels = data[:10]
    total_uploads = total_sum(channels, "uploads")
    print(f"The total amount of uploads for the top 10 channels is {total_uploads}\n")

def not_us_not_music_entertainment(data):
    data_copy = filter_or(data, {"Country": ("United States", "nan"), "category": ("Music", "Entertainment", "nan")}, True)
    print("Top 10 channels that are not from the US and are not in the music or entertainment category:")
    for i, channel in enumerate(data_copy[:10], 1):
        print(f"{i}.) {channel['Title']}: Category - {channel['category']}, Country - {channel['Country']}")
    print()

def quit_program(data):
    print("Goodbye!")
    exit()

def main():
    # get directory for csv file
    csv_dir = 'data/Global-YouTube-Statistics.csv'
    
    # open csv file
    with open(csv_dir, 'r', encoding='latin-1') as file:
        # convert csv file to a dictionary
        reader = csv.DictReader(file)
        # store a list of dictionaries
        data = list(reader)
    
    # user menu
    options = {
        "1": (top_channel_by_country, "Get the top channel by country"),
        "2": (top_channel_by_category, "Get the top channel by category"),
        "3": (avg_views, "Get the average number of views for all channels"),
        "4": (youtube_channels_creation_year, "Get the channels created on a specific date"),
        "5": (popular_categories, "Get the most popular categories"),
        "6": (top_ten_total_uploads, "Get the total amount of uploads for the top 10 channels"),
        "7": (least_popular_category, "Get the least popular category"),
        "8": (not_us_not_music_entertainment, "Get top 10 channels that are not from the US and are not in the music or entertainment category"),
        "q": (quit_program, "Quit the program")
        # add more options here
    }
    
    print("Welcome to the YouTube Statistics Program")
    while True:
        for key, value in options.items():
            print(f"{key}.) {value[1]}")

        # get user input
        user_input = input("Enter an option: ").strip()
        
        # validate user input
        if user_input not in options:
            print("Invalid option. Please try again.")
            continue
        
        # run the user input
        clear_console()
        options[user_input][0](data)

if __name__ == '__main__':
    main()