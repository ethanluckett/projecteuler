
def is_palindrome(x):
    str_x = str(x)
    bin_x = bin(x)[2:]
    s_offset = len(str_x) % 2 == 0
    b_offset = len(bin_x) % 2 == 0
    b10 = (str_x[:len(str_x)//2] == str_x[:-len(str_x)//2-s_offset:-1])
    b2  = (bin_x[:len(bin_x)//2] == bin_x[:-len(bin_x)//2-b_offset:-1])

    return b2 and b10

palindromes = list(filter(is_palindrome, range(1000000)))
print(sum(palindromes))