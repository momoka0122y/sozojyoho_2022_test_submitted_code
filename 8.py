import re
import math

f = open('data/infections2.txt', 'r')


listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))

math.log()
n = len(split_list)


max_a = float("-inf")
for s in range(n-30):
