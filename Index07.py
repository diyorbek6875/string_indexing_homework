def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    
    if len(s)==n:
        a=s[n]
    else:
        a=False

    return a
s=input("")
n=int(input("sooni kiriting "))
print(main(s,n))
