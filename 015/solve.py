#!/usr/bin/env/python3

def factorial_list(n) :
    rtn = [1] * (n+1)
    for i in range(1, n+1) :
        rtn[i] = rtn[i-1] * i

    return rtn

def main() :
    
    f_list = factorial_list(40)
    return f_list[40] // (f_list[20] * f_list[20])

if __name__ == "__main__" :
    ans = main()
    print(ans)
