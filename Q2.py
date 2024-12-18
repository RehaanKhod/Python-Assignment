String1 = str(input("Enter the first String: ")) #input the first string
String2 = str(input("Enter the second String: "))#input the second string

String1 = String1.lower()
String2 = String2.lower()
# converts both string to lowercase

sortedString1 = sorted(String1)
sortedString2 = sorted(String2)
# sorts both strings, separated each character from the words so they can be compared

print("String1 after sorting: ", sortedString1)
print("String2 after sorting: ", sortedString2)
# outputs the sorted strings

def AnagramCheck():
    if (sortedString1 == sortedString2):# compares the firsr sorted string with the second sorted string
        return(String1, " and " , String2, " are anagrams")
    else:
        return(String1, " and " , String2, " are NOT anagrams")
    # if both sorted string are the same, then they are anagrams. if not they are not anagrams
print(AnagramCheck())# prints the result of the anagram 

