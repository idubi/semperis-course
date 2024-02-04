from os import mkdir
from ..LIZA.const.file_const import FILE_HOME

def crete_file (file_name : str) :
    try :
        with open(file_name, 'w') as f : 
            f.close()
    except:
        print('failed to create file')
        return False
    else:
        return True

def create_directory (name : str , path : str = '' ):
    if not name:
        print('directory name cant be empty')
        return '' 
    directory_to_be_created= (f'{path}{name}')
    try : 
        mkdir(directory_to_be_created)
    except:
        print('directory {directory_to_be_created} cant be empty')
        return ''
    else:
        return (f'{path}{name}/')
    
def execute_ex_1 (base_dir_path : str = FILE_HOME, dir_name : str = '') :
    created_directory = create_directory(dir_name,base_dir_path)
    if created_directory :
        crete_file('file1.txt',create_directory)



execute_ex_1('job') 


