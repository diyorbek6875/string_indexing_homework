def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.count('*')==0:
        a=0
    else:
        a=s.count("*")
    return a
s=input("")
print(main(s))

        