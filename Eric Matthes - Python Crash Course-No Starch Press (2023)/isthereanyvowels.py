string1 = "Hello python"
vowels = ['a', 'e', 'i', 'o', 'u']
for i in vowels:    #iterate ech element from vowels
    if i in string1.lower(): #each element from vowel is checking in the lowered string1
        print(f"Vowel {i} found in string.")    #If that is true print the element is present in the string named str1
