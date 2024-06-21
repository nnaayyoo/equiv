def check_reflexive(R, A):
  '''
  반사적인가?
  '''
  for a in A:
    if (a, a) not in R:
      return False
    return True

def check_symmetric(R):
  '''
  대칭적인가?
  '''
  for (a, b) in R:
    if (b, a) not in R:
      return False
  return True

def check_transitive(R):
  '''
  추이적인가?
  '''
  for (a, b) in R:
    for (c, d) in R:
      if b == c and (a, d) not in R:
        return False
  return True

def check_equivalence(R, A):
  '''
  동치인가?
  '''
  return check_reflexive(R, A) and check_symmetric(R) and check_transitive(R)

def main():
    A = set()
    print("집합 A를 입력하세요. 각 원소를 한 줄에 하나 씩 입력하세요")
    print("입력이 끝나면 빈 줄을 입력하세요.")
    while True:
        line = input()
        if line.strip() == "":
            break
        A.add(int(line))

    print("관계 집합 R을 입력하세요. 각 원소는 'a b' 형태로 입력해야 합니다. *** 숫자만, 띄어쓰기로 구분")
    print("입력이 끝나면 빈 줄을 입력하세요.")
    R = set()
    while True:
        line = input()
        if line.strip() == "":
            break
        a, b = map(int, line.split())
        R.add((a, b))

    print("반사:", check_reflexive(R, A))
    print("대칭:", check_symmetric(R))
    print("추이:", check_transitive(R))
    print("동치관계:", check_equivalence(R, A))

    if check_equivalence(R, A):
        print("주어진 A와 R은 동치관계입니다")
    else:
        print("주어진 A와 R은 동치관계가 아닙니다")

if __name__ == "__main__":
    main()

# (2) 모듈이 설명과 함께 올라온 깃허브 링크 추가:
