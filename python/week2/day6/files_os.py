from os import mkdir,path
from shutil import rmtree,move

FILE_HOME = './resources/temporary_files/'

def create_file (file_name : str) :
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
        return False 
    directory_to_be_created= (f'{path}{name}')
    try : 
        mkdir(directory_to_be_created)
    except:
        print('directory {directory_to_be_created} cant be empty')
        return False
    else:
        return True
    

# if destination directory is empty then we remove directory 
# (move a directory with name to nothing)

def rename_directory(base_dir_path,from_name:str,to_name:str):
    source_dir = f'{base_dir_path}{from_name}'
    destination_dir = f'{base_dir_path}{to_name}'
    if (path.isdir(destination_dir)):
        print('destination directory already exists, can\'t move directory to destination')
        return False        
    if not (path.isdir(source_dir)):
        print('source directory does not exist, can\'t. can\'t move non existing directory')
        return False        
    try:
        move(source_dir,destination_dir)
    except OSError as e :
        print(f'an error was raised while trying to change folder name : {e}')
        return False
    else :
        if (not path.isdir(source_dir) )and( path.isdir(destination_dir)):
            print(f'directory was renamed from {source_dir} to {destination_dir}')
            return True
        else :
            print(f' action failed')
            if path.isdir(source_dir):
                print('source directory still available')
            if not path.isdir(destination_dir):
                print('destination directory not created ')
            return False
        
        
     

def create_directory_and_sub_file (base_dir_path : str , dir_name : str ,file_name:str) :
    # if one of them is empty thin it is False
    if not (dir_name and file_name) :
       print('directory name or file name cant be empty') 
       return False 
    
    dir_path = f'{base_dir_path}{dir_name}/'
    file_path = f'{dir_path}{file_name}'

    if path.isfile(file_path):
        print('file already exist')    
        return True 

    if not path.isdir(dir_path):
        if create_directory(dir_path):
            create_file(file_path)
            
            
    if path.isfile(file_path):
        print('file created successfully')
    else:
        print('failed to create file')        
    

def remove_directory(base_dir_path : str , dir_name : str ) :
    try:
        rmtree(f'{base_dir_path}{dir_name}')
    except:
        pass
    if path.isdir(f'{base_dir_path}{dir_name}'):
        print(f'failed to remove directory {base_dir_path}{dir_name}')
        return False 
    else :
        print(f'directory {base_dir_path}{dir_name} was removed successfully')
        return True
    
    

create_directory_and_sub_file(FILE_HOME,'job', 'file1.txt')
rename_directory(FILE_HOME,'job', 'job2')
remove_directory(FILE_HOME,'job')
remove_directory(FILE_HOME,'job2')


