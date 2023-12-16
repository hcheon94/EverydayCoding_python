# Git 정리
## 1. git,github이 무엇인가
### 1.1 git
+ VCS(Version Control System)의 일종, 프로그램 버전관리를 위한툴
### 1.2 github
+ Git으로 관리하는 프로젝트들을 온라인 공간에 공유하여 협업할 수 있는 협업 서비스

## 2. git 명령어 정리
### 2.1 기본 명령어
>   + git status : 현재 상태확인
>   + git init : git 저장소 생성하기
>   + git clone [https:~~] : 저장소 복제 및 다운로드
>   + git log : log확인하기
>   + git add *, [-A] : 저장소에 코드 추가
>   + git commit -m : 커밋생성
>   + git push origin master : 변경 사항 원격 서버 업로드(push)
>   + git pull : 원격저장소의 변경내용 현재 디렉토리로 가져오기
>   + git fetch : 원격저장소에 있는 변경사항을 로컬에 병합하기전 내용확인
>   + git merge : 두 개 이상의 branch를 하나로 합치는 작업
>   + git diff[branch이름][다른 branch] : 변경내용 merge 하기 전에 바뀐내용 비교
### 2.2 branch관련
>   * git init : 해당폴더에 .git이라는 파일 생성
>   * git remote add origin[github 주소] : github와 연결
>   * git branch[브랜치명] : 브랜치 생성
>   * git checkout(-b)[브랜치명] : 해당 브랜치로 이동,(-b는 바로 이동)
>   * git branch(-a) : 원하는 브랜치로 이동했는지 확인(-a 모든 브랜치 확인)
>   * git add . : 파일 및 폴더 add
>   * 

## 3. 용어
git에서 Commit을 할 때 총 3가지 영역을 바탕으로 동작합니다.
+ Working Directory : 내가 작업하고 있는 디렉토리
+ Staging Area : 커밋을 하기 전 임시저장, git add로 추가한 파일들이 모인 공간
+ Repositort : 커밋들이 모인 장소
* * * * * *
File 상태
+ Untracked : Working Directory에 있는 파일이지만 Git으로 버전관리를 하지 않은 상태
+ Unmodified : 신규로 파일이 추가되었을 때, new File 상태와 같다
+ Modified : 파일이 추가된 이후 해당 파일이 수정되었을때
+ Staged : Staging Area에 반영된 상태

## 4. Git Flow전략
### 4.1 정의
Git Flow 전략은 Git브랜치 전략의 대표적인 사례로써 Git 브랜치를 효과적으로 관리하기 위한 워크 플로우이다.
### 4.2 브랜치 종류
+ Main branch(필수)
    - 출시 가능한 프로덕션 코드를 모아두는 브랜치. 개발 프로세스 전반에 걸쳐 유지되며 배포된 각 버전을 Tag를 이용해 표시해 둠.
+ Develop branch(필수)
    - 다음 버전 개발을 위한 코드를 모아두는 branch. 개발이 완료되면, main 브랜치로 merge
+ Supporting branch(필요에 따라)
    - Feature branch
        * 하나의 기능을 개발하기 위한 브랜치. Develop에서 생성하며, 완료 되면 다시 Develop으로 merge. 네이밍은 *feature/branch-name* 와 같은 형태로 생성한다.
    - Release branch
        * 배포를 준비하기 위한 브랜치. 역시 Develop에서 생성하며 버전,데이터 수정, 사소한 버그 수정을 위해 사용.   
        * 배포준비가 완료되면 Main과 Develop에 merge함. 이떄 Main에는 버전을 태그에 표시 
    - Hotfix branch
        * 배포 버전에 문제가 생겼다면 Hotfix를 사용하여 문제해결 Main에서 생성하고 해결 시 main과 develop에 merge한다.
        * 네이밍은 **hotfix/v1.0.1** 과 같은 형태로 생성한다.

### 4.3 마무리
+ GitFlow전략은 웹어플리케이션에는 적합하지 않다고 함.
+ github Flow, Gitlab Flow등 여러 브랜치 전략이 있음

### 참고
+ [Gitbranch전략](https://hudi.blog/git-branch-strategy/)
+ [Git의 기본개념과 용어 정리](https://co-no.tistory.com/entry/Git-Git%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%9A%A9%EC%96%B4-%EC%A0%95%EB%A6%AC, "Git 사용법")
