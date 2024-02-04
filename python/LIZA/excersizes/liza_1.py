# # 
# Exercise: Writing to a Text File

# Instructions:
# Write a function called "write_to_file" that takes in two arguments: a file name and a list of strings. The function should open the file in write mode, and write each string from the list on a new line in the file. Make sure to close the file after writing.

# Example:
# write_to_file("output.txt", ["Hello", "World", "DevOps"])

# Expected Output:
# The file "output.txt" should be created (if it does not exist), and contain the following contents:
# Hello
# World
# DevOps

# Hint:
# To open a file in write mode, you can use the "with" statement with the built-in "open" function.
# Inside the "with" block, you can use the file object's "write" method to write to the file. 
# Remember to add a newline character ("\n") after each string to write them on separate lines.
# # 

def write_to_file(file_name:str,str_lst : list = []):
  assert len(str_lst) > 0  , 'list of strings to write is empty , Aborting Operation'
  try :
      with open(file_name,'w') as file :
          for line in str_lst:
              file.write(f'{line}\n')
          file.close()
  except Exception as E:
      print (f'failed to open file {file_name} to write ')




   