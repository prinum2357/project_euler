#!/usr/bin/env/python3

def eratosthenes(n) :
    limit = n + 1
    isprime = [True] * limit

    isprime[0] = False
    isprime[1] = False

    for s in range(2, limit) :

        if isprime[s] == False :
            continue

        else :
            for i in range(2*s, limit, s) :
                isprime[i] = False

    rtn = []
    for i, _ in enumerate(isprime) :
        if isprime[i] == True :
            rtn.append(i)

    return rtn

def main() :
    n = 2 
    while True : 
        p_list = eratosthenes(n)
        
        if len(p_list) >= 10001 :
            return p_list[10000]
            
        else :
            n *= 2

if __name__ == "__main__" :
    ans = main()
    print(ans)
