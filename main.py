# Local Imports
from utils.config.main_config import CONFIG
#from test_module import the_module


def main():
    print("Running the main app.")
    #the_module.my_module("Testing")

    print(CONFIG.WELCOME_MESSAGE)


if __name__ == '__main__':
    main()