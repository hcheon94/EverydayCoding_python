#%%
from Zoo import Parrot,Sheep,Snake,Wolf
class Cage ():
    def __init__(self,id_number) -> None:
        self.animals = []
        self.id_number = id_number
        
    def __repr__(self) -> str:
        output =  f'Cage{self.id_number}'
        output += '\n'.join('\t' +str(animal) for animal in self.animals)
        return output 
    
    def add_animal(self,*animals) :
        for one_animal in animals :
            self.animals.append(one_animal)
        
# %%
wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')
# %%
c1 = Cage(1)
# %%
c1.add_animal(wolf,sheep)
# %%
print(c1)
# %%
