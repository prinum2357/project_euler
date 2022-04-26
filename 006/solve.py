#!/usr/bin/env/python3

def main() :
    a = sum([i**2 for i in range(1, 101)])
    b = sum([i for i in range(1, 101)]) ** 2

    return b - a

if __name__ == "__main__" :
    ans = main()
    print(ans)
