from stability import blocking_pairs


# Gale-Shapley matching algorithm
def match(pm, pw):
    assert len(pm) == len(pw)
    n = len(pm)

    pairs = []
    while len(pairs) < n:
        for m, prefs in prefs_m.items():
            for w in prefs:
                if not any(filter(lambda p: p[1] == w, pairs)):
                    pairs.append((m, w))
                    break
                else:
                    m_old = next(filter(lambda p: p[1] == w, pairs))[0]
                    p_old = prefs_w[w].index(m_old)
                    p_new = prefs_w[w].index(m)
                    if p_new < p_old:
                        pairs.remove((m_old, w))
                        pairs.append((m, w))
                        break
    return sorted(pairs)


if __name__ == '__main__':
    # Example from p. 10: A stable matching is found.

    prefs_m = {
        1: [4, 1, 2, 3],
        2: [2, 3, 1, 4],
        3: [2, 4, 3, 1],
        4: [3, 1, 4, 2],
    }

    prefs_w = {
        1: [4, 1, 3, 2],
        2: [1, 3, 2, 4],
        3: [1, 2, 3, 4],
        4: [4, 1, 3, 2],
    }

    pairs = match(prefs_m, prefs_w)
    print('matching', pairs)
    blocking = blocking_pairs(pairs, prefs_m, prefs_w)
    print('blocking', blocking)
