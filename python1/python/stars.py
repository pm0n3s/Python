'''Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.'''

# def stars(arr):
#     for i in range(0, len(arr)):
#         print "*" * arr[i]
# x = [4, 6, 1, 3, 5, 7, 25]
# stars(x)

'''Part II
Modify the function above. Allow a list containing integers and strings to be passed to 
the draw_stars() function. When a string is passed, instead of displaying *, display the 
first letter of the string according to the example below. You may use the .lower() string 
method for this part.'''

def stars(arr):
    for i in range(0, len(arr)):
        if isinstance(arr[i], int):
            print "*" * arr[i]
        elif isinstance(arr[i], str):
            print arr[i][0].lower() * len(arr[i])

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)