#%%
def strsort(word) :
    
    return ''.join(sorted(word))
# %%
#문자열이 주어졋을 때 각각의 단어로 구분하고 단어를 알파벳 순서로 정렬하기
def sen_sort(sentence) :
    output = []
    for split_word in sentence.split(' ')  :
        output.append(''.join(sorted(split_word)))
        
    return ','.join(output)
# %%
