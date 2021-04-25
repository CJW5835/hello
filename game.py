import random

num = int(input("로또 추첨 수를 입력하세요 : "))

print("로또 번호 추출기 입니다.")
print("-----------------")
# 넣은 수 만큼 출력반복
for x in range(1, num+1):
    lotto = [0, 0, 0, 0, 0, 0]

    lotto[0] = random.randrange(1, 46, 1)

    lotto[1] = lotto[0]
    lotto[2] = lotto[0]
    lotto[3] = lotto[0]
    lotto[4] = lotto[0]
    lotto[5] = lotto[0]

    #중복수 제거
    while (lotto[0] == lotto[1]):
        lotto[1] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[2] or lotto[1] == lotto[2]):
        lotto[2] = random.randrange(1, 46, 1)    
    while (lotto[0] == lotto[3] or lotto[1] == lotto[3] or lotto[2] == lotto[3]):
        lotto[3] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[4] or lotto[1] == lotto[4] or lotto[2] == lotto[4] or lotto[3] == lotto[4]):
        lotto[4] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[5] or lotto[1] == lotto[5] or lotto[2] == lotto[5] or lotto[3] == lotto[5] or lotto[4] == lotto[5]):
        lotto[5] = random.randrange(1, 46, 1)
        
        
    lotto.sort() 
    print(lotto)       
print("--가즈아ㅏ아아아아아아!!!!--")

#교수님 저는 이 추출기로 일확천금을 따오겠습니다.

#전에 강의 때 만들었던 아이디는 운영정책 위반으로 정지되있습니다. 왜 정지당한지는 모르겠습니다.
#그래서 새 아이디를 만들어서 했습니다.
