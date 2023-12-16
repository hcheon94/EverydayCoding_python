#%%
MENU = dict( sandwitch = 3000, noodle=4000, soup=2500,steak=6000,salmon=7000)
# %%
def restaurant () :
    order = ''
    total= 0
    while True:
        order = input('Order : ').strip() # 문자열 양쪽 공백을 제거하는 함수
        if not order : 
            break
            # if(order=='')
        
        if order in MENU :
            total += MENU[order]
            print(f'{order} costs {MENU[order]}, total is {total}')
        elif order not in MENU :
            print(f'Sorry, we are fresh out of {order} today')
            
        
    print(f'Your total is {total}')
            
# %%
