# read(r), write(w), append(a), text mode(t), binary mode(b)

# f = open('./Dockerfile', 'r', encoding='UTF-8')
# print(f.name)
# cts= f.read()
# print(cts)
# f.close()


# with open('./Dockerfile', 'r', encoding='UTF-8') as f:
    # c = f.read()
    # c = f.read(20) # 20byte
    # print(c)
    # line = f.readline()
    # print(line)
    # print(list(c))


with open('./Dockerfile', 'w' ) as f:
    # f.write('FROM apache:2.4.38\n')
    list=['FROM apache:2.4.38\n', 'RUN apt-get update\n', 'USER root\n']
    f.writelines(list)


with open('./log.txt', 'w' ) as f:
    print('Log', file=f)

# with open('./Dockerfile', 'a' ) as f:
#     f.write('RUN apt-get update\n')