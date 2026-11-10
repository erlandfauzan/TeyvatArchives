# 📚 TeyvatArchives - Bibliographic Metadata & MARC21/DDC Compliance Suite

![Metadata Audit](https://img.shields.io/badge/Metadata-Audit-blue)
![Python](https://img.shields.io/badge/Python-v3.14-green)
![Pytest](https://img.shields.io/badge/Pytest-v8.x-orange)
![Build Passing](https://img.shields.io/badge/Build-Passing-brightgreen)

An automated bibliographic data quality assurance (Data QA) engine designed to audit, validate, and enforce MARC21 structural requirements and Dewey Decimal Classification (DDC) standards across library catalog repositories.

---

## 📌 1. Executive Summary

In digital library operations and Online Public Access Catalog (OPAC) management, metadata integrity is critical for knowledge discovery. This automated testing project is built to validate system reliability across core metadata layers:

1. **MARC21 Structural Layer:** Automated validation of mandatory bibliographic tags (e.g., `082`, `100`, `245`, `264`) ensuring complete bibliographic item description.
2. **Classification & Department Layer:** Custom regex validation rules enforcing Dewey Decimal Classification (DDC) formats and departmental mappings.

All test scenarios utilize **Data-Driven Testing (DDT)** architecture, where bibliographic records and assertions are isolated into independent JSON datasets (`mock_teyvat_books.json`) without hardcoded values in the execution scripts.

---

## 💡 2. Problem Statement & Real-World Impact

In real-world library operations, managing large-scale Online Public Access Catalog (OPAC) systems and digital repositories often presents significant operational challenges:

- **Human Error in Data Entry:** Librarians and data entry staff frequently face human fatigue, leading to mistyped ISBNs, missing digits, or malformed DDC classification codes during cataloging.
- **Corrupted Search & Discovery:** Invalid catalog metadata directly disrupts search indexing. A single wrong character in an ISBN or DDC notation can make a newly acquired academic book "invisible" to students and researchers.
- **System Integrity Risks:** Inconsistent metadata schema across library branches can corrupt union catalog aggregations and database indexing.

### How TeyvatArchives Solves This:
**TeyvatArchives** serves as an automated quality gate between cataloging input and live database indexing:
- **Automated Metadata Audit:** Replaces manual catalog checking by instantly validating incoming bibliographic data against international MARC21 and DDC standards.
- **Data Compliance Enforcement:** Ensures that institutional repositories reject malformed records before they reach discovery layers.
- **Time Efficiency:** Reduces the manual audit workload for cataloging librarians, allowing them to focus on collection development rather than routine data verification.

---

## 🛠️ 3. Key Features

- **Bibliographic Metadata Integrity:** Dedicated validation engine (`TeyvatArchiveValidator`) enforcing international library standards for MARC21 structural requirements and DDC notations.
- **Data-Driven Testing (DDT):** Test datasets and validation rules are cleanly separated from core logic (`config/validation_rules.json` and `data/mock_teyvat_books.json`).
- **Rich Terminal Diagnostics:** Utilizes the `rich` visual engine to format audit reports into clear, color-coded compliance tables in the terminal.
- **Automated Unit Verification:** Integrated `pytest` test suite to verify validation logic under various valid and invalid data scenarios.
- **Containerized Environment:** Fully dockerized setup using `Dockerfile` for zero-configuration, environment-agnostic test runs.
- **Automated CI/CD:** Fully integrated GitHub Actions workflow (`ci-pipeline.yml`) executing test suites automatically on every `push` and `pull_request`.

---

## ⚙️ 4. Installation & Usage Guide

### Prerequisites
- **Python**: 3.10 or higher (compatible with Python 3.14)
- **Git**: Installed and configured
- **Docker** *(Optional, for containerized execution)*

### Step 1: Clone the Repository
`git clone https://github.com/erlandfauzan/TeyvatArchives.git`
`cd TeyvatArchives`

### Step 2: Install Dependencies
`python -m pip install --upgrade pip`
`python -m pip install -r requirements.txt`

### Step 3: Run the Catalog Metadata Audit
Execute the main script to process the mock catalog dataset and view the compliance report:
`python main.py`

### Step 4: Run Automated Tests
Run the test suite using `pytest`:
`python -m pytest -v`

---

## 🌲 5. Origin & Naming Lore
In the lore of *Genshin Impact*, **Irminsul** is a majestic silver-white tree connected to all ley lines in Teyvat. It acts as a universal knowledge repository recording every piece of history, memory, and information. However, corrupted records within Irminsul can alter knowledge and destabilize reality.

**TeyvatArchives** draws direct inspiration from this concept. Designed for digital library ecosystems, it serves as a metadata sentinel that validates bibliographic catalog metadata and ensures institutional record integrity. By catching missing mandatory tags, malformed DDC call numbers, and metadata anomalies, **TeyvatArchives** maintains the accuracy and reliability of modern library knowledge systems.

---

## 📊 6. Test Execution Evidence

### 1. Terminal Execution Log
![Terminal Test Output](assets/terminal_execution.png)

---

## 7. Repository Structure

- `.github/workflows/ci-pipeline.yml` — GitHub Actions CI/CD Pipeline
- `config/validation_rules.json` — Department classifications & mandatory MARC rules
- `core/models.py` — Native dataclass schema for book records
- `core/validator.py` — Core MARC21 & DDC metadata validation engine
- `data/mock_teyvat_books.json` — Mock bibliographic dataset for audit testing
- `tests/test_validator.py` — Automated unit test suite
- `Dockerfile` — Containerization setup
- `main.py` — CLI entry point & audit report generator
- `requirements.txt` — Lightweight project dependencies
- `README.md` — Project Documentation

---

## ⏳ 8. Architecture & Test Flow Diagram

The diagram below illustrates the end-to-end execution workflow of the testing suite from data ingestion to CI/CD pipeline triggers:

```mermaid
flowchart TD
    subgraph Data Layer
        A[Config Rules<br/>config/validation_rules.json]
        B[Catalog Dataset<br/>data/mock_teyvat_books.json]
    end

    subgraph Execution Layer
        C[Pytest Test Runner]
    end

    subgraph Validation Engine
        D[TeyvatArchiveValidator<br/>core/validator.py]
        E[Dataclass Schemas<br/>core/models.py]
    end

    subgraph Test Scenarios & CLI
        F[Unit Tests<br/>tests/test_validator.py]
        G[CLI Audit Tool<br/>main.py]
    end

    subgraph Reporting & CI/CD
        H[Rich Terminal Audit Table]
        I[GitHub Actions Pipeline<br/>.github/workflows/]
    end

    A --> D
    B --> D
    C --> F
    C --> G
    D --> E
    F --> H
    G --> H
    H --> I