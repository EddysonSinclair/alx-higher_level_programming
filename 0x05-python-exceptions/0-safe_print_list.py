#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Safely prints elements from my_list up to index x.

    Parameters:
        my_list (list): The list of elements to print.
        x (int): The index up to which elements should be printed.

    Returns:
        int: The number of elements actually printed.
    """
    count = 0
    try:
        for i in range(x):
            print("{:}".format(my_list[i]), end="")
            count += 1
        print()
    except IndexError:
        pass
        print()
    return (count)
