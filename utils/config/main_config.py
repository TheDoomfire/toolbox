from dataclasses import dataclass, field

# Local Imports
from utils.config.files.files import ProjectFiles
from utils.config.paths.paths import ProjectPaths


"""
Project Configuration Module
----------------------------

To save all configurations in one place. While being easy to use.

EXAMPLE:
    from utils.config.main_config import CONFIG
    welcome = CONFIG.WELCOME_MESSAGE
    root_path = CONFIG.PATHS.PROJECT_ROOT

TODO:
    Perhaps save every name in a list/object.
    Then for each name, have regex patterns, validations, schema, filetype, etc.

"""


# -------- EXPORTED MAIN CONFIG --------
# Only touch this if needed new classes are added.
@dataclass
class ProjectConfig:
    """Main configuration hub for the entire project"""
    PATHS: ProjectPaths = field(default_factory=ProjectPaths)

    FILES: ProjectFiles = field(default_factory=ProjectFiles)

    # Add: Files etc here?

    WELCOME_MESSAGE: str = "Hello World!"


# Instantiate the main configuration
CONFIG = ProjectConfig()