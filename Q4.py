String = str(input("Please enter the String: "))
vowels = ["a", "e", "i", "o", "u"]

if not String:
    print("The input string is empty. Please try again.")
    String = str(input("Please enter the String: "))

def VowelCheck():
    vowelcount = 0
    for i in String:    
        if i.lower() in vowels:
            vowelcount += 1
    return vowelcount
vowelcount = VowelCheck()

if vowelcount == 0:
    print("Vowel count is 0")
else:
    print("The number of vowels in, ", String, "is", vowelcount)

rep = {}
for j in String:
    if j in rep:
        rep[j] += 1
    else:
        rep[j] = 1
print("The frequency of each character is: ", rep)

if all(value == 1 for value in rep.values()):
    print("Therea are no repeating characters")
else:
    maxount = max(rep.values())
    repchar = [char for char, count in rep.items() if count == maxount]
    if len(repchar) == 1:
        print(f"The most frequent character is '{repchar[0]}' with {maxount} occurrences.")
    else:
        print(f"The most frequent characters are {', '.join(repchar)} with {maxount} occurrences.")
        
