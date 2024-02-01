def change_list_index(lst):
    try:
        lst[5]="a"   
    except ZeroDivisionError:
        print(f'a zero divide error')
        raise
    # except:
    #     print(f'any error')
    finally :
        raise
         
    
def change_list_index_assertion(lst):
    try:
        assert  len(lst) > 5 ,'ljkjkkj'  
    except ZeroDivisionError:
        print(f'a zero divide error')
    except:
        print(f'any error')
    finally :
        return 0
# lst = [3,4,5,6,7,7,7,7,7,7,7,7,6]
# lst = [7,7,7,7,6]
lst = '4354535435353453553'


def add_to_set(ss,item) :
    ss.update(item)
    
# print(f'{lst}    ,{change_list_index(lst) } ==> {lst}')
s = {1,2,3}
add_to_set(s,[4])
print(s)
add_to_set(s,[9])

add_to_set(s,[3])
print(s)
