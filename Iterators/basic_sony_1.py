sony=["abc", "def", "gef", "they", "chel", "hjut"]
sonyobj=iter(sony)
for i in range(len(sony)):
    print(next(sonyobj))
print(next(sonyobj))
