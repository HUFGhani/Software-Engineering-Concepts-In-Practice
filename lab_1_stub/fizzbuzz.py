# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print “Fizz” instead of the number and for the
# multiples of five print “Buzz”. For numbers which are multiples of
# both three and five print “FizzBuzz”.


for num in range(1,100):
    msg = ""
    if num % 3 ==0:
        msg += "Fizz"
    if num % 5 ==0:
        msg += "Buzz"
    if not msg :
        msg += str(num)
    print(msg)
