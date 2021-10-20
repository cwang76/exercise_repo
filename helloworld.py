# This function prints Hello, world!

def helloworld():
    print('Hello, world!')


if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    
    helloworld()
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.

