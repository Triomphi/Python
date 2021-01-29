if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maxi = max(arr)
    i = 0
    length = len(arr)
    while i < length:
        if arr[i] == maxi:
            arr.remove(arr[i])
            length -= 1 
            continue
        i += 1
    print(max(arr))
