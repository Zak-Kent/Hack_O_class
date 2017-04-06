from random import shuffle


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

def test_func(a_list, size):
    """
    This is an example of how to solve the problem using a list comprehension
    """
    shuffle(a_list)
    output =  [a_list[name: name+size] for name in range(0, len(a_list), size)] 

    # check to see if there is only one name in last group if so add to another
    if len(output[-1]) == 1:
        remaining = output.pop(-1)
        output[0].append(remaining)
            
    return output

if __name__ == '__main__':
    test = names_ans_func(range(11), 2)
#    test = [item for item in test]
    print("here is my result: {}".format(test))
