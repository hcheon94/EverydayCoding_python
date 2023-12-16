#%%
#피그 라틴 문장 만들기
import pig_latin
def pl_sentence() :
    sentence = input('what sentence : ')
    senSplit = sentence.split(' ')
    strList = []
    for word in senSplit :
        pl_word = pig_latin(word)
        strList.append(pl_word)
    
    return ' '.join(strList)
# %%
