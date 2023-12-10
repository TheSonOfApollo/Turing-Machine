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
        time.sleep(0.025) 
    delayTime = 14000000
    while delayTime > 0:
        delayTime -= 1
    print("\n")
    
Zustandsmenge = {
    "Z0" : 0,
    "Za" : 1,
    "Zb" : 2, 
    "Zc" : 3, 
    "Zr" : "Ende"
}

def DTM(word): 
    wordAsList = list(word)
    i = len(wordAsList)
    j = 0
    zustand = 0
    while j < i: 
        if wordAsList[0] == "a" and zustand == 0: 
            wordAsList[0] = "x"
            j += 1
            zustand = 1
            #print("first case") #control purposes only
            retro(wordAsList)
        elif wordAsList[j] == "a" and zustand == 1: 
            wordAsList[j] = "x"
            j += 1
            #print("second case") #control purposes only
            retro(wordAsList)
        
            
            
            
        else: 
            retro("Simulation failed...") #infinite loop, could fix with "break" statement but makes it more funny not stopping
            # semidecidable languague at its finest 
    retro("Finished.")
    retro("Simulation success!")




# Definitions are kept up here ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("\n")
retro("Hello World")

'''
print("\n")
delay_output("This is a test")
delay_output("This is the second part of the text")
testNumber = 3
delay_output("This is the third part of the test, tests until now: " + str(testNumber))
'''

'''
print("\n") 
retro("hello this is a retro test")
print("\n") 
delay_output(retro("Hello"))
print("\n") 
delay_output(retro("If you are seing this"))
print("\n") 
delay_output(retro("The test was succesful!"))
'''

'''
retro("This is another test")
retro("Now we are testing other things")
retro("This was the last test, we have a success!")
retro(";)")
'''
DTM("aaa")