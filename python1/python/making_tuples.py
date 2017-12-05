'''Write a function that takes in a dictionary and returns a list of 
tuples where the first tuple item is the key and the second is the value.'''

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_in_tup_out(dic):
    output = []
    for k, v in dic.iteritems():
        output.append((k, v))
    print output

dict_in_tup_out(my_dict)