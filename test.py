def fix_input(option, word):
    if option == 'fn' or option == 'ln':
        mx = 30
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'kim' or option == 'rk':
        mx = 15
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'pn':
        mx = 4
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'pos':
        mx = 65
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'eg':
        return word[:1]

    elif option == 'hr':
        mx = 3
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'et':
        mx = 3
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word

    elif option == 'email':
        mx = 90
        wlen = len(word)
        for x in range(0 ,(mx-wlen)):
            word = word+' '
        return word
    
print(len(fix_input('email','nyasha')))