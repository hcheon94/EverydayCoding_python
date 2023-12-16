import random
"""
name = input('Enter your name : ')
print(f'Hello, {name}!')
"""
"""
def guessing_number() : # 이건 내가 한거 f'문자열로 바꿔보면
    number = random.randint(0, 100)

    while True :
        user_guess = int(input('what is your guess? :'))
        if user_guess > number:
            print("Too high")
        elif user_guess < number:
            print("Too low")
        elif user_guess == number :
            print("Right!")
            break


guessing_number()
"""

def guessing_game():
    answer = random.randint(0,100) # 랜덤값 변수를 answer라고 정함

    while True :
        user_guess = int(input('what is your guess? ')) # 인풋함수를 반복문 안에 넣음으로써 break가 아니면 계속 입력받음
        if user_guess == answer :
            print(f'Right! The answer is{user_guess}') # 문자열과 변수 같이 출력하기 f'문자열 {변수}'
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else :
            print(f'Your guess of {user_guess} is too high!')


guessing_game()
