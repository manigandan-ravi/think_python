def sep(addr):
    uname,domain = addr.split("@")

    return uname, domain

def printall(*word):
    print(word)


def sort_by_length(words):

    t = []
    for w in words:
        t.append((len(w),w))
        print(t)
    t.sort(reverse=True)
    print(t)
sort_by_length(('abc','mani','honey'))
#zip(t1,t2) --> list of tuples
#dict.item() --> list of tuples in key value pairs
# for index,element in enumerate("abc""b""c"):
#     print(index, element)
#print(printall(67,34,45))
# print(sep("manirsg16@gmail.com"))
