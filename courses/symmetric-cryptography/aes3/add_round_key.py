state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    ans = state
    for i in range(len(s)):
        for j in range(len(s[0])):
            ans[i][j] = state[i][j] ^ round_key[i][j]
    return ans

def matrix2bytes(matrix):
    res = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res += chr(matrix[i][j])
    return res

plain = add_round_key(state, round_key)
print(matrix2bytes(plain))

