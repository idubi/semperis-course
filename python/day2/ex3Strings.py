# importing json module
import json

x = "0123456ed9abcdef"
y = "0123456efabcdesf"
z = "0123456ee9abcdef"
a = "0123456459abcdef"
b = "01234"





versions={
    'ed':'Version A',
    'ef':'Version A' 
}

def get_version(serian_number) : 
    if len(serian_number) > 9 :
        version_result= versions.get( serian_number[7:9]) or 'Version B'
    else :
        version_result = 'string is too short'  
    return version_result


    
print(f'x , {x}  ==>',get_version(x))
print(f'y , {y}  ==>',get_version(y))
print(f'z , {z}  ==>',get_version(z))
print(f'a , {a}  ==>',get_version(a))
print(f'b , {b}  ==>',get_version(b))
    


