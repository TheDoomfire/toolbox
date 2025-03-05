from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    """Central repository for ALL project paths"""
    # Base directories
    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent.parent
    
    #TEST_FOLDER: Path = PROJECT_ROOT / "test" 

    # API-related paths
    #TEST_MONKEY: Path = TEST_FOLDER / "monkey"
