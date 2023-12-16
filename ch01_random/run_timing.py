#%%
def run_timing() :
    number_of_runs = 0
    total_time = 0
    while True:
        one_run = input('Enter 10 km run time :')
        if not one_run :
            break
        
        number_of_runs += 1
        total_time += float(one_run) 
        
        average_time = total_time/number_of_runs
        
        print(f'Average of {average_time:.2f}, over{number_of_runs} runs')
        
run_timing()
# %%
# ++ 부동소수점 1개와 정수 2개를 매개변수로 받고 before만큼 부동소수점의  정수부분,after만큼 소수점 아래부분 추출
def float_before_after():
    float_num = float(input('what float number : '))
    before = int(input('what before   number :'))
    after = int(input('what after number :'))
    
    print (f'{float_num:.nf}')
# %%
