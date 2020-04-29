# 基于列表的算法：冒泡排序法
records = [19, 9, 7, 20, 6, 1, 1, 2]
i = 0
compare = 0
len_records = len(records)
while i < len_records:
    j = 1
    while j < len_records - i:
        if records[j - 1] > records[j]:
            compare = records[j - 1]
            records[j - 1] = records[j]
            records[j] = compare
        j+=1
    i+=1
print(records)
