x = 'HELLO WORLD'
y = x.lower()
z = y[0:4]
ALL = f'{y} {z}'

def print_str(name , str) :
    print(f'{name} ==> {str} ')
    
    
print_str('x',x)
print_str('y',y)
print_str('z',z)
print_str('ALL',ALL)