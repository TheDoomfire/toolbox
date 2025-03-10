from dataclasses import dataclass
import re
from typing import List, Dict, Optional, Union, Pattern, Iterator

@dataclass
class PatternSpec:
    """Container for individual pattern with metadata"""
    compiled: Pattern
    description: str = ""
    example: str = ""

@dataclass
class MatcherGroup:
    """Group of patterns under a common category"""
    category: str
    patterns: List[PatternSpec]
    description: str = ""
    priority: int = 0

    def find_matches(self, text: str) -> Iterator[dict]:
        """Yield matches found in text for this group"""
        for pattern in self.patterns:
            for match in pattern.compiled.finditer(text):
                yield {
                    "category": self.category,
                    "match": match.group(),
                    "span": match.span(),
                    "pattern_description": pattern.description,
                    "example": pattern.example
                }

class PatternRegistry:
    """Central registry for managing pattern groups"""
    _groups: Dict[str, MatcherGroup] = {}
    
    @classmethod
    def register_pattern(
        cls,
        category: str,
        regex: str,
        *,
        description: str = "",
        example: str = "",
        flags: re.RegexFlag = re.IGNORECASE
    ):
        """Register a new pattern in a category"""
        try:
            compiled = re.compile(regex, flags)
        except re.error as e:
            raise ValueError(f"Invalid regex for {category}: {e}")

        spec = PatternSpec(compiled, description, example)
        
        if category not in cls._groups:
            cls._groups[category] = MatcherGroup(
                category=category,
                patterns=[],
                description=f"Patterns for {category} detection"
            )
            
        cls._groups[category].patterns.append(spec)

    @classmethod
    def find_matches(cls, text: str) -> List[dict]:
        """Find all matches across all registered patterns"""
        return sorted(
            (match for group in cls._groups.values() for match in group.find_matches(text)),
            key=lambda x: (-x['span'][0], x['category'])
        )

    @classmethod
    def get_categories(cls) -> List[str]:
        """Get list of registered categories"""
        return list(cls._groups.keys())

# Example usage ##################################################
# Register multiple URL patterns
PatternRegistry.register_pattern(
    "url",
    r"https?://(?:www\.)?[-\w@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-\w()@:%_+.~#?&/=]*",
    description="Standard HTTP/HTTPS URL",
    example="https://example.com"
)

PatternRegistry.register_pattern(
    "url",
    r"\b(?:www\.)[-\w@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-\w()@:%_+.~#?&/=]*",
    description="URL without protocol",
    example="www.example.com/path",
    flags=re.IGNORECASE
)

# Register email patterns
PatternRegistry.register_pattern(
    "email",
    r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b",
    description="Standard email format",
    example="user@example.com"
)

# Register file path patterns
PatternRegistry.register_pattern(
    "file_path",
    r"""
    (?:
        # Windows paths (C:\path\to\file.txt)
        [A-Za-z]:\\                  # Drive letter
        (?:[^\\/:*?"<>|\r\n]+\\)+    # Directory structure
        [^\\/:*?"<>|\r\n]*           # Filename
        \.\w{2,4}                    # File extension
    )|(?:
        # Unix paths (/home/user/file.txt or ~/file.txt)
        (?:\/|~\/)                   # Root or home directory
        (?:[^/\\:*?"<>|\r\n]+\/)*    # Directory structure
        [^/\\:*?"<>|\r\n]*           # Filename
        \.\w{2,4}                    # File extension
    )
    """,
    description="File paths with extensions (Windows or Unix format)",
    example="C:\\Users\\file.txt or /home/user/file.txt",
    flags=re.VERBOSE
)

PatternRegistry.register_pattern(
    "file_path",
    r"""
    \b
    (?:
        # Filename with extension (standalone)
        [\w\-]+\.[\w.]{2,10}        # Filename and extension
        (?:\.(?:gz|zip|tar))?       # Optional compressed extensions
    )\b
    """,
    description="Standalone filenames with common extensions",
    example="document.pdf or archive.tar.gz",
    flags=re.VERBOSE
)


# Detection example ##############################################
""" sample_text = "Check example.com and https://secure.site.com or contact user@domain.co.uk"
results = PatternRegistry.find_matches(sample_text)

for match in results:
    print(f"Category: {match['category']}")
    print(f"Matched: {match['match']}")
    print(f"Description: {match['pattern_description']}")
    print(f"Example: {match['example']}")
    print("-" * 50) """