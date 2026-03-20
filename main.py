def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    #loop over the data and remove any values that are not integers or are outside of a reasonable range (e.g., 30-220 bpm)
    #if statements
    """
    
    cleaned_values = []
    missing_values = []

    for item in data:
        if item.isdigit() and 30 <= int(item) <= 220:
            cleaned_values.append(int(item))
        else:
            missing_values.append(item)
    
    return cleaned_values, missing_values
    


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


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    f = open(file)
    for line in f:
        data.append(line.strip())
    
    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_values, missing_values = clean_heartrate_data(data)
    
    # calculate the average, median, and range of this file using the functions you've wrote
    avg = average(cleaned_values)
    med = median(cleaned_values)
    rng = range(cleaned_values)
    
    # print out your data quality measure to the console
    print(f"File: {file}")
    print(f"Cleaned Data: {cleaned_values}\n Values extracted from Data: {missing_values}")
   
    # print out your descriptive statistics to the console
    print(f"This is the average for {file} : {avg}")
    print(f"This is the median for {file} : {med}")
    print(f"This is the range for {file} : {rng}\n")


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
