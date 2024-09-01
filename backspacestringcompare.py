def removeItem(s):
    idx = 0
    for i in range (0,len(s)):
        if s[i] != '#':
            s = s[:idx] + s[i] + s[idx+1:]
            idx += 1
        elif s[i] == '#' and idx >= 0:
            idx -= 1

        if idx < 0:
            idx = 0

    ans = ''
    for i in range (0, idx):
        ans += s[i]
    return ans
s = "a#c"
t = "b"
if (removeItem(s) == removeItem(t)):
    print("true")
else:
    print("false")
    
