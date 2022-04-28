#!/usr/bin/env/python3

def main() :
    n_list = [int(i) for i in list(str(2**1000))]
    return sum(n_list)

if __name__ == "__main__" :
    ans = main()
    print(ans)
