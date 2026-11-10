# Library Catalog Metadata & MARC21/DDC Validator

> An automated backend quality assurance (QA) pipeline and CLI tool designed to validate bibliographic records against MARC21 structural requirements and Dewey Decimal Classification (DDC) standards.

---

## 🚀 Overview
In modern digital libraries and institutional repositories, metadata integrity is critical for effective information retrieval and OPAC integration. This tool automates the auditing process by scanning catalog datasets, verifying mandatory MARC tags, checking DDC classification formats, and generating clean compliance reports.

## 🛠️ Tech Stack
* **Language:** Python (utilizing native `dataclasses` for lightweight schema parsing)
* **CLI Interface:** `rich` for professional terminal formatting and data tables
* **Testing Framework:** `pytest` for robust unit testing
* **CI/CD:** GitHub Actions for automated pipeline validation

---

## 📁 Project Directory Structure
```text
TeyvatArchives/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml
├── config/
│   └── validation_rules.json
├── core/
│   ├── __init__.py
│   ├── models.py
│   └── validator.py
├── data/
│   └── mock_teyvat_books.json
├── tests/
│   ├── __init__.py
│   └── test_validator.py
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md