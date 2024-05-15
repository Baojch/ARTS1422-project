import json
import os
import re
import csv

csv.field_size_limit(500 * 1024 * 1024)

# 指定目录和输入的JSON文件
directory = 'data/reviews'
genre_appids_file = 'data/genre_top_appids.json'

# 读取包含appids的JSON文件
with open(genre_appids_file, 'r',encoding='utf-8',errors = 'ignore') as f:
    genre_data = json.load(f)

# 准备一个结果字典
results = {}

# 函数，用于去除非标准Unicode字符
def clean_text(text):
    # 正则表达式，用于保留可打印字符并去除特殊字符
    cleaned_text = re.sub(r'[^\x20-\x7E]', '', text)  # 只保留ASCII可打印字符
    return cleaned_text.strip()  # 去除两侧空白

# 遍历各个类型和对应的top appids
for genre, data in genre_data.items():
    top_appids = data.get("top_10_appids", [])
    
    # 创建一个列表来存储每个genre的name和metacritic score
    genre_results = []
    
    for appid in top_appids:
        # 构造文件路径
        file_path = os.path.join(directory, f"{appid}.csv")
        
        num_comment=0
        voted_up=0
        playtime=0
        negative=0
        comment_comment=0
        if os.path.exists(file_path):
            with open(file_path, 'r',encoding='utf-8',errors = 'ignore') as app_file:
                reader=csv.reader(app_file)
                next(reader)
                for row in reader:
                    num_comment+=1
                    if row[7]!='True' and row[7]!='False':
                        voted_up+=int(row[7])
                        tmp=eval(row[1])["playtime_forever"]
                        if tmp==None:
                            tmp=0
                        playtime+=int(tmp)
                        negative+=0
                        comment_comment+=int(row[10]) 
                    
        emotion_path="data/processed_emotion/"+"processed_emotion_"+f"{appid}.csv"
        with open(emotion_path, 'r',encoding='utf-8',errors = 'ignore') as emotions:
            reader=csv.reader(emotions)
            next(reader)
            for row in reader:
                negative+= int(row[2])
        
        genre_results.append({
            "appid": appid,
            "num_comment":num_comment,
            "playtime":playtime,
            "voted_up":voted_up,
            "negative":negative,
            "comment_comment":comment_comment,
        })
    
    # 将这个genre的结果加入最终结果
    results[genre] = genre_results

# 定义输出文件名
output_filename = 'data/compareinfo.json'

# 将结果保存到JSON文件
with open(output_filename, 'w',encoding='utf-8',errors = 'ignore') as out_file:
    json.dump(results, out_file, ensure_ascii=False, indent=4)  # 使用indent参数使输出更具可读性

print(f"Results have been saved to {output_filename}.")