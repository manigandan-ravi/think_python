

class Cards:

    suite_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit=0,rank=0):
        self.suite = suit
        self.rank = rank

    def __str__(self):
        return ('%s of %s'%(Cards.rank_names[self.rank],Cards.suite_names[self.suite]))

    def __cmp__(self, other):
        t1 = self.rank,self.suite
        t2 = other.rank,other.suite
        return cmp(t1,t2)


c1 = Cards(2,11)
c2 = Cards(3,12)
print(c1.__cmp__(c2))