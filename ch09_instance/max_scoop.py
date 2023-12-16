#%%
class Scoop() :
    
    def __init__(self,flavor:str) -> str:
        self.flavor = flavor
    
    
class Bowl() :
    max_scoops = 3
    def __init__(self) -> None:
        self.scoops = []
        
    def add_scoops(self,*new_scoops) :
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops :
                self.scoops.append(one_scoop)
            
    def __repr__(self) -> str:
        return '\n'.join(s.flavor for s in self.scoops)
#%%    
class Bigbowl(Bowl) :
    max_scoops = 5 
    
# %%
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor4')
s5 = Scoop('flavor5')
# %%
bb=Bigbowl()
bb.add_scoops(s1,s2)
# %%
bb.add_scoops(s3)
# %%
bb.add_scoops(s4,s5)
#%%
print(bb)
#%%
