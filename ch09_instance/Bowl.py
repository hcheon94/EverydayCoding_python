#%%

class Bowl :
    def __init__(self) -> None:
        self.scoops = []
        
    def add_scoops(self,*new_scoops) :
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
            
    def __repr__(self) -> str:
        return '\n'.join(s.flavor for s in self.scoops)
# %%
from dataclasses import dataclass, field
from typing import List
from Scoop import Scoop

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b= Bowl()
b.add_scoops(s1,s2)
b.add_scoops(s3)
# %%
#bowl을 데이터 클래스로 정의 한다면

@dataclass
class Bowl() :
    scoops : List[Scoop] = field(default_factory=list)
    
    def add_scoops(self,*new_scoops):
        for one_scoop in new_scoops :
            self.scoops.append(one_scoop)
            
    def __repr__ (self):
        return '\n'.join(s.flavor for s in self.scoops)
# %%
