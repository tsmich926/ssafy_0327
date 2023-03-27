# 순열 부분집합 조합

# 1- 순열
# 2-조합
# 3-부분집합

# 순열 프로그램 짜기
#
# N = 4
# def per(k):
#
#     for i in range(N):
#         if used[i]:
#             continue
#         #i를 방문표시
#         used[i] = True
#         result[k] = i
#         per(k+1)
#         # i 방문 표시 해제/ 옆으로 가면 방문표시가 영향을 주면 안된다
#         used[i] = False
#
# used = [False]*N
# result = [-1]*N


012345



def per(k):
    if k==N:
        print(result)
        return

    for i in range(N):
        if not used[i]:
            used[i]=True
            result[k]=i
            per(k+1)
            used[i] =False

N = 6
used = [False] *N
result = [-1]*N
per(0)