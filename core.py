def word_count(text: str) -> int:
    """
    Number of whitespace-separated tokens in `text`.
    """
    return len(text.split())


def char_frequencies(text: str) -> dict[str, int]:
    """
    Count of each character, ignoring whitespace and case.
    """
    splited = text.lower().split()
    res = {}
    for tok in splited:
        for char in tok:
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
    return res


def longest_word(text: str) -> str:
    """
    The longest token. Raises ValueError on empty input.
    """
    splited = text.split()
    if not splited:
        raise ValueError
    max, max_world = 0, ""
    for tok in splited:
        if len(tok) > max:
            max = len(tok)
            max_world = tok
    return max_world