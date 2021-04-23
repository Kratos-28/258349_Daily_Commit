from itertools import zip_longest,chain,tee
def change_list(lst):
    lst2=tee(iter(lst),2)
    return list(chain.from_iterable(zip_longest(lst[1::2],lst[::2])))
n=[11,22,33,44,55,66,77,88]
print("before changing the list: ",n)
print("Change list to: ",change_list(n))
