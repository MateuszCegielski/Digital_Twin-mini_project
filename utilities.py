""" Here we find a function, which allows adding new values to existing keys in dictionary."""


def add_to_dict(final_dict, key, value):
    """ Here we find a function, which allows adding new values to existing keys in dictionary."""
    final_dict[key].append(value)
    return final_dict
