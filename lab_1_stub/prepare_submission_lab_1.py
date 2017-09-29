from pathlib import Path
import argparse
import zipfile
assignment_name = "Lab1"

def file2string(path):
    with path.open('r') as f:
        return f.read()

def check_file(path, stub=""):
    if path.exists():
        print('%s exists' % path.name)
        contents = file2string(path).strip()
        if contents == stub:
            print('%s is empty or identical to the stub. Not including it!' % path.name)
        else:
            print('%s seems to be modified. Adding it to submission archive.' % path.name)
            return path
    return None # the default

def make_submission(assignment, username):
    dirp = Path('.')
    target_name = '%s_%s'%(username, assignment)
    target_filename = (target_name + '.zip')
    print('Creating zipped file called %s for submission.' % target_filename)
    try:
        sub = zipfile.ZipFile(target_filename, mode='w', compression=zipfile.ZIP_DEFLATED)
    except NotImplementedError:
        sub = zipfile.ZipFile(target_filename, mode='w')

    fizz = check_file(Path('fizzbuzz.py'), '''# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print “Fizz” instead of the number and for the
# multiples of five print “Buzz”. For numbers which are multiples of
# both three and five print “FizzBuzz”.''')

    if fizz:
        sub.write(str(fizz), str(Path(target_name) / fizz.name))

    rain = check_file(Path('rainfall.py'), '''# Design a program called rainfall that consumes a list of numbers
# representing daily rainfall amounts as entered by a user. The list may
# contain the number -999 indicating the end of the data of interest.
# Produce the average of the non-negative values in the list up to the
# first -999 (if it shows up). There may be negative numbers other than
# -999 in the list.

def average_rainfall(input_list):
    # Here is where your code should go
    return "Your computed average as a integer" #<-- change this!

# Don't touch anything below this line.
if __name__ == "__main__":
    import sys

    # We get the arguments assuming that they are a list of *integers*
    rainfall_measurements = sys.argv[1:]

    # We print the average.
    print(average_rainfall(rainfall_measurements))''')
    if rain:
        sub.write(str(rain), str(Path(target_name) / rain.name))
    golf = Path('fizzbuzzgolf.py')
    if golf.exists():
        print("You've chosen to play fizzbuzz golf! Cool. Including.")
        sub.write(str(golf), str(Path(target_name) / golf.name))
    else:
        print("You're don't seem to be playing fizzbuzz golf, which is fine! But check your submission if you intended to.")
    print('\nYour submittable archive is called %s' % target_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sanity check and prepare your %s for upload to Blackboard.' % assignment_name)
    parser.add_argument('username', help="Your central username, often looks like 'mbassbp2'.")
    #parser.add_argument('srcdir', help="The path to the directory containing all the parts of your submission. You can use a relative path from the directory you run the script in.")
    args = parser.parse_args()

    make_submission(assignment_name, args.username)
