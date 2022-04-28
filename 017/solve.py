#!/usr/bin/env/python3

def main() :
    number_letter = [""] * 1001
    
    # 1-19 step 1
    for idx, word in enumerate(["", "one" , "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]) :
        number_letter[idx] = word

    # 20-90 step 10
    for idx, word in enumerate(["twenty" , "thirty", "fourty", "fify", "sixty", "seventy", "eighty", "ninety"]) :
        number_letter[20 + idx*10] = word

    # 100-900 step 100
    for i in range(1, 10) :
        number_letter[i*100] = number_letter[i] + "hundred"

    # 1000
    number_letter[1000] = "onethousand"

    # 21-99 
    for i in range(2,10) :
        for j in range(1, 10) :
            number_letter[i*10+j] = number_letter[i*10] + number_letter[j]

    # 101 - 999 match *01 - *19
    for i in range(1, 10) :
        for j in range(1, 20) :
            number_letter[i*100+j] = number_letter[i*100] + "and" + number_letter[j]

    # 101 - 999 match *20 - *90
    for i in range(1, 10) :
        for j in range(2, 10) :
            number_letter[i*100+j*10] = number_letter[i*100] + "and" + number_letter[j*10]
    
    ## 101 - 999 except *01 - *19 and *20 - *90
    for i in range(1, 10) :
        for j in range(2,10) :
            for k in range(1, 10) :
                number_letter[i*100+j*10+k] = number_letter[i*100] + "and" + number_letter[j*10] + number_letter[k]

    total_length = 0
    for idx, word in enumerate(number_letter) :
        total_length += len(word)


    return total_length
    
if __name__ == "__main__" :
    ans = main()
    print(ans)
