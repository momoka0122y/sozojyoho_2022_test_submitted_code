import re


# print(tenth_highest("data/data/data01.txt"))
def get_ruijido(path_i, path_j):
    f_i = open(path_i, 'r')
    f_j = open(path_j, 'r')

    data_list_i = list(
        map(int, re.split('[:]', [s for s in f_i.readlines()][0])))

    data_list_j = list(
        map(int, re.split('[:]', [s for s in f_j.readlines()][0])))

    # print(data_list_i)
    # print(data_list_i)
    if len(data_list_i) > len(data_list_j):
        n = len(data_list_j)
        m = len(data_list_i)
        y_list = data_list_j
        x_list = data_list_i
    else:
        n = len(data_list_i)
        m = len(data_list_j)
        y_list = data_list_i
        x_list = data_list_j

    min_i = float("inf")
    min_s = float("inf")
    for i in range(m-n+1):
        s = 0
        for k in range(n):
            s += (x_list[k+i]-y_list[k])**2
        if s < min_s:
            min_s = s
            min_i = i
        # print(-s)
    return min_i, -min_s


print(get_ruijido("data/data/data02.txt", "data/data/data42.txt"))
max_ruijido = float("-inf")
paths = []
for i in range(46):
    i += 1
    if i < 10:
        num = "0"+str(i)
    else:
        num = str(i)

    for j in range(i+1, 47):
        j += 1
        if j < 10:
            num_j = "0"+str(j)
        else:
            num_j = str(j)

        path_i = "data/data/data"+num+".txt"
        path_j = "data/data/data"+num_j+".txt"

        i, ruijido = get_ruijido(path_i, path_j)
        # print(ruijido)
        if ruijido > max_ruijido:
            max_ruijido = ruijido
            paths = [(path_i, path_j)]
        elif ruijido == max_ruijido:
            paths.append((path_i, path_j))
print(max_ruijido)
print(paths)
