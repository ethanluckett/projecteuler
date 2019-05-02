
num_sets = {
	'3': set(n * (n + 1) // 2 for n in range(45, 141)),
	'4': set(n**2 for n in range(32, 100)),
	'5': set(n * (3*n - 1) // 2 for n in range(26, 82)),
	'6': set(n * (2*n - 1) for n in range(23, 71)),
	'7': set(n * (5*n - 3) // 2 for n in range(21, 64)),
	'8': set(n * (3*n - 2) for n in range(18, 59))
}

# basically a recursive graph search, where an edge indicates two numbers can be consecutive in the list
# numbers from lists we've already used are pruned via filter
def build_list(current_list, unused_keys):
	for key in unused_keys:
		for n in num_sets[key]:
			if len(current_list) == 0 or current_list[-1] % 100 == n // 100:
				new_list = current_list + [n]
				yield from build_list(new_list, list(filter(lambda k: k != key, unused_keys)))
	yield current_list

for l in build_list([], ['3', '4', '5', '6', '7', '8']):
	if len(l) == 6 and l[-1] % 100 == l[0] // 100:
		print(l)
		print(sum(l))
		break