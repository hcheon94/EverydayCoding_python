#%%
# reversed와 enumerate 함수 사용하긔
#16진수를 입력받고 10진수로 변환해서 리턴하는 함수
for index, one_letter in enumerate('abcd'):
    print(f'{index}:{one_letter}')
    
# %%
def hex_output(int_num):
    int_sum = 0
    str_num = str(int_num)
    hex_num = '0x'+str_num 
    
    for index,one_number in enumerate(reversed(hex_num)):
        int_sum = int_sum + int(one_number) * (16**index)
        if one_number == 'x':
            break
    
    return hex_num
    
    
# %%
#정답
#enumerate함수, reversed함수, int()함수 알기, 무식하게 억지로 바꿔주지 않기
#인자 입력받는거 생활화 하기
def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ') #매개변수없이 input()으로 인자받기
    for power, digit in enumerate (reversed(hexnum)):
        print(f'{power},{digit}')
        decnum += int(digit,16)*(16**power)
    print(decnum)
# %%
