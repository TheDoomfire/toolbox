import xml.etree.ElementTree as ET
from utils.config.files.validators.file_validator_registry import FileValidatorRegistry

@FileValidatorRegistry.register("xml")
def validate_xml(content: str) -> bool:
    try:
        ET.fromstring(content)
        return True
    except ET.ParseError:
        return False
