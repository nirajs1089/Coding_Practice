def find_by_key(data, target):  # get the scalar value NOT a dict as a value for the matched key

    """

        :param data(Dict): to be searched in
        :param target(str):traverse to find the key
        :return:
        (str) returns the value of the key matched with target

    """

    # recursively search the dict for the key
    for key, value in data.items():
        if isinstance(value, dict):
            yield from find_by_key(value, target)
        elif key == target:
            yield value


def find_table_key(data, target):  # this works for getting non sub query tables

    """

        :param data(Dict): to be searched in
        :param target(str):traverse to find the key
        :return:
        (str) returns the value of the key matched with target -> 'table'
    """

    # recursively search the dict for the key


    if isinstance(data, list):
        yield from find_by_key_pattern(data[0], target)

    if isinstance(data, dict):

        for key, value in data.items():

            if isinstance(value, dict):
                if key == target:
                    if data[key].get('schema') is not None:  # do not get the alias but full table name
                        yield '{0}.{1}'.format(data[key]['schema'], data[key]['name'])
                elif key != target:
                    yield from find_table_key(value, target)
            elif isinstance(value, list) and len(value) > 0:
                for v in value:  # loop through each element of list which is a value in dict
                    yield from find_table_key(v, target)


def find_by_key_pattern(data, target):
    """

    :param data(Dict): to be searched in
    :param target(str):traverse to find the key
    :return:
    (Dict) matching the target using regex as the key name

    """
    # use regex to find the pattern in the key like subquery-\d in subquery-0,1,2
    if isinstance(data, list):
        yield from find_by_key_pattern(data[0], target)

    if isinstance(data, dict):

        pattern = r"{0}".format(target)

        find = re.compile(pattern)

        for key, value in data.items():

            if find.search(key) is not None:
                yield value  # return the value -> dictionary
            elif find.search(key) is None and isinstance(value, dict):
                yield from find_by_key_pattern(value, target)
            elif isinstance(value, list) and len(value) > 0:
                yield from find_by_key_pattern(value[0], target)
