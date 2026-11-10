import pytest
from core.validator import TeyvatArchiveValidator

@pytest.fixture
def validator():
    return TeyvatArchiveValidator()

def test_valid_book_record(validator):
    valid_record = {
        "book_id": "LIB-TEST-01",
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "department": "Literature",
        "ddc_code": "891.73",
        "marc_fields": {
            "082": "891.73",
            "100": "Fyodor Dostoevsky",
            "245": "The Brothers Karamazov",
            "264": "Russian Messenger Press"
        }
    }
    result = validator.validate_single_record(valid_record)
    assert result.is_valid is True
    assert len(result.errors) == 0

def test_invalid_ddc_and_missing_author(validator):
    invalid_record = {
        "book_id": "LIB-TEST-02",
        "title": "Anonymous Manuscript",
        "author": "",
        "department": "Social Sciences",
        "ddc_code": "INVALID",
        "marc_fields": {
            "082": "INVALID",
            "245": "Anonymous Manuscript"
        }
    }
    result = validator.validate_single_record(invalid_record)
    assert result.is_valid is False
    assert any("DDC classification format" in err for err in result.errors)
    assert any("Author metadata" in err for err in result.errors)