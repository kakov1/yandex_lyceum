n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]
data_ = list(zip(*data))
x, y = list(map(int, input().split()))
k = int(input())
print(data, data_, sep='\n')
