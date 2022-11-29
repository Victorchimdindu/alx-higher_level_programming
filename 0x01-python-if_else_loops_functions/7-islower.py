Executable File  7 lines (7 sloc)  142 Bytes

#!/usr/bin/python3
def islower(c):
    check = ord(c)
    if check >= 97 and check <= 122:
        return True
    else:
        return False
