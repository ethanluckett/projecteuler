def problem59():
    ciphertext = [int(c) for c in open('problem59.txt').read().strip().split(',')]

    alpha = [ord('a') + i for i in range(26)]
    keys = [(a, b, c) for a in alpha for b in alpha for c in alpha]

    # to find the key (exp)
    for key in keys:
        plaintext = ''
        for i, c in enumerate(ciphertext):
            plaintext += chr(c ^ key[i % 3])
        if 'unexpectedly' in plaintext: # found by brute force searching keys
            break


    plaintext = []
    for i, c in enumerate(ciphertext):
        plaintext.append(c ^ key[i % 3])

    return sum(plaintext)


if __name__ == '__main__':
    solution = problem59()
    print(solution)
    assert solution == 129448
