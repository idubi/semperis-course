x = 'a2 Be a bear or not to Beeeeeee a goargea'

def count_for(str,char) :
    count = 0
    for chr in str:
        if chr.lower() == char.lower():
            count+=1
    return count

def count_while(str,char):
    count = 0
    iterator = 0  
    while (iterator < len(str)):
        if str[iterator].lower()==char.lower():
            count+=1
        iterator +=1        
    return count 

def count_find(str,char):
    return str.lower().count(char.lower())



def is_even(x : int ):
    return (x % 2 == 0) 

def foo(i:int)->str:
    return i

def is_pal (s:str) :
    pal_indicator = True
    counter = 0
    while (counter < (len(s)//2) and pal_indicator ):
        pal_indicator = s[counter] == s[len(s)-counter-1]
        counter+=1
    return pal_indicator   

if len(x)>=10:
    chr = 'a'
    a = 34
    cnt = count_while(x,chr)
    print(f'while loop show {cnt}')
    cnt = count_for(x,chr)
    print(f'for loop show {cnt}')
    cnt = count_find(x,chr)
    print(f'find show {cnt}')
    print (f'the number {a} even ? {is_even(a)}')
else :
    print('string too short')


print(foo('lllll'))
print(f'isPal --> {is_pal("abccba")}')

#AnalizaAnaliza!!!!4
