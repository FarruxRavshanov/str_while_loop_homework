def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    from string import punctuation
    p = punctuation
    i = 0
    a = 0
    while i < len(s):
        if s[i] in p:
            a += 1
        i += 1
    return a