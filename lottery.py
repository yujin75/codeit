from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    list = []
    for num in range(1, 7):
        lot_num = randint(1, 45)
        while lot_num in list:
            lot_num = randint(1, 45)
        list.append(lot_num)
    list.sort()
    return list

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    list = generate_numbers()
    bonus = randint(1, 45)
    while bonus in list:
        bonus = randint(1, 45)
    list.append(bonus)
    return list

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    match = 0
    for i1 in range(len(list1)):
        if(list1[i1] in list2):
            match += 1
    return match

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    winning_gen = winning_numbers[0:6]
    match = count_matching_numbers(numbers, winning_gen)
    if(match == 6):
        return 1000000000
    elif(match == 5 and winning_numbers[-1] in numbers):
        return 50000000
    elif(match == 5):
        return 1000000
    elif(match == 4):
        return 50000
    elif(match == 3):
        return 5000
    else:
        return 0