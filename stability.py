# Determines if the unmatched pair (l, r) is unstable considering the matching
# and the individual preferences prefs_m and prefs_w for l and r, respectively.
def is_blocking(l, r, matching, prefs_m, prefs_w):
    actual_r = next(filter(lambda p: p[0] == l, matching))[1]
    actual_l = next(filter(lambda p: p[1] == r, matching))[0]
    l_prefers_other = prefs_m[l].index(r) < prefs_m[l].index(actual_r)
    r_prefers_other = prefs_w[r].index(l) < prefs_w[r].index(actual_l)
    return l_prefers_other and r_prefers_other


# Returns the blocking (unrealized) pairs in the (realized) matching.
def blocking_pairs(matching, prefs_m, prefs_w):
    return list(
        filter(
            lambda p: is_blocking(p[0], p[1], matching, prefs_m, prefs_w),
            unrealized_pairs(matching)))


def unrealized_pairs(matching):
    all_pairs = []
    n = len(matching)
    for i in range(1, n+1):
        for j in range(1, n+1):
            all_pairs.append((i, j))
    return sorted(list(filter(lambda p: p not in matching, all_pairs)))


if __name__ == '__main__':
    # Example from p. 6/7: Six blocking pairs are found.
    # >>> blocking_pairs(matching)
    # [(1, 2), (1, 4), (2, 1), (2, 4), (3, 2), (4, 4)]

    prefs_m = {
        1: [2, 4, 1, 3],
        2: [3, 1, 4, 2],
        3: [2, 3, 1, 4],
        4: [4, 1, 3, 2],
    }
    prefs_w = {
        1: [2, 1, 4, 3],
        2: [4, 3, 1, 2],
        3: [1, 4, 3, 2],
        4: [2, 1, 4, 3],
    }

    matching = set([(1, 1), (2, 2), (3, 4), (4, 3)])
    print('matching', matching)
    print('blocking', blocking_pairs(matching, prefs_m, prefs_w))
