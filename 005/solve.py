#!/usr/bin/env/python3
from math import lcm

def main() :
    rtn = [i for i in range(1,21)]

    return lcm(*rtn)

if __name__ == "__main__" :
    ans = main()
    print(ans)
