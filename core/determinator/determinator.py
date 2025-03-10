#from utils.config.main_config import CONFIG
from core.determinator.file_determinator import determine_file
from utils.config.matches.matches import PatternRegistry


"""

ALL TYPES:
    Text Type: 	str
    Numeric Types: 	int, float, complex
    Sequence Types: 	list, tuple, range
    Mapping Type: 	dict
    Set Types: 	set, frozenset
    Boolean Type: 	bool
    Binary Types: 	bytes, bytearray, memoryview
    None Type: 	NoneType

"""


class Determinator:
    def __init__(self, config):
        self.config = config

    def determine(self, *args, **kwargs):
        """Analyze each input in args and return metadata, using options from kwargs."""
        if not args:
            raise ValueError("At least one input argument is required.")
        
        results = [self._determine_single(arg, **kwargs) for arg in args]
        return results[0] if len(results) == 1 else results

    def _determine_single(self, input_data, **options):
        """Process a single input and return structured metadata, applying options."""
        result = {
            "type": type(input_data).__name__,
            "value": input_data,
            "details": {},
            "elements": []  # For collections (lists/dicts)
        }

        if isinstance(input_data, list):
            result["elements"] = [self._determine_single(item, **options) for item in input_data]
        elif isinstance(input_data, dict):
            result["elements"] = {
                key: self._determine_single(value, **options) for key, value in input_data.items()
            }
        elif isinstance(input_data, str):
            result["details"].update(self._determine_string(input_data, **options))
        # Extend here for other data types as needed
        
        return result


    def _determine_string(self, input_string, **options):
        """Analyze a string, considering options like filename."""
        details = {}
        # Example: Use options to enhance string analysis
        if 'myfirstoption' in options:
            details['filename'] = options['myfirstoption']
        # Add more analysis (e.g., check file path, extensions)

        """ TODO: HOW TO HANDLE THIS?
        
        Now we know its a string (_determine_string).

        We can use the PatternRegistry to find matches.
        matches  = PatternRegistry.find_matches(input_string)
        details.append(matches)

        If a match for a path is found, check if its a filename in it, extract it, 
        and run: determine_file(input_string)

        file = determine_file(input_string)
        details.append(file)
        
        nothing is found? run: determine_file(input_string)



        """

        # Look if there is a match in the string.
        # TODO: Maybe have path in here?
        # TODO: If the match is a certain type, then run something with it splitted?
        matches  = PatternRegistry.find_matches(input_string)
        if matches:
            #print("Matches:", matches)
            for match in matches:
                print("MATCH:", match)
                print("category", match['category'])
            #details['matches'].append(matches)

        # TODO: CHECK FOR PATH?
        # TODO: OR, CHECK FOR FILE?
        # TODO: IF matches.file or matches.path, then extract the name and run determine_file(input_string)?

        file = determine_file(input_string)
        if file:
            print("File: ", file)
            #details['file'].append(file)

        return details 
    

    def _determine_type(self, input_data):
        self.input_data = input_data  # Save the data
        self.type = type(input_data)   # Save its type
        return self.type


    def _determine_path(self, input_str):
        pass


    def _determine_matches(self, input_str):
        pass


    """ def _get_file_type(self, path):
        for file_type, pattern in self.file_patterns.items():
            if re.search(pattern, path, re.IGNORECASE):
                return file_type
        return 'unknown_file' """
    


    


def main():
    print("--- Running the determinators ---")


if __name__ == '__main__':
    main()