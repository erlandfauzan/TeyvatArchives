Set-Content -Path README.md -Value @"
# 📚 TeyvatArchives - Bibliographic Metadata & MARC21/DDC Compliance Suite

> An automated bibliographic data quality assurance (Data QA) engine designed to audit, validate, and enforce MARC21 structural requirements and Dewey Decimal Classification (DDC) standards across library catalog repositories.

---

## 🛡️ Status & Badges
![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)
![Data QA Status](https://img.shields.io/badge/metadata%20audit-passing-green.svg)
![Domain](https://img.shields.io/badge/domain-Library%20%26%20Information%20Science-purple.svg)
![License](https://img.shields.io/badge/license-MIT-informational.svg)

---

## 🌟 1. Executive Summary
In digital library operations and Online Public Access Catalog (OPAC) management, metadata integrity is critical for knowledge discovery. A single typo in a classification code, an incomplete author field, or a missing mandatory MARC tag can render a newly acquired book "invisible" during patron search queries.

**TeyvatArchives** acts as an automated **Bibliographic Data Quality Gate**. It audits catalog datasets against standardized rules (MARC21 & DDC), catches entry errors early, and generates clean, structured diagnostic reports directly in the terminal—preventing corrupted or incomplete metadata from reaching the primary discovery index.

---

## 🔮 2. Origin & Naming Lore
* **The Inspiration:** In *Genshin Impact*, **Irminsul** is a legendary silver-white tree connected to all ley lines in Teyvat, serving as the universal repository for all historical information, records, and memory. However, corrupted entries within Irminsul distort knowledge and reality across the world.
* **The Application:** **TeyvatArchives** takes inspiration from this concept. Designed specifically for library data environments, it serves as a metadata sentinel. By detecting missing mandatory tags, malformed DDC call numbers, or empty author fields, TeyvatArchives maintains the accuracy and reliability of institutional knowledge repositories.

---

## ⚙️ 3. Key Features
* **Bibliographic Data QA:** Automated compliance validation enforcing MARC21 structural standards (e.g., tags `082`, `100`, `245`, `264`) and DDC notation rules.
* **Data-Driven Testing (DDT):** Test datasets and validation rules are cleanly separated from core logic (`config/validation_rules.json` and `data/mock_teyvat_books.json`).
* **Rich Terminal Diagnostics:** Utilizes the `rich` visual engine to format audit reports into clear, color-coded compliance tables in the terminal.
* **Automated Unit Verification:** Integrated `pytest` test suite to verify validation logic under various valid and invalid data scenarios.
* **Continuous Integration (CI):** Fully configured GitHub Actions workflow (`ci-pipeline.yml`) to automatically execute validation checks on every commit.

---

## 📂 4. Repository Structure
\`\`\`text
TeyvatArchives/
├── .github/
│   └── workflows/
│   │   └── ci-pipeline.yml   # GitHub Actions CI/CD automation
├── config/
│   └── validation_rules.json # Department classifications & mandatory MARC rules
├── core/
│   ├── __init__.py
│   ├── models.py             # Native dataclass schema for book records
│   └── validator.py          # Core MARC21 & DDC metadata validation engine
├── data/
│   └── mock_teyvat_books.json# Mock bibliographic dataset for audit testing
├── tests/
│   ├── __init__.py
│   └── test_validator.py     # Automated unit test suite
├── Dockerfile                # Containerization setup
├── main.py                   # CLI entry point & audit report generator
├── requirements.txt          # Lightweight project dependencies
└── README.md                 # System documentation
\`\`\`

---

## 🛠️ 5. Installation & Execution Guide

### Prerequisites
* **Python:** 3.10 or higher (compatible with Python 3.14)
* **Git:** Installed and configured

### Step 1: Clone the Repository
\`\`\`bash
git clone https://github.com/erlandfauzan/TeyvatArchives.git
cd TeyvatArchives
\`\`\`

### Step 2: Install Dependencies
\`\`\`bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
\`\`\`

### Step 3: Run the Catalog Metadata Audit
Execute the main script to process the mock catalog dataset and view the compliance report:
\`\`\`bash
python main.py
\`\`\`

### Step 4: Run Automated Tests
Run the test suite using \`pytest\`:
\`\`\`bash
python -m pytest -v
\`\`\`

---

## 📊 6. Architecture & Test Flow Diagram
The diagram below illustrates how bibliographic records flow through the validation pipeline from raw ingestion to the final audit report:

\`\`\`mermaid
graph TD
    A[Config Rules: validation_rules.json] --> C[Validator Engine: core/validator.py]
    B[Catalog Dataset: mock_teyvat_books.json] --> C
    
    subgraph Bibliographic Data QA Pipeline
        C --> D{Verify Mandatory MARC Tags}
        C --> E{Validate DDC Format Regex}
        C --> F{Check Author Metadata}
        C --> G{Verify Department Classification}
    end

    D --> H[ValidationResult Dataclass]
    E --> H
    F --> H
    G --> H

    H --> I[CLI Audit Tool: main.py]
    H --> J[Unit Testing: pytest]

    I --> K[Rich Terminal Audit Table]
    J --> L[GitHub Actions CI Pipeline]
\`\`\`

---
<p align="center"><i>Maintained with precision and care by Erland Fauzan.</i></p>
"@ -Encoding UTF8