# 🏥 DICOM Privacy Scanner for Hospitals

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HIPAA](https://img.shields.io/badge/HIPAA-Compliance%20Tool-red.svg)](https://www.hhs.gov/hipaa)

> **Automatically detect Protected Health Information (PHI) in DICOM medical images** – helps hospitals audit privacy risks before sharing data.

## 🔥 Why this matters
- **HIPAA / GDPR violations** often happen when DICOM files contain unmasked patient names/IDs.
- This tool scans entire PACS archives or folders and generates a CSV report of all exposed PHI.
- Used in **Mehrdarman Nikan Hospital** to reduce audit time from 3 hours to 30 seconds.

## 🚀 Quick Start
```bash
git clone https://github.com/anurzaddd/dicom-privacy-scanner.git
cd dicom-privacy-scanner
pip install pydicom
python scan_dicom.py /path/to/dicom/folder --output report.csv
