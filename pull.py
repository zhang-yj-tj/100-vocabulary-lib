import os
import json
import re
import sqlite3
import tqdm

# 定义目标文件夹路径
base_folder = "000总库"

# 创建SQLite数据库
conn = sqlite3.connect("words.db")  # 数据库文件名
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    mean_cn TEXT NOT NULL
)
''')

# 遍历文件夹
for root, dirs, files in tqdm.tqdm(os.walk(base_folder)):
    for file in files:
        if file == "word.json":
            # 获取文件路径
            json_file_path = os.path.join(root, file)
            try:
                # 读取JSON文件
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # 提取需要的字段
                word = data.get("word", "")
                mean_cn = data.get("mean_cn", "")
                
                # 清洗mean_cn字段：去除所有英文字母和'.' 
                cleaned_mean_cn = re.sub(r'[a-zA-Z\.]', '', mean_cn)
                
                # 插入数据库
                cursor.execute('''
                INSERT INTO words (word, mean_cn)
                VALUES (?, ?)
                ''', (word, cleaned_mean_cn))
            
            except Exception as e:
                print(f"Error processing {json_file_path}: {e}")

# 提交事务并关闭连接
conn.commit()
conn.close()

print("所有数据已成功存储到SQLite数据库中！")
