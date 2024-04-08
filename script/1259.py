while True:
    arr = list(str(input()))
    if arr[0] == '0':
        break
    else:
        if arr == list(reversed(arr)):
            print('yes')
        else:
            print('no')