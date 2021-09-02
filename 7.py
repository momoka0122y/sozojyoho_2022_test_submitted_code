
import re


f = open('data/infections2.txt', 'r')


listt = [s for s in f.readlines()]
data = listt[0]
# print(listt[0])

split_list = list(map(int, re.split('[:]', data)))
print(split_list)
print()

n = len(split_list)
IX, I, X, I2 = 0, 0, 0, 0
for i in range(len(split_list)):
    IX += i*split_list[i]
    I += i
    X += split_list[i]
    I2 = i**2

a = (n*IX - I*X)/(n*I2-I**2)
k = (I2*X - IX*I)/(n*I2-I**2)


print(a, k)
