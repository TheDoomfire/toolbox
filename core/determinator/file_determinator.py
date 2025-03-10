# file: core/determinator/determinator.py
import os
from utils.config.files.validators.file_validator_registry import FileValidatorRegistry
from utils.config.files.files import ProjectFiles
from utils.config.main_config import CONFIG  # your file config


"""
    IF file extention is found, 
    perhaps return something that indicates its a filename
    IF raw content is found return something that indicates its a file. + file_config.extensions for that given file type
"""

def determine_file(input_data: str, project_files: ProjectFiles = CONFIG.FILES):
    """
    Determine the file type for the input data.
    1. First, check if input_data is a filename by matching extensions.
    2. If not, iterate through validators in the registry.
    """
    # Check if input_data is a filename by looking for an extension
    _, ext = os.path.splitext(input_data)
    if ext:
        for file_config in project_files.FILE_TYPES.values():
            if ext.lower() in (e.lower() for e in file_config.extensions):
                # Optionally validate file content if needed:
                try:
                    with open(input_data, 'r') as f:
                        content = f.read()
                    validator = FileValidatorRegistry.get_validator(file_config.id)
                    if not validator or validator(content):
                        return file_config
                except Exception:
                    # If file reading fails, fallback to extension-based config
                    return file_config

    # If input_data is raw content, use the validators
    file_type = FileValidatorRegistry.validate(input_data)
    if file_type:
        return project_files.FILE_TYPES.get(file_type)
    
    return None