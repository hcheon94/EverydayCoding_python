#%%

def ubbi_dubbi () :
    words = []
    word = input('input word : ')
    for i in word :
        if i in 'aeiou' :
            push_i = 'ub' + i # f'ub{letter(여기서는 i)}' f'포맷 생활화 하기
            words.append(push_i)
        else :
            words.append(i)
    
    return ''.join(words)
        
# %%
