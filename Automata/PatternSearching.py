def construct_transition_table(pattern, alphabet):
    m = len(pattern)
    transition_table = {}

    for state in range(m + 1):
        transition_table[state] = {}
        for char in alphabet:
            k = min(m + 1, state + 2)
            while k > 0 and not (pattern[:state] + char).endswith(pattern[:k - 1]):
                k -= 1
            transition_table[state][char] = k

    return transition_table


def pattern_search(text, pattern):
    alphabet = set(text)
    transition_table = construct_transition_table(pattern, alphabet)

    n = len(text)
    m = len(pattern)
    current_state = 0
    indices = []

    for i in range(n):
        if text[i] in transition_table[current_state]:
            current_state = transition_table[current_state][text[i]]
        else:
            current_state = 0

        if current_state == m:
            indices.append(i - m + 1)

    return indices


if __name__ == '__main__':
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    indices = pattern_search(text, pattern)

    if indices:
        print(f"Pattern found at indices: {indices}")
    else:
        print("Pattern not found in the text.")
