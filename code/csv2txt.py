import csv
import os


# 指定文件夹路径
folder_path = 'D:/ShanghaiTech/Grade3/VIS/finalproject/data/output_english'

output_folder = os.path.join('D:/ShanghaiTech/Grade3/VIS/finalproject/data', 'txt')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 获取文件夹中所有文件的列表
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

for file in files:
    output_file_name = os.path.join(output_folder, f'{file[:-4]}.txt')
        
    # 打开输入文件
    with open(os.path.join(folder_path, file), 'r',  encoding = 'utf-8') as csvfile:

            reader = csv.reader(csvfile)
            
            # 打开TXT文件
            with open(output_file_name, mode='w', encoding='utf-8') as txt_file:
                
                try:
                    first_row = next(reader)
                except StopIteration:
                    continue
                
                try:
                    author_index = first_row.index('author')
                    language_index = first_row.index('language')
                    review_index = first_row.index('review')
                    timestamp_index = first_row.index('timestamp_created')
                    votes_up_index = first_row.index('votes_up')
                    funny_index = first_row.index('votes_funny')
                    comment_index = first_row.index('comment_count')
                except ValueError:
                    continue
                # 遍历CSV中的每一行
                for row in reader:
                    txt = row[review_index]
                    # 将每一行转换为字符串，并用逗号分隔各个字段
                    # 写入到TXT文件，并添加换行符
                    txt_file.write(txt + '\n')