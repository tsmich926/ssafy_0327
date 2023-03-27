def part(k):
    if k==N:
        print(result)
        return

        result[k]=0
        part(k+1)
        result[k] = 1
        part(k+1)