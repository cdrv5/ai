def solve_crypto(puzzle, letters, digits):
    if not letters:
        s, e, n, d, m, o, r, y = puzzle
        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
        if send + more == money and s != 0 and m != 0:
            print('S=', s, 'E=', e, 'N=', n, 'D=', d, 'M=', m, 'O=', o, 'R=', r, 'Y=', y)
    else:
        for digit in digits:
            solve_crypto(puzzle + [digit], letters[1:], digits - {digit})

# The set of letters we need to assign digits to
letters = 'SENDMORY'
# Calling the recursive function
solve_crypto([], letters, set(range(10)))