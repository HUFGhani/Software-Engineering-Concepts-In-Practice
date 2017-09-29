# Design a program called rainfall that consumes a list of numbers
# representing daily rainfall amounts as entered by a user. The list may
# contain the number -999 indicating the end of the data of interest.
# Produce the average of the non-negative values in the list up to the
# first -999 (if it shows up). There may be negative numbers other than
# -999 in the list.

def average_rainfall(input_list):
    # Here is where your code should go
    count = 0
    sum = 0
    if len(input_list) > 0:
        for n in input_list:
            if n == -999:
                break
            else:
                sum = sum + n
                count = count + 1
        average = sum / count
    return average

# Don't touch anything below this line.
if __name__ == "__main__":
    import sys

    # We get the arguments assuming that they are a list of *integers*
    # We parse the input to get the right type.
    # There's no error checking!
    rainfall_measurements = list(map(int, sys.argv[1:]))

    # We print the average.
    print(average_rainfall(rainfall_measurements))
