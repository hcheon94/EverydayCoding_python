#%%
#이터러블 객체의 요소 하나하나를 함수의 매개변수로 전달해야 하는 경우 많이 사용되는 코드
# 매개변수로 리스트를 전달할때 *[1,2,3] 이런식으로 전달
def mysum(*numbers) :
    output=0
    for number in numbers:
        output = output + number
        print(output,number)
        
    return output
# %%
num_list = [1,2,3,4]
print(mysum(*num_list))
# %%
#예제1 기본적인 sum함수처럼 첫 번째 매개변수로 리스트를 받고, 두 번째 매개변수로 어떤숫자를 더할지 지정
def yourSum (num,*nums):
    sum = 0
    output = 0
    for number in nums :
        sum = number
    output = num + sum
    return output
# %%
#평균구하기
def myAvg (*numbers) :
    
    output=0
    for number in numbers:
        output = output + number
        
    return output/len(numbers)

# %%
strList = ['average','sum','minus']

def Strcal(*strlist):
    resultList = []
    sum=max=min=tmp = 0
    for i in strlist :
        tmp = len(i)
        sum += tmp
        if min == 0:
            min = tmp
        if max <= tmp :
            max = tmp
        elif min >=tmp :
            min = tmp
        
    resultList.append(max)
    resultList.append(min)
    resultList.append(sum/len(strlist))
    return resultList
        
    
# %%
