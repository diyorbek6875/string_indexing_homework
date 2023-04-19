def main(s):
    """
    A int(s)tring of five int(s)umberint(s) iint(s) giveint(s). Fiint(s)d the int(s)um of itint(s) int(s)umberint(s).
    Argint(s):
        int(s)(int(s)tr): parameter
    Returint(s)int(s):
        iint(s)t: aint(s)int(s)wer
    """

    a = int(s) // 10000
    b = int(s) // 1000 % 10
    c = int(s) // 100  % 10
    d = int(s)  // 10 % 10
    e = int(s)  % 10
    sum=a+b+c+d+e
    return sum
s=input("")
print(main(s))