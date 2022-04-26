#!/usr/bin/env/python3

def main() :
    F0, F1 = 0, 1
    f, fs = [F0, F1], F0+F1
    s = 0

    f_next = sum(f)
    while f_next <= 4000000 :
        f_next = sum(f)
        f.append(f_next)
        fs += f_next
        
        if f_next % 2 == 0 :
            s += f_next

        f = f[1:]
    
    return s

if __name__ == "__main__" :
    ans = main()
    print(ans)
