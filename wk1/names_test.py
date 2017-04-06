import unittest
from names_challenge import names_func 


class TestNamesFunc(unittest.TestCase):
    """
    This is a simple test case that makes sure you've created a function that
    returns the correct values when called in different ways. Throughout our 
    class we will writing tests to give us a quick way to make sure things
    behave as expected.

    As a quick reference you can find a list built in assert methods here:
    https://docs.python.org/3/library/unittest.html#assert-methods
    """

    def test_names_func_exists(self):
        self.assertNotEqual(type(names_func), None)

    def test_names_func_returns_correct_list_of_lists(self):
        test_list = range(10)
        output = names_func(test_list, 2)
        # output should have a list of lists with 5 inner lists
        self.assertEqual(len(output), 5)

    def test_names_func_returns_correct_list_when_names_not_evenly_divis(self):
        test_list = range(11)
        output = names_func(test_list, 2)
        # output should still have list of list with 5 inner lists
        self.assertEqual(len(output), 5)

        # check that the remaining item has been added to another group
        item_check = [len(item) for item in output]
        self.assertEqual(3 in item_check, True)

    def test_that_a_remaining_group_of_3_is_handled_properly(self):
        test_list = range(18)
        output = names_func(test_list, 5)
        # output should have 4 inner lists
        self.assertEqual(len(output), 4)

        # check that inner lists has a group of 3
        item_check = [len(item) for item in output]
        self.assertEqual(3 in item_check, True)


if __name__ == '__main__':
    unittest.main()

# example solution
#def names_ans_func(a_list, size):
#    """
#    This is an example of how to solve the problem using a list comprehension
#    """
#    shuffle(a_list)
#    output =  [a_list[name: name+size] for name in range(0, len(a_list), size)]
#
#    # check to see if there isn't a full group as last elm if so add to other
#    if len(output[-1]) == 1:
#        remaining = output.pop(-1)
#        output[0].append(remaining)
#    return output
             
