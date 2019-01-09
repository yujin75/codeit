from random import randint
in_file = open('vocabulary.txt', 'r')
dict_word = {}

for line in in_file:
    data = line.strip().split(": ")
    dict_word[data[-1]] = data[0]

keys = list(dict_word.keys())

while True:
    random_num = randint(0, len(keys)-1)
    user = input(keys[random_num] + ": ")
    if(user == 'q'):
        break
    if(dict_word[keys[random_num]] == user ):
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % dict_word[keys[random_num]])