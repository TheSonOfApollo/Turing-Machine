# This file is used to test new functions, features, etc...

import sys, time

def delay_output(text): 
    delayTime = 14000000
    while delayTime > 0:
        delayTime -= 1
    print(text)


def retro(text): 
    for char in text: 
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.2) 
        



# Definitions are kept up here ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("\n")
print("Hello World")

print("\n")
delay_output("This is a test")
delay_output("This is the second part of the text")
testNumber = 3
delay_output("This is the third part of the test, tests until now: " + str(testNumber))

print("\n") 
retro("hello this is a retro test")