import re


def tenth_highest(string):
    f = open(string, 'r')
    listt = [s for s in f.readlines()]
    data = listt[0]
    # print(listt[0])

    split_list = re.split('[:]', data)
    # print(split_list)
    split_list = list(map(int, split_list))
    # print(split_list)
    # print(len(split_list))
    listt = list(set(split_list))
    # print("listt", len(listt))

    listt = sorted(listt)
    # print(listt)
    return listt[-10]


# print(tenth_highest("data/data/data01.txt"))


tenth_highest_list = []
for i in range(47):
    i += 1
    if i < 10:
        num = "0"+str(i)
    else:
        num = str(i)

    path = "data/data/data"+num+".txt"
    # print(path)
    tenth_highest_list.append(tenth_highest(path))
    # print(tenth_highest_list)
print(tenth_highest_list)
# print(len(tenth_highest_list))
print(sum(tenth_highest_list))
