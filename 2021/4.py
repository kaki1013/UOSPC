V, E, T = map(int, input().split())
adj = [[] for _ in range(V+1)]
mod = 10**9 + 7
for i in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

pack = [0] * (V+1)
temp = [0] * (V+1)
pack[1] = 1

for _ in range(T):
    for i in range(1, V+1):
        if pack[i]:
            for j in adj[i]:
                temp[j] += pack[i]
#    print(_, temp)
    for i in range(1, V+1):
        pack[i] = temp[i] % mod
        temp[i] = 0
#    print(_, pack)
print(sum(pack) % mod)