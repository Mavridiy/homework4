immutable_var = 1, 2, True, 'apple'
print(immutable_var)
#immutable_var[1] = 11
#print(immutable_var)   элементы кортежа не изменяемый
mutable_list = [1, 2, True, 'apple']
print(mutable_list)
mutable_list[2] = False
mutable_list.append([5,6])
print(mutable_list)