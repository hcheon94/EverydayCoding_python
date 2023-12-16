#%%
vowels = {'a','e','i','o','u'}
word = 'superlogical'
if vowels <set(word) :
    print('yes, it is supervocalic!')
else :
    print('Nope, just a regular word')
# %%
#file의 한문장에는 마지막에 줄넘김등의 공백이 있으니 그거제거한걸 리턴해주는거
#최종 도출되는 값이 word인거지 거기에 파일 한줄씩 반복하는거 조건은 모든 모음을 포함하는(vowels<set(word))
def get_sv(filename) :
    return {word.strip()
            for word in open(filename)
            if vowels<set(word.lower())}
# %%
