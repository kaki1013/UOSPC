# 최대  = N - (다 반대로 한 것의 최소)
# 최소 = 올바른 괄효열인지 체크하면서 (열는 괄호 >= 닫는 괄호) 더 많도록 유지
def mini(arr, n):
    stack = []
    open = 0  # open 은 n개 까지만
    change = 0
    breaker = False
    for i in range(n):
#        print(i, stack)
        if open == n//2:
            breaker = True
            end_idx = i
            break
        if arr[i] == '(':
            stack.append('(')
            open += 1
        else:
            if stack:
                stack.pop()
            else:
                stack.append('(')
                open += 1
                change += 1
    if breaker:
        for i in range(end_idx, n):
            if arr[i] == '(':
                change += 1
    return change


N = int(input())
s = list(input())
ss = []
for i in range(N):
    if s[i] == '(':
        ss.append(')')
    else:
        ss.append('(')

print(N - mini(ss, N))
print(mini(s, N))