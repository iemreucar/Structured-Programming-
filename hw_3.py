def decodeText (key, code):
    result=""
    for i in code:
        result+=key[i]
    return result

key="the quick brown fox jumps over the lazy dog"
code = [7,12,11,11,2,7,0]
decoded_text=decodeText(key,code)
print(decoded_text)


# additional_codes from txt file

code0 = [35, 6, 12, 14, 24, 3, 6, 14, 3, 36, 3, 7, 36, 42, 2]
code1 = [24, 6, 14, 42, 35, 2, 3, 12, 5, 0, 3, 0, 1, 2, 3, 13, 2, 36, 8, 3, 35, 6, 14, 8, 3, 6, 14, 3, 0, 1, 2, 3, 7, 1, 36, 6, 14]
code2 = [36, 3, 42, 2, 14, 2, 11, 36, 0, 6, 12, 14, 3, 40, 36, 22, 36, 42, 2, 40, 3, 6, 14, 3, 0, 1, 2, 3, 10, 11, 36, 6, 14]
code3 = [6, 3, 35, 35, 3, 35, 6, 16, 0, 3, 22, 38, 3, 1, 2, 36, 40, 3, 5, 23, 3, 1, 6, 42, 1, 3, 36, 14, 40, 3, 24, 2, 2, 3, 0, 1, 2, 3, 24, 5, 14]
code4 = [36, 14, 40, 3, 0, 1, 2, 14, 3, 13, 1, 2, 14, 3, 6, 0, 3, 24, 3, 22, 38, 3, 0, 5, 11, 14, 3, 3, 6, 3, 35, 35, 3, 22, 36, 8, 2, 3, 24, 5, 11, 2, 3, 0, 1, 
36, 0, 3, 6, 3, 24, 23, 36, 11, 2, 3, 14, 12, 3, 12, 14, 2]

for i in [code0, code1, code2, code3, code4]: 
    decoded_text=decodeText(key,i)
    print(decoded_text)

# respect PENTAGRAM