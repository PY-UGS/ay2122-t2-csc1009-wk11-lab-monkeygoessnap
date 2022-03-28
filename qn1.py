# Question 1:
# Define a calculator class for 4 types of operations, with methods adder(), subtractor(),
# multiplier(), divider(), and clear().
# a. adder(): input1 + input2.
# b. subtractor(): input1 – input2.
# c. multiplier(): input1 * input2
# d. divider(): input1 / input2.
# e. clear(): reset to 0.
# Create an object for calculator class. Perform all operations by keyboard inputs for 2
# numbers. Then display the results. Finally reset to 0.

# Program output 1: 
# Enter number 1: 10  
# Enter number 2: 50
# Adder : 10.0 + 50.0 = 60.0
# Subtractor : 10.0 - 50.0 = -40.0
# Multiplier : 10.0 * 50.0 = 500.0
# Divider : 10.0 / 50.0 = 0.2
# Inputs cleared

# Program output 2 (Error checking):
# Enter number 1: 10
# Enter number 2: 0
# Adder : 10.0 + 0.0 = 10.0
# Subtractor : 10.0 - 0.0 = 10.0
# Multiplier : 10.0 * 0.0 = 0.0
# Divider : Cannot divide by zero!
# Inputs cleared

# create new calculator class
class Calculator:
    # constructor for calculator
    def __init__(self):
        # error checking to make sure input is a number
        try:
            # get input 1
            self.input1 = float(input("Enter number 1: "))
            # get input 2
            self.input2 = float(input("Enter number 2: "))
        # handles exception
        except:
            # prints invalid string
            print("invalid inputs, must be a number")
            # exits the program
            exit(1)
    # adder method
    def adder(self):
        # prints adder formatting
        print("Adder : ", end='')
        # prints results of input1 + input2
        print("{} + {} = {}".format(self.input1,self.input2,self.input1+self.input2))

    # subtractor method
    def subtractor(self):
        # prints substractor formatting
        print("Subtractor : ", end='')
        # prints results of input1 - input2
        print("{} - {} = {}".format(self.input1,self.input2,self.input1-self.input2))

    # multiplier method
    def multiplier(self):
        # prints multiplier formatting
        print("Multiplier : ", end='')
        # prints results of input1 * input2
        print("{} * {} = {}".format(self.input1,self.input2,self.input1*self.input2))

    # divider method
    def divider(self):
        # prints divider formatting
        print("Divider : ", end='')
        # handles error
        try:
            # prints results of input1/input2
            print("{} / {} = {}".format(self.input1,self.input2,self.input1 / self.input2))
        # handles zerodivision exception
        except ZeroDivisionError:
            # prints error string
            print("Cannot divide by zero!")

    # clear method
    def clear(self):
        # sets all inputs to 0
        self.input1 = 0
        self.input2 = 0
        # prints confirmation
        print("Inputs cleared")

# main method
def main():
    # initiate a new calculator object
    c = Calculator()
    # calls the adder method
    c.adder()
    # calls the subtractor method
    c.subtractor()
    # calls the multiplier method
    c.multiplier()
    # calls the divider method
    c.divider()
    # calls the clear method to clear inputs
    c.clear()

# check name and run main
if __name__ == '__main__':
    main()