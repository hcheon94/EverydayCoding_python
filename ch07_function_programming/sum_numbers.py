#%%

def sum_numbers () :
    str_num = input('문자열 쓰세요')
    words = str_num.split()
    return sum(int(num_word) for num_word in words if num_word.isdigit())

# %%
sum_numbers()
# %%
#텍스트 파일을 읽어 들이고 20글자 이상이면서 적어도 하나의 모음을 포함하고 있는 줄일 출력해라

def txt_function (filename) :
    try:
        with open(filename,'r') as file :
            filtered_line = [line.strip() for line in file if len(line.strip()) >=20 and any( char.lower() in 'aeiou'for char in line)]
    except FileNotFoundError :
        print(f"파일 '{filename}'을 찾을 수 없습니다.")
    return filtered_line
# %%
