# 1. 마크다운 설명 및 장-단점 정리
## 1.1 장점
1. 간결하다.
2. 별도의 도구없이 작성 가능.
3. 다양한 형태로 변환 가능
4. 텍스트로 저장되기 떄문에 용량이 적다.
5. 버전관리시스템을 이용하여 변경이력 관리 가능
6. 지원하는 프로그램과 플랫폼이 다양하다.
## 1.2 단점
1. 표준이 없다. 그래서 도구에 따라서 변환방식이나 생성물이 다르다
2. 모든 HTML마크업을 대신 못한다
# 2. 사용법
## 2.1 헤더 Headers

* 글머리 1~6까지 지원
<pre>
    #
    ##
    ###
    ####
    #####
    ######
</pre>
# 예시1
## 예시2
### 예시3
#### 예시4
##### 예시5
###### 예시6

* 큰제목
<pre>
example
=============
</pre>
큰제목 예시
=============
* 작은제목
<pre>
example
------------
</pre>
작은제목 예시
------------
## 2.2 BlockQuote
<pre>
> 블럭인용문자를 이용한다고 한다
>   > 이렇게
>   >   > 한번더
</pre>
> ### 블럭인용문자를 이용한다고 한다
>   > + 이렇게 다른 요소도 넣을수 있다
>   >   > 1. 한번더

## 2.3 목록
* 순서있는 목록(ordered list)

    순서있는 목록은 그냥 숫자와 점 쓰기
<pre>
1. 일번
2. 2번
3. 삼번
</pre>
1. 일번
2. 2번
3. 삼번
* 순서없는 목록(unordered list)
    
    이건 '*','+','-' 사용함
<pre>
* 빨강
    * 녹색
        * 파랑
            + 혼합해서
                - 사용도 가능
</pre>
* 빨강
    * 녹색
        * 파랑
            + 혼합해서
                - 사용도 가능
## 2.4 코드
들여쓰기를 하는 방법과 코드블럭을 이용하는 방법이 있다.

2.4.1들여쓰기 방법

    들여쓰기(tab)를 하면 지금처럼 블록이 생긴다

다시 들여쓰기를 안쓰면 일반 텍스트로 전환

2.4.2코드블록 방법 

    1. <pre><code>{code}</code></pre>
    2. "```"

1번방법
<pre><code>
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, world");
  } 
}
</code></pre>
2번방법 "```" 
    "```" 옆에 사용언어를 쓰면 언어에 따른 문법강조 가능

``` java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, world");
  }
}
```
## 2.5 수평선(hr/)
수평선을 만드는 키워드
```
* * *

***

*****

- - -

---------------------------------------
```
* 실제 예시

* * *

***

*****

- - -

---------------------------------------


## 2.6 링크
+ 참조 링크
```
[link keyword][id]

[id]: URL "Optional Title here"

// code
Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"
```
[link keyword][id]

[id]: URL "Optional Title here"


Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"

* 외부링크

```
사용문법 :[title](link)
적용예 : [Naver](https://www.naver.com/,"naver link")
```

Link: [Naver](https://www.naver.com/, "naver link")

+ 자동연결
```
일반적인 URL 혹은 이메일주소인 경우 적절한 형식으로 링크를 형성한다.

* 외부링크: <http://example.com/>
* 이메일링크: <address@example.com>
```

* 외부링크: <http://example.com/>
* 이메일링크: <address@example.com>

## 2.7 강조

```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
~~cancelline~~
```

*single asterisks*   
_single underscores_   
**double asterisks**   
__double underscores__   
~~cancelline~~   
+ 중간 팁 줄바꿈을 하려면 띄어쓰기 세번을 하면 된다

## 마지막 사용하는 이유?
+ 잘 쓰면 가독성이 좋아지고 코드표현에 용이하다
+ Github에서 필수적으로 쓰이기 때문에

참고링크 : [Github](https://gist.github.com/ihoneymon/652be052a0727ad59601, "마크다운 사용법")