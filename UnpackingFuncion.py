def print_params(a=1, b='hello', c=True):
    print(a, b, c)

values_list = [5, 'cherry', False]
print_params(*values_list)

values_dict = {'a': 1, 'b': 'hello', 'c': True}
print_params(**values_dict)

values_list_2 = [10, 'string']
print_params(*values_list_2, 42)

print_params()
print_params(a='python')
print_params(b=25)
print_params(c=[1,2,3])


