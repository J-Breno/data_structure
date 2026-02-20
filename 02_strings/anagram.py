def is_anagram(s: str, t: str) -> bool:
    if len(s) < 1 or len(s) > 50000 or len(t) < 1 or len(t) > 50000:
        raise Exception("String fora dos limites")

    return sorted(s) == sorted(t)


print(is_anagram("rat","car"))