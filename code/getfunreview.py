import csv
import os
import sys

max_length = 2**31 -1
csv.field_size_limit(max_length)
# 指定文件夹路径
folder_path = 'D:/ShanghaiTech/Grade3/VIS/finalproject/data/review'

output_folder = os.path.join('D:/ShanghaiTech/Grade3/VIS/finalproject/data', 'output_funny')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 获取文件夹中所有文件的列表
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]




for file in files:
    output_file_name = os.path.join(output_folder, f'output_{file}')
    with open(output_file_name, 'w', newline='', encoding='utf-8') as new_csvfile:
        # 创建CSV写入器
        writer = csv.writer(new_csvfile)
        
        # 打开输入文件
        with open(os.path.join(folder_path, file), 'r',  encoding = 'utf-8') as csvfile:
            # 创建CSV读取器
            reader = csv.reader(csvfile)
            first_row = next(reader)
            try:
                funny_index = first_row.index('votes_funny')
                language_index = first_row.index('language')
            except ValueError:
                continue
            review_index = first_row.index('review')
            desired_columns = [review_index, funny_index]
            writer.writerow([first_row[i] for i in desired_columns if i < len(first_row)])
            # 逐行读取CSV文件
            for row in reader:
                # 仅保留所需列的数据
                if row[language_index] == 'english' and int(row[funny_index]) > 20 and len(row[review_index]) < 100:
                    selected_data = [row[i] for i in desired_columns if i < len(row)]
                
                    # 将选定的数据写入新的CSV文件
                    writer.writerow(selected_data)