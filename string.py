def find(word,char):

    for i in range(len(word)):
        if(word[i] == char):
            return i

    return -1

def freq(word,char):
    count = 0
    for ch in word:
        if ch == char:
            count += 1
    return count
# print(freq('banana', 'a'))

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print (letter)

# print(in_both('mani', 'manigandan'))

def is_reverse(word1,word2):

    if len(word1)!=len(word2):
        return False

    else:
        i = 0
        j = len(word2)
        for ch in word1:
            if ch != word2[j-1]:
                return False
            j -= 1
        return True

#print(is_reverse('pots','stopp'))

def is_asc(word):

    if(len(word))<=1:
        return True
    if(word[0] > word[1]):
        return False
    return is_asc(word[1:])

print(is_asc("abcd"))