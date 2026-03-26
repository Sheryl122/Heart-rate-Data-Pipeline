from data_cleaning import clean_heartrate_data
from statisticals import average, median, range
import statistics as stats

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
    
    data_variance = round(stats.variance(cleaned_values),2)
    
    # print out your data quality measure to the console
    print(f"File: {file}")
    print(f"This is the variance is {data_variance}")
    print(f"Cleaned Data: {cleaned_values}\nValues extracted from Data: {missing_values}")
   
    # print out your descriptive statistics to the console
    print(f"Average : {avg}")
    print(f"Median: {med}")
    print(f"Range : {rng}\n")



if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
