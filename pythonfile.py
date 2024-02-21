def check(s):
    if len(s) < 3:
        return False
    s = str(s).lower()
    if s[-3::] != ".py":
        return False
    for i in s:
        if ord(i) < ord('a') and ord(i) > ord('z') and ord(i) != ord('.') and ord(i) != ord('_'):
            return False
    return True

n = input()
if check(n):
    print("yes")
else:
    print("no")
