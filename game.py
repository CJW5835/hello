import random
print("빙고와 단어맞추기")
print("1. 5자리 1~20 빙고판 ")
print(" 5자리 빙고를 시작합니다.")

num = int(input("빙고판의 갯수를 정해주세요 : "))


print("빙고판이 출력됩니다..")
print("-----------------")
# 넣은 수 만큼 출력반복
for x in range(1, num+1):
    bingo = [0, 0, 0, 0, 0, 0]

    bingo[0] = random.randrange(1, 20, 1)

    bingo[1] = bingo[0]
    bingo[2] = bingo[0]
    bingo[3] = bingo[0]
    bingo[4] = bingo[0]
    bingo[5] = bingo[0]

    #중복수 제거
    while (bingo[0] == bingo[1]):
        bingo[1] = random.randrange(1, 20, 1)
    while (bingo[0] == bingo[2] or bingo[1] == bingo[2]):
        bingo[2] = random.randrange(1, 20, 1)    
    while (bingo[0] == bingo[3] or bingo[1] == bingo[3] or bingo[2] == bingo[3]):
        bingo[3] = random.randrange(1, 20, 1)
    while (bingo[0] == bingo[4] or bingo[1] == bingo[4] or bingo[2] == bingo[4] or bingo[3] == bingo[4]):
        bingo[4] = random.randrange(1, 20, 1)
    while (bingo[0] == bingo[5] or bingo[1] == bingo[5] or bingo[2] == bingo[5] or bingo[3] == bingo[5] or bingo[4] == bingo[5]):
        bingo[5] = random.randrange(1, 20, 1)
        
        
    bingo.sort() 
    print(bingo)       
x = int(input("대기시간을 입력하세요"))

for i in range(1, x+1):

    for j in range(x+1-i):
        print("",end="")

    for j in range(2*i-1):
        print("*",end="")
    print()


print('2. 단어 맞추기 게임')
print('단어를 맞추는 게임 입니다.')

dictionary = {
    'zoo': '동물원', 
    '痛み': '고통',
    '가장 존경하는 인물': '교수님' 
}

keys = list(dictionary.keys())
random.shuffle(keys)

count = 0
for english in keys:
    korean = dictionary[english]

    guess = input('{} 맞춰보세요: '.format(english))

    if guess == korean: 
        print(' 맞습니다.') 
        count += 1
    else: 
        print('틀립니다.')

score = count / len(dictionary) * 100
print('100 점 만점 {} 점입니다.'.format(score))

print("게임이 끝났습니다.")

#교수님 강의때 쓰던 깃허브 아이디가 어째서인지 정지되있어서 
#깃허브 아이디를 새로 만들어서 하느라 저장된게 없어졌습니다.
#그 결과 종합게임선물세트가 탄생했습니다.
#20180943 2C 차정원

#빙고판에서 [](리스트)랑 랜덤함수 사용했고 영단어 맞추기에서 딕셔너리 사용했습니다.
#교수님 저는 A를 받고싶어서 열심히 했습니다. 
#근대 안될것 같아서 머리를 짜낸 결과 이렇게 나왔습니다.
#뵐 면목이 없습니다...