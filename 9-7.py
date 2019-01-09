in_file = open('chicken.txt', 'r')

sum = 0
day = 0
for line in in_file:
    #매출 총합 구하기
    sum += int(line.strip().split(": ")[-1])
    #일수 세기
    day += 1

#평균 계산
print(sum / day)
in_file.close()