import json
from utils.config.files.validators.file_validator_registry import FileValidatorRegistry


@FileValidatorRegistry.register("json")
def validate_json(content: str) -> bool:
    try:
        json.loads(content)
        return True
    except json.JSONDecodeError:
        return False
