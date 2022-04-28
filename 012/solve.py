#!/usr/bin/env/python3

def count_of_divisor(n) :
    lis = [0] * (n+1)
    lis[0] = 0

    for i in range(1, n+1):
        for j in range(i, n+1, i) :
            lis[j] += 1

    return lis[-1]

def main() :
    
    t = [0] 
    n = 1
    while True :
        t.append(count_of_divisor(n))
        n += 1

        if n < 2 :
            continue

        if n % 2 == 0 :
            tn, tau = (n-2)//2*(n-1), t[(n-2)//2]*t[(n-1)]

        else :
            tn, tau = (n-2)*(n-1)//2, t[(n-2)]*t[(n-1)//2]


        if tau >= 500 :
            return tn

if __name__ == "__main__" :
    ans = main()
    print(ans)
