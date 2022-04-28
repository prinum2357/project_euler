#!/usr/bin/env/python3

def collatz_length(n) :
    ln = 1
    while n != 1 :
        if n % 2 == 0 :
            n = n // 2
        
        else :
            n = 3 * n + 1

        ln += 1

    return ln
            

def main() :
    maximum = 0 
    idx = 0
    for i in range(1, 1000000) :
        if i % 100000 == 0 :
            print(i)
        c = collatz_length(i)
        if c > maximum :
            maximum = c
            idx = i
    
    return idx

if __name__ == "__main__" :
    ans = main()
    print(ans)
