def print_params(a=1,b='строка',c=True):
    print(a,b,c)
print_params(c=[1,2,3])
print_params(b=25)
values_list=[25,'three',False]
values_dict={'a':6,'b':'for','c':True}
print_params(* values_list)
print_params(**values_dict)
values_list_2=[3.14,'ball']
print_params(*values_list_2,42)
