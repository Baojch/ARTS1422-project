import json
import os
import re

# 指定目录和输入的JSON文件
directory = 'data/detail'
genre_appids_file = 'data/genre_top_appids.json'

# 读取包含appids的JSON文件
with open(genre_appids_file, 'r') as f:
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
        file_path = os.path.join(directory, f"{appid}.json")
        
        # 检查文件是否存在
        if os.path.exists(file_path):
            with open(file_path, 'r') as app_file:
                app_data = json.load(app_file)
                
                # 提取name和metacritic的score
                raw_name = app_data.get("name", "Unknown")
                name = clean_text(raw_name)
                metacritic_score = app_data.get("metacritic", {}).get("score", "N/A")
                
                # 将结果加入genre_results
                genre_results.append({
                    "appid": appid,
                    "name": name,
                    "metacritic_score": metacritic_score
                })
    
    # 将这个genre的结果加入最终结果
    results[genre] = genre_results

# 定义输出文件名
output_filename = 'data/gameinfo.json'

# 将结果保存到JSON文件
with open(output_filename, 'w') as out_file:
    json.dump(results, out_file, ensure_ascii=False, indent=4)  # 使用indent参数使输出更具可读性

print(f"Results have been saved to {output_filename}.")