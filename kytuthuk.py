def find(n,k):
    if k == 2**(n-1):
        return n
    if k > 2**(n-1):
        return find(n-1, k-2**(n-1))
    return find(n-1, k)
#n = 3, k = 2
#find(3 , 2) -> return find(2, 2) -> return 2
#print(chr(2 + ord('A') - 1))

t = int(input())
for i in range(t):
    n,k = [int(x) for x in input().split()]
    print(chr(find(n,k) + ord('A') - 1))
#ham chr: chuyen int sang unicode : chr(97) = a
#ham ord: chuyen character sang int: ord('h') = 104