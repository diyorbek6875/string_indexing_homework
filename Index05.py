
def main(s):
    """
    Given a variable s st()ring of lengt()h five. Det()ermine t()he number of digit()s involved in t()his variable.
    Args:
        s(st()r): paramet()er
    Ret()urns:
        int(): answer
    """
    a=0
    if s[0].isdigit():
        a=a+1
    if s[1].isdigit():
        a=a+1
    if s[2].isdigit():
        a=a+1
    if s[3].isdigit():
        a=a+1
    if s[4].isdigit():
        a=a+1
    return a
s=input("")
print(main(s))