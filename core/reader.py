from core.determinator.determinator import Determinator

"""
    Get options
"""


class Reader:
    def __init__(self, config):
        self.config = config


    def reader(self, *args, **kwargs):
        """Analyze each input in args and return metadata, using options from kwargs."""
        config = {}

        if not args:
            raise ValueError("At least one input argument is required.")
        
        # TODO: Check options
        options = self._find_options(**kwargs)
        # TODO: check if filename, path, filepath
        if 'filename' in options:
            config['filename'] = options['filename']
        if 'path' in options:
            config['path'] = options['path']
        if 'filepath' in options:
            config['filepath'] = options['filepath']

        # If I have a file.
        if config['filepath']:
            # TODO: Run reader based on the file type.
            pass
        elif config['path'] and config['filename']:
            # TODO: Run reader based on the path and filename.
            pass
        else:
            determinator = Determinator(config)  # Instance creation
            result = determinator.determine(*args)  # Call on instance
            # TODO: FIND THE INFORMATION NEEDED TO READ IT.



        """ results = [self._reader_single(arg, **kwargs) for arg in args]
        return results[0] if len(results) == 1 else results """


    def _find_options(self, **options):
        """Find the options"""
        result = {}
        if 'path' in options:
            path = options['path']
            result['path'] = path
        if 'filename' in options:
            filename = options['filename']
            result['filename'] = filename
        if 'filepath' in options:
            filepath = options['filepath']
            result['filename'] = filepath

        # TODO: If result, return it?
        return result


    def _reader_single(self, input_data, **options):
        """Read the file based on the input data"""
        pass


def main():
    print("--- Running the: reader ---")


if __name__ == '__main__':
    main()