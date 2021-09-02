import re


f = open('data/infections.txt', 'r')


listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))
print(split_list)

maxx = -100
minn = float("inf")
n = len(split_list)
print()
summ = 0
for i in range(3, n-3):
    ave_i = sum(split_list[i-3:i+4])/7
    if ave_i > maxx:
        maxx = ave_i
    if ave_i < minn:
        minn = ave_i
    summ += ave_i

print(maxx, minn, summ)
