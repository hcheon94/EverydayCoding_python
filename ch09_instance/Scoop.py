#%%
class Scoop :
    
    def __init__(self,flavor:str) -> str:
        self.flavor = flavor
    
    

def create_scoops() :
    scoops = [Scoop(flavor) for flavor in ('choco','vanila','persimmon')]
    for scoop in scoops :
        print(scoop.flavor)
    


# %%
#추가문제 Beverage 클래스 만들기
class Beverage :
    def __init__(self, name:str,temperature:int) -> None:
        self.name = name
        self.temperature = temperature
        
# %%
def create_beverage () :
    beverages = [Beverage('pocari',75),Beverage('coke',65),Beverage('juice',80)]
    for beverage in beverages :
        print(f'첫번째 음료는 {beverage.name}이고 온도는{beverage.temperature}이죠')
    # %%
#class에서 name만 주어졌을때 온도를 75도로 하기
class Beverage :
        def __init__(self, name:str,temperature:int=75) -> None:
            self.name = name
            self.temperature = temperature
# %%
