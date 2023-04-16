from pathlib import Path 
import colorama 
from colorama import Fore,Back,Style
import sys 

colorama.init(autoreset=True)

def get_args():
    """Returns the commandline arguments. Must specify the path"""
    if len(sys.argv)<2:
        print("Please specify directory path")
        exit() 
    return sys.argv[1]

def full_path(directory:str)->Path:
    """Returns the full path to the chosen directory. Checks if its 
        '.' for current directory or full path to a directory
    """
    if directory ==".":
        return Path.cwd()
    else:
        if Path(directory).exists():
            return Path(directory)
        else:
            print("The directory path does not exist")
            exit()


def parsing_directory(name:str, path_directory:Path)->None:
    """Walks through the directories"""
    print(Fore.GREEN + Style.BRIGHT + '\n'+name)
    for path in path_directory.iterdir():
        if path.is_dir():
            subdirectory = str(path).split('/')[-1]
            print(Fore.CYAN + Style.BRIGHT + '\t> '+ subdirectory)
        if path.is_file():
            filepath = str(path).split('/')[-1]
            if(filepath[0] =='.'):
                print(Fore.BLUE + Style.DIM + '\t- ' + filepath)
            else:
                print(Fore.BLUE + Style.NORMAL + '\t- '+ filepath)


if __name__ == "__main__":
    directory_path = get_args()     
    directory_path = full_path(directory_path)    
    directory_name = str(directory_path).split('/')[-1]
    parsing_directory(directory_name,directory_path)
