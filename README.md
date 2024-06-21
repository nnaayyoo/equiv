# 동치 관계 판별 모듈 (equivalence.py)

이 Python 모듈 'equivalence.py'는 주어진 관계 집합이 반사, 대칭, 추이 성질을 만족하는지를 검사하여 동치 관계인지 판단합니다.

## 동치 관계란?

동치 관계는 다음 세 가지 성질을 모두 만족하는 관계 집합을 말합니다:
- **반사성 (Reflexive)**: 모든 집합의 요소는 자기 자신과 관계를 맺습니다.
- **대칭성 (Symmetric)**: 만약 (a, b)가 관계에 속한다면, (b, a)도 관계에 속해야 합니다.
- **추이성 (Transitive)**: 만약 (a, b)와 (b, c)가 관계에 속한다면, (a, c)도 관계에 속해야 합니다.

## 사용 방법

터미널에서 다음 명령어를 사용하여 스크립트를 실행합니다:

python equivalence.py

## 입력 예시
**집합 A를 입력하세요. 각 원소를 한 줄에 하나 씩 입력하세요.
입력이 끝나면 빈 줄을 입력하세요.**
1  
2  
3  
4  

**관계 집합 R을 입력하세요. 각 원소는 'a b' 형태로 입력해야 합니다. 숫자만, 띄어쓰기로 구분합니다.
입력이 끝나면 빈 줄을 입력하세요.**
1 1  
1 3  
2 2  
3 3  
3 1  
3 4  
4 4  
4 3  


**반사: True**  
**대칭: True**  
**추이: False**  
**동치관계: False**  
**주어진 A와 R은 동치관계가 아닙니다**
