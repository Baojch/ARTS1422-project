import json
import os
import csv

genre_appids_file = 'data/genre_top_appids.json'

# 读取包含appids的JSON文件
with open(genre_appids_file, 'r') as f:
    genre_data = json.load(f)

# print(genre_data)
keys = genre_data.keys()
print(keys)

dir = 'data/processed_output_emotion_by_gameid'


for key in keys:
    date_ranges = set()  # 使用集合来存储日期范围，以确保不重复

    appid_list = genre_data[key]['top_10_appids']
    for appid in appid_list:
        file_path = os.path.join(dir, f'processed_emotion_{appid}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                # 获取日期范围列表
                date_range = [entry['date'] for entry in data]
                date_ranges.update(date_range)  # 将日期范围添加到集合中
    
    # 对日期范围进行排序并计算并集
    sorted_date_ranges = sorted(date_ranges)
    oldest_date = sorted_date_ranges[0]
    newest_date = sorted_date_ranges[-1]
    # print(len(sorted_date_ranges))
    # print(f"Genre: {key}, Oldest Date: {oldest_date}, Newest Date: {newest_date}")
    json_data = []
    for date in sorted_date_ranges:
        row = {'date': date, 'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
        datenum = 0
        
        for appid in appid_list:
            file_path = os.path.join(dir, f'processed_emotion_{appid}.json')
            if os.path.exists(file_path):
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    for entry in data:
                        if entry['date'] == date:
                            row['compound'] += entry['compound']
                            row['neg'] += entry['neg']
                            row['neu'] += entry['neu']
                            row['pos'] += entry['pos']
                            datenum += 1
        
        if datenum > 0:
            row['compound'] = int(row['compound'] / datenum)
            row['neg'] = int(row['neg'] / datenum)
            row['neu'] = int(row['neu'] / datenum)
            row['pos'] = int(row['pos'] / datenum)
        
        json_data.append(row)
    output_file_path = os.path.join("data/average_processed_output_emotion", f'{key}.json')
    with open(output_file_path, 'w') as output_file:
        json.dump(json_data, output_file, indent=4)



