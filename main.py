# Local Imports
from core.determinator.determinator import Determinator
from utils.config.main_config import CONFIG
#from core import exporter


"""

TODO:
    Create a cental place for all **kwargs.
        like:
        
        kwargs = {
            'file': "Example file or/and extension",
            'path': "Example path or/and filepath",
            'data': "mydata",
        }
        Then have a Reader, Exporter, etc use these.

    I want to export a file:

    Exporter.export(data="mydata", filename="mydata.json")
    or
    Exporter.export(varible)




"""


def main():
    print("Running the main app.")
    print(CONFIG.WELCOME_MESSAGE)
    #the_module.my_module("Testing")

    input_data = [1, 2, 3]
    input_data = "Testing"
    """ 
    input_data = "https://mywebsite.com/"
    input_data = "https://www.mywebsite.com/"
    # paths
    input_data = "D:\Downloads"
    input_data = "D:/Downloads"
    input_data = "/home/user/Downloads"

    # Path + filename + extension
    input_data = "Downloads/my_file.json"

    # filename + extension
    input_data = "my_file.csv"

    """


    input_data = "https://www.mywebsite.com/"
    # Create an INSTANCE first
    config = {}  # Your configuration dictionary here
    determinator = Determinator(config)  # Instance creation

    result = determinator.determine(input_data)  # Call on instance
    print("Result:", result)



if __name__ == '__main__':
    main()