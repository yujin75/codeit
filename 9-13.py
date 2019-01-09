in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    user = input(data[-1] + ": ")
    if(user == data[0]):
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % data[0])

in_file.close()