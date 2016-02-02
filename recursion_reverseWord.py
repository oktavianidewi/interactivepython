# recursively
# write a function that takes string as parameter
# and returns a new string that is reverse of the old string

from stack import stack

rev = stack()
wordlist = []
reverseWord = ""

# reverse word tanpa recursion
def reverse(words):
    # 4, 3, 2, 1, 0
    iterasi = len(words)-1

    while iterasi >= 0:
        letter = words[iterasi]
        rev.push(letter)
        iterasi = iterasi - 1

    sisa = words[:4]
    return sisa

# reverse word dengan recursion
def reverseRefactor(words):
    # 4, 3, 2, 1, 0
    iterasi = len(words)-1

    if iterasi >= 0:
        wordlist.append(words[iterasi])
        reverseRefactor(words[:iterasi])

    reverseWord = "".join(wordlist)
    return reverseWord

# return true/false kalo polindrome
print(reverseRefactor("fellow"))