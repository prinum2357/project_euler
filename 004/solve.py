#!/usr/bin/env/python3

def main() :
    rtn = 0
    for i in range(999, 99, -1) :
        for j in range(999, 99, -1) :
            p = i*j

            if str(p) == str(p)[::-1] :
                if p >= rtn :
                    rtn = p

    return rtn

if __name__ == "__main__" :
    ans = main()
    print(ans)
