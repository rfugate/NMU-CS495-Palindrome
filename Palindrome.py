with open('american-english', encoding='utf-8') as fp:
    
    #fileList = [line.strip() for line in fp]
    palindromeList = [line.strip() for line in fp if str(line.strip()) == str(line.strip())[::-1]]

    maxLength = max(len(s) for s in palindromeList)
    longestPalindromes = [s for s in palindromeList if len(s) == maxLength]
    
    #print("\n---  File List  ---")
    #print(fileList)
    print("\n---  Palindrome List  ---")
    print(palindromeList)
    print("\n---  Largest Palindrome   ---")
    print(longestPalindromes)
