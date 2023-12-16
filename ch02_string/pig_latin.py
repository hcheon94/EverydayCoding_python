#%%
#내가 푼 풀이
#각각 변수에 way 혹은 ay를 뒤에 +로 붙임 ay를 붙인경우 strip()을 사용하여 맨앞 글자 뺌
def pig_latin():
    word = input('input : ')
    if word[0] in 'aeiou' :
        result_word = word+'way'
        
    else :
        result_word =word +'ay'
        result_word =result_word.strip(word[0])
        
    return result_word
    
# %%
#정답해설
#f' string 사용함
def pig_latin(word) :
    if word[0] in 'aeiou' :
        return f'{word}way'
    
    return f'{word[1:]}{word[0]}ay'
# %%
#대문자가 섞여있는 단어 처리하기
#첫 번째 글자가 대문자이고 나머지 글자가 대문자가 아닌 단어를 입력받았다면
# 대문자인지 확인하는 함수 isupper <-> 소문자는 islower()
def pig_latin_upper (word) :
    if word[0].isupper() :
        if word[0] in 'AEIOU':
            return f'{word}way'
        else :
            return f'{word[1:]}{word[0]}ay'
    

    return pig_latin(word)
       
# %%
#모음이 두개 이상이면 way 1개만 있으면 ay붙이기
#세트 자료형도 in 사용해서 있는지 없는지 확인 가능(중복이 없으니)
#
def pig_latin_vowel_count(word) :
    count = 0
    wordSet  = set(word)
    for wordCount in wordSet :        
        if wordCount in 'aeiou' :
            count += 1
        
    if count >= 2:
        return f'{word}way'
    elif count == 1:
        return f'{word[1:]}{word[0]}ay'
    else :
        return word
            
# %%
