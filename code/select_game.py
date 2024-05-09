import os
import json
import pandas as pd
from collections import defaultdict

def collect_appids_by_genre(directory):
    # Change the dictionary to use genre descriptions as keys
    genre_info = defaultdict(lambda: {'appids': []})

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Check if 'genres' and 'steam_appid' exist in the JSON
                if 'genres' in data and 'steam_appid' in data:
                    steam_appid = data['steam_appid']
                    # Add the steam_appid to each genre's list
                    for genre in data['genres']:
                        genre_description = genre['description']
                        genre_info[genre_description]['appids'].append(steam_appid)

    return genre_info



def get_review_counts_from_csv(file_path):
    # Read the CSV file and create a dictionary of appid to review counts
    review_data = pd.read_csv(file_path)
    review_count_map = {}

    # Assume CSV has 'steam_appid' and 'review_count' columns
    for _, row in review_data.iterrows():
        appid = row['appid']
        review_count = row['review_num']
        review_count_map[appid] = review_count
    
    return review_count_map


def get_top_15_appids_by_reviews(genre_info, review_count_map):
    top_appids_by_genre = {}

    for genre, info in genre_info.items():
        # Sort the appids in this genre by their review count
        sorted_appids = sorted(
            info['appids'], 
            key=lambda appid: review_count_map.get(appid, 0), 
            reverse=True
        )
        # Keep only the top 15 appids for this genre
        top_appids_by_genre[genre] = {
            'top_10_appids': sorted_appids[:10]
        }
    
    return top_appids_by_genre


# Paths and result collection
directory = 'data/detail'  # Path to JSON files
csv_path = 'data/item_list_selected.csv'  # CSV with review counts
output_file_path = 'data/genre_top_appids.json'  # Output file name

# Collect genre info and review counts
genre_info = collect_appids_by_genre(directory)
review_count_map = get_review_counts_from_csv(csv_path)

# Get the top 15 appids by review count for each genre
top_appids_by_genre = get_top_15_appids_by_reviews(genre_info, review_count_map)

# Save the top appids to a JSON file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(top_appids_by_genre, output_file, ensure_ascii=False, indent=4)

print(f"Top 15 appids by review count for each genre have been saved to {output_file_path}.")