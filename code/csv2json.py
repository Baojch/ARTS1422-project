import csv
import os
import json

genre_appids_file = 'data/genre_top_appids.json'

# 读取包含appids的JSON文件
with open(genre_appids_file, 'r') as f:
    genre_data = json.load(f)

# print(genre_data)
keys = genre_data.keys()
print(keys)

dir = 'data/processed_output_emotion_by_gameid'

for key in keys:
    print(genre_data[key]['top_10_appids'])
    appid_list = genre_data[key]['top_10_appids']
    for appid in appid_list:
        file_path = os.path.join(dir, f'processed_emotion_{appid}.csv')
        file_path_json = os.path.join(dir, f'processed_emotion_{appid}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                json_data = []
                for row in csv_reader:
                    row['compound'] = int(row['compound'])
                    row['neg'] = int(row['neg'])
                    row['neu'] = int(row['neu'])
                    row['pos'] = int(row['pos'])
                    json_data.append(row)
                
                # 写入到JSON文件
                with open(file_path_json, 'w') as json_file:
                    json.dump(json_data, json_file, indent=4)
        else:
            print(f"No CSV file found for appid {appid}")