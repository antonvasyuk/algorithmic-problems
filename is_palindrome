def is_palindrome(s):
    '''является ли строка палиндромом'''
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha():
            if s[j].isalpha():
                if s[i].lower != s[j].lower:
                    return False
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return True
