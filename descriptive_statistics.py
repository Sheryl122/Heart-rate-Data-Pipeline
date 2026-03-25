def stats_module(


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for i in data:
        total += i
    return round(total / len(data), 2)


# median of odd number of elements is middle num which is data[len // 2]
#median of an even number is (data[(len//2) - 1] - data[(len//2)])/2
def median(data: list) -> float:
    """
    """
    sorted_data = sorted(data)
    data_length = len(sorted_data)  
    middle_num = data_length // 2
    
    if data_length % 2 == 0:
        median = (sorted_data[middle_num - 1] + sorted_data[middle_num])/2
    
    else:
        median = sorted_data[(middle_num)]

    return median

# def range(data: list) -> float:
#     """
#     """
#     max_num = data[0]

#     for item in data: 
#         if item > max_num:
#             max_num = item

    min_num = data[0]
    for item in data:
        if item < min_num:
            min_num = item
    
    data_range = max_num - min_num

    return f"Minimum: {min_num}, Maximum: {max_num}, Range: {data_range}"
)