"""
Catz Facts

This code gets facts from cat facts api and gives you a little image too

This code contains the following functions:
  * funct(var), description
  * command_input(str = "", process = 0), call for an input while 
    allowing EXIT whenever
"""

def main():
    """
    SUMMARY (if different than main doc) 
    """
    print("\nWelcome to \"Catz Facts\"" +
          "\n  - " +
          "\n  - Enter EXIT at any time to leave. ")

def funct(var):
    """
    SUMMARY
    
    Args:
        var (TYPE): 
    
    Return:
        var (TYPE): 
    """

def command_input(prompt = "", process = 0):
    """
    A simple function that allows the user to input values while having access 
    to EXIT. If a bool_mode is enabled it will look for certain keywords and 
    process them as True or False
    
    Process values
        0, string mode, return the input
        1, bool mode, force the user to choose True or False
        2, bool mode passthrough, ask the user if they'd like to do something,
           if they don't input anything return False
        
    Args:
        prompt (str = ""): The prompt for asking the user with
        process (int = 0): Determines the process mode
    
    Return:
        return_input (str): The user input after having checked for exit
        (bool): If bool mode is on
        return_bool (bool): If bool mode passthrough is on
    """
    # Bool mode check words
    true_words = ["yes", "correct", "true"]
    false_words =["no", "incorrect", "false"]
    
    if process == 0:
        # String mode
        return_input = input(prompt)
        if return_input.lower() == "exit":
            print("\nExiting...\n")
            exit()
        else:
            return return_input
    elif process == 1:
        # Bool mode
        while(True):
            bool_input = input(prompt).lower()
            if bool_input == "exit":
                print("\nExiting...\n")
                exit()
            else:
                if bool_input == "y" or bool_input in true_words:
                    return True
                    break
                if bool_input == "n" or bool_input in false_words:
                    return False
                    break
                input("\nFailed bool_mode input, please use Y or N ")
    elif process == 2:
        # Bool mode passthrough
        bool_input = input(prompt).lower()
        if bool_input == "exit":
            print("\nExiting...\n")
            exit()
        else:
            return_bool = False
            if bool_input == "y" or bool_input in true_words:
                return_bool = True
            return return_bool

if __name__ == '__main__':
    main()