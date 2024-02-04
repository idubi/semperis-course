
import random
# print (random.randint(0,5))
random.gauss(34.33,543534.66)
exit


RESURCE_DIR = './resources/temporary_files/'

def write_file_and_get_count_words_in_one_transaction (path,text,word_to_count):
    with open(path,'w+') as f : 
        f.writelines(text)
        f.seek(0)
        data = f.readlines()
        f.close()
        return str(data).count(word_to_count)    
    
word = 'hello'
file_name = f'{RESURCE_DIR}example.txt'
text = ''' 
- hello my friend 
- hello back 
- thanks , it is very funny to hear you and think about you at thesame time 
- to be or not to be is the best question 
'''
print (f' number of instances to {word} {write_file_and_get_count_words_in_one_transaction(file_name ,text,word)}')
print (f' number of instances to {"best"} {write_file_and_get_count_words_in_one_transaction(file_name ,text,"best")}')

print (random.randint(0,5))
    
    