def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit()==False:
        a=-1

    else:
        a=int(s)
    return a
s=input("")
print(main(s))