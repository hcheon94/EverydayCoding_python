#%%

def join_numbers(numbers):
    
    return ','.join(str(number) for number in  range(numbers) if number<=10) # if는 심화버젼
# %%
all_places = {
    'USA' :['Philadelphia','NewYork','Cleveland','San Jose','San Francisco'],
    'China' : ['Beijing','Shanghai','Guangzhou'],
    'UK' : [ 'London'],
    'India' : ['Hyderabad']
}
# %%
[one_city 
 for one_country , all_cities in all_places.items() 
 for one_city in all_cities]
# %%
all_places.items()
# %%
[(one_city,one_country )
 for one_country , all_cities in all_places.items() 
 for one_city in all_cities]
# %%
[(one_city,one_country )
 for one_country , all_cities in all_places.items() 
 for one_city in sorted(all_cities)]
# %%
# map 함수 예시
words = 'this is a bunch of words'.split()
x = map(len,words) 
print(sum(x))
# %%
#filter 예시
def is_a_long_word(one_word) :
    return len(one_word)>4
x= filter(is_a_long_word,words) # 첫번째는 함수, 두번째는 이터러블, T,F를 활용해서 필터하는 역할
print(' '.join(x))
# %%
import operator
letters = 'abcd'
numbers = range(1,5)
x = map(operator.mul,letters,numbers) # letters와 numbers에 있는 요소를 하나씩 꺼내서 곱하기함
print(' '.join(x))

print(' '.join(operator.mul(one_letter,one_number)for one_letter, one_number in zip(letters,numbers))) # 내포로 했을때
# %%
