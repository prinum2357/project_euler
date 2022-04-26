#!/usr/bin/env/python3

def eratosthenes(n) :
    root_n = int(n ** 0.5) + 1
    isprime = [True] * (root_n)

    isprime[0] = False
    isprime[1] = False

    for s in range(2, root_n) :

        if isprime[s] == False :
            continue

        else :
            for i in range(2*s, root_n, s) :
                isprime[i] = False

    rtn = []
    for i, _ in enumerate(isprime) :
        if isprime[i] == True :
            rtn.append(i)

    return rtn

def main() :
    n = 600851475143
    p_list = eratosthenes(n)

    for p in reversed(p_list) :
        if n % p == 0 :
            return p

    return 1

if __name__ == "__main__" :
    ans = main()
    print(ans)
