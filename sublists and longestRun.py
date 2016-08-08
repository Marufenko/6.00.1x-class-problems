def getSublists(L, n):
    return [L[i:i+n] for i in range(len(L)-n+1)]

def longestRun(L):
    tmp_list = []
    longest_value = 0
    for i in range(len(L)+1):
        for k in getSublists(L, i):
            tmp_list.append(k)
    for h in tmp_list:
        if sorted(h) == h and len(h) >= longest_value:
            longest_value = len(h)
    return longest_value
\
