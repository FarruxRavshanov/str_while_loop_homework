def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    from string import punctuation

    i = 0
    a = 0
    while i < len(s):
        if not s[i].isdigit() or s[i].isalpha() or s[i].iswhitespace():
            a += 1
        i += 1
    return a