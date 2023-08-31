#convert from roman numerals to arabic numerals 

roman = input("Enter roman numeral string: ")

def romanNum(s):
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and dict[s[i]] > dict[s[i-1]]:
            int_val += dict[s[i]] - 2 * dict[s[i-1]]
        else:
            int_val += dict[s[i]]
    return int_val

print(romanNum(roman))
