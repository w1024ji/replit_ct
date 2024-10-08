def solution(N, stages):
  answer=[]
  length = len(stages)

  for i in range(1, N+1):
    # 해당 스테이지에 머물러 있는 사람의 수 계산
    count=stages.count(i)

    # 실패율 계산
    if length ==0:
      fail=0
    else:
      fail = count/length

    answer.append((i, fail))
    length -= count

  # 실패율을 기준으로 내림차순 정렬
  answer = sorted(answer, key=lambda t:t[1], reverse=True)

  # 정렬된 스테이지 번호 출력
  answer = [i[0] for i in answer]
  return answer

# 스테이지 개수 n
n = int(input())

# 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
stages = list(map(int, input().split()))

print(solution(n, stages))