from dataclasses import dataclass
from typing import Callable, List, Optional, Dict
from utils.config.files.validators.file_validator_registry import FileValidatorRegistry



@dataclass
class FileTypeConfig:
    id: str  # e.g., 'json'
    extensions: List[str]
    mime: Optional[str] = None
    type_category: Optional[str] = None  # e.g., 'data', 'script', 'markup'
    validator: Optional[Callable[[str], bool]] = None
    description: Optional[str] = None


class ProjectFiles:
    """Central configuration for file types used throughout the project."""
    FILE_TYPES: Dict[str, FileTypeConfig] = {
        "json": FileTypeConfig(
            id="json",
            extensions=[".json"],
            mime="application/json",
            type_category="data",
            description="JavaScript Object Notation"
        ),
        "javascript": FileTypeConfig(
            id="javascript",
            extensions=[".js", ".jsx"],
            mime="application/javascript",
            type_category="script",
            description="JavaScript file"
        ),
        "python": FileTypeConfig(
            id="python",
            extensions=[".py"],
            mime="text/x-python",
            type_category="script",
            description="Python source file"
        ),
        "xml": FileTypeConfig(
            id="xml",
            extensions=[".xml"],
            mime="application/xml",
            type_category="data",
            validator=None,  # You could add an XML validator here
            description="eXtensible Markup Language"
        ),
    }