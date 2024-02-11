# main() file

import sys
import os
import urllib

# DIRECTORIES
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.append(scripts_dir)

# BOTH IMPORT METHODS WORK
# from packages import mygame as g  # can use mygame.,anotherFunction> without the 'packages' prefix.
import packages.mygame as g         # can use g. but otherwise must always us packages.mygame.<anotherFunction>


# import draw
# import game
# from . import mygame.draw
# from . import mygame.game

# from mygame import draw
# from mygame import game



def main():
    print(" RUN: main().")
    # LESSON 1 - Running a modulized game
    # g.game.play_game()


    # scriptToExecute = "PythonTutorial.py"
    # scriptToExecute = "ch11. NumpyArrays.py"
    scriptToExecute = "ch12PandasBasics.py"
    
    ExeScript(scriptToExecute)
    
    
'''
# USED ONLY FOR CLASS INITIALIZATIONS
def __init__():
    print("RUN: __init__().")
    '''
def ExeScript(ScriptToExecute, ActiveDiretory=None):
    
    defaultScriptsDirectory = "scripts"
    
    if ActiveDiretory is None:
        ActiveDiretory = defaultScriptsDirectory
        
    LocationToScripts = "./%s/%s" % (ActiveDiretory, ScriptToExecute)
    # print("The file path is: s%s" % LocationToScripts)
    print("Running file: %s" % ScriptToExecute)
    exec( open(LocationToScripts).read())
if __name__ == "__main__":
    main()