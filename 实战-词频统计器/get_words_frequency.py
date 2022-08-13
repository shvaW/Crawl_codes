import jieba
from collections import Counter


def readfile(file_path):
    # windows默认使用GBK读取文件，需要标注解码方式
    with open(file_path, "r", encoding="utf8") as fp:
        text = fp.read()
    return text


# 文件提取
file_name = "novel.txt"
txt = readfile(file_name)

# 分词
words = jieba.cut(txt)
spam_words = ["，", "。", "的", "了", "就", "在", "\n", "着"]
word_list = [word for word in words if word and word not in spam_words]
sum_words = len(word_list)

# 词数统计
res = Counter(word_list)

# 由多到少排序
res_sort = sorted(res.items(), key=lambda x: x[1], reverse=True)
words_top5 = res_sort[:5]
for word in words_top5:
    word_rate = round(word[1] / sum_words, 3)
    print(f"【{word[0]}】出现了{word[1]}次\n， 词频是{word_rate}\n")
