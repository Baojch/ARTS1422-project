import json
import os
import re
import csv

# 指定目录和输入的JSON文件
directory = 'data/fun_comment'
genre_appids_file = 'data/genre_top_appids.json'

# 读取包含appids的JSON文件
with open(genre_appids_file, 'r') as f:
    genre_data = json.load(f)

# 准备一个结果字典
results = {}

def clean_text(text):
    # 正则表达式，用于保留可打印字符并去除特殊字符
    cleaned_text = re.sub(r'[^\x20-\x7E]', '', text)  # 只保留ASCII可打印字符
    return cleaned_text.strip()  # 去除两侧空白

for genre, data in genre_data.items():
    top_appids = data.get("top_10_appids", [])
    
    # 创建一个列表来存储每个genre的name和metacritic score
    
    for appid in top_appids:
        # 构造文件路径
        file_path = os.path.join(directory, "output_"+f"{appid}.csv")
        
        # 检查文件是否存在
        if os.path.exists(file_path):
            with open(file_path, 'r',encoding='utf-8',errors = 'ignore') as app_file:
                reader = csv.reader(app_file)
                next(reader)
                comment={"default1":-1,"default2":-1,"default3":-1,"default4":-1,"default5":-1}
                for row in reader:
                    comment[row[0]]=int(row[1])
                    
                
                comments=sorted(comment.items(),key=lambda item:item[1],reverse=True)
                # 将结果加入results
                results[str(appid)]=[comments[0][0],comments[1][0],comments[2][0],
                                    comments[3][0],comments[4][0]]



output_filename = 'data/fun_comment.json'

# 将结果保存到JSON文件
with open(output_filename, 'w',encoding='utf-8',errors = 'ignore') as out_file:
    json.dump(results, out_file, ensure_ascii=False, indent=4)  # 使用indent参数使输出更具可读性

print(f"Results have been saved to {output_filename}.")