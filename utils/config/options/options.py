from dataclasses import dataclass
from functools import wraps
from typing import Union, List, Optional, Callable, Dict, Any
import os


@dataclass
class SourceConfig:
    file: Union[str, List[str], None] = None
    path: Union[str, List[str], None] = None
    url: Union[str, List[str], None] = None


def with_source_config(
    processors: Dict[str, Callable[[Any], Any]] = None
) -> Callable:
    """Decorator to inject and preprocess SourceConfig parameters."""
    if processors is None:
        processors = {}

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, config: Optional[SourceConfig] = None, **kwargs) -> Any:
            # Merge config into kwargs (config takes lower precedence than explicit kwargs)
            if config:
                config_dict = {k: v for k, v in config.__dict__.items() if v is not None}
                kwargs = {**config_dict, **kwargs}

            # Preprocess parameters using the provided processor functions
            for param, processor in processors.items():
                if param in kwargs:
                    kwargs[param] = processor(kwargs[param])

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator



def process_file(file: Union[str, List[str]]) -> Union[str, List[str]]:
    # Example: Validate file existence or expand paths
    if isinstance(file, list):
        return [check_single_file(f) for f in file]
    else:
        return check_single_file(file)

def check_single_file(file: str) -> str:
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} does not exist!")
    return os.path.abspath(file)

def process_url(url: str) -> str:
    # Example: Validate URL format
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"Invalid URL: {url}")
    return url

# Map parameters to their processors
SOURCE_PROCESSORS = {
    "file": process_file,
    "url": process_url,
}


# EXAMPLE:
""" class Reader:
    @with_source_config(processors=SOURCE_PROCESSORS)
    def read(self, **kwargs) -> None:
        # Access parameters directly from kwargs (no need for config=SourceConfig(...))
        file = kwargs.get("file")
        url = kwargs.get("url")
        print(f"Reading from file={file}, url={url}")

class Writer:
    @with_source_config(processors=SOURCE_PROCESSORS)
    def write(self, **kwargs) -> None:
        path = kwargs.get("path")
        print(f"Writing to path={path}") """