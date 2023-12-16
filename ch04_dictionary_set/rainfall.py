#%%
def get_rainfall() :
    rainfall = {}
    while True :
        city_name = input('Enter city name : ').strip()
        if not city_name :
            break
        mm_rainfall = input('Enter_mm_rain : ')
        rainfall[city_name] = rainfall.get(city_name,0) +int(mm_rainfall)
        #get(x,'~~~') x라는 key가 딕셔너리에 없는 경우 ~~~라는 디폴트값을 돌려줌 여기선 0을 디폴트로 주고 강수량을 더해주는것
        
        for city, rain in rainfall.items():
            print(f'{city}: {rain}')
#%%
#예외처리 버전 try catch
def get_rainfall() :
    rainfall = {}
    while True :
        city_name = input('Enter city name : ').strip()
        if not city_name :
            break
        try :
            mm_rainfall = input('Enter_mm_rain : ')
        except ValueError:
            print('You didn`t enter a valid integer; try again')
            continue
        #이부분이 핵심이네여 get메소드 알아 놓기
        rainfall[city_name] = rainfall.get(city_name,0) +int(mm_rainfall)
       
        
        for city, rain in rainfall.items(): 
            print(f'{city}: {rain}') #한꺼번에 for문을 반복할때 items를 씁니다
# %%
#defaultdict 활용
from collections import defaultdict
def get_rainfall() :
    rainfall = defaultdict(int)
    while True :
        city_name = input('Enter city name : ').strip()
        if not city_name :
            break
        try :
            mm_rainfall = input('Enter_mm_rain : ')
        except ValueError:
            print('You didn`t enter a valid integer; try again')
            continue
        #이부분이 핵심이네여 get메소드 알아 놓기
        #rainfall[city_name] = rainfall.get(city_name,0) +int(mm_rainfall)
        rainfall[city_name] +=int(mm_rainfall)
       
        
        for city, rain in rainfall.items(): 
            print(f'{city}: {rain}') #한꺼번에 for문을 반복할때 items를 씁니다
# %%
