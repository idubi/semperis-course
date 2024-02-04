# #
# Exercise: Counting Files in a Directory

# Instructions:
# Write a Python program that counts the number of files in a specified directory. 

# Example:
# Suppose we have a directory named "documents" that contains the following files:
# - file1.txt
# - file2.txt
# - file3.txt

# The program should output: 
# Number of files in directory: 3

# Hint:
# To solve this exercise, you can use the os module in Python. 
# The os module provides functions for interacting with the operating system, 
# including working with directories. Specifically, you can use the os.listdir() 
# function to get a list of files in a directory, and then use the len() 
# function to count the number of files in the list.
# #


from os import listdir
from os.path import isfile
# mode_recoursive - by default dont look for subdirectories , but if true , then drill down 
def count_files(directory_path , mode_recoursive = False) :
    try:
        all_entities = listdir(directory_path)  
        counter = 0
        for path in all_entities:
            path_of_dir_and_entity = f'{directory_path}{path}'
            if  isfile(path_of_dir_and_entity) :
                counter+=1
            else : 
                if mode_recoursive :
                    # directory is not a file so if no recoursive then it worth 0
                    counter += count_files(path_of_dir_and_entity+'/',mode_recoursive)
        return counter
    except FileNotFoundError  :
            return 0
    except NotADirectoryError :
        # path not exist or not a file
        if isfile(directory_path) : 
            return 1
        return 0 
        
