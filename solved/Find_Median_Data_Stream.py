def median_stream(inst, num_list):
    """
    """

    headers = [ "new", "small", "large"]
    rows = []


    import math

    # split the incoming numbers into 1 lists small and large
    small,large = [],[]
    if len(num_list) == 0:
        return None
    index = math.ceil(len(num_list)/2)
    middle_num = num_list[index-1]
    # sort the list optional
    num_list = sorted(num_list)
    print(num_list)
    # heapq.heapify()
    for new in num_list:
        # if the input is less than the middle number than in small else large list
        if new <= middle_num:
            # insert the numbers in small list as max heap with -ve numbers so largest is the root
            heapq.heappush(small,-new)
        else:
            heapq.heappush(large, new)

        rows.append([new, str(small), str(large)])

    table_data(headers, rows)

    rows = []
    # if the size of heaps is imbalanced then balance them
    if (len(small) - len(large)) > 1:
        headers = [ "small", "large"]
        while (len(small) - len(large)) != 1:
            if (len(small) - len(large)) > 1:  # small is bigger than large by 2 or more
                extra = heapq.heappop(small)
                heapq.heappush(large, -extra)
            rows.append([str(small), str(large)])
        table_data(headers, rows)

    elif len(small) < len(large):
        headers = [ "small", "large"]
        while len(small) != len(large):
            if (len(small) - len(large)) > 1:  # small is bigger than large by 2 or more
                extra = heapq.heappop(small)
                heapq.heappush(large, -extra)
            rows.append([str(small), str(large)])
        table_data(headers, rows)

    # since for odd count , median is root of small then small = (large OR large + 1 ) is intended
    median = None

    if len(num_list) % 2 ==0:
        median = (-heapq.heappop(small)+heapq.heappop(large))/2
    else:
        median = -heapq.heappop(small)

    print(median)

median_stream("",[1, 1, 1, 1, 2, 3, 4, 2, 1, 2, 3])
