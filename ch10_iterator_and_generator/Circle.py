#%%
#보조 이터레이터클래스로 구현 여기서  __next__함수를 구현하는건데 생성자에서 인덱스 선언해줌
#__next__에서는 StopIteration을 걸어줘서 맥스값보다 크면 다시 인덱스 0으로 
# index값은 계속 올려도 됨 %로 장치를 걸어줬기때문에
# 그다음 return value로 값전달
class CircleIterator () :  
    def __init__(self,data,max_times) -> None:
        self.data = data
        self.max_items = max_times
        self.index=0
    def __next__ (self) :
        if self.index >= self.max_items :
            raise StopIteration
        value = self.data[self.index%len(self.data)]
        self.index += 1
        return value
    
class Circle() :
    def __init__(self,data,max_times) -> None:
        self.data = data
        self.max_times = max_times
        
    def __iter__(self) :
        return CircleIterator(self.data,self.max_times)
    
c = Circle('abc',5)
print(list(c))
# %%
