# Python code to convert into dictionary
def Convert(tup, di):
    di = dict(tup)
    return di
      
# Driver Code 
tups = [("akash", 10), ("Aman", 12), ("Raju", 14), 
    ("suraj", 20), ("Dhiraj", 25), ("Shivam", 30)]
dictionary = {}
print (Convert(tups, dictionary))