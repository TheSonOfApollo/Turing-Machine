# This file is used to test new functions, features, etc...


print("\n")
print("Hello World")

def delay_output(text): 
    i = 14000000
    while i > 0:
        i -= 1
    print(text)


print("\n")
delay_output("This is a test")
delay_output("This is the second part of the text")
testNumber = 3
delay_output("This is the third part of the test, tests until now: " + str(testNumber))