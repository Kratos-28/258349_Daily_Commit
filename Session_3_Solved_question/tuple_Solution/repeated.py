#create a tuple
tuplex = 200, 400, 500, 600, 200, 300, 400, 400, 700 
print(tuplex)
#return the number of times it appears in the tuple.
n=int(input("Enter the number from tuple and check how many time is repeated: "))
count = tuplex.count(n)
print(count)