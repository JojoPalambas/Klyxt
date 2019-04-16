

def isNumber(s):
    if not s or s == "":
        return False
    for c in s:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            return False
    return True
