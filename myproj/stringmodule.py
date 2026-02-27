
def find_names_greater(names: list[str], length: int) -> list[str]:
    """
    This function takes a list of names and an integer length, and returns a list of names that are greater than the specified length.

    Parameters:
    names (list[str]): A list of names to be filtered.
    length (int): The length threshold for filtering names.

    Returns:
    list[str]: A list of names that are greater than the specified length.
    """

    # big_names : list[str] = []
    # for name in names:
    #     if len(name) > length:
    #         big_names.append(name)

    # List Comprehension - A concise way to create lists. It consists of brackets containing an expression followed by a for clause,
    # then zero or more for or if clauses.
    return [name for name in names if len(name) > length]