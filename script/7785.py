n = int(input())
arr = set()
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        arr.add(name)
    elif state == 'leave':
        arr.remove(name)

for _ in sorted(arr, reverse=True):
    print(_)