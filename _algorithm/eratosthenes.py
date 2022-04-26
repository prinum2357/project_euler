def eratosthenes(n) :
    limit = n + 1
    lis = [True] * limit

    lis[0] = False
    lis[1] = False

    for s in range(2, limit) :
        if lis[s] == False :
            continue

        else :
            for i in range(s+1, limit) :
                if i % s == 0 :
                    lis[i] = False

    rtn = []
    for i in range(len(lis)) :
        if lis[i] == True :
            rtn.append(i)

    return rtn


print(eratosthenes(100))
#eratosthenes(600851475143)
