from excersizes.liza_1 import write_to_file
from excersizes.liza_2 import count_files
from const.file_const import FILE_HOME


list_of_words = ["Hello", "World", "DevOps"]
# write_to_file(f'{FILE_HOME}output.txt',list_of_words)
dir =FILE_HOME

print (f'number of files in directory : {dir} is  {count_files(dir,True)} ' )
# print (f'number of files in directory : {"../../Home/ido"} is  {count_files("/Home/ido",True)} ' )
# print (f'number of files in directory : {dir} is  {count_files(dir+"example.txt")} ' )