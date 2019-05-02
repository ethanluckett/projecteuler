
fibs = {}

def fib(n):
    if n in fibs:
        return fibs[n]
    else:
        if n <= 2:
            fibs[n] = 1
            return 1
        else:
            result = fib(n-1) + fib(n-2)
            fibs[n] = result
            return result

# just keep calculating bigger values to fill fibs
# until log10(fib(n)) == 999

