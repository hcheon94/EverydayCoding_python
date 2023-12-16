#%%
def plword(word):
    if word[0] in 'aeiou' :
        return word + 'way'
    
    return word[1:] +word[0] +'ay'

def plfile (filename) :
    return ' '.join(plword(oneword)
                     for oneline in open(filename)
                     for oneword in oneline.split())
# %%
