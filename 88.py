def move_hyphens(s):
    if s is None:
        return None
    hyphens=s.count("_")
    result='-'*hyphens
    for ch in s:
        if ch !='-':
            result +=ch

    return result
#Test
s=input("enter string:")
print("Original:",s)
print("Modified:",move_hyphen(s))
