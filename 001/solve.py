#!/usr/bin/env/python3

def main() :
    s = 0
    for i in range(1000) :
        if i % 3 == 0 or i % 5 == 0 :
            s += i

    return s

if __name__ == "__main__" :
    ans = main()
    print(ans)
