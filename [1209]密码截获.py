while True:
    try:
        stri = input()
        stri_len = len(stri)
    except EOFError:
        break
    maxlen = 0
    for i in range(stri_len):
        for j in range(i,stri_len):
            s = stri[i:j+1]
            if s == s[::-1] and maxlen < j - i + 1:
                maxlen = j - i + 1
    print(maxlen)
