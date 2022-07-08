""" Here we find a function, which allows adding new values to existing keys in dictionary."""


def adding_to_dict(dictionary, key, value):
    """ Here we find a function, which allows adding new values to existing keys in dictionary."""
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
