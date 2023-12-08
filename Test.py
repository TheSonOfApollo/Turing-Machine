# This file is used to test new functions, features, etc...

def delay_output(text): 
    i = 14000000
    while i > 0:
        i -= 1
    print(text)


def retro(text): 
    delay = 10000000
    i = len(text)
    k = 0
    while k < i: 
        print(text[k])
        k += 1
        while delay > 0: 
            delay -= 1



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