# ------------------------------------------------------------------------------------------------------------
# Create a function that will receive a value as an input and will convert it into integer if it is possible. 
# Create a decorator to the function that will add 100 to the result of the original function. 
# ------------------------------------------------------------------------------------------------------------

def ask_and_convert(func):
    def ask_for_values(*args):
        text_to_ask = args
        value = input(text_to_ask)
        return func(value)
    return ask_for_values

            

@ask_and_convert
def to_int(text):
    try:
        val = int(text)
    except:
        print (f'{text} cant be turned into integer')
        val =0
    return val + 100


print (to_int("type in text :"))

