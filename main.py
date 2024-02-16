# main() file

from keyword import kwlist
import sys
import os
import urllib
import logging

from decorators import logging_decorators
# from decorators import file_identity_decorators
from decorators.file_identity_decorators import location_of_file, name_of_file

# Configure the logging system
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    filemode='w')

# Define a handler to output log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)


def print_function_call(executing_file_name, _=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Executing file: '{executing_file_name}'.")
            return func(*args, **kwargs)
        return wrapper
    
    return decorator

# @print_function_call(__file__)
def main():

    # Log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')    
    print("RUN: main().")
    # LESSON 1 - Running a modulized game
    # g.game.play_game()

    # Specify a script file to execute.
    # scriptToExecute = "PythonTutorial.py"
    # scriptToExecute = "ch11. NumpyArrays.py"
    script_to_execute = "ch12PandasBasics.py"    # Adjust this as needed
    
    # Execute the specified script
    execute_script( script_to_execute )
    return 
    
    
'''
# USED ONLY FOR CLASS INITIALIZATIONS
def __init__():
    print("RUN: __init__().")
    '''
    
# @print_function_call
@name_of_file
@location_of_file
def execute_script(script_to_execute, active_directory = None ):
    
    default_scripts_directory = "scripts"
    
    if active_directory is None:
        active_directory = default_scripts_directory
    else:
        active_directory = active_directory
        
    # Construct the path to the script file
    location_to_scripts = "./%s/%s" % (active_directory, script_to_execute)


    # Check if the script file exists
    if os.path.exists(location_to_scripts):
        print("Running file: %s" % script_to_execute)
        
        # Execute the script file
        exec( open(location_to_scripts).read())
    else:
        print( f"The script file: '{script_to_execute}' not found." )

if __name__ == "__main__":
    main()