#%%
def get_final_line(filename) :
    final_line = ''
    f= open(filename) #r읽기, w 쓰기. a append모드, rb 바이트 읽기, wb 바이트 쓰기, ab append 모드 r 이 디폴트
    for current_line in f:
        final_line = current_line    #pass #아무것도 안해 계속 그럼 current_line에는 마지막 줄이 들어있겠지
    return final_line


    """    
    with open(filename) as f :
        for one_line in f:
            print(len(one_line))
    """            
    

# %%
