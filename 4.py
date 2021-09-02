import re


f = open('data/infections.txt', 'r')

listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))
print("data")
print(split_list)
print()


diff_list = []

before = 0
for num in split_list:
    diff_list.append(num-before)
    before = num


def find_maximum_sum_from_diff_data(diff_list):
    now = [0, 0]
    maxx = [0, 0, 0]  # sum,start,length
    for i, num in enumerate(diff_list, 1):
        if now[0] <= 0:
            now = [num, i]
        elif now[0]+num > num:
            now[0] = now[0]+num
            if now[0] > maxx[0]:
                maxx = [now[0], now[1], i-now[1]]
            if now[0] == maxx[0] and i-now[1] < maxx[2]:
                maxx = [now[0], now[1], i-now[1]]

    return maxx[0], maxx[1], maxx[1]+maxx[2]


print("diff")
print(diff_list)
# print(find_maximum_sum_from_diff_data([5, -1, 2, -6, 7, 8]))
print()
print("ans")
print(find_maximum_sum_from_diff_data(diff_list))
# print(find_maximum_sum_from_diff_data(diff_list[108:306]))
