# Bolivia Forest Data Quality & Reconciliation

A reproducible Python project for auditing, integrating and
analyzing forest loss and carbon data from Bolivia (2001–2025).

## Project Overview

This project demonstrates professional data quality practices
using five environmental datasets from Global Nature Watch.

**Technologies:** Python, pandas, NumPy, Matplotlib,
scikit-learn, Google Colab and unittest.

## Data Sources

- Subnational 2 Tree Cover Loss
- Subnational 2 Carbon Data
- Subnational 2 Drivers
- Subnational 2 Primary Loss
- Subnational 2 Primary Drivers

Source: https://globalnaturewatch.org/dashboards/country/BOL/

## Methodology

1. Data profiling and structural quality audits
2. Geographic, temporal and threshold coverage validation
3. Composite key validation
4. Multi-source integration at the 30% canopy threshold
5. Cross-dataset numerical reconciliation
6. IQR-based statistical outlier detection
7. OLS and RANSAC sensitivity analysis
8. Exploratory analysis and automated validation

## Key Results

| Metric | Result |
|---|---|
| Original datasets | 5 |
| Total original source rows | 46,953 |
| Integrated dataset | 2,800 rows, 23 columns |
| Structural integration checks | 10/10 passed |
| Final validation checks | 6/6 passed |
| Automated integration tests | 5 passed |
| Tree Cover / Drivers matching coverage | 58.43% |
| Tree Cover / Drivers net reconciliation gap | -0.23% |

## Data Quality Decisions

- Original measurements were preserved.
- Structural missing values were not automatically imputed.
- Statistical outliers were flagged rather than deleted.
- Numerical discrepancies were retained and documented.
- Detailed driver categories remain available in source datasets.

## Project Structure

- `src/` — Reusable Python integration code
- `tests/` — Automated integration tests
- `notebooks/` — Documented Google Colab analysis
- `reports/` — Quality and reconciliation reports
- `figures/` — Analytical visualizations
- `data/raw/` — Local source data location

## Installation

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Place the five original CSV files in `data/raw/`.

Run integration tests:

```bash
python -m unittest discover -s tests -v
```

Example integration:

```python
from pathlib import Path
from src.integration import build_dataset

df = build_dataset(Path("data/raw"))
print(df.shape)
```

## Limitations

The integrated dataset uses a 30% canopy density threshold.
Source coverage varies by geography and time period.

Statistical outliers are not necessarily measurement errors.
Reconciliation metrics are not overall data quality scores.
Tree cover loss does not always represent permanent deforestation.

## Data Attribution

Data source: Global Nature Watch / World Resources Institute.
Dataset-specific citations and redistribution permissions
should be verified before publishing source CSV files.

## Portfolio Purpose

Demonstrates reproducible data preparation, data quality
auditing, multi-source reconciliation and analytical reporting.

## Detailed Case Study

Read the [full Data Quality Case Study](reports/CASE_STUDY.md).
