class test:
    id : str 
    name : str 
    
    def __init__(self, **args) -> None:
        id = args['id'] 
        name = args['name'] 


t1 = test(name = 'kuku' , id='34445')
t2 = test(name='ido' , id = '453534')
t3=t2.copy()
__init__({t1}{t2}{t3})