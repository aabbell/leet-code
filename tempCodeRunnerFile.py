stack = []
s = "aa#c"
t = "b"
for  char in s:
    if char == "#":
        if stack:
            stack.pop()
        else:
           stack.append(char)
        s ="".join(stack)

        stackk = []
        for  char in t:
            if char == "#":
                if stackk:
                    stackk.pop()
            else:
                stackk.append(char)
        t = "".join(stackk)

        if s == t:
            ans = "true"
        else:
            ans = "false"

        print(ans)
