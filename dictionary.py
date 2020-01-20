def histogram(word):
    d = dict()
    for ch in word:
        # if ch not in d:
        #     d[ch] = 1
        # else:
        #     d[ch] += 1
        d[ch] = d.get(ch,0)+1

    return d

print(histogram("manigandan"))
def reverse_lookup(dic,v):
    for c in dic:
        if dic[c] == v:
            return c
    raise ValueError('Value not in the dictionary')

known = {0:0, 1:1}
def fib(n):
    if n in known:
        return  known[n]
    else:
        res = fib(n-1) + fib(n-2)
        known[n] = res
        return res

#print(fib(5))
# h = histogram('manigandan')
# print(reverse_lookup(h,5))
# for k in h:
#     print(k , "," , h[k])
