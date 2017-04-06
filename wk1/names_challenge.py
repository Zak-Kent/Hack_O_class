""" 
The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists match the bin size. 

For example calling the function with a list of names and size 2 should return 
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is 
remaining add that name to another inner list.
"""

def names_func(a_list, size):
    """
    This func should take a list and size, break the list into lists of the
    size and return a list of lists.
    """
    
    return None


if __name__ == '__main__':
    # Any code here will run when the file is called by name on the command line
    print(names_func([1,], 2))
