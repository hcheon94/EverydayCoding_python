#%%
for index, letter in enumerate('abc') :
    print(f'{index} : {letter}')
# %%
class MyEnumerate() :
    def __init__(self,data) -> None:
        self.index = 0
        self.data = data
    
    def __iter__(self) :
        return self
    
    def __next__ (self) :
        if self.index >=len(self.data) :
            raise StopIteration
        value = (self.index , self.data[self.index])
        self.index += 1
        return value
    
            
# %%
for index,letter in MyEnumerate('abc') :
    print(f'{index} : {letter}')
# %%
