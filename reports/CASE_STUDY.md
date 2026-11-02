# Case Study: Bolivia Forest Data Quality

## 1. Business Problem

Five environmental datasets contained information about
forest loss, carbon emissions, and deforestation drivers
in Bolivia.

Although the original files contained no missing cells
or exact duplicate rows, integrating them required
addressing differences in geographic, temporal,
and canopy threshold coverage.

The goal was to create a reproducible analytical dataset
while preserving the integrity of source measurements.

## 2. Data Sources

Source: Global Nature Watch

- Tree Cover Loss
- Carbon Data
- Drivers
- Primary Forest Loss
- Primary Forest Drivers

Period: 2001–2025, depending on the source.

Original records across five datasets: 46,953

## 3. Data Quality Assessment

The initial audit identified:

- Zero missing cells in the original CSV files.
- Zero exact duplicate rows.
- Different geographic coverage across datasets.
- Different temporal coverage.
- Different available canopy density thresholds.

These differences required controlled integration
rather than automatic deletion or imputation.

## 4. Data Integration

A composite key was used:

country + subnational1 + subnational2 + threshold + year

Driver-attributed losses were aggregated before joining.

Integration was restricted to the 30% canopy threshold.

Final integrated dataset:

- Rows: 2,800
- Columns: 23
- Missing measurements after integration: 4,196

Missing values created by unmatched joins were retained.

## 5. Source Coverage

| Source          |   Matched |   Unmatched |   Coverage (%) |
|:----------------|----------:|------------:|---------------:|
| carbon          |      2800 |           0 |         100    |
| primary_loss    |      1296 |        1504 |          46.29 |
| drivers         |      1636 |        1164 |          58.43 |
| primary_drivers |      1272 |        1528 |          45.43 |

## 6. Statistical Outlier Analysis

Potential outliers were identified using the IQR method.

| Dataset         |   Observations |   Outliers |   Outliers (%) |
|:----------------|---------------:|-----------:|---------------:|
| carbon          |           2800 |        476 |          17    |
| tree_cover      |           2800 |        473 |          16.89 |
| drivers         |           8351 |       1298 |          15.54 |
| primary_drivers |           6506 |        944 |          14.51 |
| primary_loss    |           1296 |        165 |          12.73 |

Statistical outliers were retained because they were
not independently confirmed as erroneous measurements.

OLS and RANSAC were compared using log-transformed
carbon measurements from 2024.

The regression analysis was exploratory and was
not used to alter the source data.

## 7. Cross-Dataset Reconciliation

Tree Cover Loss vs. Drivers:

- Matched observations: 1,636
- Tree Cover total: 10,543,870 ha
- Driver-attributed total: 10,519,423 ha
- Net relative difference: -0.23%

Primary Forest Loss vs. Primary Drivers:

- Matched observations: 1,272
- Numerical discrepancies:
  1,115
- Net relative difference: -0.1796%

These results measure reconciliation differences,
not overall data quality or measurement accuracy.

## 8. Exploratory Findings

- Highest annual tree cover loss: 2024.
- Highest annual gross carbon emissions:
  2024.
- Permanent agriculture and wildfire were the
  two largest attributed loss categories in both
  driver datasets over the common analysis period.

These results depend on dataset coverage and
the selected canopy threshold.

## 9. Processing Decisions

| Finding | Decision |
|---|---|
| Different temporal coverage | Preserve missing observations |
| Different canopy thresholds | Use threshold 30 for integration |
| Different geographic coverage | Use validated joins |
| Statistical outliers | Flag and retain |
| Numerical discrepancies | Document without altering values |
| Detailed driver categories | Preserve original source tables |

No unsupported measurement corrections were applied.

## 10. Verification

- Structural integration checks: 10/10 passed.
- Final structural checks: 6/6 passed.
- Automated integration tests: 5 passed.
- Integrated dataset reproducibility: verified.
- Base Tree Cover measurements: preserved.

## 11. Limitations

- Not all source measurements have equal coverage.
- Statistical anomalies are not confirmed errors.
- The integrated dataset uses threshold 30 only.
- Reconciliation percentages are not accuracy scores.
- The analysis does not establish causal relationships.
- Original measurements were not independently verified.

## 12. Deliverables

- Python integration module.
- Automated integration tests.
- Validated analytical dataset.
- Data quality and reconciliation reports.
- Exploratory analysis notebook.
- Statistical visualizations.
- Documentation of processing decisions.

## 13. Conclusion

The project demonstrates reproducible data preparation,
source reconciliation, data quality auditing,
statistical anomaly detection, and analytical reporting.

The main contribution is a validated integration process
with documented coverage limitations, rather than
artificially modifying source measurements.
