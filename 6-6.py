from random import randint
i = 4
#랜덤수 생성
answer = randint(1, 20)

#4번의 기회
while i>0:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % i))
    if(guess == answer):
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (4-i+1))
        break
    elif(guess > answer):
        print("Down")
        i = i - 1
    else:
        print("Up")
        i = i - 1
if(i == 0):
    print("아쉽습니다. 정답은 %d였습니다." % answer)