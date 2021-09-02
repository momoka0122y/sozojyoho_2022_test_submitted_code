import re


f = open('data/infections.txt', 'r')


listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))
# print(split_list)


diff_list = []

before = 0
for num in split_list:
    diff_list.append(num-before)
    before = num
# print(diff_list)
ans = ""
for num in diff_list:
    if num >= 0:
        ans += "+"+str(num)
    else:
        ans += str(num)
print(ans)
# print(len(ans))
