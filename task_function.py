def get_summ(one, two, delimiter = '&'):
    result = f'{one}{delimiter}{two}'
    return result


total = get_summ('Learn', 'python')
print(total.upper())
