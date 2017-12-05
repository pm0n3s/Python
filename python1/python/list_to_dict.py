'''Create a function that takes in two lists and creates a single dictionary 
where the first list contains keys and the second values. Assume the lists will 
be of equal length.
Your first function will take in two lists containing some strings.'''

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    if len(arr1) >= len(arr1):
        new_dict = dict(zip(arr1, arr2))
    else:
        new_dict = dict(zip(arr2, arr1))
    return new_dict
print make_dict(name, favorite_animal)