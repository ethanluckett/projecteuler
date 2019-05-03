from collections import defaultdict


def problem62():
    cubes = [x**3 for x in range(10000)]
    sorted_digits = [int(''.join(sorted(str(x), reverse=True))) for x in cubes]
    reverse_indices = defaultdict(list)
    for i, d in enumerate(sorted_digits):
        reverse_indices[d].append(i)
    sorted_cubes = sorted(sorted_digits)

    for i in range(len(sorted_cubes) - 4):
        if all(sorted_cubes[i] == sorted_cubes[i+x] for x in range(5)):
            return min(cubes[j] for j in reverse_indices[sorted_cubes[i]])


if __name__ == '__main__':
    solution = problem62()
    print(solution)
    assert solution == 127035954683
