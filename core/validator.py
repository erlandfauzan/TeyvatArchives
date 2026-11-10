import json
import re
from core.models import TeyvatBookRecord, ValidationResult

class TeyvatArchiveValidator:
    def __init__(self, rules_path: str = "config/validation_rules.json"):
        with open(rules_path, "r") as f:
            self.rules = json.load(f)
        
        self.mandatory_tags = self.rules.get("mandatory_marc_tags", [])
        self.ddc_pattern = re.compile(r"^\d{3}(\.\d+)?$")

    def validate_single_record(self, record_data: dict) -> ValidationResult:
        errors = []
        try:
            record = TeyvatBookRecord(**record_data)
        except Exception as e:
            return ValidationResult(
                book_id=record_data.get("book_id", "UNKNOWN"),
                title=record_data.get("title", "UNKNOWN"),
                is_valid=False,
                errors=[f"Schema Parsing Error: {str(e)}"]
            )

        # 1. Cek Mandatory MARC21 Tags
        for tag in self.mandatory_tags:
            if tag not in record.marc_fields or not str(record.marc_fields[tag]).strip():
                errors.append(f"Missing mandatory MARC21 tag: [{tag}]")

        # 2. Cek Format DDC
        if not self.ddc_pattern.match(record.ddc_code):
            errors.append(f"Invalid DDC classification format: '{record.ddc_code}'")

        # 3. Cek Author
        if not record.author.strip():
            errors.append("Author metadata is missing or empty.")

       # 4. Cek Department Koleksi
        if record.department not in self.rules.get("valid_departments", []):
            errors.append(f"Unknown library department classification: '{record.department}'")

        return ValidationResult(
            book_id=record.book_id,
            title=record.title,
            is_valid=len(errors) == 0,
            errors=errors
        )