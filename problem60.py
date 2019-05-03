import numpy as np


#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1


def problem60():
    primes_small = set(primesfrom3to(10000))
    primes_1b = set(primesfrom3to(100000000))

    primes_small_list_str = list(str(p) for p in primes_small)
    primes_small_list_int = list(primes_small)
    lowest_sum = 1e30
    for i in range(len(primes_small)):
        a = primes_small_list_str[i]

        for j in range(i+1, len(primes_small)):
            b = primes_small_list_str[j]
            if int(a + b) not in primes_1b or int(b + a) not in primes_1b:
                continue

            for k in range(j+1, len(primes_small)):
                c = primes_small_list_str[k]
                if not all(int(x + c) in primes_1b and int(c + x) in primes_1b for x in [a, b]):
                    continue

                for l in range(k+1, len(primes_small)):
                    d = primes_small_list_str[l]
                    if not all(int(x + d) in primes_1b and int(d + x) in primes_1b for x in [a, b, c]):
                        continue
                    
                    for m in range(l + 1, len(primes_small)):
                        e = primes_small_list_str[m]
                        if not all(int(x + e) in primes_1b and int(e + x) in primes_1b for x in [a, b, c, d]):
                            continue

                        quintuple = tuple(int(primes_small_list_int[x]) for x in [i, j, k, l, m])
                        if sum(quintuple) < lowest_sum:
                            lowest_sum = sum(quintuple)
                            lowest_quintuple = quintuple

    return lowest_sum


if __name__ == '__main__':
    solution = problem60()
    print(solution)
    assert solution == 26033
