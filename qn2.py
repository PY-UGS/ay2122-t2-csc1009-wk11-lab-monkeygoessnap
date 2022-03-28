# Question 2:
# Define a clockTime class, with attributes hours, minutes, seconds, and methods
# setHours(), setMinutes(), setSeconds(), setTime(), and showTime().
# a. setHours(): only set hours’ value.
# b. setMinutes(): only set minutes’ value.
# c. setSeconds(): only set seconds’ value
# d. setTime(): set hours’, minutes’, seconds’ values.
# e. showTime(): display the time in the format of hours:minutes:seconds.
# Create an object for clockTime class. Set the time by keyboard inputs for hours’ value,
# minutes’ value, and seconds’ value. Then display the time after setting of the new time.

# class clocktime
class clockTime:
    # constructor
    def __init__(self):
        # set hour to 0
        self.hours = 0
        # set minutes to 0
        self.minutes = 0
        # set seconds to 0
        self.seconds = 0
    # method to set hours
    def setHours(self, hours):
        # assign hours to self hours field        
        self.hours = hours
    # method to set minutes
    def setMinutes(self, mins):
        # assign minutes to self minutes field
        self.minutes = mins
    # method to set seconds
    def setSeconds(self, secs):
        # assign seconds to self seconds field
        self.seconds = secs
    # method to set time
    def setTime(self, hour, mins, secs):
        # assign hour to self hours field
        self.hours = hour
        # assign mins to self minutes field
        self.minutes = mins
        # assign secs to self seconds field
        self.seconds = secs
    # method to shot time
    def showTime(self):
        # format output stirng to 00:00:00
        # prints the output string
        print("{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds))
# main method
def main():
    # create new clocktime object
    ct = clockTime()
    # error handling
    try:
        # error handling for float or string values
        hour = int(input("Enter hours value: "))
        # error handling for non permissible values of hour
        if hour < 0 or hour > 23:
            # raise exception
            raise Exception("Hour cannot be less than 0 or more than 23")
        # set hours
        ct.setHours(hour)
        # error handling for float or string values
        min = int(input("Enter minutes value: "))
        # error handling for non permissible values
        if min < 0 or min > 59:
            # raise exception
            raise Exception("Minute cannot be less than 0 or more than 59")
        # set minutes
        ct.setMinutes(min)
        # error handing for float or string values
        sec = int(input("Enter seconds value: "))
        # error handling for non permissible values
        if sec < 0 or sec > 59:
            # raise exception
            raise Exception("Seconds cannot be less than 0 or more than 59")
        # set seconds
        ct.setSeconds(sec)
    # handles exceptiosn
    except Exception as e:
        # prints the error strings
        print(e.args[0])
        # exits the program if error
        exit(1)
    # runs the method showtime which prints the formatted time string
    ct.showTime()

# check name and run main
if __name__ == '__main__':
    main()
