#%%
import json 
import glob
scores = {}
def print_score(dirname):
    
    for filename in glob.glob(f'{dirname}/*.json') : # 각파일 열어서 딕셔너리(scores) 세팅 싹 해주는 역할
        scores[filename] = {}
        
        
        with open(filename,'r') as infile :
            for result in json.load(infile) : #load가 딕셔너리 형태로 리턴이 되거덩, 그래서 각줄의 딕셔너리에 대한 연산
                for subject,score in result.items(): # 이젠 각 아이템을 조지는거 과목이랑 점수("math" : 92)
                    scores[filename].setdefault(subject,[]) # 외부 딕셔너리 처음꺼부터 하는거겠지 setdefault(k,v)는 k라는 키가 없을때 v으로 초기화 하겠다 
                    scores[filename][subject].append(score)
                print(scores[filename])
                    
    for one_class in scores : # sco
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores)/len(subject_scores))
            
            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')
# %%
import json #json 예제코드

# JSON 문자열 파싱
json_str = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_str)
print(data)

# Python 객체를 JSON 문자열로 변환
python_dict = {'name': 'Jane', 'age': 25, 'city': 'San Francisco'}
json_str = json.dumps(python_dict)
print(json_str)
# %%
def reverse_lines(infilename,outfilename) : 
    with open(infilename) as infile , open(outfilename,'w') as outfile :
        for one_line in infile :
            #str.strip(one_line) 이건 내가한거
            #outfile.write(one_line[::-1])
            outfile.write(f'{one_line.rstrip()[::-1]}\n') #책에서 한거
# %%
