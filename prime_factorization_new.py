# Write a function which does prime factorization of a number, e.g. 20633239 = 11*29*71*911. Calculate the prime factorization of L(60) and L(61).
import primefac


def prime_factorization(num):
    return list(primefac.primefac(num))


print(prime_factorization(61))
