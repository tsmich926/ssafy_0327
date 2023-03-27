#선택정렬함수를 재귀적 알고리즘으로 작성

# 제일 작은 얘를 맨 앞으로
# k가  n-1번이 될때까지만 정렬하면 된다


# 1 k를 입력받아서 k부터 그 뒤를 검사하면서 제일 작은 값을 찾은 뒤에 k번째의 데이터와 교환
#2 k를 증가하여 재귀호출

lst = [4,3,5,6,1,8,10]
N = len(lst)
def selectionSort(k):
    if k==N-1:
        return


    #1번작업
    minp= k
    for i in range(k+1,N):
        if lst[i] < lst[minp]:
            minp= i 
            #제일 작은 데이터가 있는 위치를 찾음
    lst[minp],lst[k] = lst[k],lst[minp]
    #2번
    selectionSort(k+1)

selectionSort(0)
print(lst)