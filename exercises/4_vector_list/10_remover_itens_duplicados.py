# Dada uma lista de números, remova os elementos duplicados.

my_list = [1,2,3,4,5,6,3,7,8,9]
my_list = list(dict.fromkeys(my_list))
print(my_list)