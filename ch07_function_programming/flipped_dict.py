#%%
d = {'a':1,'b':2,'c':3}
# %%
"""
{key : VALUE
for ITEM in ITERABLE
}    
ITERABLE에는 지금까지 본 문자열,리스트,튜플,딕셔너리, 세트, 파일 등의 객체 가능
"""
def flipped_dict(dict) :
    return {d[key] : key for key in d} # key : value니까 d['a']=>1이 됨  굿
# %%
def flipped_dict_for(dict) :
    return {
        value : key for key,value in dict.items()
    } 
# %%
