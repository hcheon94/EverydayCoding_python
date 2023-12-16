#%%
#리스트 자료구조를 통해 해결가능 index를 이용하기 백준 11720


n= input()
numbers = list(input())
sum = 0
for i in numbers :
    sum = sum+int(i)
    
print(sum)

# %%
#버블정렬
#백준 11399  
N = int(input())
A = list(map(int,input().split()))
S = [0]*N

#삽입정렬
for i in range(1,N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1,-1,-1):
        if(A[j])<A[i]:
            insert_point = j+1
            break
        if j==0:
            insert_point = 0
    
    for j in range(i,insert_point,-1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1]+A[i]
    
sum = 0
for i in range(0,N):
    sum = sum+S[i]
    
print(sum)
# %%
def solution(str1, str2):
    answer = ''
    for a,b in str1,str2:
        answer
    return answer