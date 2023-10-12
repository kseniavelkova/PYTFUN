
def generate_permutations(a, n):
    if n == 0:
        print(''.join(a))
    else:
        for i in range(n):
            generate_permutations(a, n - 1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
        generate_permutations(a, n - 1)


word = "Try123456 Word789"
perm = 20
for p in range(perm):
    generate_permutations(list(word), len(word) - 1)


