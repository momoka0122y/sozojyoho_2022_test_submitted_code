import re


f = open('data/infections.txt', 'r')


listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))

# print(split_list)
# print(len(split_list))
listt = list(set(split_list))  # 重複なくす
# print("listt", len(listt))

listt = sorted(listt)
print(listt)
print(listt[-10])
