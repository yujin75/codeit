from random import randint
#컴퓨터 list 생성
numbers = []

while len(numbers) < 3:
    new_number = randint(0, 9)

    #중복 판별
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

print("컴퓨터 : ", end = '')
print(numbers)

#게임 시작
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")
user_try = 0
while True:
    i = 1
    user = []
    while i <= 3:
        new_user = int(input("%d번째 수를 입력하세요: " % i))
        #중복 판별
        while new_user in user:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            new_user = int(input("%d번째 수를 입력하세요: " % i))
        #범위 판별
        while new_user < 0 or new_user > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            new_user = int(input("%d번째 수를 입력하세요: " % i))
        #통과
        else:
            user.append(new_user)
            i += 1
    #사용자 list 확인
    print("사용자 : ", end='')
    print(user)

    i = 0; strike = 0; ball = 0

    #strike, ball 여부
    while i < 3:
        if(user[i] == numbers[i]):
            strike += 1
        elif(user[i] in numbers):
            ball += 1
        i = i + 1

    print("%dS %dB\n" % (strike, ball))
    user_try += 1#다시 반복

    #게임 종료 조건
    if(strike == 3):
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % user_try)
        break