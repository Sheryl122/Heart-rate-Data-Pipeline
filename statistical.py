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