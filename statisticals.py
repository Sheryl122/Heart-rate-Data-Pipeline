import statistics as stats
import math as m

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for i in data:
        total += i
    return round(total / len(data), 2)

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

def range(data: list) -> float:
    """
    """
    max_num = data[0]

    for item in data: 
        if item > max_num:
            max_num = item

    min_num = data[0]
    for item in data:
        if item < min_num:
            min_num = item
    
    data_range = max_num - min_num

    return f"Minimum: {min_num}, Maximum: {max_num}, Range: {data_range}"

def data_variance(data: list) -> float:
    calc_variance = round(stats.variance(data),2)
    standard_dev = round(m.sqrt(calc_variance),2)
    
    return calc_variance, standard_dev


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass