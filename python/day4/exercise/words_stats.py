strings_to_process = [ "who is a question that reffer other people", "is to be or not to be , that is a good question"]



def count_words(list_of_words):
    dict_word_counter = {}
    set_of_words = set()
    # loooking for the word in the dictionay increase each encounter
    for word in list_of_words:
        dict_word_counter[word]=(dict_word_counter.get(word) or 0 ) + 1
        set_of_words.add(word)
    dict_word_counter['set_of_words'] = set_of_words
    return dict_word_counter

def print_dict_recurrency(dict) : 
   for item in dict:
        if item == 'set_of_words':
            continue
        left_align_text = item.ljust(15,'.')
        right_align_text = str(dict.get(item)).rjust(5,'.')
        print(f'\t\t{left_align_text}{right_align_text}')  

sentences_statistics = {}
for i in range(2) :
  sentences_statistics[i] = count_words(strings_to_process[i].split())
    
print('first sentence statistics  : ')
print_dict_recurrency(sentences_statistics[1])

print('seccond sentence statistics :') 
print_dict_recurrency(sentences_statistics[1])


print(f'common values : {sentences_statistics[0].get("set_of_words") & sentences_statistics[1].get("set_of_words")  }')
print(f'Diff values : {sentences_statistics[0].get("set_of_words") ^ sentences_statistics[1].get("set_of_words")  }')







    
    
    

          
        
        
    

