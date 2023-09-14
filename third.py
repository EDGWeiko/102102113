import csv
from collections import Counter
import pandas as pd

list_set = []
with open("./bili_danmu2.csv", 'r', encoding ='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:                         #读取每一列数据
        for word in row:                       #读取每一个元素
            if '\u4e00' <= word <= '\u9fff':   #判断是否为中文字符串
                list_set.append(word)          #元素添加到集合

words_count = Counter(list_set)
statics = words_count.most_common()[:20]   #得到词频排序前20名
comments_dict = {'comments': statics}  # 定义一个字典
df = pd.DataFrame(comments_dict)
df.to_csv('top20.csv', encoding='utf-8-sig')  # 保存为csv格式的文件