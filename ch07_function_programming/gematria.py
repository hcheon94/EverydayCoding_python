#%%
import string

def gematria_dict() :
    return {char : index
            for index,char in enumerate(string.ascii_lowercase,1)}
# %%
#a=1 꼴의 문장이 있는 파일을 열어서 'a' : 1 형식의 딕셔너리로 만들기
def config_to_dict(filename):
    return {key.strip():value.strip() 
            for one_line in open(filename)
            for key,value in [one_line.split('=')]
            
    }
# %%
def config_to_dict(filename): 
    return {key.strip():int(value.strip()) 
            for one_line in open(filename)
            for key,value in [one_line.split('=')]
            if value.strip().isdigit()
    }
# %%
GEMATRIA  = gematria_dict()
def gematria_for (word) :
    return sum(GEMATRIA.get(one_char,0) for one_char in word)

def gematria_equal_word(input_word) :
    our_score = gematria_for(input_word.lower())
    return [one_word.strip()
            for one_word in open('./words.txt')
            if gematria_for(one_word.lower()) == our_score ]
# %%
