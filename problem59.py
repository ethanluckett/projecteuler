
ciphertext = [int(c) for c in open('problem59.txt').read().strip().split(',')]


alpha = [ord('a') + i for i in range(26)]
keys = [(a, b, c) for a in alpha for b in alpha for c in alpha]

## to find the key (exp)
# for key in keys:
# 	plaintext = ''
# 	for i, c in enumerate(ciphertext):
# 		plaintext += chr(c ^ key[i % 3])
# 	if 'the' in plaintext and 'and' in plaintext:
# 		print(plaintext)
# 		print(''.join([chr(c) for c in key]))


key = tuple(ord(c) for c in 'exp')


plaintext = []
for i, c in enumerate(ciphertext):
    plaintext.append(c ^ key[i % 3])

print(sum(plaintext))