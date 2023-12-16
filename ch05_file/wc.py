#%%
def wordcount(filename) :
    
    count = {'characters' :0,
             'word' : 0,
             'lines' : 0}
    unique_words =set()    
    
    for one_line in open(filename) :
        count['lines'] += 1
        count['characters'] += len(one_line)
        count['word'] += len(one_line.split())
        unique_words.update(one_line.split())
    
    count['unique words'] = len(unique_words)
    for key,value in count.items() :
        print(f'{key}:{value}')
    
    
# %%
def wordcount_2(filename) :
    words= input('단어 입력해주세요 :')
    word_list = words.split()
    word_count = {}
    for word in word_list :
        word_count[word] = 0
    
    for line in open(filename) :
        words_list =line.split()
        for w in word_list :
            if w in word_count.keys() :
                word_count[w] += 1
            
    
    for key,value in word_count.items() :
        print(f'{key}:{value}')
                
             
        
# %%
