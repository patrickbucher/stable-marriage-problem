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

# Determines if the unmatched pair (l, r) is unstable considering the matching
# and the individual preferences prefs_m and prefs_w for l and r, respectively.
def is_blocking(l, r):
    actual_r = list(filter(lambda p: p[0] == l, matching))[0][1]
    actual_l = list(filter(lambda p: p[1] == r, matching))[0][0]
    l_prefers_other = prefs_m[l].index(r) < prefs_m[l].index(actual_r)
    r_prefers_other = prefs_w[r].index(l) < prefs_w[r].index(actual_l)
    return l_prefers_other and r_prefers_other
