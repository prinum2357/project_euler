#!/usr/bin/env/python3


def main() :
    for a in range(1, 1001) :
        for b in range(a, 1001-a) :
            c = 1000 - a - b
        
            if a**2 + b**2 == c**2 :
                return a*b*c

    return -1
    
if __name__ == "__main__" :
    ans = main()
    print(ans)
