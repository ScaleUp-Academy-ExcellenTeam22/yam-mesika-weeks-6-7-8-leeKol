from typing import Callable, Collection


def group_by(function: Callable, iterable: Collection) -> dict:
    """
        The function receives a function as the first parameter, and iterable as the second parameter.
        The function returns a dictionary, where the keys are the values
        returned from the function passed as the first parameter,
        and the value of each key is a list of all the items for which the value appearing
        in the key is returned.
        :param function: The function that will be executed on the iterable items.
        :param iterable: The iterable whose items will be grouped in a dictionary
               according to the results of the function.
        :return: A dictionary that groups the iterable items according to the results of the function.
    """
    group_dictionary = {}
    for item in iterable:
        group_dictionary.setdefault(function(item), []).append(item)
    return group_dictionary
