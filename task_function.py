def get_summ(one, two, delimiter='&'):
    arg1_str=str(one)
    arg2_str=str(two)
    result=arg1_str+delimiter+arg2_str
    return result
total=get_summ('Learn', 'python')
print(total.upper())
