import os
import pandas as pd
import json

data_path = os.path.join('D:/ShanghaiTech/Grade3/VIS/finalproject/data', 'genre_top_appids.json')
with open(data_path, 'r') as file:
    data = json.load(file)
    
input_folder = './output_emotion'  # 输入文件夹
output_folder = 'processed_output_emotion_by_gameid'  # 输出文件夹
os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹


for genre, details in data.items():
    for app_id in details['top_10_appids']:
        # 在定义grouped_data之前，需要先初始化grouped_data为一个空DataFrame。
        grouped_data = pd.DataFrame(columns=['date','compound', 'neg', 'neu', 'pos'])
        file_path = os.path.join(input_folder, f'output_emotion_output_{app_id}.csv')
        if os.path.exists(file_path):
            # 读取CSV文件
            df = pd.read_csv(file_path, header=None, names=['emotion', 'timestamp'])
            
            # 将时间戳转换为日期时间格式
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            
            # 将时间段设置为每月，可以使用'df['timestamp'].dt.to_period('M')'来实现。
            df['date'] = df['timestamp'].dt.to_period('M')
            
            
            
            # 按照日期和情绪类型分组并计数
            grouped_data = df.groupby(['date', 'emotion']).size().unstack(fill_value=0)
            grouped_data = grouped_data.reindex(columns=['compound', 'neg', 'neu', 'pos'], fill_value=0)
            # 生成输出文件路径
            output_file_path = os.path.join(output_folder, f'processed_emotion_{app_id}.csv')
            # 将处理后的数据保存到输出文件
            grouped_data.to_csv(output_file_path, index=True)
            
        
        
print("所有文件处理完毕！")