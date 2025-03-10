# file: utils/validators/file_validator_registry.py

class FileValidatorRegistry:
    """Registry for file validators."""
    _validators = {}

    @classmethod
    def register(cls, file_type: str):
        """
        Decorator to register a validator function for a given file type.
        Usage:
            @FileValidatorRegistry.register("json")
            def validate_json(content):
                ...
        """
        def decorator(func):
            cls._validators[file_type] = func
            return func
        return decorator

    @classmethod
    def get_validator(cls, file_type: str):
        """Retrieve a validator for the given file type."""
        return cls._validators.get(file_type)

    @classmethod
    def validate(cls, content: str):
        """
        Iterates over all registered validators.
        Returns the file type if a validator returns True,
        or None if no validators match.
        """
        for file_type, validator in cls._validators.items():
            if validator(content):
                return file_type
        return None

    @classmethod
    def all_validators(cls):
        """Return a dictionary of all registered validators."""
        return cls._validators.copy()
