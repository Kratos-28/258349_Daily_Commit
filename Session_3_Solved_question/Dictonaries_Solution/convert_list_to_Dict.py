num_list = [11, 22, 33, 44]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)