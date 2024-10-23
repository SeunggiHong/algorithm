import sys
import heapq

n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))

answer = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum_value = a + b

    answer += sum_value
    heapq.heappush(arr, sum_value)

print(answer)