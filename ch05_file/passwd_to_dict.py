#%%
def passwd_to_dict() :
    
    
    return
# %%
# 추가적인 문자열 메서드
# 문자열이 특정 문자열로 시작하는지 T/F
s = 'abcd'
s.startswith('a') #True
s.startswith('abc') #True
s.startswith('b') #false
# %%
# 문자열이 특정 문자열로 끝나는지
s.endswith('d') #True
s.endswith('cd') #true
s.endswith('b') #false
# %%
# 양옆 공백 제거
sa = '\t\t\ta b c \t\t\n'
sa.strip() #a b c
sa.lstrip() #a b c \t\t\n
sa.rstrip() #\t\t\ta b c

# %%
def passwd_to_dict(filename) :
    users ={}
    with open(filename) as passwd :
        for line in passwd :
            if not line.startswith(('#','\n')) :
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2]) 
    return users

print(passwd_to_dict('etc\passwd.txt'))
# %%
#passwd파일 읽어들이고 키로 '로그인 셸', 값으로 '로그인한 사용자'를 리스트로 갖는 딕셔너리
def user_bash_dict(filename):
    users ={}
    users_key =[]
    users_value = []
    with open(filename) as passwd :
        for line in passwd :
            if not line.startswith(('#','\n')) :
                user_info = line.split(':')
                if user_info[-1] not in users:
                    users[user_info[-1]] = [user_info[0]]
                else :
                    users[user_info[-1]].append(user_info[0])
                
                #print(users)
        print(users.keys())
    return users
# %%
#키값은 사용자 이름id,홈디렉터리,셸을 갖는 딕셔너리
def user_home_dict(filename) :
    users ={}
    with open(filename) as passwd :
        for line in passwd :
            if not line.startswith(('#','\n')) :
                user_info = line.split(':')
                users[user_info[0]] = [user_info[2],user_info[-2],user_info[-1]]
    return users
# %%
