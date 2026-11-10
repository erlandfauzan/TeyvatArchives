from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class TeyvatBookRecord:
    book_id: str
    title: str
    author: str = ""
    department: str = ""   # Disamakan jadi department
    ddc_code: str = ""
    marc_fields: Dict[str, str] = field(default_factory=dict)

@dataclass
class ValidationResult:
    book_id: str
    title: str
    is_valid: bool
    errors: List[str]