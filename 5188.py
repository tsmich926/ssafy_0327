# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [ list(map(int,input().split())) for _ in range(N)]
#
# 00
# 22 도달



# 오른쪽0
# 아래 1
# 부분집합 문제와 유사
# 재귀로도 가능


def solve(row,col,curS):
    # if row,col이 goal이면:
    if row==N-1 and col==N-1:
        return

    if 0<=row<N and 0<=col<N:
    solve(row,col+1,curSum+arr[row][col+1])

    solve(row+1,col,curSum+arr[row+1][col])
