# write description here 
# write some more 

def delay(): 
    print("Delaying...")
    
def retro(text): 
    for char in text: 
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.025) 
    delayTime = 14000000
    while delayTime > 0:
        delayTime -= 1
    print("\n")  
    
# Definitions are kept up here ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("\nWelcome to the Deterministic Turing Machine Simulator")
delay()
print("The machine is set by default to identify the languague a^n b^n c^n, n element No ")
delay()
word = input("Enter the word you wish to check ")
print("You wrote: " + word)
