#%%
class Book :
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
class Shelf :
    
    def __init__(self):
        self.books = []
        self.total_price = 0 
    def add_book(self, *books) : 
        for one_book in books :
            self.books.append(one_book)
            
    def __repr__(self) -> str:
        return '\n'.join(b.title + ":" + str(b.price) for b in self.books)
    
    def calculate_total_price(self) :
        for book in self.books :
            self.total_price += book.price
        return self.total_price
# %%
b = [Book('가짜노동','외국인', 15000),Book('소통의 온도','한국인',7000),Book('벽어쩌구','일본인',45600)]


# %%

print(b)
# %%
print(b[0])
# %%
shelf  = Shelf()
for book in b :
    shelf.add_book(book)
 
# %%
print(shelf)
# %%
print(shelf.calculate_total_price())   
# %%
