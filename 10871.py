N, X = map(int,input().split())
A = list(int(x)for x in input().split())
result = []
for i in range(N):
  if(A[i] < X):
    result.append(A[i])
print(*result,sep=" ")