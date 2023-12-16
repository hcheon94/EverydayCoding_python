# 전에 코드 복사욤
import random
def guessing_game():
    answer = random.randint(0,100) # 랜덤값 변수를 answer라고 정함
    count = 3

    while (True) :
        user_guess = int(input('what is your guess? '))  # 인풋함수를 반복문 안에 넣음으로써 break가 아니면 계속 입력받음

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}') # 문자열과 변수 같이 출력하기 f'문자열 {변수}'
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
            count = count-1
            print(count)
        else:
            print(f'Your guess of {user_guess} is too high!')
            count = count-1
            print(count)
        if count == 0:
            print(f'정답을 맞추지 못하였습니다. 정답은 {answer}')



guessing_game()

