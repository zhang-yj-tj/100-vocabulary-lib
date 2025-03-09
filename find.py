import sqlite3

try:
    # 连接到数据库
    conn = sqlite3.connect("baicizhanciku\\words.db")
    cursor = conn.cursor()
except:
    print("连接词库失败")
    
def get_mean_cn(word):
    """
    根据输入的单词查询数据库并返回对应的mean_cn字段。
    
    :param word: 需要查询的单词
    :return: 如果找到匹配的单词，返回mean_cn；否则返回提示信息
    """
    # 去除单词两端的空格并转换为小写
    cleaned_word = word.strip().lower()
    
    # 去掉单词中的所有空格
    cleaned_word_no_space = cleaned_word.replace(" ", "")
    
    try:
        # 执行模糊查询，去掉数据库中单词的空格并转换为小写
        cursor.execute("SELECT mean_cn FROM words WHERE LOWER(REPLACE(word, ' ', '')) = ?", (cleaned_word_no_space,))
        
        # 获取查询结果
        result = cursor.fetchone()
        
        # 返回结果
        if result:
            return result[0]
        else:
            return word
    except sqlite3.Error as e:
        print(f"查询时发生错误: {e}")
        return word

def count_words():
    """
    查询数据库中单词的总数。
    
    :return: 单词的总数
    """
    # 连接到数据库
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    
    # 执行查询
    cursor.execute("SELECT COUNT(*) FROM words")
    
    # 获取查询结果
    result = cursor.fetchone()
    
    # 关闭连接
    conn.close()
    
    # 返回总数
    if result:
        return result[0]
    else:
        return 0

def remove_duplicates():
    """
    删除数据库中重复的单词项，只保留第一个出现的单词。
    """
    try:
        # 获取所有单词
        cursor.execute("SELECT rowid, word FROM words")
        words = cursor.fetchall()

        # 创建一个字典来存储单词及其行号
        word_dict = {}

        for rowid, word in words:
            # 去除单词两端的空格并转换为小写
            cleaned_word = word.strip().lower()
            # 去掉单词中的所有空格
            cleaned_word_no_space = cleaned_word.replace(" ", "")

            # 如果单词已经在字典中，标记为重复
            if cleaned_word_no_space in word_dict:
                cursor.execute("DELETE FROM words WHERE rowid = ?", (rowid,))
            else:
                word_dict[cleaned_word_no_space] = rowid

        # 提交事务
        conn.commit()

        print("重复项已成功删除。")
    except sqlite3.Error as e:
        print(f"删除重复项时发生错误: {e}")
        
def appenddb(word, mean_cn):
    try:      
        # 执行插入操作
        cursor.execute("INSERT INTO words (word, mean_cn) VALUES (?, ?)", (word, mean_cn))
        
        # 提交事务
        conn.commit()
        
        #print(f"单词 '{word}' 已成功添加到数据库。")
    except sqlite3.Error as e:
        print(f"添加单词时发生错误: {e}")

# 示例用法
if __name__ == "__main__":
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    remove_duplicates()
    print(f"数据库中总共有 {count_words()} 个单词。")
    while 1:
        word = input("请输入要查询的单词: ")
        print(get_mean_cn(word))
